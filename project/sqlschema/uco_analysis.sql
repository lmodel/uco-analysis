

CREATE TABLE "Action" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	error TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, error, instrument, object, participant, result, location, "endTime", "startTime", "actionCount", "actionStatus")
);

CREATE TABLE "ActionArgumentFacet" (
	"argumentName" TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("argumentName", value)
);

CREATE TABLE "ActionEstimationFacet" (
	"estimatedCost" TEXT, 
	"estimatedEfficacy" TEXT, 
	"estimatedImpact" TEXT, 
	objective TEXT, 
	PRIMARY KEY ("estimatedCost", "estimatedEfficacy", "estimatedImpact", objective)
);

CREATE TABLE "ActionFrequencyFacet" (
	rate FLOAT NOT NULL, 
	scale TEXT NOT NULL, 
	units TEXT NOT NULL, 
	trend VARCHAR(10) NOT NULL, 
	PRIMARY KEY (rate, scale, units, trend)
);

CREATE TABLE "ActionLifecycle" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	phase TEXT NOT NULL, 
	error TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, instrument, object, participant, result, location, phase, error, "endTime", "startTime", "actionCount", "actionStatus")
);

CREATE TABLE "ActionPattern" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	error TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, error, instrument, object, participant, result, location, "endTime", "startTime", "actionCount", "actionStatus")
);

CREATE TABLE "Analysis" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	error TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, error, instrument, object, participant, result, location, "endTime", "startTime", "actionCount", "actionStatus")
);

CREATE TABLE "AnalyticResult" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	"originatingAnalysis" TEXT, 
	"resultContent" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement, "originatingAnalysis", "resultContent")
);

CREATE TABLE "Annotation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement, object)
);

CREATE TABLE "ArrayOfAction" (
	action TEXT, 
	PRIMARY KEY (action)
);

CREATE TABLE "ArtifactClassification" (
	"classificationConfidence" FLOAT, 
	class TEXT, 
	PRIMARY KEY ("classificationConfidence", class)
);

CREATE TABLE "ArtifactClassificationResultFacet" (
	classification TEXT, 
	PRIMARY KEY (classification)
);

CREATE TABLE "Assertion" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement)
);

CREATE TABLE "AttributedName" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"namingAuthority" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "namingAuthority")
);

CREATE TABLE "Bag" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "Bundle" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "CoItem" (
	"itemOf" TEXT, 
	PRIMARY KEY ("itemOf")
);

CREATE TABLE "Collection" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "Compilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ConfidenceFacet" (
	confidence INTEGER NOT NULL, 
	PRIMARY KEY (confidence)
);

CREATE TABLE "ContextualCompilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "ControlledDictionary" (
	entry TEXT, 
	PRIMARY KEY (entry)
);

CREATE TABLE "ControlledDictionaryEntry" (
	"key" TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("key", value)
);

CREATE TABLE "ControlledVocabulary" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"constrainingVocabularyReference" TEXT, 
	"constrainingVocabularyName" TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "constrainingVocabularyReference", "constrainingVocabularyName", value)
);

CREATE TABLE "Dictionary" (
	entry TEXT NOT NULL, 
	PRIMARY KEY (entry)
);

CREATE TABLE "DictionaryEntry" (
	"key" TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("key", value)
);

CREATE TABLE "EnclosingCompilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "ExternalReference" (
	"referenceURL" TEXT, 
	"definingContext" TEXT, 
	"externalIdentifier" TEXT, 
	PRIMARY KEY ("referenceURL", "definingContext", "externalIdentifier")
);

CREATE TABLE "GPSCoordinatesFacet" (
	hdop FLOAT, 
	pdop FLOAT, 
	tdop FLOAT, 
	vdop FLOAT, 
	PRIMARY KEY (hdop, pdop, tdop, vdop)
);

CREATE TABLE "Grouping" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	context TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object, context)
);

CREATE TABLE "Hash" (
	"hashValue" TEXT NOT NULL, 
	"hashMethod" TEXT NOT NULL, 
	PRIMARY KEY ("hashValue", "hashMethod")
);

CREATE TABLE "IdentityAbstraction" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Item" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "LatLongCoordinatesFacet" (
	altitude FLOAT, 
	latitude FLOAT, 
	longitude FLOAT, 
	PRIMARY KEY (altitude, latitude, longitude)
);

CREATE TABLE "List" (
	element TEXT, 
	size INTEGER, 
	item TEXT, 
	"lastItem" TEXT, 
	"firstItem" TEXT, 
	PRIMARY KEY (element, size, item, "lastItem", "firstItem")
);

CREATE TABLE "ListItem" (
	"itemOf" TEXT, 
	_index INTEGER NOT NULL, 
	PRIMARY KEY ("itemOf", _index)
);

CREATE TABLE "Location" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "LogicalPattern" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"patternExpression" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "patternExpression")
);

CREATE TABLE "MarkingDefinitionAbstraction" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ModusOperandi" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Pattern" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Relationship" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"endTime" DATETIME, 
	"isDirectional" BOOLEAN NOT NULL, 
	"kindOfRelationship" TEXT, 
	source TEXT NOT NULL, 
	"startTime" DATETIME, 
	target TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "endTime", "isDirectional", "kindOfRelationship", source, "startTime", target)
);

CREATE TABLE "Set" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "SimpleAddressFacet" (
	"addressType" TEXT, 
	country TEXT, 
	locality TEXT, 
	"postalCode" TEXT, 
	region TEXT, 
	street TEXT, 
	PRIMARY KEY ("addressType", country, locality, "postalCode", region, street)
);

CREATE TABLE "Thread" (
	element TEXT, 
	size INTEGER, 
	item TEXT, 
	PRIMARY KEY (element, size, item)
);

CREATE TABLE "ThreadItem" (
	"itemContent" TEXT, 
	PRIMARY KEY ("itemContent")
);

CREATE TABLE "UcoObject" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);
