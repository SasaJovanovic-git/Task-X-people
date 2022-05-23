import json
from typing import Dict

files = ["ConsentCountryRegion", "Country_ConsentBasedCategory", "DataElement", "Elem_ConsentBasedCategory", "Elem_EdgeType", "Elem_SolnSrvc", "IoTEdgeType", "PrivacyConsentBasedCategory", "SolutionService", "TaxonCls", "TaxonClsType"]    

print()
for file in files:
	print(file)
	table_name = file
	output_file = "/home/sjovanovic/Documents/Data/DataJson2.2New/" + file + ".sql"

	file = "/home/sjovanovic/Documents/Data/Data2.25April2022/Data.V2.2, April 5th/" + file + ".json"
	print("Reading ", file)
	f = open(file, 'r')
	
	print("Writing ", output_file)
	f_write = open(output_file, 'w')
	f_write.close()
	f_write = open(output_file, "a")
	 
	## Returns JSON object as a dictionary
	data = json.load(f)
	# print(data)
	print()

	ConsentCountryRegion =  {"id": "int", "name": "string", "code": "string"}
	Country_ConsentBasedCategory = {"id": "int", "consentBasedCategoryId": "int", "countryId": "int"}
	DataElement = {"id": "int", "attributeId": "string", "atomicAttributeName": "string", "businessTitle": "string", "classificationId": "int", "description": "string", "strNecCount": "string"}
	Elem_ConsentBasedCategory = {"id": "int", "consentBasedCategoryId": "int", "dataElementId": "int"}
	Elem_EdgeType = {}
	Elem_SolnSrvc = {"id": "int", "dataElementId": "int", "solnSrvcId": "int"}
	IoTEdgeType = {}
	PrivacyConsentBasedCategory = {"id": "int", "consentCategoryCd": "string", "alpacaPurposeId": "string"}
	SolutionService = {"id": "int", "description": "string", "documentationLink": "string", "ownerName": "string", "programLevelName": "string", "serviceId": "string", "serviceName": "string"}
	TaxonCls = {"id": "int", "code": "string", "name": "string", "parentId": "int", "taxonClsTypeId": "int"}
	TaxonClsType = {"id": "int", "code": "string", "name": "string"}

	for level1 in data:
		# print(level1)
		insert = "INSERT INTO " + table_name + "  ("
		names = ""
		values = ""
		for level2 in level1['columns']:
			# print(level2['column']['name'])
			names = names + level2['column']['name'] + ", "
			#print(ConsentCountryRegion[level2['column']['name']])
			if (eval(table_name)[level2['column']['name']] == 'int'):
				values = values + str(level2['column']['value']).rstrip() + ", "
			else:
				values = values + "\"" + str(level2['column']['value']) + "\", "
		names = names[:-2]
		values = values[:-2]
		insert = insert + names + ")  values  ("
		insert = insert + values + ");\n"
		# print(insert)
		f_write.write(insert)
		# f_write.close()