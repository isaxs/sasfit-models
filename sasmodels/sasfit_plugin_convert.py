#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Program to convert sasfit plugin models to sasmodels template

The script will perform following:
1) Read in sasfit file header information
2) Generate sasmodels python file
3) Generate category hierarchy
4) Translates sasfit errors handling into parameter ranges

The script returns converted c file and python template file.
The template file should in principle be ready to use but
some additional information ,may need to be filled in
"""


__author__ = "Wojtek Potrzebowski"
__maintainer__ = "Wojtek Potrzebowski"
__email__ = "Wojciech.Potrzebowski@esss.se"

import os
import optparse
from re import search
from string import capwords
from collections import OrderedDict

#TODO: Look for pattern:  /* ################ start ff_fuzzysphere ################
#TODO: and then parse parmeters
#TODO: finish off on /* ################ stop ff_fuzzysphere ################ */
#TODO: Default values as before?
#TODO: In cfile create I(q) F(q), form_volume()
#TODO: How to handle volume parameters

def extract_parameters_definition( model_name, tcl_filename ):
    """
    Extracting the definitions of paramters that can be then supplied with the
    parameter table

    :param tcl_file:
    :return:
    """
    tcl_lines = open(tcl_filename).readlines()
    parameters_definition = []
    model_name_upper = "".join(map(lambda p : capwords(p),
                                       model_name.split("_")))
    print "Model name in TCL", model_name_upper, model_name
    for index, line in enumerate(tcl_lines):
        if search(model_name_upper+ " {", line) or search("\""
                                    +model_name_upper+"\" {", line):
            model_def_index = index
    #TODO Some models have extra parameters, so the range with 13 won't work
    model_def_lines = tcl_lines[model_def_index+2:model_def_index+13]
    for def_line in model_def_lines:
        pardef = def_line.split("return \"")[1].strip("\\n\"}\r\n")
        parameters_definition.append(pardef)
    return parameters_definition

def extract_parameters_definition_from_private(private_filename):
    """
    Extracting the definitions of paramters that can be then supplied with the
    parameter table

    :param tcl_file:
    :return:
    """

    private_lines = open(private_filename).readlines()
    parameters = []
    for line in private_lines:
        regm = search("#define", line)
        if regm and search("param->", line):
            param = line[regm.end():]
            regm = search("\s+[\w.-]+( |\t)", param)
            # regm = search("(\s+\t+)\b", param)
            param = param[1:regm.end()]
            param = param.strip("\t")
            param = param.strip(" ")
            parameters.append(param)
    return parameters


def extract_parameters_definition_from_check_cond1( model_name, sasfit_lines):
    """
    Extracting the definitions of paramters that can be then supplied with the
    parameter table

    First defining lines between which parameters statements can be identified

    :param tcl_file:
    :return:
    """
    parameters = []
    model_found = False
    for line in sasfit_lines:
        # TODO: There are other define statements, so check if it is not failing
        start_regm = search('# start '+model_name+' #', line)
        if start_regm:
            model_found = True
        stop_regm = search('# start '+model_name+' #', line)
        if stop_regm:
            model_found = True
        if model_found:
            param = line[regm.end() + 1:].split(",")[3]
            param = param.split(");")[0]
            parameters.append(param)

    return parameters

def generate_python_header(model_name, output_python_file, parameters_definition):
    """
    Python file header generator
    :param output_python_file:
    :return:
    """
    header_lines = "r\"\"\"\n"

    header_lines += "This file has been automatically gereated by sasfit_plugin_convert\n"

    header_lines += "The model calculates an empirical functional form " \
                    "for SAS data characterized\n"
    header_lines += "by "+model_name+"\n\n"
    header_lines += "Definition:\n"
    header_lines += "-----------\n\n"

    header_lines += "References:\n"
    header_lines += "-----------\n\n"

    header_lines += "\"\"\"\n"

    header_lines += "from numpy import inf\n\n"

    header_lines += "name = \""+model_name+"\"\n"
    header_lines += "title = \" \"\n"
    header_lines += "description = \""+parameters_definition[0]+"\"\n"
    header_lines += "category = \" \"\n"

    output_python_file.writelines(header_lines)

def convert_sasfit_model(model_name, sasfit_file, output_c_file,
                         output_python_file, parameters, parameters_definition):
    """
    Main conversion function
    :param sasfit_file:
    :param output_c_file:
    :param output_python_file:
    :return:
    """
    sasfit_lines = open(sasfit_file).readlines()
    output_c_lines = []
    output_intro_lines = []
    output_python_lines = []

    #DO regular expression and remove if it is in line
    c_intro_lines = "///////////////////////////////////////////////////\n"
    c_intro_lines += "//    This is automatically genearted file       //\n"
    c_intro_lines += "//    by sasfit_convert.py                       //\n"
    c_intro_lines += "//    Some editting might be required            //\n"
    c_intro_lines += "///////////////////////////////////////////////////\n\n"

    output_intro_lines.append(c_intro_lines)


    #Add paramters to excluded list, so they don't get redifned - shaky
    exclude_list.append("scalar "+", ".join(parameters))


    #If the compariosn with sasview ETA should be swapped with sld
    #fixed_paramters = []
    #for param in parameters:
    #    if "ETA" in param and not "THETA" in param:
    #        param = param.replace("ETA","sld")
    #    fixed_paramters.append(param)
    #parameters = fixed_paramters

    print "Parameters", parameters
    Iq_lines = "double Iq( double q,"
    Fq_lines = "double Fq( double q, "
    Fq_func = "Fq( q, "
    form_volume_lines = "double form_volume( "
    form_volume_func = "form_volume("
    include_libs = []
    for line in sasfit_lines:
        line = line.strip()
        allowed = 1

        # Replace string in line when need
        #for sub in substitution_dict.keys():
        #    if search(sub, line):
        #        line = line.replace(sub, substitution_dict[sub])

        #Create a new header for Iq function
        #if search("sasfit_ff_"+model_name, line) and not search("src", line):
        if search(r"scalar sasfit_[ff_]+"+model_name+"_f\((.*?)\)", line):
            regm = search(r"sasfit_[ff_]+" + model_name + "_f", line)
            sasfit_Fq = line[regm.start():regm.end()]
            substitution_dict[sasfit_Fq] = "Fq"

            for param in parameters[:-1]:
                Fq_lines+=" double "+param+", "
            Fq_lines+=" double "+parameters[-1]+")"
            output_c_lines.append(Fq_lines+"\n")
            output_intro_lines.append(Fq_lines+";\n")

            allowed = 0
        if search(r"scalar sasfit_[ff_]+"+model_name+"_v\((.*?)\)", line):
            regm = search(r"sasfit_[ff_]+" + model_name + "_v",line)
            sasfit_form_volume = line[regm.start():regm.end()]
            substitution_dict[sasfit_form_volume] = "form_volume"

            for param in parameters[:-1]:
                form_volume_lines+=" double "+param+", "
            form_volume_lines+=" double "+parameters[-1]+")"
            output_c_lines.append(form_volume_lines+"\n")
            output_intro_lines.append(form_volume_lines+";\n")
            allowed = 0
        if search(r"scalar sasfit_[ff_]+"+model_name+"\((.*?)\)", line):
            swap_parameters = ""
            swap_parameters_def = ""
            for param in parameters[:-1]:
                swap_parameters += param+", "
                swap_parameters_def +=" double "+param+", "
                Iq_lines+=" double "+param+", "
            swap_parameters += parameters[-1]
            swap_parameters_def +=" double "+parameters[-1]
            Iq_lines+=" double "+parameters[-1]+")"

            output_c_lines.append(Iq_lines+"\n")
            output_intro_lines.append(Iq_lines+";\n")
            #substitution_dict["sasfit_param *param"] = swap_parameters_def
            #substitution_dict["sasfit_param * param"] = swap_parameters_def
            #substitution_dict["param"] = swap_parameters
            allowed = 0
        for banned_term in exclude_list:
            if search(banned_term, line):
                allowed = 0

        for func in libinclude_dict.keys():
            if search(func, line):
                for libfile in libinclude_dict[func]:
                    if not libfile in include_libs:
                        include_libs.append(libfile)

        #Replace string in line when need
        #for sub in substitution_dict.keys():
        #    if search(sub, line):
        #        line = line.replace(sub, substitution_dict[sub])


        #Skip empty lines
        if line=="":
            allowed = 0

        if allowed:
            output_c_lines.append(line+"\n")

    # Replace string in line when need
    out_c_lines = []
    for line in output_c_lines:

        #TODO:It will be better if it works for abitrary numnber of spaces
        if search(r"sasfit_param\s\*param", line):
            line = line.replace("sasfit_param *param", swap_parameters_def)
        elif search(r"sasfit_param\s\*\sparam", line):
            line = line.replace("sasfit_param * param", swap_parameters_def)
        elif search(r"param", line) and not search(r"_param", line):
            line = line.replace("param", swap_parameters)

        for sub in substitution_dict.keys():
            if search(sub, line):
                line = line.replace(sub, substitution_dict[sub])
        out_c_lines.append(line)

    #output_c_lines += output_Vol_lines + output_Fq_lines + output_Iq_lines

    #TODO: Not exactly sure how to handle this
    header_Iqxy_line = "double Iqxy( double qx, double qy,"
    for param in parameters[:-1]:
        header_Iqxy_line+=" double "+param+","
    header_Iqxy_line+=" double "+parameters[-1]+")"
    output_intro_lines.append(header_Iqxy_line+";\n")
    header_Iqxy_line += "\n"
    header_Iqxy_line+="{\n"
    header_Iqxy_line+="\tdouble q = sqrt(qx*qx + qy*qy);\n"
    header_Iqxy_line+="\treturn Iq( q,"
    for param in parameters[:-1]:
        header_Iqxy_line+=" "+param+","
    header_Iqxy_line+=" "+parameters[-1]+");\n"
    header_Iqxy_line+="}\n"
    out_c_lines.append(header_Iqxy_line)

    #Generating python parameter file
    #It looks from interface that first value is set to 10.0, 4th to 1.0
    #and the rest is 0.0 and apparently standard models takes no more than
    #10 pramateres
    parameters_values = [10.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    output_python_lines = "#pylint: disable=bad-whitespace, line-too-long\n"
    output_python_lines += "parameters = [\n"
    for index, param in enumerate(parameters):
        try:
            param_def = parameters_definition[index+1]
        except:
            param_def = " "
        #print "Param def", param, param_def
        output_python_lines += " [ \""+param+"\", \t\"\", \t"\
                               +str(parameters_values[index])+", " \
                                "\t[-inf, inf], \t\"\", " \
                                "\t\""+param_def+"\"],\n"
    output_python_lines += "]\n"
    output_python_lines +=" #pylint: enable=bad-whitespace, line-too-long\n\n"
    #FIXME: It should refer to c_file not model name
    output_python_lines +="source = [ "

    for libfile in include_libs:
        libfile = os.path.join("lib", libfile)
        output_python_lines += "\""+libfile+"\", "
    output_python_lines += " \"sasfit_" + model_name + ".c\" ]\n\n"


    output_python_lines +="demo = dict(\n"
    for index, param in enumerate(parameters[:-1]):
        output_python_lines += "\t"+param+" = " \
            +str(parameters_values[index])+",\n"

    output_python_lines += "\t"+parameters[-1]+" = "\
                           +str(parameters_values[len(parameters)-1]) + ")\n"

    output_c_file.writelines(output_intro_lines)

    output_c_file.writelines(out_c_lines)
    output_python_file.writelines(output_python_lines)

def extract_params(model_name, tcl_file, sasfit_file, private_file):
    """

    :param model_name:
    :param tcl_file:
    :param sasfit_file:
    :return:
    """
    parameters = []
    parameters_definition = []
    sasfit_lines = open(sasfit_file).readlines()
    try:
        parameters_definition = extract_parameters_definition(model_name,
                                                          tcl_file)
    except:
        parameters_definition = []
        for i in range(11):
            parameters_definition.append("")

    # There a few different ways to extract parameters
    # 1. From sasfit_get_param
    if len(parameters) == 0:
        for line in sasfit_lines:
            regm = search("sasfit_get_param\(", line)
            if regm:
                params = line[regm.end():].strip(");\r\n").split(", ")
                number_of_params = int(params[1])
                parameters = map(lambda p: p.lstrip("&"),
                             params[2:2 + number_of_params])

    # 2. From define statement in the c file
    if len(parameters) == 0:
        for line in sasfit_lines:
            # TODO: There are other define statements, so check if it is not failing
            regm = search("#define", line)
            if regm and search("param->", line):
                param = line[regm.end():]
                regm = search("\s+[\w.-]+( |\t)", param)
                #regm = search("(\s+\t+)\b", param)
                param = param[1:regm.end()]
                param = param.strip("\t")
                param = param.strip(" ")
                parameters.append(param)

    # 2. From SASFIT_CHECK_COND1 in the c file
    if len(parameters) == 0:
        parameters = extract_parameters_definition_from_check_cond1(
                model_name, sasfit_lines)


    # But if 2 above don't work then read it from parameters definition
    if len(parameters) == 0:
        for pardef in parameters_definition[1:]:
            param = pardef.split(":")[0]
            if param != "":
                parameters.append(param)

    #Add parameters anything is included in the private include file
    parameters+=extract_parameters_definition_from_private(private_file)

    #TODO: Quite risky but have to see if there are any consequneces
    if "q" in parameters:
        parameters.remove("q")
    return  parameters, parameters_definition

if __name__=="__main__":
    doc = """
            Script to convert sasfit files to sasmodels
            Usage: python sasfit_convert.py --help
        """
    print doc
    usage = "usage: %prog [options] args"
    option_parser_class = optparse.OptionParser
    parser = option_parser_class( usage = usage, version='0.1' )

    parser.add_option("-f", "--sasfit_file", dest="sasfit_file",
                      help="SASFit c file [OBLIGATORY]")
    parser.add_option("-o", "--output_file", dest="output_file",
                      help="Output c file and python file name [NO EXTENSION]")
    parser.add_option("-t", "--tcl_file", dest="tcl_file",
                      help="TCL file containing parameter definition c file ")
    parser.add_option("-p", "--private_file", dest="private_file",
                      help="Include private file containing parameters ")
    options, args = parser.parse_args()

    exclude_model_terms = ["sasfit","ff","ff_ff","../",".."]
    if options.output_file:
        model_name = options.output_file
    else:
        #Remove sasfit_ff prefix and .c suffix
        model_name = options.sasfit_file.split("/")[2]
        model_name = "_".join([name_term for name_term in model_name.split("_")
                               if name_term not in exclude_model_terms])
        #model_name = model_name.rstrip(".c")
        model_name = model_name[:-2]
    print model_name, options.sasfit_file
    output_c_filename = "sasfit_"+model_name+".c"
    output_python_filename = "sasfit_"+model_name+".py"

    output_c_file = open(output_c_filename,"w")
    output_python_file =  open(output_python_filename,"w")

    parameters, parameters_definition = extract_params(model_name,
                                        options.tcl_file, options.sasfit_file,
                                        options.private_file)

    #Exit when no parameters for model can be defined
    if len(parameters) == 0:
        exit()

    generate_python_header(model_name, output_python_file, parameters_definition)

    convert_sasfit_model(model_name, options.sasfit_file, output_c_file,
                         output_python_file, parameters, parameters_definition)
