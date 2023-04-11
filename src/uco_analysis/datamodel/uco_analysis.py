# Auto generated from uco_analysis.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-11T23:32:43
# Schema: uco-analysis
#
# id: https://w3id.org/linkmodel/uco-analysis
# description: This ontology defines classes and properties for characterizing analytic analysiss and results.
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Decimal, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "1.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AFC = CurieNamespace('AFC', 'http://purl.allotrope.org/ontologies/common#AFC_')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
ERO = CurieNamespace('ERO', 'http://purl.obolibrary.org/obo/ERO_')
GSSO = CurieNamespace('GSSO', 'http://purl.obolibrary.org/obo/GSSO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://identifiers.org/sio/')
SWO = CurieNamespace('SWO', 'http://purl.obolibrary.org/obo/SWO_')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://identifiers.org/wikidata/')
ACTION = CurieNamespace('action', 'https://w3id.org/lmodel/uco-action/')
ANALYSIS = CurieNamespace('analysis', 'https://w3id.org/lmodel/uco-analysis/')
CO = CurieNamespace('co', 'http://purl.org/co/')
COLLECTIONS = CurieNamespace('collections', 'https://w3id.org/lmodel/collections/')
CORE = CurieNamespace('core', 'https://w3id.org/lmodel/uco-core/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EDAM_DATA = CurieNamespace('edam_data', 'http://edamontology.org/data_')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LM_CORE = CurieNamespace('lm_core', 'https://w3id.org/lmodel/core/')
LOCATION = CurieNamespace('location', 'https://w3id.org/lmodel/uco-location/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PATTERN = CurieNamespace('pattern', 'https://w3id.org/lmodel/uco-pattern/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SCHEMA_COLLECTIONS = CurieNamespace('schema_collections', 'https://w3id.org/lmodel/collections/schema/')
SCHEMA_UCO_ACTION = CurieNamespace('schema_uco_action', 'https://w3id.org/lmodel/uco-action/schema/')
SCHEMA_UCO_CORE = CurieNamespace('schema_uco_core', 'https://w3id.org/lmodel/uco-core/schema/')
SCHEMA_UCO_LOCATION = CurieNamespace('schema_uco_location', 'https://w3id.org/lmodel/uco-location/schema/')
SCHEMA_UCO_PATTERN = CurieNamespace('schema_uco_pattern', 'https://w3id.org/lmodel/uco-pattern/schema/')
SCHEMA_UCO_TYPES = CurieNamespace('schema_uco_types', 'https://w3id.org/lmodel/uco-types/schema/')
SCHEMA_UCO_VOCABULARY = CurieNamespace('schema_uco_vocabulary', 'https://w3id.org/lmodel/uco-vocabulary/schema/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
TYPES = CurieNamespace('types', 'https://w3id.org/lmodel/uco-types/')
VOCABULARY = CurieNamespace('vocabulary', 'https://w3id.org/lmodel/uco-vocabulary/')
WIKIDATA = CurieNamespace('wikidata', 'http://identifiers.org/wikidata/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ANALYSIS


# Types
class StringType(String):
    """ A string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string type"
    type_model_uri = ANALYSIS.StringType


class LiteralType(String):
    """ Literals are used for values such as strings, numbers, and dates. """
    type_class_uri = RDF.literal
    type_class_curie = "rdf:literal"
    type_name = "literal type"
    type_model_uri = ANALYSIS.LiteralType


class NonNegativeIntegerType(Integer):
    """ real number strictly greater than zero """
    type_class_uri = XSD.nonNegativeInteger
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "non negative integer type"
    type_model_uri = ANALYSIS.NonNegativeIntegerType


class StatementType(StringType):
    """ "meaningful declarative sentence that is either true or false, or that which a true or false declarative sentence asserts" """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "statement type"
    type_model_uri = ANALYSIS.StatementType


class IriType(Uriorcurie):
    """ A IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = ANALYSIS.IriType


class BooleanType(Boolean):
    """ A boolean value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean type"
    type_model_uri = ANALYSIS.BooleanType


class HexBinaryType(hex):
    """ "Represents arbitrary hex-encoded binary data" """
    type_class_uri = XSD.hexBinary
    type_class_curie = "xsd:hexBinary"
    type_name = "hex binary type"
    type_model_uri = ANALYSIS.HexBinaryType


class DecimalType(Decimal):
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal type"
    type_model_uri = ANALYSIS.DecimalType


class PositiveInteger(Integer):
    """ integer greater than zero; natural number explicitly excluding zero """
    type_class_uri = XSD.positiveInteger
    type_class_curie = "xsd:positiveInteger"
    type_name = "positive integer"
    type_model_uri = ANALYSIS.PositiveInteger


# Class references



class UcoThing(YAMLRoot):
    """
    UcoThing is the top-level class within UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoThing
    class_class_curie: ClassVar[str] = "core:UcoThing"
    class_name: ClassVar[str] = "UcoThing"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.UcoThing


class UcoInherentCharacterizationThing(UcoThing):
    """
    A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a
    UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoInherentCharacterizationThing
    class_class_curie: ClassVar[str] = "core:UcoInherentCharacterizationThing"
    class_name: ClassVar[str] = "UcoInherentCharacterizationThing"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.UcoInherentCharacterizationThing


@dataclass
class ArtifactClassification(UcoInherentCharacterizationThing):
    """
    "An artifact classification is a single specific assertion that a particular class of a classification taxonomy
    applies to something."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.ArtifactClassification
    class_class_curie: ClassVar[str] = "analysis:ArtifactClassification"
    class_name: ClassVar[str] = "ArtifactClassification"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ArtifactClassification

    classificationConfidence: Optional[Union[Decimal, DecimalType]] = None
    class: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.classificationConfidence is not None and not isinstance(self.classificationConfidence, DecimalType):
            self.classificationConfidence = DecimalType(self.classificationConfidence)

        if self.class is not None and not isinstance(self.class, str):
            self.class = str(self.class)

        super().__post_init__(**kwargs)


@dataclass
class ArrayOfAction(UcoInherentCharacterizationThing):
    """
    "An array of action is an ordered list of references to things that may be done or performed."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ArrayOfAction
    class_class_curie: ClassVar[str] = "action:ArrayOfAction"
    class_name: ClassVar[str] = "ArrayOfAction"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ArrayOfAction

    action: Optional[Union[dict, Action]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.action is not None and not isinstance(self.action, Action):
            self.action = Action(**as_dict(self.action))

        super().__post_init__(**kwargs)


@dataclass
class ExternalReference(UcoInherentCharacterizationThing):
    """
    Characteristics of a reference to a resource outside of the UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ExternalReference
    class_class_curie: ClassVar[str] = "core:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ExternalReference

    referenceURL: Optional[Union[str, IriType]] = None
    definingContext: Optional[str] = None
    externalIdentifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.referenceURL is not None and not isinstance(self.referenceURL, IriType):
            self.referenceURL = IriType(self.referenceURL)

        if self.definingContext is not None and not isinstance(self.definingContext, str):
            self.definingContext = str(self.definingContext)

        if self.externalIdentifier is not None and not isinstance(self.externalIdentifier, str):
            self.externalIdentifier = str(self.externalIdentifier)

        super().__post_init__(**kwargs)


class Facet(UcoInherentCharacterizationThing):
    """
    A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Facet
    class_class_curie: ClassVar[str] = "core:Facet"
    class_name: ClassVar[str] = "Facet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Facet


class AnalyticResultFacet(Facet):
    """
    "An analytic result facet is a grouping of characteristics unique to the results of an analysis action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.AnalyticResultFacet
    class_class_curie: ClassVar[str] = "analysis:AnalyticResultFacet"
    class_name: ClassVar[str] = "AnalyticResultFacet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.AnalyticResultFacet


@dataclass
class ArtifactClassificationResultFacet(AnalyticResultFacet):
    """
    "An artifact classification result facet is a grouping of characteristics unique to the results of an artifact
    classification analysis action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.ArtifactClassificationResultFacet
    class_class_curie: ClassVar[str] = "analysis:ArtifactClassificationResultFacet"
    class_name: ClassVar[str] = "ArtifactClassificationResultFacet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ArtifactClassificationResultFacet

    classification: Optional[Union[Union[dict, ArtifactClassification], List[Union[dict, ArtifactClassification]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.classification, list):
            self.classification = [self.classification] if self.classification is not None else []
        self.classification = [v if isinstance(v, ArtifactClassification) else ArtifactClassification(**as_dict(v)) for v in self.classification]

        super().__post_init__(**kwargs)


@dataclass
class ActionArgumentFacet(Facet):
    """
    "An action argument facet is a grouping of characteristics unique to a single parameter of an action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionArgumentFacet
    class_class_curie: ClassVar[str] = "action:ActionArgumentFacet"
    class_name: ClassVar[str] = "ActionArgumentFacet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ActionArgumentFacet

    argumentName: str = None
    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.argumentName):
            self.MissingRequiredField("argumentName")
        if not isinstance(self.argumentName, str):
            self.argumentName = str(self.argumentName)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class ActionEstimationFacet(Facet):
    """
    "An action estimation facet is a grouping of characteristics unique to decision-focused approximation aspects for
    an action that may potentially be performed."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionEstimationFacet
    class_class_curie: ClassVar[str] = "action:ActionEstimationFacet"
    class_name: ClassVar[str] = "ActionEstimationFacet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ActionEstimationFacet

    estimatedCost: Optional[str] = None
    estimatedEfficacy: Optional[str] = None
    estimatedImpact: Optional[str] = None
    objective: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.estimatedCost is not None and not isinstance(self.estimatedCost, str):
            self.estimatedCost = str(self.estimatedCost)

        if self.estimatedEfficacy is not None and not isinstance(self.estimatedEfficacy, str):
            self.estimatedEfficacy = str(self.estimatedEfficacy)

        if self.estimatedImpact is not None and not isinstance(self.estimatedImpact, str):
            self.estimatedImpact = str(self.estimatedImpact)

        if self.objective is not None and not isinstance(self.objective, str):
            self.objective = str(self.objective)

        super().__post_init__(**kwargs)


@dataclass
class ActionFrequencyFacet(Facet):
    """
    "An action frequency facet is a grouping of characteristics unique to the frequency of occurrence for an action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionFrequencyFacet
    class_class_curie: ClassVar[str] = "action:ActionFrequencyFacet"
    class_name: ClassVar[str] = "ActionFrequencyFacet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ActionFrequencyFacet

    rate: Union[Decimal, DecimalType] = None
    scale: str = None
    units: str = None
    trend: Union[str, "TrendEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rate):
            self.MissingRequiredField("rate")
        if not isinstance(self.rate, DecimalType):
            self.rate = DecimalType(self.rate)

        if self._is_empty(self.scale):
            self.MissingRequiredField("scale")
        if not isinstance(self.scale, str):
            self.scale = str(self.scale)

        if self._is_empty(self.units):
            self.MissingRequiredField("units")
        if not isinstance(self.units, str):
            self.units = str(self.units)

        if self._is_empty(self.trend):
            self.MissingRequiredField("trend")
        if not isinstance(self.trend, TrendEnum):
            self.trend = TrendEnum(self.trend)

        super().__post_init__(**kwargs)


@dataclass
class ConfidenceFacet(Facet):
    """
    A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some
    information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ConfidenceFacet
    class_class_curie: ClassVar[str] = "core:ConfidenceFacet"
    class_name: ClassVar[str] = "ConfidenceFacet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ConfidenceFacet

    confidence: Union[int, NonNegativeIntegerType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.confidence):
            self.MissingRequiredField("confidence")
        if not isinstance(self.confidence, NonNegativeIntegerType):
            self.confidence = NonNegativeIntegerType(self.confidence)

        super().__post_init__(**kwargs)


@dataclass
class UcoObject(UcoThing):
    """
    A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or
    indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and
    relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent,
    unifying and interoperable foundation for all explicit and inter-relatable content objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoObject
    class_class_curie: ClassVar[str] = "core:UcoObject"
    class_name: ClassVar[str] = "UcoObject"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.UcoObject

    createdBy: Optional[str] = None
    description: Optional[Union[str, List[str]]] = empty_list()
    externalReference: Optional[Union[str, List[str]]] = empty_list()
    hasFacet: Optional[Union[str, List[str]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectMarking: Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]] = empty_list()
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.createdBy is not None and not isinstance(self.createdBy, str):
            self.createdBy = str(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, str) else str(v) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, str) else str(v) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstraction) else MarkingDefinitionAbstraction(**as_dict(v)) for v in self.objectMarking]

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        super().__post_init__(**kwargs)


@dataclass
class Action(UcoObject):
    """
    "An action is something that may be done or performed."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.Action
    class_class_curie: ClassVar[str] = "action:Action"
    class_name: ClassVar[str] = "Action"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Action

    subaction: Optional[Union[Union[dict, "Action"], List[Union[dict, "Action"]]]] = empty_list()
    environment: Optional[Union[dict, "UcoObject"]] = None
    performer: Optional[Union[dict, "UcoObject"]] = None
    error: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    instrument: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    object: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    participant: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    result: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    location: Optional[Union[Union[dict, "Location"], List[Union[dict, "Location"]]]] = empty_list()
    endTime: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    actionCount: Optional[Union[int, NonNegativeIntegerType]] = None
    actionStatus: Optional[Union[str, "ActionStatusTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.subaction, list):
            self.subaction = [self.subaction] if self.subaction is not None else []
        self.subaction = [v if isinstance(v, Action) else Action(**as_dict(v)) for v in self.subaction]

        if self.environment is not None and not isinstance(self.environment, UcoObject):
            self.environment = UcoObject(**as_dict(self.environment))

        if self.performer is not None and not isinstance(self.performer, UcoObject):
            self.performer = UcoObject(**as_dict(self.performer))

        if not isinstance(self.error, list):
            self.error = [self.error] if self.error is not None else []
        self.error = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.error]

        if not isinstance(self.instrument, list):
            self.instrument = [self.instrument] if self.instrument is not None else []
        self.instrument = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.instrument]

        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        if not isinstance(self.participant, list):
            self.participant = [self.participant] if self.participant is not None else []
        self.participant = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.participant]

        if not isinstance(self.result, list):
            self.result = [self.result] if self.result is not None else []
        self.result = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.result]

        if not isinstance(self.location, list):
            self.location = [self.location] if self.location is not None else []
        self.location = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.location]

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.actionCount is not None and not isinstance(self.actionCount, NonNegativeIntegerType):
            self.actionCount = NonNegativeIntegerType(self.actionCount)

        if self.actionStatus is not None and not isinstance(self.actionStatus, ActionStatusTypeEnum):
            self.actionStatus = ActionStatusTypeEnum(self.actionStatus)

        super().__post_init__(**kwargs)


class Analysis(Action):
    """
    "An analysis is an action of detailed examination of something in order to understand its nature, context or
    essential features."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.Analysis
    class_class_curie: ClassVar[str] = "analysis:Analysis"
    class_name: ClassVar[str] = "Analysis"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Analysis


@dataclass
class ActionLifecycle(Action):
    """
    "An action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action
    lifecycles."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionLifecycle
    class_class_curie: ClassVar[str] = "action:ActionLifecycle"
    class_name: ClassVar[str] = "ActionLifecycle"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ActionLifecycle

    phase: Union[dict, "ArrayOfAction"] = None
    error: Optional[Union[dict, "UcoObject"]] = None
    endTime: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    actionCount: Optional[Union[int, NonNegativeIntegerType]] = None
    actionStatus: Optional[Union[str, "ActionStatusTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.phase):
            self.MissingRequiredField("phase")
        if not isinstance(self.phase, ArrayOfAction):
            self.phase = ArrayOfAction(**as_dict(self.phase))

        if self.error is not None and not isinstance(self.error, UcoObject):
            self.error = UcoObject(**as_dict(self.error))

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.actionCount is not None and not isinstance(self.actionCount, NonNegativeIntegerType):
            self.actionCount = NonNegativeIntegerType(self.actionCount)

        if not isinstance(self.error, list):
            self.error = [self.error] if self.error is not None else []
        self.error = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.error]

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.actionStatus is not None and not isinstance(self.actionStatus, ActionStatusTypeEnum):
            self.actionStatus = ActionStatusTypeEnum(self.actionStatus)

        super().__post_init__(**kwargs)


class ActionPattern(Action):
    """
    "An action pattern is a grouping of characteristics unique to a combination of actions forming a consistent or
    characteristic arrangement."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionPattern
    class_class_curie: ClassVar[str] = "action:ActionPattern"
    class_name: ClassVar[str] = "ActionPattern"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ActionPattern


@dataclass
class Assertion(UcoObject):
    """
    An assertion is a statement declared to be true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Assertion
    class_class_curie: ClassVar[str] = "core:Assertion"
    class_name: ClassVar[str] = "Assertion"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Assertion

    statement: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.statement, list):
            self.statement = [self.statement] if self.statement is not None else []
        self.statement = [v if isinstance(v, str) else str(v) for v in self.statement]

        super().__post_init__(**kwargs)


@dataclass
class AnalyticResult(Assertion):
    """
    "An analytic result is a characterization of the understanding resulting from an analysis action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.AnalyticResult
    class_class_curie: ClassVar[str] = "analysis:AnalyticResult"
    class_name: ClassVar[str] = "AnalyticResult"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.AnalyticResult

    originatingAnalysis: Optional[Union[dict, Analysis]] = None
    resultContent: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.originatingAnalysis is not None and not isinstance(self.originatingAnalysis, Analysis):
            self.originatingAnalysis = Analysis(**as_dict(self.originatingAnalysis))

        if not isinstance(self.resultContent, list):
            self.resultContent = [self.resultContent] if self.resultContent is not None else []
        self.resultContent = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.resultContent]

        super().__post_init__(**kwargs)


@dataclass
class Annotation(Assertion):
    """
    An annotation is an assertion made in relation to one or more objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Annotation
    class_class_curie: ClassVar[str] = "core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Annotation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class AttributedName(UcoObject):
    """
    An attributed name is a name of an entity issued by some attributed naming authority.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.AttributedName
    class_class_curie: ClassVar[str] = "core:AttributedName"
    class_name: ClassVar[str] = "AttributedName"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.AttributedName

    namingAuthority: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.namingAuthority is not None and not isinstance(self.namingAuthority, str):
            self.namingAuthority = str(self.namingAuthority)

        super().__post_init__(**kwargs)


class Compilation(UcoObject):
    """
    A compilation is a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Compilation
    class_class_curie: ClassVar[str] = "core:Compilation"
    class_name: ClassVar[str] = "Compilation"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Compilation


@dataclass
class ContextualCompilation(Compilation):
    """
    A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed
    on a given day, all accounts associated with a given person).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ContextualCompilation
    class_class_curie: ClassVar[str] = "core:ContextualCompilation"
    class_name: ClassVar[str] = "ContextualCompilation"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ContextualCompilation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class ControlledVocabulary(UcoObject):
    """
    A controlled vocabulary is an explicitly constrained set of string values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ControlledVocabulary
    class_class_curie: ClassVar[str] = "core:ControlledVocabulary"
    class_name: ClassVar[str] = "ControlledVocabulary"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ControlledVocabulary

    value: str = None
    constrainingVocabularyReference: Optional[Union[str, IriType]] = None
    constrainingVocabularyName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.constrainingVocabularyReference is not None and not isinstance(self.constrainingVocabularyReference, IriType):
            self.constrainingVocabularyReference = IriType(self.constrainingVocabularyReference)

        if self.constrainingVocabularyName is not None and not isinstance(self.constrainingVocabularyName, str):
            self.constrainingVocabularyName = str(self.constrainingVocabularyName)

        super().__post_init__(**kwargs)


@dataclass
class EnclosingCompilation(Compilation):
    """
    An enclosing compilation is a container for a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.EnclosingCompilation
    class_class_curie: ClassVar[str] = "core:EnclosingCompilation"
    class_name: ClassVar[str] = "EnclosingCompilation"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.EnclosingCompilation

    object: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


class Bundle(EnclosingCompilation):
    """
    A bundle is a container for a grouping of UCO content with no presumption of shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Bundle
    class_class_curie: ClassVar[str] = "core:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Bundle


@dataclass
class Grouping(ContextualCompilation):
    """
    A grouping is a compilation of referenced UCO content with a shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Grouping
    class_class_curie: ClassVar[str] = "core:Grouping"
    class_name: ClassVar[str] = "Grouping"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Grouping

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    context: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.context, list):
            self.context = [self.context] if self.context is not None else []
        self.context = [v if isinstance(v, str) else str(v) for v in self.context]

        super().__post_init__(**kwargs)


class IdentityAbstraction(UcoObject):
    """
    An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the identity:Identity class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.IdentityAbstraction
    class_class_curie: ClassVar[str] = "core:IdentityAbstraction"
    class_name: ClassVar[str] = "IdentityAbstraction"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.IdentityAbstraction


class Item(UcoObject):
    """
    An item is a distinct article or unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Item
    class_class_curie: ClassVar[str] = "core:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Item


class MarkingDefinitionAbstraction(UcoObject):
    """
    A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data
    marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the marking MarkingDefinition class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.MarkingDefinitionAbstraction
    class_class_curie: ClassVar[str] = "core:MarkingDefinitionAbstraction"
    class_name: ClassVar[str] = "MarkingDefinitionAbstraction"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.MarkingDefinitionAbstraction


class ModusOperandi(UcoObject):
    """
    A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ModusOperandi
    class_class_curie: ClassVar[str] = "core:ModusOperandi"
    class_name: ClassVar[str] = "ModusOperandi"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ModusOperandi


@dataclass
class Relationship(UcoObject):
    """
    A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to
    another object in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Relationship
    class_class_curie: ClassVar[str] = "core:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Relationship

    isDirectional: Union[bool, BooleanType] = None
    source: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    target: Union[dict, "UcoObject"] = None
    endTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    kindOfRelationship: Optional[str] = None
    startTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.isDirectional):
            self.MissingRequiredField("isDirectional")
        if not isinstance(self.isDirectional, BooleanType):
            self.isDirectional = BooleanType(self.isDirectional)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.source]

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, UcoObject):
            self.target = UcoObject(**as_dict(self.target))

        if not isinstance(self.endTime, list):
            self.endTime = [self.endTime] if self.endTime is not None else []
        self.endTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.endTime]

        if self.kindOfRelationship is not None and not isinstance(self.kindOfRelationship, str):
            self.kindOfRelationship = str(self.kindOfRelationship)

        if not isinstance(self.startTime, list):
            self.startTime = [self.startTime] if self.startTime is not None else []
        self.startTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.startTime]

        super().__post_init__(**kwargs)


@dataclass
class GPSCoordinatesFacet(Facet):
    """
    A GPS coordinates facet is a grouping of characteristics unique to the expression of quantified dilution of
    precision (DOP) for an asserted set of geolocation coordinates typically associated with satellite navigation such
    as the Global Positioning System (GPS).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.GPSCoordinatesFacet
    class_class_curie: ClassVar[str] = "location:GPSCoordinatesFacet"
    class_name: ClassVar[str] = "GPSCoordinatesFacet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.GPSCoordinatesFacet

    hdop: Optional[Union[Decimal, DecimalType]] = None
    pdop: Optional[Union[Decimal, DecimalType]] = None
    tdop: Optional[Union[Decimal, DecimalType]] = None
    vdop: Optional[Union[Decimal, DecimalType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hdop is not None and not isinstance(self.hdop, DecimalType):
            self.hdop = DecimalType(self.hdop)

        if self.pdop is not None and not isinstance(self.pdop, DecimalType):
            self.pdop = DecimalType(self.pdop)

        if self.tdop is not None and not isinstance(self.tdop, DecimalType):
            self.tdop = DecimalType(self.tdop)

        if self.vdop is not None and not isinstance(self.vdop, DecimalType):
            self.vdop = DecimalType(self.vdop)

        super().__post_init__(**kwargs)


@dataclass
class LatLongCoordinatesFacet(Facet):
    """
    A lat long coordinates facet is a grouping of characteristics unique to the expression of a geolocation as the
    intersection of specific latitude, longitude, and altitude values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.LatLongCoordinatesFacet
    class_class_curie: ClassVar[str] = "location:LatLongCoordinatesFacet"
    class_name: ClassVar[str] = "LatLongCoordinatesFacet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.LatLongCoordinatesFacet

    altitude: Optional[Union[Decimal, DecimalType]] = None
    latitude: Optional[Union[Decimal, DecimalType]] = None
    longitude: Optional[Union[Decimal, DecimalType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.altitude is not None and not isinstance(self.altitude, DecimalType):
            self.altitude = DecimalType(self.altitude)

        if self.latitude is not None and not isinstance(self.latitude, DecimalType):
            self.latitude = DecimalType(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, DecimalType):
            self.longitude = DecimalType(self.longitude)

        super().__post_init__(**kwargs)


class Location(UcoObject):
    """
    A location is a geospatial place, site, or position.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.Location
    class_class_curie: ClassVar[str] = "location:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Location


@dataclass
class SimpleAddressFacet(Facet):
    """
    A simple address facet is a grouping of characteristics unique to a geolocation expressed as an administrative
    address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.SimpleAddressFacet
    class_class_curie: ClassVar[str] = "location:SimpleAddressFacet"
    class_name: ClassVar[str] = "SimpleAddressFacet"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.SimpleAddressFacet

    addressType: Optional[str] = None
    country: Optional[str] = None
    locality: Optional[str] = None
    postalCode: Optional[str] = None
    region: Optional[str] = None
    street: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.addressType is not None and not isinstance(self.addressType, str):
            self.addressType = str(self.addressType)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        if self.locality is not None and not isinstance(self.locality, str):
            self.locality = str(self.locality)

        if self.postalCode is not None and not isinstance(self.postalCode, str):
            self.postalCode = str(self.postalCode)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.street is not None and not isinstance(self.street, str):
            self.street = str(self.street)

        super().__post_init__(**kwargs)


class Pattern(UcoObject):
    """
    A pattern is a combination of properties, acts, tendencies, etc., forming a consistent or characteristic
    arrangement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATTERN.Pattern
    class_class_curie: ClassVar[str] = "pattern:Pattern"
    class_name: ClassVar[str] = "Pattern"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Pattern


@dataclass
class LogicalPattern(Pattern):
    """
    A logical pattern is a grouping of characteristics unique to an informational pattern expressed via a structured
    pattern expression following the rules of logic.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATTERN.LogicalPattern
    class_class_curie: ClassVar[str] = "pattern:LogicalPattern"
    class_name: ClassVar[str] = "LogicalPattern"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.LogicalPattern

    patternExpression: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.patternExpression is not None and not isinstance(self.patternExpression, str):
            self.patternExpression = str(self.patternExpression)

        super().__post_init__(**kwargs)


class PatternExpression(UcoInherentCharacterizationThing):
    """
    A pattern expression is a grouping of characteristics unique to an explicit logical expression defining a pattern
    (e.g., regular expression, SQL Select expression, etc.).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATTERN.PatternExpression
    class_class_curie: ClassVar[str] = "pattern:PatternExpression"
    class_name: ClassVar[str] = "PatternExpression"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.PatternExpression


@dataclass
class Dictionary(UcoInherentCharacterizationThing):
    """
    "A dictionary is list of (term/key, value) pairs with each term/key existing no more than once."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Dictionary
    class_class_curie: ClassVar[str] = "types:Dictionary"
    class_name: ClassVar[str] = "Dictionary"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Dictionary

    entry: Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.entry):
            self.MissingRequiredField("entry")
        self._normalize_inlined_as_dict(slot_name="entry", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ControlledDictionary(Dictionary):
    """
    "A controlled dictionary is a list of (term/key, value) pairs where each term/key exists no more than once and is
    constrained to an explicitly defined set of values."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.ControlledDictionary
    class_class_curie: ClassVar[str] = "types:ControlledDictionary"
    class_name: ClassVar[str] = "ControlledDictionary"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ControlledDictionary

    entry: Optional[Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entry", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DictionaryEntry(UcoInherentCharacterizationThing):
    """
    "A dictionary entry is a single (term/key, value) pair."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.DictionaryEntry
    class_class_curie: ClassVar[str] = "types:DictionaryEntry"
    class_name: ClassVar[str] = "DictionaryEntry"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.DictionaryEntry

    key: str = None
    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, str):
            self.key = str(self.key)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class ControlledDictionaryEntry(DictionaryEntry):
    """
    "A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an
    explicitly defined set of values."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.ControlledDictionaryEntry
    class_class_curie: ClassVar[str] = "types:ControlledDictionaryEntry"
    class_name: ClassVar[str] = "ControlledDictionaryEntry"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ControlledDictionaryEntry

    key: str = None
    value: str = None

@dataclass
class Hash(UcoInherentCharacterizationThing):
    """
    "A hash is a grouping of characteristics unique to the result of applying a mathematical algorithm that maps data
    of arbitrary size to a bit string (the 'hash') and is a one-way function, that is, a function which is practically
    infeasible to invert. This is commonly used for integrity checking of data. [based on
    https://en.wikipedia.org/wiki/Cryptographic_hash_function]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Hash
    class_class_curie: ClassVar[str] = "types:Hash"
    class_name: ClassVar[str] = "Hash"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Hash

    hashValue: hex = None
    hashMethod: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.hashValue):
            self.MissingRequiredField("hashValue")
        if not isinstance(self.hashValue, hex):
            self.hashValue = hex(self.hashValue)

        if self._is_empty(self.hashMethod):
            self.MissingRequiredField("hashMethod")
        if not isinstance(self.hashMethod, str):
            self.hashMethod = str(self.hashMethod)

        super().__post_init__(**kwargs)


@dataclass
class ThreadItem(YAMLRoot):
    """
    "A ThreadItem is a member of a thread."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.CoItem
    class_class_curie: ClassVar[str] = "collections:CoItem"
    class_name: ClassVar[str] = "ThreadItem"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ThreadItem

    itemContent: Optional[Union[Union[dict, "CoItem"], List[Union[dict, "CoItem"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.itemContent, list):
            self.itemContent = [self.itemContent] if self.itemContent is not None else []
        self.itemContent = [v if isinstance(v, CoItem) else CoItem(**as_dict(v)) for v in self.itemContent]

        super().__post_init__(**kwargs)


class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Thing
    class_class_curie: ClassVar[str] = "collections:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Thing


@dataclass
class Collection(Thing):
    """
    A group of objects that can be considered as a whole.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Collection
    class_class_curie: ClassVar[str] = "collections:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Collection

    element: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    size: Optional[Union[int, PositiveInteger]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.element]

        if self.size is not None and not isinstance(self.size, PositiveInteger):
            self.size = PositiveInteger(self.size)

        super().__post_init__(**kwargs)


class Bag(Collection):
    """
    Collection that can have a number of copies of each object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Bag
    class_class_curie: ClassVar[str] = "collections:Bag"
    class_name: ClassVar[str] = "Bag"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Bag


@dataclass
class Thread(Bag):
    """
    "A semi-ordered array of items, that can be present in multiple copies. Implemetation of a UCO Thread is similar
    to a Collections Ontology List, except a Thread may fork and merge - that is, one of its members may have two or
    more direct successors, and two or more direct predecessors."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Thread
    class_class_curie: ClassVar[str] = "types:Thread"
    class_name: ClassVar[str] = "Thread"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Thread

    item: Optional[Union[Union[dict, "ThreadItem"], List[Union[dict, "ThreadItem"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.item, list):
            self.item = [self.item] if self.item is not None else []
        self.item = [v if isinstance(v, ThreadItem) else ThreadItem(**as_dict(v)) for v in self.item]

        super().__post_init__(**kwargs)


@dataclass
class CoItem(Thing):
    """
    Element belonging to a bag
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.CoItem
    class_class_curie: ClassVar[str] = "collections:CoItem"
    class_name: ClassVar[str] = "CoItem"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.CoItem

    itemOf: Optional[Union[dict, Bag]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.itemOf is not None and not isinstance(self.itemOf, Bag):
            self.itemOf = Bag(**as_dict(self.itemOf))

        super().__post_init__(**kwargs)


@dataclass
class List(Bag):
    """
    An ordered array of items, that can be present in multiple copies
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.List
    class_class_curie: ClassVar[str] = "collections:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.List

    item: Optional[Union[Union[dict, "ListItem"], List[Union[dict, "ListItem"]]]] = empty_list()
    lastItem: Optional[Union[dict, "ListItem"]] = None
    firstItem: Optional[Union[dict, "ListItem"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="item", slot_type=ListItem, key_name="_index", keyed=False)

        if self.lastItem is not None and not isinstance(self.lastItem, ListItem):
            self.lastItem = ListItem(**as_dict(self.lastItem))

        if self.firstItem is not None and not isinstance(self.firstItem, ListItem):
            self.firstItem = ListItem(**as_dict(self.firstItem))

        super().__post_init__(**kwargs)


@dataclass
class ListItem(CoItem):
    """
    element belonging to a list
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.ListItem
    class_class_curie: ClassVar[str] = "collections:ListItem"
    class_name: ClassVar[str] = "ListItem"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.ListItem

    _index: Union[int, PositiveInteger] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self._index):
            self.MissingRequiredField("_index")
        if not isinstance(self._index, PositiveInteger):
            self._index = PositiveInteger(self._index)

        super().__post_init__(**kwargs)


class Set(Collection):
    """
    A collection that cannot contain duplicate elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Set
    class_class_curie: ClassVar[str] = "collections:Set"
    class_name: ClassVar[str] = "Set"
    class_model_uri: ClassVar[URIRef] = ANALYSIS.Set


# Enumerations
class AccountTypeEnum(EnumDefinitionImpl):
    """
    "An account type represents the endpoint type where the account is located; for example, ADS for an
    ActiveDirectory endpoint type, or LDAP for an LDAP, etc."
    """
    ldap = PermissibleValue(text="ldap")
    nis = PermissibleValue(text="nis")
    openid = PermissibleValue(text="openid")
    radius = PermissibleValue(text="radius")
    tacacs = PermissibleValue(text="tacacs")
    unix = PermissibleValue(text="unix")
    windows_domain = PermissibleValue(text="windows_domain")
    windows_local = PermissibleValue(text="windows_local")

    _defn = EnumDefinition(
        name="AccountTypeEnum",
        description="\"An account type represents the endpoint type where the account is located; for example, ADS for an ActiveDirectory endpoint type, or LDAP for an LDAP, etc.\"",
    )

class ActionArgumentNameEnum(EnumDefinitionImpl):

    API = PermissibleValue(text="API")
    Command = PermissibleValue(text="Command")
    Flags = PermissibleValue(text="Flags")
    Hostname = PermissibleValue(text="Hostname")
    Options = PermissibleValue(text="Options")
    Password = PermissibleValue(text="Password")
    Protection = PermissibleValue(text="Protection")
    Reason = PermissibleValue(text="Reason")
    Server = PermissibleValue(text="Server")
    Username = PermissibleValue(text="Username")

    _defn = EnumDefinition(
        name="ActionArgumentNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "APC Address",
                PermissibleValue(text="APC Address") )
        setattr(cls, "APC Mode",
                PermissibleValue(text="APC Mode") )
        setattr(cls, "Access Mode",
                PermissibleValue(text="Access Mode") )
        setattr(cls, "Application Name",
                PermissibleValue(text="Application Name") )
        setattr(cls, "Base Address",
                PermissibleValue(text="Base Address") )
        setattr(cls, "Callback Address",
                PermissibleValue(text="Callback Address") )
        setattr(cls, "Code Address",
                PermissibleValue(text="Code Address") )
        setattr(cls, "Control Code",
                PermissibleValue(text="Control Code") )
        setattr(cls, "Control Parameter",
                PermissibleValue(text="Control Parameter") )
        setattr(cls, "Creation Flags",
                PermissibleValue(text="Creation Flags") )
        setattr(cls, "Database Name",
                PermissibleValue(text="Database Name") )
        setattr(cls, "Delay Time (ms)",
                PermissibleValue(text="Delay Time (ms)") )
        setattr(cls, "Destination Address",
                PermissibleValue(text="Destination Address") )
        setattr(cls, "Error Control",
                PermissibleValue(text="Error Control") )
        setattr(cls, "File Information Class",
                PermissibleValue(text="File Information Class") )
        setattr(cls, "Function Address",
                PermissibleValue(text="Function Address") )
        setattr(cls, "Function Name",
                PermissibleValue(text="Function Name") )
        setattr(cls, "Function Ordinal",
                PermissibleValue(text="Function Ordinal") )
        setattr(cls, "Hook Type",
                PermissibleValue(text="Hook Type") )
        setattr(cls, "Host Name",
                PermissibleValue(text="Host Name") )
        setattr(cls, "Initial Owner",
                PermissibleValue(text="Initial Owner") )
        setattr(cls, "Mapping Offset",
                PermissibleValue(text="Mapping Offset") )
        setattr(cls, "Number of Bytes Per Send",
                PermissibleValue(text="Number of Bytes Per Send") )
        setattr(cls, "Parameter Address",
                PermissibleValue(text="Parameter Address") )
        setattr(cls, "Privilege Name",
                PermissibleValue(text="Privilege Name") )
        setattr(cls, "Proxy Bypass",
                PermissibleValue(text="Proxy Bypass") )
        setattr(cls, "Proxy Name",
                PermissibleValue(text="Proxy Name") )
        setattr(cls, "Request Size",
                PermissibleValue(text="Request Size") )
        setattr(cls, "Requested Version",
                PermissibleValue(text="Requested Version") )
        setattr(cls, "Service Name",
                PermissibleValue(text="Service Name") )
        setattr(cls, "Service State",
                PermissibleValue(text="Service State") )
        setattr(cls, "Service Type",
                PermissibleValue(text="Service Type") )
        setattr(cls, "Share Mode",
                PermissibleValue(text="Share Mode") )
        setattr(cls, "Shutdown Flag",
                PermissibleValue(text="Shutdown Flag") )
        setattr(cls, "Size (bytes)",
                PermissibleValue(text="Size (bytes)") )
        setattr(cls, "Sleep Time (ms)",
                PermissibleValue(text="Sleep Time (ms)") )
        setattr(cls, "Source Address",
                PermissibleValue(text="Source Address") )
        setattr(cls, "Starting Address",
                PermissibleValue(text="Starting Address") )
        setattr(cls, "System Metric Index",
                PermissibleValue(text="System Metric Index") )
        setattr(cls, "Target PID",
                PermissibleValue(text="Target PID") )
        setattr(cls, "Transfer Flags",
                PermissibleValue(text="Transfer Flags") )

class ActionNameEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ActionNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Accept Socket Connection",
                PermissibleValue(text="Accept Socket Connection") )
        setattr(cls, "Add Connection to Network Share",
                PermissibleValue(text="Add Connection to Network Share") )
        setattr(cls, "Add Network Share",
                PermissibleValue(text="Add Network Share") )
        setattr(cls, "Add Scheduled Task",
                PermissibleValue(text="Add Scheduled Task") )
        setattr(cls, "Add System Call Hook",
                PermissibleValue(text="Add System Call Hook") )
        setattr(cls, "Add User",
                PermissibleValue(text="Add User") )
        setattr(cls, "Add Windows Hook",
                PermissibleValue(text="Add Windows Hook") )
        setattr(cls, "Allocate Virtual Memory in Process",
                PermissibleValue(text="Allocate Virtual Memory in Process") )
        setattr(cls, "Bind Address to Socket",
                PermissibleValue(text="Bind Address to Socket") )
        setattr(cls, "Change Service Configuration",
                PermissibleValue(text="Change Service Configuration") )
        setattr(cls, "Check for Remote Debugger",
                PermissibleValue(text="Check for Remote Debugger") )
        setattr(cls, "Close Port",
                PermissibleValue(text="Close Port") )
        setattr(cls, "Close Registry Key",
                PermissibleValue(text="Close Registry Key") )
        setattr(cls, "Close Socket",
                PermissibleValue(text="Close Socket") )
        setattr(cls, "Configure Service",
                PermissibleValue(text="Configure Service") )
        setattr(cls, "Connect to IP",
                PermissibleValue(text="Connect to IP") )
        setattr(cls, "Connect to Named Pipe",
                PermissibleValue(text="Connect to Named Pipe") )
        setattr(cls, "Connect to Network Share",
                PermissibleValue(text="Connect to Network Share") )
        setattr(cls, "Connect to Socket",
                PermissibleValue(text="Connect to Socket") )
        setattr(cls, "Connect to URL",
                PermissibleValue(text="Connect to URL") )
        setattr(cls, "Control Driver",
                PermissibleValue(text="Control Driver") )
        setattr(cls, "Control Service",
                PermissibleValue(text="Control Service") )
        setattr(cls, "Copy File",
                PermissibleValue(text="Copy File") )
        setattr(cls, "Create Dialog Box",
                PermissibleValue(text="Create Dialog Box") )
        setattr(cls, "Create Directory",
                PermissibleValue(text="Create Directory") )
        setattr(cls, "Create Event",
                PermissibleValue(text="Create Event") )
        setattr(cls, "Create File",
                PermissibleValue(text="Create File") )
        setattr(cls, "Create File Alternate Data Stream",
                PermissibleValue(text="Create File Alternate Data Stream") )
        setattr(cls, "Create File Mapping",
                PermissibleValue(text="Create File Mapping") )
        setattr(cls, "Create File Symbolic Link",
                PermissibleValue(text="Create File Symbolic Link") )
        setattr(cls, "Create Hidden File",
                PermissibleValue(text="Create Hidden File") )
        setattr(cls, "Create Mailslot",
                PermissibleValue(text="Create Mailslot") )
        setattr(cls, "Create Module",
                PermissibleValue(text="Create Module") )
        setattr(cls, "Create Mutex",
                PermissibleValue(text="Create Mutex") )
        setattr(cls, "Create Named Pipe",
                PermissibleValue(text="Create Named Pipe") )
        setattr(cls, "Create Process",
                PermissibleValue(text="Create Process") )
        setattr(cls, "Create Process as User",
                PermissibleValue(text="Create Process as User") )
        setattr(cls, "Create Registry Key",
                PermissibleValue(text="Create Registry Key") )
        setattr(cls, "Create Registry Key Value",
                PermissibleValue(text="Create Registry Key Value") )
        setattr(cls, "Create Remote Thread in Process",
                PermissibleValue(text="Create Remote Thread in Process") )
        setattr(cls, "Create Service",
                PermissibleValue(text="Create Service") )
        setattr(cls, "Create Socket",
                PermissibleValue(text="Create Socket") )
        setattr(cls, "Create Symbolic Link",
                PermissibleValue(text="Create Symbolic Link") )
        setattr(cls, "Create Thread",
                PermissibleValue(text="Create Thread") )
        setattr(cls, "Create Window",
                PermissibleValue(text="Create Window") )
        setattr(cls, "Delete Directory",
                PermissibleValue(text="Delete Directory") )
        setattr(cls, "Delete File",
                PermissibleValue(text="Delete File") )
        setattr(cls, "Delete Named Pipe",
                PermissibleValue(text="Delete Named Pipe") )
        setattr(cls, "Delete Network Share",
                PermissibleValue(text="Delete Network Share") )
        setattr(cls, "Delete Registry Key",
                PermissibleValue(text="Delete Registry Key") )
        setattr(cls, "Delete Registry Key Value",
                PermissibleValue(text="Delete Registry Key Value") )
        setattr(cls, "Delete Service",
                PermissibleValue(text="Delete Service") )
        setattr(cls, "Delete User",
                PermissibleValue(text="Delete User") )
        setattr(cls, "Disconnect from Named Pipe",
                PermissibleValue(text="Disconnect from Named Pipe") )
        setattr(cls, "Disconnect from Network Share",
                PermissibleValue(text="Disconnect from Network Share") )
        setattr(cls, "Disconnect from Socket",
                PermissibleValue(text="Disconnect from Socket") )
        setattr(cls, "Download File",
                PermissibleValue(text="Download File") )
        setattr(cls, "Enumerate DLLs",
                PermissibleValue(text="Enumerate DLLs") )
        setattr(cls, "Enumerate Network Shares",
                PermissibleValue(text="Enumerate Network Shares") )
        setattr(cls, "Enumerate Processes",
                PermissibleValue(text="Enumerate Processes") )
        setattr(cls, "Enumerate Protocols",
                PermissibleValue(text="Enumerate Protocols") )
        setattr(cls, "Enumerate Registry Key Subkeys",
                PermissibleValue(text="Enumerate Registry Key Subkeys") )
        setattr(cls, "Enumerate Registry Key Values",
                PermissibleValue(text="Enumerate Registry Key Values") )
        setattr(cls, "Enumerate Services",
                PermissibleValue(text="Enumerate Services") )
        setattr(cls, "Enumerate System Handles",
                PermissibleValue(text="Enumerate System Handles") )
        setattr(cls, "Enumerate Threads",
                PermissibleValue(text="Enumerate Threads") )
        setattr(cls, "Enumerate Threads in Process",
                PermissibleValue(text="Enumerate Threads in Process") )
        setattr(cls, "Enumerate Users",
                PermissibleValue(text="Enumerate Users") )
        setattr(cls, "Enumerate Windows",
                PermissibleValue(text="Enumerate Windows") )
        setattr(cls, "Find File",
                PermissibleValue(text="Find File") )
        setattr(cls, "Find Window",
                PermissibleValue(text="Find Window") )
        setattr(cls, "Flush Process Instruction Cache",
                PermissibleValue(text="Flush Process Instruction Cache") )
        setattr(cls, "Free Library",
                PermissibleValue(text="Free Library") )
        setattr(cls, "Free Process Virtual Memory",
                PermissibleValue(text="Free Process Virtual Memory") )
        setattr(cls, "Get Disk Free Space",
                PermissibleValue(text="Get Disk Free Space") )
        setattr(cls, "Get Disk Type",
                PermissibleValue(text="Get Disk Type") )
        setattr(cls, "Get Elapsed System Up Time",
                PermissibleValue(text="Get Elapsed System Up Time") )
        setattr(cls, "Get File Attributes",
                PermissibleValue(text="Get File Attributes") )
        setattr(cls, "Get Function Address",
                PermissibleValue(text="Get Function Address") )
        setattr(cls, "Get Host By Address",
                PermissibleValue(text="Get Host By Address") )
        setattr(cls, "Get Host By Name",
                PermissibleValue(text="Get Host By Name") )
        setattr(cls, "Get Host Name",
                PermissibleValue(text="Get Host Name") )
        setattr(cls, "Get Library File Name",
                PermissibleValue(text="Get Library File Name") )
        setattr(cls, "Get Library Handle",
                PermissibleValue(text="Get Library Handle") )
        setattr(cls, "Get NetBIOS Name",
                PermissibleValue(text="Get NetBIOS Name") )
        setattr(cls, "Get Process Current Directory",
                PermissibleValue(text="Get Process Current Directory") )
        setattr(cls, "Get Process Environment Variable",
                PermissibleValue(text="Get Process Environment Variable") )
        setattr(cls, "Get Process Startup Information",
                PermissibleValue(text="Get Process Startup Information") )
        setattr(cls, "Get Processes Snapshot",
                PermissibleValue(text="Get Processes Snapshot") )
        setattr(cls, "Get Registry Key Attributes",
                PermissibleValue(text="Get Registry Key Attributes") )
        setattr(cls, "Get Service Status",
                PermissibleValue(text="Get Service Status") )
        setattr(cls, "Get System Global Flags",
                PermissibleValue(text="Get System Global Flags") )
        setattr(cls, "Get System Host Name",
                PermissibleValue(text="Get System Host Name") )
        setattr(cls, "Get System Local Time",
                PermissibleValue(text="Get System Local Time") )
        setattr(cls, "Get System NetBIOS Name",
                PermissibleValue(text="Get System NetBIOS Name") )
        setattr(cls, "Get System Network Parameters",
                PermissibleValue(text="Get System Network Parameters") )
        setattr(cls, "Get System Time",
                PermissibleValue(text="Get System Time") )
        setattr(cls, "Get Thread Context",
                PermissibleValue(text="Get Thread Context") )
        setattr(cls, "Get Thread Username",
                PermissibleValue(text="Get Thread Username") )
        setattr(cls, "Get User Attributes",
                PermissibleValue(text="Get User Attributes") )
        setattr(cls, "Get Username",
                PermissibleValue(text="Get Username") )
        setattr(cls, "Get Windows Directory",
                PermissibleValue(text="Get Windows Directory") )
        setattr(cls, "Get Windows System Directory",
                PermissibleValue(text="Get Windows System Directory") )
        setattr(cls, "Get Windows Temporary Files Directory",
                PermissibleValue(text="Get Windows Temporary Files Directory") )
        setattr(cls, "Hide Window",
                PermissibleValue(text="Hide Window") )
        setattr(cls, "Impersonate Process",
                PermissibleValue(text="Impersonate Process") )
        setattr(cls, "Impersonate Thread",
                PermissibleValue(text="Impersonate Thread") )
        setattr(cls, "Inject Memory Page",
                PermissibleValue(text="Inject Memory Page") )
        setattr(cls, "Kill Process",
                PermissibleValue(text="Kill Process") )
        setattr(cls, "Kill Thread",
                PermissibleValue(text="Kill Thread") )
        setattr(cls, "Kill Window",
                PermissibleValue(text="Kill Window") )
        setattr(cls, "Listen on Port",
                PermissibleValue(text="Listen on Port") )
        setattr(cls, "Listen on Socket",
                PermissibleValue(text="Listen on Socket") )
        setattr(cls, "Load Driver",
                PermissibleValue(text="Load Driver") )
        setattr(cls, "Load Library",
                PermissibleValue(text="Load Library") )
        setattr(cls, "Load Module",
                PermissibleValue(text="Load Module") )
        setattr(cls, "Load and Call Driver",
                PermissibleValue(text="Load and Call Driver") )
        setattr(cls, "Lock File",
                PermissibleValue(text="Lock File") )
        setattr(cls, "Logon as User",
                PermissibleValue(text="Logon as User") )
        setattr(cls, "Map File",
                PermissibleValue(text="Map File") )
        setattr(cls, "Map Library",
                PermissibleValue(text="Map Library") )
        setattr(cls, "Map View of File",
                PermissibleValue(text="Map View of File") )
        setattr(cls, "Modify File",
                PermissibleValue(text="Modify File") )
        setattr(cls, "Modify Named Pipe",
                PermissibleValue(text="Modify Named Pipe") )
        setattr(cls, "Modify Process",
                PermissibleValue(text="Modify Process") )
        setattr(cls, "Modify Registry Key",
                PermissibleValue(text="Modify Registry Key") )
        setattr(cls, "Modify Registry Key Value",
                PermissibleValue(text="Modify Registry Key Value") )
        setattr(cls, "Modify Service",
                PermissibleValue(text="Modify Service") )
        setattr(cls, "Monitor Registry Key",
                PermissibleValue(text="Monitor Registry Key") )
        setattr(cls, "Move File",
                PermissibleValue(text="Move File") )
        setattr(cls, "Open File",
                PermissibleValue(text="Open File") )
        setattr(cls, "Open File Mapping",
                PermissibleValue(text="Open File Mapping") )
        setattr(cls, "Open Mutex",
                PermissibleValue(text="Open Mutex") )
        setattr(cls, "Open Port",
                PermissibleValue(text="Open Port") )
        setattr(cls, "Open Process",
                PermissibleValue(text="Open Process") )
        setattr(cls, "Open Registry Key",
                PermissibleValue(text="Open Registry Key") )
        setattr(cls, "Open Service",
                PermissibleValue(text="Open Service") )
        setattr(cls, "Open Service Control Manager",
                PermissibleValue(text="Open Service Control Manager") )
        setattr(cls, "Protect Virtual Memory",
                PermissibleValue(text="Protect Virtual Memory") )
        setattr(cls, "Query DNS",
                PermissibleValue(text="Query DNS") )
        setattr(cls, "Query Disk Attributes",
                PermissibleValue(text="Query Disk Attributes") )
        setattr(cls, "Query Process Virtual Memory",
                PermissibleValue(text="Query Process Virtual Memory") )
        setattr(cls, "Queue APC in Thread",
                PermissibleValue(text="Queue APC in Thread") )
        setattr(cls, "Read File",
                PermissibleValue(text="Read File") )
        setattr(cls, "Read From Named Pipe",
                PermissibleValue(text="Read From Named Pipe") )
        setattr(cls, "Read From Process Memory",
                PermissibleValue(text="Read From Process Memory") )
        setattr(cls, "Read Registry Key Value",
                PermissibleValue(text="Read Registry Key Value") )
        setattr(cls, "Receive Data on Socket",
                PermissibleValue(text="Receive Data on Socket") )
        setattr(cls, "Receive Email Message",
                PermissibleValue(text="Receive Email Message") )
        setattr(cls, "Release Mutex",
                PermissibleValue(text="Release Mutex") )
        setattr(cls, "Rename File",
                PermissibleValue(text="Rename File") )
        setattr(cls, "Revert Thread to Self",
                PermissibleValue(text="Revert Thread to Self") )
        setattr(cls, "Send Control Code to File",
                PermissibleValue(text="Send Control Code to File") )
        setattr(cls, "Send Control Code to Pipe",
                PermissibleValue(text="Send Control Code to Pipe") )
        setattr(cls, "Send Control Code to Service",
                PermissibleValue(text="Send Control Code to Service") )
        setattr(cls, "Send DNS Query",
                PermissibleValue(text="Send DNS Query") )
        setattr(cls, "Send Data on Socket",
                PermissibleValue(text="Send Data on Socket") )
        setattr(cls, "Send Data to Address on Socket",
                PermissibleValue(text="Send Data to Address on Socket") )
        setattr(cls, "Send Email Message",
                PermissibleValue(text="Send Email Message") )
        setattr(cls, "Send ICMP Request",
                PermissibleValue(text="Send ICMP Request") )
        setattr(cls, "Send Reverse DNS Query",
                PermissibleValue(text="Send Reverse DNS Query") )
        setattr(cls, "Set File Attributes",
                PermissibleValue(text="Set File Attributes") )
        setattr(cls, "Set NetBIOS Name",
                PermissibleValue(text="Set NetBIOS Name") )
        setattr(cls, "Set Process Current Directory",
                PermissibleValue(text="Set Process Current Directory") )
        setattr(cls, "Set Process Environment Variable",
                PermissibleValue(text="Set Process Environment Variable") )
        setattr(cls, "Set System Global Flags",
                PermissibleValue(text="Set System Global Flags") )
        setattr(cls, "Set System Host Name",
                PermissibleValue(text="Set System Host Name") )
        setattr(cls, "Set System Time",
                PermissibleValue(text="Set System Time") )
        setattr(cls, "Set Thread Context",
                PermissibleValue(text="Set Thread Context") )
        setattr(cls, "Show Window",
                PermissibleValue(text="Show Window") )
        setattr(cls, "Shutdown System",
                PermissibleValue(text="Shutdown System") )
        setattr(cls, "Sleep Process",
                PermissibleValue(text="Sleep Process") )
        setattr(cls, "Sleep System",
                PermissibleValue(text="Sleep System") )
        setattr(cls, "Start Service",
                PermissibleValue(text="Start Service") )
        setattr(cls, "Unload Driver",
                PermissibleValue(text="Unload Driver") )
        setattr(cls, "Unload Module",
                PermissibleValue(text="Unload Module") )
        setattr(cls, "Unlock File",
                PermissibleValue(text="Unlock File") )
        setattr(cls, "Unmap File",
                PermissibleValue(text="Unmap File") )
        setattr(cls, "Upload File",
                PermissibleValue(text="Upload File") )
        setattr(cls, "Write to File",
                PermissibleValue(text="Write to File") )
        setattr(cls, "Write to Process Virtual Memory",
                PermissibleValue(text="Write to Process Virtual Memory") )

class ActionRelationshipTypeEnum(EnumDefinitionImpl):

    Dependent_On = PermissibleValue(text="Dependent_On")
    Equivalent_To = PermissibleValue(text="Equivalent_To")
    Followed_By = PermissibleValue(text="Followed_By")
    Initiated = PermissibleValue(text="Initiated")
    Initiated_By = PermissibleValue(text="Initiated_By")
    Preceded_By = PermissibleValue(text="Preceded_By")
    Related_To = PermissibleValue(text="Related_To")

    _defn = EnumDefinition(
        name="ActionRelationshipTypeEnum",
    )

class ActionStatusTypeEnum(EnumDefinitionImpl):

    Error = PermissibleValue(text="Error")
    Fail = PermissibleValue(text="Fail")
    Ongoing = PermissibleValue(text="Ongoing")
    Pending = PermissibleValue(text="Pending")
    Success = PermissibleValue(text="Success")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="ActionStatusTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete/Finish",
                PermissibleValue(text="Complete/Finish") )

class ActionTypeEnum(EnumDefinitionImpl):

    Accept = PermissibleValue(text="Accept")
    Access = PermissibleValue(text="Access")
    Add = PermissibleValue(text="Add")
    Alert = PermissibleValue(text="Alert")
    Allocate = PermissibleValue(text="Allocate")
    Archive = PermissibleValue(text="Archive")
    Assign = PermissibleValue(text="Assign")
    Audit = PermissibleValue(text="Audit")
    Backup = PermissibleValue(text="Backup")
    Bind = PermissibleValue(text="Bind")
    Block = PermissibleValue(text="Block")
    Call = PermissibleValue(text="Call")
    Change = PermissibleValue(text="Change")
    Check = PermissibleValue(text="Check")
    Clean = PermissibleValue(text="Clean")
    Click = PermissibleValue(text="Click")
    Close = PermissibleValue(text="Close")
    Compare = PermissibleValue(text="Compare")
    Compress = PermissibleValue(text="Compress")
    Configure = PermissibleValue(text="Configure")
    Connect = PermissibleValue(text="Connect")
    Control = PermissibleValue(text="Control")
    Create = PermissibleValue(text="Create")
    Decode = PermissibleValue(text="Decode")
    Decompress = PermissibleValue(text="Decompress")
    Decrypt = PermissibleValue(text="Decrypt")
    Deny = PermissibleValue(text="Deny")
    Depress = PermissibleValue(text="Depress")
    Detect = PermissibleValue(text="Detect")
    Disconnect = PermissibleValue(text="Disconnect")
    Download = PermissibleValue(text="Download")
    Draw = PermissibleValue(text="Draw")
    Drop = PermissibleValue(text="Drop")
    Encode = PermissibleValue(text="Encode")
    Encrypt = PermissibleValue(text="Encrypt")
    Enumerate = PermissibleValue(text="Enumerate")
    Execute = PermissibleValue(text="Execute")
    Extract = PermissibleValue(text="Extract")
    Filter = PermissibleValue(text="Filter")
    Find = PermissibleValue(text="Find")
    Flush = PermissibleValue(text="Flush")
    Fork = PermissibleValue(text="Fork")
    Free = PermissibleValue(text="Free")
    Get = PermissibleValue(text="Get")
    Hide = PermissibleValue(text="Hide")
    Hook = PermissibleValue(text="Hook")
    Impersonate = PermissibleValue(text="Impersonate")
    Initialize = PermissibleValue(text="Initialize")
    Inject = PermissibleValue(text="Inject")
    Install = PermissibleValue(text="Install")
    Interleave = PermissibleValue(text="Interleave")
    Join = PermissibleValue(text="Join")
    Kill = PermissibleValue(text="Kill")
    Listen = PermissibleValue(text="Listen")
    Load = PermissibleValue(text="Load")
    Lock = PermissibleValue(text="Lock")
    Map = PermissibleValue(text="Map")
    Merge = PermissibleValue(text="Merge")
    Modify = PermissibleValue(text="Modify")
    Monitor = PermissibleValue(text="Monitor")
    Move = PermissibleValue(text="Move")
    Open = PermissibleValue(text="Open")
    Pack = PermissibleValue(text="Pack")
    Pause = PermissibleValue(text="Pause")
    Press = PermissibleValue(text="Press")
    Protect = PermissibleValue(text="Protect")
    Quarantine = PermissibleValue(text="Quarantine")
    Query = PermissibleValue(text="Query")
    Queue = PermissibleValue(text="Queue")
    Raise = PermissibleValue(text="Raise")
    Read = PermissibleValue(text="Read")
    Receive = PermissibleValue(text="Receive")
    Release = PermissibleValue(text="Release")
    Rename = PermissibleValue(text="Rename")
    Replicate = PermissibleValue(text="Replicate")
    Restore = PermissibleValue(text="Restore")
    Resume = PermissibleValue(text="Resume")
    Revert = PermissibleValue(text="Revert")
    Run = PermissibleValue(text="Run")
    Save = PermissibleValue(text="Save")
    Scan = PermissibleValue(text="Scan")
    Schedule = PermissibleValue(text="Schedule")
    Search = PermissibleValue(text="Search")
    Send = PermissibleValue(text="Send")
    Set = PermissibleValue(text="Set")
    Shutdown = PermissibleValue(text="Shutdown")
    Sleep = PermissibleValue(text="Sleep")
    Snapshot = PermissibleValue(text="Snapshot")
    Start = PermissibleValue(text="Start")
    Stop = PermissibleValue(text="Stop")
    Suspend = PermissibleValue(text="Suspend")
    Synchronize = PermissibleValue(text="Synchronize")
    Throw = PermissibleValue(text="Throw")
    Transmit = PermissibleValue(text="Transmit")
    Unblock = PermissibleValue(text="Unblock")
    Unhide = PermissibleValue(text="Unhide")
    Unhook = PermissibleValue(text="Unhook")
    Uninstall = PermissibleValue(text="Uninstall")
    Unload = PermissibleValue(text="Unload")
    Unlock = PermissibleValue(text="Unlock")
    Unmap = PermissibleValue(text="Unmap")
    Unpack = PermissibleValue(text="Unpack")
    Update = PermissibleValue(text="Update")
    Upgrade = PermissibleValue(text="Upgrade")
    Upload = PermissibleValue(text="Upload")
    Write = PermissibleValue(text="Write")

    _defn = EnumDefinition(
        name="ActionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Copy/Duplicate",
                PermissibleValue(text="Copy/Duplicate") )
        setattr(cls, "Login/Logon",
                PermissibleValue(text="Login/Logon") )
        setattr(cls, "Logout/Logoff",
                PermissibleValue(text="Logout/Logoff") )
        setattr(cls, "Remove/Delete",
                PermissibleValue(text="Remove/Delete") )
        setattr(cls, "Wipe/Destroy/Purge",
                PermissibleValue(text="Wipe/Destroy/Purge") )

class BitnessEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="BitnessEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "32",
                PermissibleValue(text="32") )
        setattr(cls, "64",
                PermissibleValue(text="64") )

class CharacterEncodingEnum(EnumDefinitionImpl):

    ASCII = PermissibleValue(text="ASCII")

    _defn = EnumDefinition(
        name="CharacterEncodingEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "UTF-16",
                PermissibleValue(text="UTF-16") )
        setattr(cls, "UTF-32",
                PermissibleValue(text="UTF-32") )
        setattr(cls, "UTF-8",
                PermissibleValue(text="UTF-8") )
        setattr(cls, "Windows-1250",
                PermissibleValue(text="Windows-1250") )
        setattr(cls, "Windows-1251",
                PermissibleValue(text="Windows-1251") )
        setattr(cls, "Windows-1252",
                PermissibleValue(text="Windows-1252") )
        setattr(cls, "Windows-1253",
                PermissibleValue(text="Windows-1253") )
        setattr(cls, "Windows-1254",
                PermissibleValue(text="Windows-1254") )
        setattr(cls, "Windows-1255",
                PermissibleValue(text="Windows-1255") )
        setattr(cls, "Windows-1256",
                PermissibleValue(text="Windows-1256") )
        setattr(cls, "Windows-1257",
                PermissibleValue(text="Windows-1257") )
        setattr(cls, "Windows-1258",
                PermissibleValue(text="Windows-1258") )

class ContactAddressScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactAddressScopeEnum",
    )

class ContactEmailScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    cloud = PermissibleValue(text="cloud")

    _defn = EnumDefinition(
        name="ContactEmailScopeEnum",
    )

class ContactPhoneEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    mobile = PermissibleValue(text="mobile")
    main = PermissibleValue(text="main")
    pager = PermissibleValue(text="pager")

    _defn = EnumDefinition(
        name="ContactPhoneEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "home fax",
                PermissibleValue(text="home fax") )
        setattr(cls, "work fax",
                PermissibleValue(text="work fax") )

class ContactSIPScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactSIPScopeEnum",
    )

class ContactURLScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    homepage = PermissibleValue(text="homepage")

    _defn = EnumDefinition(
        name="ContactURLScopeEnum",
    )

class DiskTypeEnum(EnumDefinitionImpl):

    CDRom = PermissibleValue(text="CDRom")
    Fixed = PermissibleValue(text="Fixed")
    RAMDisk = PermissibleValue(text="RAMDisk")
    Remote = PermissibleValue(text="Remote")
    Removable = PermissibleValue(text="Removable")

    _defn = EnumDefinition(
        name="DiskTypeEnum",
    )

class EndiannessTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EndiannessTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Big-endian",
                PermissibleValue(text="Big-endian") )
        setattr(cls, "Little-endian",
                PermissibleValue(text="Little-endian") )
        setattr(cls, "Middle-endian",
                PermissibleValue(text="Middle-endian") )

class HashNameEnum(EnumDefinitionImpl):

    MD5 = PermissibleValue(text="MD5")
    MD6 = PermissibleValue(text="MD6")
    SHA1 = PermissibleValue(text="SHA1")
    SHA224 = PermissibleValue(text="SHA224")
    SHA256 = PermissibleValue(text="SHA256")
    SHA384 = PermissibleValue(text="SHA384")
    SHA512 = PermissibleValue(text="SHA512")
    SSDEEP = PermissibleValue(text="SSDEEP")

    _defn = EnumDefinition(
        name="HashNameEnum",
    )

class LibraryTypeEnum(EnumDefinitionImpl):

    Dynamic = PermissibleValue(text="Dynamic")
    Other = PermissibleValue(text="Other")
    Remote = PermissibleValue(text="Remote")
    Shared = PermissibleValue(text="Shared")
    Static = PermissibleValue(text="Static")

    _defn = EnumDefinition(
        name="LibraryTypeEnum",
    )

class MemoryBlockTypeEnum(EnumDefinitionImpl):

    Initialized = PermissibleValue(text="Initialized")
    Overlay = PermissibleValue(text="Overlay")
    Uninitialized = PermissibleValue(text="Uninitialized")

    _defn = EnumDefinition(
        name="MemoryBlockTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bit-mapped",
                PermissibleValue(text="Bit-mapped") )
        setattr(cls, "Byte-mapped",
                PermissibleValue(text="Byte-mapped") )

class ObservableObjectRelationshipEnum(EnumDefinitionImpl):

    Allocated = PermissibleValue(text="Allocated")
    Allocated_By = PermissibleValue(text="Allocated_By")
    Attachment_Of = PermissibleValue(text="Attachment_Of")
    Bound = PermissibleValue(text="Bound")
    Bound_By = PermissibleValue(text="Bound_By")
    Characterized_By = PermissibleValue(text="Characterized_By")
    Characterizes = PermissibleValue(text="Characterizes")
    Child_Of = PermissibleValue(text="Child_Of")
    Closed = PermissibleValue(text="Closed")
    Closed_By = PermissibleValue(text="Closed_By")
    Compressed = PermissibleValue(text="Compressed")
    Compressed_By = PermissibleValue(text="Compressed_By")
    Compressed_From = PermissibleValue(text="Compressed_From")
    Compressed_Into = PermissibleValue(text="Compressed_Into")
    Connected_From = PermissibleValue(text="Connected_From")
    Connected_To = PermissibleValue(text="Connected_To")
    Contained_Within = PermissibleValue(text="Contained_Within")
    Contains = PermissibleValue(text="Contains")
    Copied = PermissibleValue(text="Copied")
    Copied_By = PermissibleValue(text="Copied_By")
    Copied_From = PermissibleValue(text="Copied_From")
    Copied_To = PermissibleValue(text="Copied_To")
    Created = PermissibleValue(text="Created")
    Created_By = PermissibleValue(text="Created_By")
    Decoded = PermissibleValue(text="Decoded")
    Decoded_By = PermissibleValue(text="Decoded_By")
    Decompressed = PermissibleValue(text="Decompressed")
    Decompressed_By = PermissibleValue(text="Decompressed_By")
    Decrypted = PermissibleValue(text="Decrypted")
    Decrypted_By = PermissibleValue(text="Decrypted_By")
    Deleted = PermissibleValue(text="Deleted")
    Deleted_By = PermissibleValue(text="Deleted_By")
    Deleted_From = PermissibleValue(text="Deleted_From")
    Downloaded = PermissibleValue(text="Downloaded")
    Downloaded_By = PermissibleValue(text="Downloaded_By")
    Downloaded_From = PermissibleValue(text="Downloaded_From")
    Downloaded_To = PermissibleValue(text="Downloaded_To")
    Dropped = PermissibleValue(text="Dropped")
    Dropped_By = PermissibleValue(text="Dropped_By")
    Encoded = PermissibleValue(text="Encoded")
    Encoded_By = PermissibleValue(text="Encoded_By")
    Encrypted = PermissibleValue(text="Encrypted")
    Encrypted_By = PermissibleValue(text="Encrypted_By")
    Encrypted_From = PermissibleValue(text="Encrypted_From")
    Encrypted_To = PermissibleValue(text="Encrypted_To")
    Extracted_From = PermissibleValue(text="Extracted_From")
    FQDN_Of = PermissibleValue(text="FQDN_Of")
    Freed = PermissibleValue(text="Freed")
    Freed_By = PermissibleValue(text="Freed_By")
    Had_Attachment = PermissibleValue(text="Had_Attachment")
    Hooked = PermissibleValue(text="Hooked")
    Hooked_By = PermissibleValue(text="Hooked_By")
    Initialized_By = PermissibleValue(text="Initialized_By")
    Initialized_To = PermissibleValue(text="Initialized_To")
    Injected = PermissibleValue(text="Injected")
    Injected_As = PermissibleValue(text="Injected_As")
    Injected_By = PermissibleValue(text="Injected_By")
    Injected_Into = PermissibleValue(text="Injected_Into")
    Installed = PermissibleValue(text="Installed")
    Installed_By = PermissibleValue(text="Installed_By")
    Joined = PermissibleValue(text="Joined")
    Joined_By = PermissibleValue(text="Joined_By")
    Killed = PermissibleValue(text="Killed")
    Killed_By = PermissibleValue(text="Killed_By")
    Listened_On = PermissibleValue(text="Listened_On")
    Listened_On_By = PermissibleValue(text="Listened_On_By")
    Loaded_From = PermissibleValue(text="Loaded_From")
    Loaded_Into = PermissibleValue(text="Loaded_Into")
    Locked = PermissibleValue(text="Locked")
    Locked_By = PermissibleValue(text="Locked_By")
    Mapped_By = PermissibleValue(text="Mapped_By")
    Mapped_Into = PermissibleValue(text="Mapped_Into")
    Merged = PermissibleValue(text="Merged")
    Merged_By = PermissibleValue(text="Merged_By")
    Modified_Properties_Of = PermissibleValue(text="Modified_Properties_Of")
    Monitored = PermissibleValue(text="Monitored")
    Monitored_By = PermissibleValue(text="Monitored_By")
    Moved = PermissibleValue(text="Moved")
    Moved_By = PermissibleValue(text="Moved_By")
    Moved_From = PermissibleValue(text="Moved_From")
    Moved_To = PermissibleValue(text="Moved_To")
    Opened = PermissibleValue(text="Opened")
    Opened_By = PermissibleValue(text="Opened_By")
    Packed = PermissibleValue(text="Packed")
    Packed_By = PermissibleValue(text="Packed_By")
    Packed_From = PermissibleValue(text="Packed_From")
    Packed_Into = PermissibleValue(text="Packed_Into")
    Parent_Of = PermissibleValue(text="Parent_Of")
    Paused = PermissibleValue(text="Paused")
    Paused_By = PermissibleValue(text="Paused_By")
    Previously_Contained = PermissibleValue(text="Previously_Contained")
    Properties_Modified_By = PermissibleValue(text="Properties_Modified_By")
    Properties_Queried = PermissibleValue(text="Properties_Queried")
    Properties_Queried_By = PermissibleValue(text="Properties_Queried_By")
    Read_From = PermissibleValue(text="Read_From")
    Read_From_By = PermissibleValue(text="Read_From_By")
    Received = PermissibleValue(text="Received")
    Received_By = PermissibleValue(text="Received_By")
    Received_From = PermissibleValue(text="Received_From")
    Received_Via_Upload = PermissibleValue(text="Received_Via_Upload")
    Redirects_To = PermissibleValue(text="Redirects_To")
    Related_To = PermissibleValue(text="Related_To")
    Renamed = PermissibleValue(text="Renamed")
    Renamed_By = PermissibleValue(text="Renamed_By")
    Renamed_From = PermissibleValue(text="Renamed_From")
    Renamed_To = PermissibleValue(text="Renamed_To")
    Resolved_To = PermissibleValue(text="Resolved_To")
    Resumed = PermissibleValue(text="Resumed")
    Resumed_By = PermissibleValue(text="Resumed_By")
    Root_Domain_Of = PermissibleValue(text="Root_Domain_Of")
    Searched_For = PermissibleValue(text="Searched_For")
    Searched_For_By = PermissibleValue(text="Searched_For_By")
    Sent = PermissibleValue(text="Sent")
    Sent_By = PermissibleValue(text="Sent_By")
    Sent_To = PermissibleValue(text="Sent_To")
    Sent_Via_Upload = PermissibleValue(text="Sent_Via_Upload")
    Set_From = PermissibleValue(text="Set_From")
    Set_To = PermissibleValue(text="Set_To")
    Suspended = PermissibleValue(text="Suspended")
    Suspended_By = PermissibleValue(text="Suspended_By")
    Unhooked = PermissibleValue(text="Unhooked")
    Unhooked_By = PermissibleValue(text="Unhooked_By")
    Unlocked = PermissibleValue(text="Unlocked")
    Unlocked_By = PermissibleValue(text="Unlocked_By")
    Unpacked = PermissibleValue(text="Unpacked")
    Unpacked_By = PermissibleValue(text="Unpacked_By")
    Uploaded = PermissibleValue(text="Uploaded")
    Uploaded_By = PermissibleValue(text="Uploaded_By")
    Uploaded_From = PermissibleValue(text="Uploaded_From")
    Uploaded_To = PermissibleValue(text="Uploaded_To")
    Used = PermissibleValue(text="Used")
    Used_By = PermissibleValue(text="Used_By")
    Values_Enumerated = PermissibleValue(text="Values_Enumerated")
    Values_Enumerated_By = PermissibleValue(text="Values_Enumerated_By")
    Written_To_By = PermissibleValue(text="Written_To_By")
    Wrote_To = PermissibleValue(text="Wrote_To")

    _defn = EnumDefinition(
        name="ObservableObjectRelationshipEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Sub-domain_Of",
                PermissibleValue(text="Sub-domain_Of") )
        setattr(cls, "Supra-domain_Of",
                PermissibleValue(text="Supra-domain_Of") )

class ObservableObjectStateEnum(EnumDefinitionImpl):

    Active = PermissibleValue(text="Active")
    Closed = PermissibleValue(text="Closed")
    Exists = PermissibleValue(text="Exists")
    Inactive = PermissibleValue(text="Inactive")
    Locked = PermissibleValue(text="Locked")
    Open = PermissibleValue(text="Open")
    Started = PermissibleValue(text="Started")
    Stopped = PermissibleValue(text="Stopped")
    Unlocked = PermissibleValue(text="Unlocked")

    _defn = EnumDefinition(
        name="ObservableObjectStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Does Not Exist",
                PermissibleValue(text="Does Not Exist") )

class PartitionTypeEnum(EnumDefinitionImpl):

    PARTITION_ENTRY_UNUSED = PermissibleValue(text="PARTITION_ENTRY_UNUSED")
    PARTITION_EXTENDED = PermissibleValue(text="PARTITION_EXTENDED")
    PARTITION_FAT32 = PermissibleValue(text="PARTITION_FAT32")
    PARTITION_FAT32_XINT13 = PermissibleValue(text="PARTITION_FAT32_XINT13")
    PARTITION_FAT_12 = PermissibleValue(text="PARTITION_FAT_12")
    PARTITION_FAT_16 = PermissibleValue(text="PARTITION_FAT_16")
    PARTITION_HUGE = PermissibleValue(text="PARTITION_HUGE")
    PARTITION_IFS = PermissibleValue(text="PARTITION_IFS")
    PARTITION_LDM = PermissibleValue(text="PARTITION_LDM")
    PARTITION_NTFT = PermissibleValue(text="PARTITION_NTFT")
    PARTITION_OS2BOOTMGR = PermissibleValue(text="PARTITION_OS2BOOTMGR")
    PARTITION_PREP = PermissibleValue(text="PARTITION_PREP")
    PARTITION_UNIX = PermissibleValue(text="PARTITION_UNIX")
    PARTITION_XENIX_1 = PermissibleValue(text="PARTITION_XENIX_1")
    PARTITION_XENIX_2 = PermissibleValue(text="PARTITION_XENIX_2")
    PARTITION_XINT13 = PermissibleValue(text="PARTITION_XINT13")
    PARTITION_XINT13_EXTENDED = PermissibleValue(text="PARTITION_XINT13_EXTENDED")
    UNKNOWN = PermissibleValue(text="UNKNOWN")
    VALID_NTFT = PermissibleValue(text="VALID_NTFT")

    _defn = EnumDefinition(
        name="PartitionTypeEnum",
    )

class ProcessorArchEnum(EnumDefinitionImpl):

    ARM = PermissibleValue(text="ARM")
    Alpha = PermissibleValue(text="Alpha")
    MIPS = PermissibleValue(text="MIPS")
    Other = PermissibleValue(text="Other")
    PowerPC = PermissibleValue(text="PowerPC")
    SPARC = PermissibleValue(text="SPARC")

    _defn = EnumDefinition(
        name="ProcessorArchEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "IA-64",
                PermissibleValue(text="IA-64") )
        setattr(cls, "Motorola 68k",
                PermissibleValue(text="Motorola 68k") )
        setattr(cls, "eSi-RISC",
                PermissibleValue(text="eSi-RISC") )
        setattr(cls, "x86-32",
                PermissibleValue(text="x86-32") )
        setattr(cls, "x86-64",
                PermissibleValue(text="x86-64") )
        setattr(cls, "z/Architecture",
                PermissibleValue(text="z/Architecture") )

class RecoveredObjectStatusEnum(EnumDefinitionImpl):

    recovered = PermissibleValue(text="recovered")
    overwritten = PermissibleValue(text="overwritten")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="RecoveredObjectStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "partially recovered",
                PermissibleValue(text="partially recovered") )

class RegionalRegistryTypeEnum(EnumDefinitionImpl):

    APNIC = PermissibleValue(text="APNIC")
    ARIN = PermissibleValue(text="ARIN")
    AfriNIC = PermissibleValue(text="AfriNIC")
    LACNIC = PermissibleValue(text="LACNIC")

    _defn = EnumDefinition(
        name="RegionalRegistryTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "RIPE NCC",
                PermissibleValue(text="RIPE NCC") )

class RegistryDatatypeEnum(EnumDefinitionImpl):
    """
    "From https //learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types, https
    //learn.microsoft.com/en-us/windows/win32/shell/hkey-type"
    """
    reg_binary = PermissibleValue(text="reg_binary",
                                           description=""Binary data in any form."")
    reg_dword = PermissibleValue(text="reg_dword",
                                         description=""A 32-bit number."")
    reg_dword_big_endian = PermissibleValue(text="reg_dword_big_endian",
                                                               description=""A 32-bit number in big-endian format. Some UNIX systems support big-endian architectures."")
    reg_expand_sz = PermissibleValue(text="reg_expand_sz",
                                                 description=""A null-terminated string that contains unexpanded references to environment Variables (for example, '%PATH%'). It will be a Unicode or ANSI string depending on wh ether you use the Unicode or ANSI functions. To expand the environment variable refere nces, use the ExpandEnvironmentStrings function."")
    reg_full_resource_descriptor = PermissibleValue(text="reg_full_resource_descriptor",
                                                                               description=""A list of hardware resources that a physical device is using, detected and written into the \HardwareDescription tree by the system."")
    reg_invalid_type = PermissibleValue(text="reg_invalid_type",
                                                       description=""Specifies an invalid key."")
    reg_link = PermissibleValue(text="reg_link",
                                       description=""A null-terminated Unicode string that contains the target path of a symboli c link that was created by calling the RegCreateKeyEx function with REG_OPTION_CREATE_ LINK."")
    reg_multi_sz = PermissibleValue(text="reg_multi_sz",
                                               description=""A sequence of null-terminated strings, terminated by an empty string (\0). The following is an example: String1\0String2\0String3\0LastString\0\0 The first \0 terminates the first string, the second to the last \0 terminates the last string, and the final \0 terminates the sequence. Note that the final terminator must be factored into the length of the string."")
    reg_none = PermissibleValue(text="reg_none",
                                       description=""No defined value type."")
    reg_qword = PermissibleValue(text="reg_qword",
                                         description=""A 64-bit number."")
    reg_resource_list = PermissibleValue(text="reg_resource_list",
                                                         description=""Device-driver resource list."")
    reg_resource_requirements_list = PermissibleValue(text="reg_resource_requirements_list",
                                                                                   description=""A device driver's list of possible hardware resources it or one of the physical devices it controls can use, from which the system writes a subset into the \ResourceMap tree"")
    reg_sz = PermissibleValue(text="reg_sz",
                                   description=""A null-terminated string. This will be either a Unicode or an ANSI string, depending on whether you use the Unicode or ANSI functions."")

    _defn = EnumDefinition(
        name="RegistryDatatypeEnum",
        description="\"From https //learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types, https //learn.microsoft.com/en-us/windows/win32/shell/hkey-type\"",
    )

class SIMFormEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SIMFormEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Full-size SIM",
                PermissibleValue(text="Full-size SIM") )
        setattr(cls, "Micro SIM",
                PermissibleValue(text="Micro SIM") )
        setattr(cls, "Nano SIM",
                PermissibleValue(text="Nano SIM") )

class SIMTypeEnum(EnumDefinitionImpl):

    SIM = PermissibleValue(text="SIM")
    UICC = PermissibleValue(text="UICC")
    USIM = PermissibleValue(text="USIM")

    _defn = EnumDefinition(
        name="SIMTypeEnum",
    )

class TaskActionTypeEnum(EnumDefinitionImpl):

    TASK_ACTION_COM_HANDLER = PermissibleValue(text="TASK_ACTION_COM_HANDLER")
    TASK_ACTION_EXEC = PermissibleValue(text="TASK_ACTION_EXEC")
    TASK_ACTION_SEND_EMAIL = PermissibleValue(text="TASK_ACTION_SEND_EMAIL")
    TASK_ACTION_SHOW_MESSAGE = PermissibleValue(text="TASK_ACTION_SHOW_MESSAGE")

    _defn = EnumDefinition(
        name="TaskActionTypeEnum",
    )

class TaskFlagEnum(EnumDefinitionImpl):

    TASK_FLAG_DELETE_WHEN_DONE = PermissibleValue(text="TASK_FLAG_DELETE_WHEN_DONE")
    TASK_FLAG_DISABLED = PermissibleValue(text="TASK_FLAG_DISABLED")
    TASK_FLAG_DONT_START_IF_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_DONT_START_IF_ON_BATTERIES")
    TASK_FLAG_HIDDEN = PermissibleValue(text="TASK_FLAG_HIDDEN")
    TASK_FLAG_INTERACTIVE = PermissibleValue(text="TASK_FLAG_INTERACTIVE")
    TASK_FLAG_KILL_IF_GOING_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_KILL_IF_GOING_ON_BATTERIES")
    TASK_FLAG_KILL_ON_IDLE_END = PermissibleValue(text="TASK_FLAG_KILL_ON_IDLE_END")
    TASK_FLAG_RESTART_ON_IDLE_RESUME = PermissibleValue(text="TASK_FLAG_RESTART_ON_IDLE_RESUME")
    TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET = PermissibleValue(text="TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET")
    TASK_FLAG_RUN_ONLY_IF_LOGGED_ON = PermissibleValue(text="TASK_FLAG_RUN_ONLY_IF_LOGGED_ON")
    TASK_FLAG_START_ONLY_IF_IDLE = PermissibleValue(text="TASK_FLAG_START_ONLY_IF_IDLE")
    TASK_FLAG_SYSTEM_REQUIRED = PermissibleValue(text="TASK_FLAG_SYSTEM_REQUIRED")
    TASK_FLAG_ZERO = PermissibleValue(text="TASK_FLAG_ZERO")

    _defn = EnumDefinition(
        name="TaskFlagEnum",
    )

class TaskPriorityEnum(EnumDefinitionImpl):

    ABOVE_NORMAL_PRIORITY_CLASS = PermissibleValue(text="ABOVE_NORMAL_PRIORITY_CLASS")
    BELOW_NORMAL_PRIORITY_CLASS = PermissibleValue(text="BELOW_NORMAL_PRIORITY_CLASS")
    HIGH_PRIORITY_CLASS = PermissibleValue(text="HIGH_PRIORITY_CLASS")
    IDLE_PRIORITY_CLASS = PermissibleValue(text="IDLE_PRIORITY_CLASS")
    NORMAL_PRIORITY_CLASS = PermissibleValue(text="NORMAL_PRIORITY_CLASS")
    REALTIME_PRIORITY_CLASS = PermissibleValue(text="REALTIME_PRIORITY_CLASS")

    _defn = EnumDefinition(
        name="TaskPriorityEnum",
    )

class TaskStatusEnum(EnumDefinitionImpl):

    SCHED_E_ACCOUNT_DBASE_CORRUPT = PermissibleValue(text="SCHED_E_ACCOUNT_DBASE_CORRUPT")
    SCHED_E_ACCOUNT_INFORMATION_NOT_SET = PermissibleValue(text="SCHED_E_ACCOUNT_INFORMATION_NOT_SET")
    SCHED_E_ACCOUNT_NAME_NOT_FOUND = PermissibleValue(text="SCHED_E_ACCOUNT_NAME_NOT_FOUND")
    SCHED_E_CANNOT_OPEN_TASK = PermissibleValue(text="SCHED_E_CANNOT_OPEN_TASK")
    SCHED_E_INVALID_TASK = PermissibleValue(text="SCHED_E_INVALID_TASK")
    SCHED_E_NO_SECURITY_SERVICES = PermissibleValue(text="SCHED_E_NO_SECURITY_SERVICES")
    SCHED_E_SERVICE_NOT_INSTALLED = PermissibleValue(text="SCHED_E_SERVICE_NOT_INSTALLED")
    SCHED_E_SERVICE_NOT_RUNNING = PermissibleValue(text="SCHED_E_SERVICE_NOT_RUNNING")
    SCHED_E_TASK_NOT_READY = PermissibleValue(text="SCHED_E_TASK_NOT_READY")
    SCHED_E_TASK_NOT_RUNNING = PermissibleValue(text="SCHED_E_TASK_NOT_RUNNING")
    SCHED_E_TRIGGER_NOT_FOUND = PermissibleValue(text="SCHED_E_TRIGGER_NOT_FOUND")
    SCHED_E_UNKNOWN_OBJECT_VERSION = PermissibleValue(text="SCHED_E_UNKNOWN_OBJECT_VERSION")
    SCHED_E_UNSUPPORTED_ACCOUNT_OPTION = PermissibleValue(text="SCHED_E_UNSUPPORTED_ACCOUNT_OPTION")
    SCHED_S_EVENT_TRIGGER = PermissibleValue(text="SCHED_S_EVENT_TRIGGER")
    SCHED_S_TASK_DISABLED = PermissibleValue(text="SCHED_S_TASK_DISABLED")
    SCHED_S_TASK_HAS_NOT_RUN = PermissibleValue(text="SCHED_S_TASK_HAS_NOT_RUN")
    SCHED_S_TASK_NOT_SCHEDULED = PermissibleValue(text="SCHED_S_TASK_NOT_SCHEDULED")
    SCHED_S_TASK_NO_MORE_RUNS = PermissibleValue(text="SCHED_S_TASK_NO_MORE_RUNS")
    SCHED_S_TASK_NO_VALID_TRIGGERS = PermissibleValue(text="SCHED_S_TASK_NO_VALID_TRIGGERS")
    SCHED_S_TASK_READY = PermissibleValue(text="SCHED_S_TASK_READY")
    SCHED_S_TASK_RUNNING = PermissibleValue(text="SCHED_S_TASK_RUNNING")
    SCHED_S_TASK_TERMINATED = PermissibleValue(text="SCHED_S_TASK_TERMINATED")
    TASK_STATE_QUEUED = PermissibleValue(text="TASK_STATE_QUEUED")
    TASK_STATE_UNKNOWN = PermissibleValue(text="TASK_STATE_UNKNOWN")

    _defn = EnumDefinition(
        name="TaskStatusEnum",
    )

class ThreadRunningStatusEnum(EnumDefinitionImpl):

    Initialized = PermissibleValue(text="Initialized")
    Ready = PermissibleValue(text="Ready")
    Running = PermissibleValue(text="Running")
    Standby = PermissibleValue(text="Standby")
    Terminated = PermissibleValue(text="Terminated")
    Transition = PermissibleValue(text="Transition")
    Unknown = PermissibleValue(text="Unknown")
    Waiting = PermissibleValue(text="Waiting")

    _defn = EnumDefinition(
        name="ThreadRunningStatusEnum",
    )

class TimestampPrecisionEnum(EnumDefinitionImpl):

    day = PermissibleValue(text="day")
    hour = PermissibleValue(text="hour")
    minute = PermissibleValue(text="minute")
    month = PermissibleValue(text="month")
    second = PermissibleValue(text="second")
    year = PermissibleValue(text="year")

    _defn = EnumDefinition(
        name="TimestampPrecisionEnum",
    )

class TrendEnum(EnumDefinitionImpl):

    Decreasing = PermissibleValue(text="Decreasing")
    Increasing = PermissibleValue(text="Increasing")

    _defn = EnumDefinition(
        name="TrendEnum",
    )

class TriggerFrequencyEnum(EnumDefinitionImpl):

    TASK_EVENT_TRIGGER_AT_LOGON = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_LOGON")
    TASK_EVENT_TRIGGER_AT_SYSTEMSTART = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_SYSTEMSTART")
    TASK_EVENT_TRIGGER_ON_IDLE = PermissibleValue(text="TASK_EVENT_TRIGGER_ON_IDLE")
    TASK_TIME_TRIGGER_DAILY = PermissibleValue(text="TASK_TIME_TRIGGER_DAILY")
    TASK_TIME_TRIGGER_MONTHLYDATE = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDATE")
    TASK_TIME_TRIGGER_MONTHLYDOW = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDOW")
    TASK_TIME_TRIGGER_ONCE = PermissibleValue(text="TASK_TIME_TRIGGER_ONCE")
    TASK_TIME_TRIGGER_WEEKLY = PermissibleValue(text="TASK_TIME_TRIGGER_WEEKLY")

    _defn = EnumDefinition(
        name="TriggerFrequencyEnum",
    )

class TriggerTypeEnum(EnumDefinitionImpl):

    TASK_TRIGGER_BOOT = PermissibleValue(text="TASK_TRIGGER_BOOT")
    TASK_TRIGGER_EVENT = PermissibleValue(text="TASK_TRIGGER_EVENT")
    TASK_TRIGGER_IDLE = PermissibleValue(text="TASK_TRIGGER_IDLE")
    TASK_TRIGGER_LOGON = PermissibleValue(text="TASK_TRIGGER_LOGON")
    TASK_TRIGGER_REGISTRATION = PermissibleValue(text="TASK_TRIGGER_REGISTRATION")
    TASK_TRIGGER_SESSION_STATE_CHANGE = PermissibleValue(text="TASK_TRIGGER_SESSION_STATE_CHANGE")
    TASK_TRIGGER_TIME = PermissibleValue(text="TASK_TRIGGER_TIME")

    _defn = EnumDefinition(
        name="TriggerTypeEnum",
    )

class URLTransitionTypeEnum(EnumDefinitionImpl):

    link = PermissibleValue(text="link")
    typed = PermissibleValue(text="typed")
    auto_bookmark = PermissibleValue(text="auto_bookmark")
    auto_subframe = PermissibleValue(text="auto_subframe")
    manual_subframe = PermissibleValue(text="manual_subframe")
    generated = PermissibleValue(text="generated")
    auto_toplevel = PermissibleValue(text="auto_toplevel")
    form_submit = PermissibleValue(text="form_submit")
    reload = PermissibleValue(text="reload")
    keyword = PermissibleValue(text="keyword")
    keyword_generated = PermissibleValue(text="keyword_generated")

    _defn = EnumDefinition(
        name="URLTransitionTypeEnum",
    )

class UnixProcessStateEnum(EnumDefinitionImpl):

    Dead = PermissibleValue(text="Dead")
    InterruptibleSleep = PermissibleValue(text="InterruptibleSleep")
    Paging = PermissibleValue(text="Paging")
    Running = PermissibleValue(text="Running")
    Stopped = PermissibleValue(text="Stopped")
    UninterruptibleSleep = PermissibleValue(text="UninterruptibleSleep")
    Zombie = PermissibleValue(text="Zombie")

    _defn = EnumDefinition(
        name="UnixProcessStateEnum",
    )

class WhoisContactTypeEnum(EnumDefinitionImpl):

    ADMIN = PermissibleValue(text="ADMIN")
    BILLING = PermissibleValue(text="BILLING")
    TECHNICAL = PermissibleValue(text="TECHNICAL")

    _defn = EnumDefinition(
        name="WhoisContactTypeEnum",
    )

class WhoisDNSSECTypeEnum(EnumDefinitionImpl):

    Signed = PermissibleValue(text="Signed")
    Unsigned = PermissibleValue(text="Unsigned")

    _defn = EnumDefinition(
        name="WhoisDNSSECTypeEnum",
    )

class WhoisStatusTypeEnum(EnumDefinitionImpl):

    ADD_PERIOD = PermissibleValue(text="ADD_PERIOD")
    AUTO_RENEW_PERIOD = PermissibleValue(text="AUTO_RENEW_PERIOD")
    CLIENT_DELETE_PROHIBITED = PermissibleValue(text="CLIENT_DELETE_PROHIBITED")
    CLIENT_HOLD = PermissibleValue(text="CLIENT_HOLD")
    CLIENT_RENEW_PROHIBITED = PermissibleValue(text="CLIENT_RENEW_PROHIBITED")
    CLIENT_TRANSFER_PROHIBITED = PermissibleValue(text="CLIENT_TRANSFER_PROHIBITED")
    CLIENT_UPDATE_PROHIBITED = PermissibleValue(text="CLIENT_UPDATE_PROHIBITED")
    DELETE_PROHIBITED = PermissibleValue(text="DELETE_PROHIBITED")
    HOLD = PermissibleValue(text="HOLD")
    INACTIVE = PermissibleValue(text="INACTIVE")
    OK = PermissibleValue(text="OK")
    PENDING_DELETE_RESTORABLE = PermissibleValue(text="PENDING_DELETE_RESTORABLE")
    PENDING_DELETE_SCHEDULED_FOR_RELEASE = PermissibleValue(text="PENDING_DELETE_SCHEDULED_FOR_RELEASE")
    PENDING_RESTORE = PermissibleValue(text="PENDING_RESTORE")
    RENEW_PERIOD = PermissibleValue(text="RENEW_PERIOD")
    RENEW_PROHIBITED = PermissibleValue(text="RENEW_PROHIBITED")
    TRANSFER_PERIOD = PermissibleValue(text="TRANSFER_PERIOD")
    TRANSFER_PROHIBITED = PermissibleValue(text="TRANSFER_PROHIBITED")
    UPDATE_PROHIBITED = PermissibleValue(text="UPDATE_PROHIBITED")

    _defn = EnumDefinition(
        name="WhoisStatusTypeEnum",
    )

class WindowsDriveTypeEnum(EnumDefinitionImpl):

    DRIVE_CDROM = PermissibleValue(text="DRIVE_CDROM")
    DRIVE_FIXED = PermissibleValue(text="DRIVE_FIXED")
    DRIVE_NO_ROOT_DIR = PermissibleValue(text="DRIVE_NO_ROOT_DIR")
    DRIVE_RAMDISK = PermissibleValue(text="DRIVE_RAMDISK")
    DRIVE_REMOTE = PermissibleValue(text="DRIVE_REMOTE")
    DRIVE_REMOVABLE = PermissibleValue(text="DRIVE_REMOVABLE")
    DRIVE_UNKNOWN = PermissibleValue(text="DRIVE_UNKNOWN")

    _defn = EnumDefinition(
        name="WindowsDriveTypeEnum",
    )

class WindowsVolumeAttributeEnum(EnumDefinitionImpl):

    Hidden = PermissibleValue(text="Hidden")
    NoDefaultDriveLetter = PermissibleValue(text="NoDefaultDriveLetter")
    ReadOnly = PermissibleValue(text="ReadOnly")
    ShadowCopy = PermissibleValue(text="ShadowCopy")

    _defn = EnumDefinition(
        name="WindowsVolumeAttributeEnum",
    )

class WirelessNetworkSecurityModeEnum(EnumDefinitionImpl):

    WEP = PermissibleValue(text="WEP")
    WPA = PermissibleValue(text="WPA")

    _defn = EnumDefinition(
        name="WirelessNetworkSecurityModeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
                PermissibleValue(text="None") )
        setattr(cls, "WPA2-PSK",
                PermissibleValue(text="WPA2-PSK") )
        setattr(cls, "WPA2-Enterprise",
                PermissibleValue(text="WPA2-Enterprise") )
        setattr(cls, "WPA3-PSK",
                PermissibleValue(text="WPA3-PSK") )
        setattr(cls, "WPA3-Enterprise",
                PermissibleValue(text="WPA3-Enterprise") )

# Slots
class slots:
    pass

slots.class = Slot(uri=ANALYSIS.class, name="class", curie=ANALYSIS.curie('class'),
                   model_uri=ANALYSIS.class, domain=None, range=Optional[str])

slots.classification = Slot(uri=ANALYSIS.classification, name="classification", curie=ANALYSIS.curie('classification'),
                   model_uri=ANALYSIS.classification, domain=None, range=Optional[Union[dict, ArtifactClassification]])

slots.classificationConfidence = Slot(uri=ANALYSIS.classificationConfidence, name="classificationConfidence", curie=ANALYSIS.curie('classificationConfidence'),
                   model_uri=ANALYSIS.classificationConfidence, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.originatingAnalysis = Slot(uri=ANALYSIS.originatingAnalysis, name="originatingAnalysis", curie=ANALYSIS.curie('originatingAnalysis'),
                   model_uri=ANALYSIS.originatingAnalysis, domain=None, range=Optional[Union[dict, Analysis]])

slots.resultContent = Slot(uri=ANALYSIS.resultContent, name="resultContent", curie=ANALYSIS.curie('resultContent'),
                   model_uri=ANALYSIS.resultContent, domain=None, range=Optional[Union[dict, UcoObject]])

slots.action = Slot(uri=ACTION.action, name="action", curie=ACTION.curie('action'),
                   model_uri=ANALYSIS.action, domain=None, range=Optional[Union[dict, Action]])

slots.actionCount = Slot(uri=ACTION.actionCount, name="actionCount", curie=ACTION.curie('actionCount'),
                   model_uri=ANALYSIS.actionCount, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.actionStatus = Slot(uri=ACTION.actionStatus, name="actionStatus", curie=ACTION.curie('actionStatus'),
                   model_uri=ANALYSIS.actionStatus, domain=None, range=Optional[Union[str, "ActionStatusTypeEnum"]])

slots.argumentName = Slot(uri=ACTION.argumentName, name="argumentName", curie=ACTION.curie('argumentName'),
                   model_uri=ANALYSIS.argumentName, domain=None, range=Optional[str])

slots._endTime = Slot(uri=ACTION._endTime, name="_endTime", curie=ACTION.curie('_endTime'),
                   model_uri=ANALYSIS._endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.environment = Slot(uri=ACTION.environment, name="environment", curie=ACTION.curie('environment'),
                   model_uri=ANALYSIS.environment, domain=None, range=Optional[Union[dict, UcoObject]])

slots.error = Slot(uri=ACTION.error, name="error", curie=ACTION.curie('error'),
                   model_uri=ANALYSIS.error, domain=None, range=Optional[Union[dict, UcoObject]])

slots.estimatedCost = Slot(uri=ACTION.estimatedCost, name="estimatedCost", curie=ACTION.curie('estimatedCost'),
                   model_uri=ANALYSIS.estimatedCost, domain=None, range=Optional[str])

slots.estimatedEfficacy = Slot(uri=ACTION.estimatedEfficacy, name="estimatedEfficacy", curie=ACTION.curie('estimatedEfficacy'),
                   model_uri=ANALYSIS.estimatedEfficacy, domain=None, range=Optional[str])

slots.estimatedImpact = Slot(uri=ACTION.estimatedImpact, name="estimatedImpact", curie=ACTION.curie('estimatedImpact'),
                   model_uri=ANALYSIS.estimatedImpact, domain=None, range=Optional[str])

slots.instrument = Slot(uri=ACTION.instrument, name="instrument", curie=ACTION.curie('instrument'),
                   model_uri=ANALYSIS.instrument, domain=None, range=Optional[Union[dict, UcoObject]])

slots.location = Slot(uri=ACTION.location, name="location", curie=ACTION.curie('location'),
                   model_uri=ANALYSIS.location, domain=None, range=Optional[Union[dict, Location]])

slots._object = Slot(uri=ACTION._object, name="_object", curie=ACTION.curie('_object'),
                   model_uri=ANALYSIS._object, domain=None, range=Optional[Union[dict, UcoObject]])

slots.objective = Slot(uri=ACTION.objective, name="objective", curie=ACTION.curie('objective'),
                   model_uri=ANALYSIS.objective, domain=None, range=Optional[str])

slots.participant = Slot(uri=ACTION.participant, name="participant", curie=ACTION.curie('participant'),
                   model_uri=ANALYSIS.participant, domain=None, range=Optional[Union[dict, UcoObject]])

slots.performer = Slot(uri=ACTION.performer, name="performer", curie=ACTION.curie('performer'),
                   model_uri=ANALYSIS.performer, domain=None, range=Optional[Union[dict, UcoObject]])

slots.phase = Slot(uri=ACTION.phase, name="phase", curie=ACTION.curie('phase'),
                   model_uri=ANALYSIS.phase, domain=None, range=Optional[Union[dict, ArrayOfAction]])

slots.rate = Slot(uri=ACTION.rate, name="rate", curie=ACTION.curie('rate'),
                   model_uri=ANALYSIS.rate, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.result = Slot(uri=ACTION.result, name="result", curie=ACTION.curie('result'),
                   model_uri=ANALYSIS.result, domain=None, range=Optional[Union[dict, UcoObject]])

slots.scale = Slot(uri=ACTION.scale, name="scale", curie=ACTION.curie('scale'),
                   model_uri=ANALYSIS.scale, domain=None, range=Optional[str])

slots._startTime = Slot(uri=ACTION._startTime, name="_startTime", curie=ACTION.curie('_startTime'),
                   model_uri=ANALYSIS._startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.subaction = Slot(uri=ACTION.subaction, name="subaction", curie=ACTION.curie('subaction'),
                   model_uri=ANALYSIS.subaction, domain=None, range=Optional[Union[dict, Action]])

slots.trend = Slot(uri=ACTION.trend, name="trend", curie=ACTION.curie('trend'),
                   model_uri=ANALYSIS.trend, domain=None, range=Optional[Union[str, "TrendEnum"]])

slots.units = Slot(uri=ACTION.units, name="units", curie=ACTION.curie('units'),
                   model_uri=ANALYSIS.units, domain=None, range=Optional[str])

slots.confidence = Slot(uri=CORE.confidence, name="confidence", curie=CORE.curie('confidence'),
                   model_uri=ANALYSIS.confidence, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=ANALYSIS.constrainingVocabularyName, domain=None, range=Optional[str])

slots.constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=ANALYSIS.constrainingVocabularyReference, domain=None, range=Optional[Union[str, IriType]])

slots.context = Slot(uri=CORE.context, name="context", curie=CORE.curie('context'),
                   model_uri=ANALYSIS.context, domain=None, range=Optional[str])

slots.createdBy = Slot(uri=CORE.createdBy, name="createdBy", curie=CORE.curie('createdBy'),
                   model_uri=ANALYSIS.createdBy, domain=IdentityAbstraction, range=Optional[str])

slots.definingContext = Slot(uri=CORE.definingContext, name="definingContext", curie=CORE.curie('definingContext'),
                   model_uri=ANALYSIS.definingContext, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=ANALYSIS.description, domain=None, range=Optional[str])

slots.endTime = Slot(uri=CORE.endTime, name="endTime", curie=CORE.curie('endTime'),
                   model_uri=ANALYSIS.endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.externalIdentifier = Slot(uri=CORE.externalIdentifier, name="externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=ANALYSIS.externalIdentifier, domain=None, range=Optional[str])

slots.externalReference = Slot(uri=CORE.externalReference, name="externalReference", curie=CORE.curie('externalReference'),
                   model_uri=ANALYSIS.externalReference, domain=ExternalReference, range=Optional[str])

slots.hasFacet = Slot(uri=CORE.hasFacet, name="hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=ANALYSIS.hasFacet, domain=None, range=Optional[str])

slots.isDirectional = Slot(uri=CORE.isDirectional, name="isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=ANALYSIS.isDirectional, domain=None, range=Optional[Union[bool, BooleanType]])

slots.kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=ANALYSIS.kindOfRelationship, domain=None, range=Optional[str])

slots.modifiedTime = Slot(uri=CORE.modifiedTime, name="modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=ANALYSIS.modifiedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=ANALYSIS.name, domain=None, range=Optional[str])

slots.namingAuthority = Slot(uri=CORE.namingAuthority, name="namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=ANALYSIS.namingAuthority, domain=None, range=Optional[str])

slots.object = Slot(uri=CORE.object, name="object", curie=CORE.curie('object'),
                   model_uri=ANALYSIS.object, domain=None, range=Optional[Union[dict, UcoObject]])

slots.objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=ANALYSIS.objectCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.objectMarking = Slot(uri=CORE.objectMarking, name="objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=ANALYSIS.objectMarking, domain=None, range=Optional[Union[dict, MarkingDefinitionAbstraction]])

slots.referenceURL = Slot(uri=CORE.referenceURL, name="referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=ANALYSIS.referenceURL, domain=None, range=Optional[Union[str, IriType]])

slots.source = Slot(uri=CORE.source, name="source", curie=CORE.curie('source'),
                   model_uri=ANALYSIS.source, domain=None, range=Optional[Union[dict, UcoObject]])

slots.specVersion = Slot(uri=CORE.specVersion, name="specVersion", curie=CORE.curie('specVersion'),
                   model_uri=ANALYSIS.specVersion, domain=None, range=Optional[str])

slots.startTime = Slot(uri=CORE.startTime, name="startTime", curie=CORE.curie('startTime'),
                   model_uri=ANALYSIS.startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.statement = Slot(uri=CORE.statement, name="statement", curie=CORE.curie('statement'),
                   model_uri=ANALYSIS.statement, domain=None, range=Optional[str])

slots.tag = Slot(uri=CORE.tag, name="tag", curie=CORE.curie('tag'),
                   model_uri=ANALYSIS.tag, domain=None, range=Optional[str])

slots.target = Slot(uri=CORE.target, name="target", curie=CORE.curie('target'),
                   model_uri=ANALYSIS.target, domain=None, range=Optional[Union[dict, UcoObject]])

slots.value = Slot(uri=CORE.value, name="value", curie=CORE.curie('value'),
                   model_uri=ANALYSIS.value, domain=None, range=Optional[str])

slots.addressType = Slot(uri=LOCATION.addressType, name="addressType", curie=LOCATION.curie('addressType'),
                   model_uri=ANALYSIS.addressType, domain=None, range=Optional[str])

slots.altitude = Slot(uri=LOCATION.altitude, name="altitude", curie=LOCATION.curie('altitude'),
                   model_uri=ANALYSIS.altitude, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.country = Slot(uri=LOCATION.country, name="country", curie=LOCATION.curie('country'),
                   model_uri=ANALYSIS.country, domain=None, range=Optional[str])

slots.hdop = Slot(uri=LOCATION.hdop, name="hdop", curie=LOCATION.curie('hdop'),
                   model_uri=ANALYSIS.hdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.latitude = Slot(uri=LOCATION.latitude, name="latitude", curie=LOCATION.curie('latitude'),
                   model_uri=ANALYSIS.latitude, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.locality = Slot(uri=LOCATION.locality, name="locality", curie=LOCATION.curie('locality'),
                   model_uri=ANALYSIS.locality, domain=None, range=Optional[str])

slots.longitude = Slot(uri=LOCATION.longitude, name="longitude", curie=LOCATION.curie('longitude'),
                   model_uri=ANALYSIS.longitude, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.pdop = Slot(uri=LOCATION.pdop, name="pdop", curie=LOCATION.curie('pdop'),
                   model_uri=ANALYSIS.pdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.postalCode = Slot(uri=LOCATION.postalCode, name="postalCode", curie=LOCATION.curie('postalCode'),
                   model_uri=ANALYSIS.postalCode, domain=None, range=Optional[str])

slots.region = Slot(uri=LOCATION.region, name="region", curie=LOCATION.curie('region'),
                   model_uri=ANALYSIS.region, domain=None, range=Optional[str])

slots.street = Slot(uri=LOCATION.street, name="street", curie=LOCATION.curie('street'),
                   model_uri=ANALYSIS.street, domain=None, range=Optional[str])

slots.tdop = Slot(uri=LOCATION.tdop, name="tdop", curie=LOCATION.curie('tdop'),
                   model_uri=ANALYSIS.tdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.vdop = Slot(uri=LOCATION.vdop, name="vdop", curie=LOCATION.curie('vdop'),
                   model_uri=ANALYSIS.vdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.patternExpression = Slot(uri=PATTERN.patternExpression, name="patternExpression", curie=PATTERN.curie('patternExpression'),
                   model_uri=ANALYSIS.patternExpression, domain=None, range=Optional[str])

slots.list = Slot(uri=TYPES.list, name="list", curie=TYPES.curie('list'),
                   model_uri=ANALYSIS.list, domain=None, range=Optional[Union[dict, List]])

slots.listItem = Slot(uri=TYPES.listItem, name="listItem", curie=TYPES.curie('listItem'),
                   model_uri=ANALYSIS.listItem, domain=None, range=Optional[Union[dict, ListItem]])

slots.identifier = Slot(uri=TYPES.identifier, name="identifier", curie=TYPES.curie('identifier'),
                   model_uri=ANALYSIS.identifier, domain=None, range=Optional[str])

slots.nativeFormatString = Slot(uri=TYPES.nativeFormatString, name="nativeFormatString", curie=TYPES.curie('nativeFormatString'),
                   model_uri=ANALYSIS.nativeFormatString, domain=None, range=Optional[str])

slots.structuredText = Slot(uri=TYPES.structuredText, name="structuredText", curie=TYPES.curie('structuredText'),
                   model_uri=ANALYSIS.structuredText, domain=None, range=Optional[str])

slots.entry = Slot(uri=TYPES.entry, name="entry", curie=TYPES.curie('entry'),
                   model_uri=ANALYSIS.entry, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.hashMethod = Slot(uri=TYPES.hashMethod, name="hashMethod", curie=TYPES.curie('hashMethod'),
                   model_uri=ANALYSIS.hashMethod, domain=None, range=Optional[str])

slots.hashValue = Slot(uri=TYPES.hashValue, name="hashValue", curie=TYPES.curie('hashValue'),
                   model_uri=ANALYSIS.hashValue, domain=None, range=Optional[hex])

slots.key = Slot(uri=TYPES.key, name="key", curie=TYPES.curie('key'),
                   model_uri=ANALYSIS.key, domain=None, range=Optional[str])

slots.threadNextItem = Slot(uri=TYPES.threadNextItem, name="threadNextItem", curie=TYPES.curie('threadNextItem'),
                   model_uri=ANALYSIS.threadNextItem, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadOriginItem = Slot(uri=TYPES.threadOriginItem, name="threadOriginItem", curie=TYPES.curie('threadOriginItem'),
                   model_uri=ANALYSIS.threadOriginItem, domain=Thread, range=Optional[Union[dict, "ThreadItem"]])

slots.threadPredecessor = Slot(uri=TYPES.threadPredecessor, name="threadPredecessor", curie=TYPES.curie('threadPredecessor'),
                   model_uri=ANALYSIS.threadPredecessor, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadPreviousItem = Slot(uri=TYPES.threadPreviousItem, name="threadPreviousItem", curie=TYPES.curie('threadPreviousItem'),
                   model_uri=ANALYSIS.threadPreviousItem, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadSuccessor = Slot(uri=TYPES.threadSuccessor, name="threadSuccessor", curie=TYPES.curie('threadSuccessor'),
                   model_uri=ANALYSIS.threadSuccessor, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadTerminalItem = Slot(uri=TYPES.threadTerminalItem, name="threadTerminalItem", curie=TYPES.curie('threadTerminalItem'),
                   model_uri=ANALYSIS.threadTerminalItem, domain=Thread, range=Optional[Union[dict, "ThreadItem"]])

slots._value = Slot(uri=TYPES._value, name="_value", curie=TYPES.curie('_value'),
                   model_uri=ANALYSIS._value, domain=None, range=Optional[str])

slots.AccountTypeVocab = Slot(uri=VOCABULARY.AccountTypeVocab, name="AccountTypeVocab", curie=VOCABULARY.curie('AccountTypeVocab'),
                   model_uri=ANALYSIS.AccountTypeVocab, domain=None, range=Optional[Union[str, "AccountTypeEnum"]])

slots.ActionArgumentNameVocab = Slot(uri=VOCABULARY.ActionArgumentNameVocab, name="ActionArgumentNameVocab", curie=VOCABULARY.curie('ActionArgumentNameVocab'),
                   model_uri=ANALYSIS.ActionArgumentNameVocab, domain=None, range=Optional[Union[str, "ActionArgumentNameEnum"]])

slots.ActionNameVocab = Slot(uri=VOCABULARY.ActionNameVocab, name="ActionNameVocab", curie=VOCABULARY.curie('ActionNameVocab'),
                   model_uri=ANALYSIS.ActionNameVocab, domain=None, range=Optional[str])

slots.ActionRelationshipTypeVocab = Slot(uri=VOCABULARY.ActionRelationshipTypeVocab, name="ActionRelationshipTypeVocab", curie=VOCABULARY.curie('ActionRelationshipTypeVocab'),
                   model_uri=ANALYSIS.ActionRelationshipTypeVocab, domain=None, range=Optional[Union[str, "ActionRelationshipTypeEnum"]])

slots.ActionStatusTypeVocab = Slot(uri=VOCABULARY.ActionStatusTypeVocab, name="ActionStatusTypeVocab", curie=VOCABULARY.curie('ActionStatusTypeVocab'),
                   model_uri=ANALYSIS.ActionStatusTypeVocab, domain=None, range=Optional[Union[str, "ActionStatusTypeEnum"]])

slots.ActionTypeVocab = Slot(uri=VOCABULARY.ActionTypeVocab, name="ActionTypeVocab", curie=VOCABULARY.curie('ActionTypeVocab'),
                   model_uri=ANALYSIS.ActionTypeVocab, domain=None, range=Optional[Union[str, "ActionTypeEnum"]])

slots.BitnessVocab = Slot(uri=VOCABULARY.BitnessVocab, name="BitnessVocab", curie=VOCABULARY.curie('BitnessVocab'),
                   model_uri=ANALYSIS.BitnessVocab, domain=None, range=Optional[Union[str, "BitnessEnum"]])

slots.CharacterEncodingVocab = Slot(uri=VOCABULARY.CharacterEncodingVocab, name="CharacterEncodingVocab", curie=VOCABULARY.curie('CharacterEncodingVocab'),
                   model_uri=ANALYSIS.CharacterEncodingVocab, domain=None, range=Optional[Union[str, "CharacterEncodingEnum"]])

slots.ContactAddressScopeVocab = Slot(uri=VOCABULARY.ContactAddressScopeVocab, name="ContactAddressScopeVocab", curie=VOCABULARY.curie('ContactAddressScopeVocab'),
                   model_uri=ANALYSIS.ContactAddressScopeVocab, domain=None, range=Optional[Union[str, "ContactAddressScopeEnum"]])

slots.ContactEmailScopeVocab = Slot(uri=VOCABULARY.ContactEmailScopeVocab, name="ContactEmailScopeVocab", curie=VOCABULARY.curie('ContactEmailScopeVocab'),
                   model_uri=ANALYSIS.ContactEmailScopeVocab, domain=None, range=Optional[Union[str, "ContactEmailScopeEnum"]])

slots.ContactPhoneScopeVocab = Slot(uri=VOCABULARY.ContactPhoneScopeVocab, name="ContactPhoneScopeVocab", curie=VOCABULARY.curie('ContactPhoneScopeVocab'),
                   model_uri=ANALYSIS.ContactPhoneScopeVocab, domain=None, range=Optional[Union[str, "ContactPhoneEnum"]])

slots.ContactSIPScopeVocab = Slot(uri=VOCABULARY.ContactSIPScopeVocab, name="ContactSIPScopeVocab", curie=VOCABULARY.curie('ContactSIPScopeVocab'),
                   model_uri=ANALYSIS.ContactSIPScopeVocab, domain=None, range=Optional[Union[str, "ContactSIPScopeEnum"]])

slots.ContactURLScopeVocab = Slot(uri=VOCABULARY.ContactURLScopeVocab, name="ContactURLScopeVocab", curie=VOCABULARY.curie('ContactURLScopeVocab'),
                   model_uri=ANALYSIS.ContactURLScopeVocab, domain=None, range=Optional[Union[str, "ContactURLScopeEnum"]])

slots.DiskTypeVocab = Slot(uri=VOCABULARY.DiskTypeVocab, name="DiskTypeVocab", curie=VOCABULARY.curie('DiskTypeVocab'),
                   model_uri=ANALYSIS.DiskTypeVocab, domain=None, range=Optional[Union[str, "DiskTypeEnum"]])

slots.EndiannessTypeVocab = Slot(uri=VOCABULARY.EndiannessTypeVocab, name="EndiannessTypeVocab", curie=VOCABULARY.curie('EndiannessTypeVocab'),
                   model_uri=ANALYSIS.EndiannessTypeVocab, domain=None, range=Optional[Union[str, "EndiannessTypeEnum"]])

slots.HashNameVocab = Slot(uri=VOCABULARY.HashNameVocab, name="HashNameVocab", curie=VOCABULARY.curie('HashNameVocab'),
                   model_uri=ANALYSIS.HashNameVocab, domain=None, range=Optional[Union[str, "HashNameEnum"]])

slots.LibraryTypeVocab = Slot(uri=VOCABULARY.LibraryTypeVocab, name="LibraryTypeVocab", curie=VOCABULARY.curie('LibraryTypeVocab'),
                   model_uri=ANALYSIS.LibraryTypeVocab, domain=None, range=Optional[Union[str, "LibraryTypeEnum"]])

slots.MemoryBlockTypeVocab = Slot(uri=VOCABULARY.MemoryBlockTypeVocab, name="MemoryBlockTypeVocab", curie=VOCABULARY.curie('MemoryBlockTypeVocab'),
                   model_uri=ANALYSIS.MemoryBlockTypeVocab, domain=None, range=Optional[Union[str, "MemoryBlockTypeEnum"]])

slots.ObservableObjectRelationshipVocab = Slot(uri=VOCABULARY.ObservableObjectRelationshipVocab, name="ObservableObjectRelationshipVocab", curie=VOCABULARY.curie('ObservableObjectRelationshipVocab'),
                   model_uri=ANALYSIS.ObservableObjectRelationshipVocab, domain=None, range=Optional[Union[str, "ObservableObjectRelationshipEnum"]])

slots.ObservableObjectStateVocab = Slot(uri=VOCABULARY.ObservableObjectStateVocab, name="ObservableObjectStateVocab", curie=VOCABULARY.curie('ObservableObjectStateVocab'),
                   model_uri=ANALYSIS.ObservableObjectStateVocab, domain=None, range=Optional[Union[str, "ObservableObjectStateEnum"]])

slots.PartitionTypeVocab = Slot(uri=VOCABULARY.PartitionTypeVocab, name="PartitionTypeVocab", curie=VOCABULARY.curie('PartitionTypeVocab'),
                   model_uri=ANALYSIS.PartitionTypeVocab, domain=None, range=Optional[Union[str, "PartitionTypeEnum"]])

slots.ProcessorArchVocab = Slot(uri=VOCABULARY.ProcessorArchVocab, name="ProcessorArchVocab", curie=VOCABULARY.curie('ProcessorArchVocab'),
                   model_uri=ANALYSIS.ProcessorArchVocab, domain=None, range=Optional[Union[str, "ProcessorArchEnum"]])

slots.RecoveredObjectStatusVocab = Slot(uri=VOCABULARY.RecoveredObjectStatusVocab, name="RecoveredObjectStatusVocab", curie=VOCABULARY.curie('RecoveredObjectStatusVocab'),
                   model_uri=ANALYSIS.RecoveredObjectStatusVocab, domain=None, range=Optional[Union[str, "RecoveredObjectStatusEnum"]])

slots.RegionalRegistry_typeVocab = Slot(uri=VOCABULARY.RegionalRegistry_typeVocab, name="RegionalRegistry typeVocab", curie=VOCABULARY.curie('RegionalRegistry_typeVocab'),
                   model_uri=ANALYSIS.RegionalRegistry_typeVocab, domain=None, range=Optional[Union[str, "RegionalRegistryTypeEnum"]])

slots.RegistryDatatypeVocab = Slot(uri=VOCABULARY.RegistryDatatypeVocab, name="RegistryDatatypeVocab", curie=VOCABULARY.curie('RegistryDatatypeVocab'),
                   model_uri=ANALYSIS.RegistryDatatypeVocab, domain=None, range=Optional[Union[str, "RegistryDatatypeEnum"]])

slots.SIMFormVocab = Slot(uri=VOCABULARY.SIMFormVocab, name="SIMFormVocab", curie=VOCABULARY.curie('SIMFormVocab'),
                   model_uri=ANALYSIS.SIMFormVocab, domain=None, range=Optional[Union[str, "SIMFormEnum"]])

slots.SIMTypeVocab = Slot(uri=VOCABULARY.SIMTypeVocab, name="SIMTypeVocab", curie=VOCABULARY.curie('SIMTypeVocab'),
                   model_uri=ANALYSIS.SIMTypeVocab, domain=None, range=Optional[Union[str, "SIMTypeEnum"]])

slots.TaskActionTypeVocab = Slot(uri=VOCABULARY.TaskActionTypeVocab, name="TaskActionTypeVocab", curie=VOCABULARY.curie('TaskActionTypeVocab'),
                   model_uri=ANALYSIS.TaskActionTypeVocab, domain=None, range=Optional[Union[str, "TaskActionTypeEnum"]])

slots.TaskFlagVocab = Slot(uri=VOCABULARY.TaskFlagVocab, name="TaskFlagVocab", curie=VOCABULARY.curie('TaskFlagVocab'),
                   model_uri=ANALYSIS.TaskFlagVocab, domain=None, range=Optional[Union[str, "TaskFlagEnum"]])

slots.TaskPriorityVocab = Slot(uri=VOCABULARY.TaskPriorityVocab, name="TaskPriorityVocab", curie=VOCABULARY.curie('TaskPriorityVocab'),
                   model_uri=ANALYSIS.TaskPriorityVocab, domain=None, range=Optional[Union[str, "TaskPriorityEnum"]])

slots.TaskStatusVocab = Slot(uri=VOCABULARY.TaskStatusVocab, name="TaskStatusVocab", curie=VOCABULARY.curie('TaskStatusVocab'),
                   model_uri=ANALYSIS.TaskStatusVocab, domain=None, range=Optional[Union[str, "TaskStatusEnum"]])

slots.ThreadRunningStatusVocab = Slot(uri=VOCABULARY.ThreadRunningStatusVocab, name="ThreadRunningStatusVocab", curie=VOCABULARY.curie('ThreadRunningStatusVocab'),
                   model_uri=ANALYSIS.ThreadRunningStatusVocab, domain=None, range=Optional[Union[str, "ThreadRunningStatusEnum"]])

slots.TimestampPrecisionVocab = Slot(uri=VOCABULARY.TimestampPrecisionVocab, name="TimestampPrecisionVocab", curie=VOCABULARY.curie('TimestampPrecisionVocab'),
                   model_uri=ANALYSIS.TimestampPrecisionVocab, domain=None, range=Optional[Union[str, "TimestampPrecisionEnum"]])

slots.TrendVocab = Slot(uri=VOCABULARY.TrendVocab, name="TrendVocab", curie=VOCABULARY.curie('TrendVocab'),
                   model_uri=ANALYSIS.TrendVocab, domain=None, range=Optional[Union[str, "TrendEnum"]])

slots.TriggerFrequencyVocab = Slot(uri=VOCABULARY.TriggerFrequencyVocab, name="TriggerFrequencyVocab", curie=VOCABULARY.curie('TriggerFrequencyVocab'),
                   model_uri=ANALYSIS.TriggerFrequencyVocab, domain=None, range=Optional[Union[str, "TriggerFrequencyEnum"]])

slots.TriggerTypeVocab = Slot(uri=VOCABULARY.TriggerTypeVocab, name="TriggerTypeVocab", curie=VOCABULARY.curie('TriggerTypeVocab'),
                   model_uri=ANALYSIS.TriggerTypeVocab, domain=None, range=Optional[Union[str, "TriggerTypeEnum"]])

slots.URLTransitionTypeVocab = Slot(uri=VOCABULARY.URLTransitionTypeVocab, name="URLTransitionTypeVocab", curie=VOCABULARY.curie('URLTransitionTypeVocab'),
                   model_uri=ANALYSIS.URLTransitionTypeVocab, domain=None, range=Optional[Union[str, "URLTransitionTypeEnum"]])

slots.UnixProcessStateVocab = Slot(uri=VOCABULARY.UnixProcessStateVocab, name="UnixProcessStateVocab", curie=VOCABULARY.curie('UnixProcessStateVocab'),
                   model_uri=ANALYSIS.UnixProcessStateVocab, domain=None, range=Optional[Union[str, "UnixProcessStateEnum"]])

slots.WhoisContactTypeVocab = Slot(uri=VOCABULARY.WhoisContactTypeVocab, name="WhoisContactTypeVocab", curie=VOCABULARY.curie('WhoisContactTypeVocab'),
                   model_uri=ANALYSIS.WhoisContactTypeVocab, domain=None, range=Optional[Union[str, "WhoisContactTypeEnum"]])

slots.WhoisDNSSECTypeVocab = Slot(uri=VOCABULARY.WhoisDNSSECTypeVocab, name="WhoisDNSSECTypeVocab", curie=VOCABULARY.curie('WhoisDNSSECTypeVocab'),
                   model_uri=ANALYSIS.WhoisDNSSECTypeVocab, domain=None, range=Optional[Union[str, "WhoisDNSSECTypeEnum"]])

slots.WhoisStatusTypeVocab = Slot(uri=VOCABULARY.WhoisStatusTypeVocab, name="WhoisStatusTypeVocab", curie=VOCABULARY.curie('WhoisStatusTypeVocab'),
                   model_uri=ANALYSIS.WhoisStatusTypeVocab, domain=None, range=Optional[Union[str, "WhoisStatusTypeEnum"]])

slots.WindowsDriveTypeVocab = Slot(uri=VOCABULARY.WindowsDriveTypeVocab, name="WindowsDriveTypeVocab", curie=VOCABULARY.curie('WindowsDriveTypeVocab'),
                   model_uri=ANALYSIS.WindowsDriveTypeVocab, domain=None, range=Optional[Union[str, "WindowsDriveTypeEnum"]])

slots.WindowsVolumeAttributeVocab = Slot(uri=VOCABULARY.WindowsVolumeAttributeVocab, name="WindowsVolumeAttributeVocab", curie=VOCABULARY.curie('WindowsVolumeAttributeVocab'),
                   model_uri=ANALYSIS.WindowsVolumeAttributeVocab, domain=None, range=Optional[Union[str, "WindowsVolumeAttributeEnum"]])

slots.WirelessNetworkSecurityModeVocab = Slot(uri=VOCABULARY.WirelessNetworkSecurityModeVocab, name="WirelessNetworkSecurityModeVocab", curie=VOCABULARY.curie('WirelessNetworkSecurityModeVocab'),
                   model_uri=ANALYSIS.WirelessNetworkSecurityModeVocab, domain=None, range=Optional[Union[str, "WirelessNetworkSecurityModeEnum"]])

slots.element = Slot(uri=COLLECTIONS.element, name="element", curie=COLLECTIONS.curie('element'),
                   model_uri=ANALYSIS.element, domain=Collection, range=Optional[Union[dict, "Thing"]])

slots.elementOf = Slot(uri=COLLECTIONS.elementOf, name="elementOf", curie=COLLECTIONS.curie('elementOf'),
                   model_uri=ANALYSIS.elementOf, domain=Thing, range=Optional[Union[dict, Collection]])

slots.firstItem = Slot(uri=COLLECTIONS.firstItem, name="firstItem", curie=COLLECTIONS.curie('firstItem'),
                   model_uri=ANALYSIS.firstItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.firstItemOf = Slot(uri=COLLECTIONS.firstItemOf, name="firstItemOf", curie=COLLECTIONS.curie('firstItemOf'),
                   model_uri=ANALYSIS.firstItemOf, domain=ListItem, range=Optional[Union[dict, List]])

slots.followedBy = Slot(uri=COLLECTIONS.followedBy, name="followedBy", curie=COLLECTIONS.curie('followedBy'),
                   model_uri=ANALYSIS.followedBy, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.item = Slot(uri=COLLECTIONS.item, name="item", curie=COLLECTIONS.curie('item'),
                   model_uri=ANALYSIS.item, domain=Bag, range=Optional[Union[dict, "CoItem"]])

slots.itemContent = Slot(uri=COLLECTIONS.itemContent, name="itemContent", curie=COLLECTIONS.curie('itemContent'),
                   model_uri=ANALYSIS.itemContent, domain=CoItem, range=Optional[Union[dict, "CoItem"]])

slots.itemContentOf = Slot(uri=COLLECTIONS.itemContentOf, name="itemContentOf", curie=COLLECTIONS.curie('itemContentOf'),
                   model_uri=ANALYSIS.itemContentOf, domain=CoItem, range=Optional[Union[dict, CoItem]])

slots.itemOf = Slot(uri=COLLECTIONS.itemOf, name="itemOf", curie=COLLECTIONS.curie('itemOf'),
                   model_uri=ANALYSIS.itemOf, domain=CoItem, range=Optional[Union[dict, Bag]])

slots.lastItem = Slot(uri=COLLECTIONS.lastItem, name="lastItem", curie=COLLECTIONS.curie('lastItem'),
                   model_uri=ANALYSIS.lastItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.lastItemOf = Slot(uri=COLLECTIONS.lastItemOf, name="lastItemOf", curie=COLLECTIONS.curie('lastItemOf'),
                   model_uri=ANALYSIS.lastItemOf, domain=ListItem, range=Optional[Union[dict, List]])

slots.nextItem = Slot(uri=COLLECTIONS.nextItem, name="nextItem", curie=COLLECTIONS.curie('nextItem'),
                   model_uri=ANALYSIS.nextItem, domain=Thing, range=Optional[Union[dict, ListItem]])

slots.precededBy = Slot(uri=COLLECTIONS.precededBy, name="precededBy", curie=COLLECTIONS.curie('precededBy'),
                   model_uri=ANALYSIS.precededBy, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.previousItem = Slot(uri=COLLECTIONS.previousItem, name="previousItem", curie=COLLECTIONS.curie('previousItem'),
                   model_uri=ANALYSIS.previousItem, domain=ListItem, range=Optional[Union[dict, "Thing"]])

slots._index = Slot(uri=COLLECTIONS._index, name="_index", curie=COLLECTIONS.curie('_index'),
                   model_uri=ANALYSIS._index, domain=ListItem, range=Optional[Union[int, PositiveInteger]])

slots.size = Slot(uri=COLLECTIONS.size, name="size", curie=COLLECTIONS.curie('size'),
                   model_uri=ANALYSIS.size, domain=Collection, range=Optional[Union[int, PositiveInteger]])

slots.AnalyticResult_resultContent = Slot(uri=ANALYSIS.resultContent, name="AnalyticResult_resultContent", curie=ANALYSIS.curie('resultContent'),
                   model_uri=ANALYSIS.AnalyticResult_resultContent, domain=AnalyticResult, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ArtifactClassificationResultFacet_classification = Slot(uri=ANALYSIS.classification, name="ArtifactClassificationResultFacet_classification", curie=ANALYSIS.curie('classification'),
                   model_uri=ANALYSIS.ArtifactClassificationResultFacet_classification, domain=ArtifactClassificationResultFacet, range=Optional[Union[Union[dict, ArtifactClassification], List[Union[dict, ArtifactClassification]]]])

slots.Action_subaction = Slot(uri=ACTION.subaction, name="Action_subaction", curie=ACTION.curie('subaction'),
                   model_uri=ANALYSIS.Action_subaction, domain=Action, range=Optional[Union[Union[dict, "Action"], List[Union[dict, "Action"]]]])

slots.Action_error = Slot(uri=ACTION.error, name="Action_error", curie=ACTION.curie('error'),
                   model_uri=ANALYSIS.Action_error, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_instrument = Slot(uri=ACTION.instrument, name="Action_instrument", curie=ACTION.curie('instrument'),
                   model_uri=ANALYSIS.Action_instrument, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_object = Slot(uri=CORE.object, name="Action_object", curie=CORE.curie('object'),
                   model_uri=ANALYSIS.Action_object, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_participant = Slot(uri=ACTION.participant, name="Action_participant", curie=ACTION.curie('participant'),
                   model_uri=ANALYSIS.Action_participant, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_result = Slot(uri=ACTION.result, name="Action_result", curie=ACTION.curie('result'),
                   model_uri=ANALYSIS.Action_result, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_location = Slot(uri=ACTION.location, name="Action_location", curie=ACTION.curie('location'),
                   model_uri=ANALYSIS.Action_location, domain=Action, range=Optional[Union[Union[dict, "Location"], List[Union[dict, "Location"]]]])

slots.Action_endTime = Slot(uri=CORE.endTime, name="Action_endTime", curie=CORE.curie('endTime'),
                   model_uri=ANALYSIS.Action_endTime, domain=Action, range=Optional[Union[str, XSDDateTime]])

slots.Action_startTime = Slot(uri=CORE.startTime, name="Action_startTime", curie=CORE.curie('startTime'),
                   model_uri=ANALYSIS.Action_startTime, domain=Action, range=Optional[Union[str, XSDDateTime]])

slots.ActionArgumentFacet_argumentName = Slot(uri=ACTION.argumentName, name="ActionArgumentFacet_argumentName", curie=ACTION.curie('argumentName'),
                   model_uri=ANALYSIS.ActionArgumentFacet_argumentName, domain=ActionArgumentFacet, range=str)

slots.ActionArgumentFacet_value = Slot(uri=CORE.value, name="ActionArgumentFacet_value", curie=CORE.curie('value'),
                   model_uri=ANALYSIS.ActionArgumentFacet_value, domain=ActionArgumentFacet, range=str)

slots.ActionFrequencyFacet_rate = Slot(uri=ACTION.rate, name="ActionFrequencyFacet_rate", curie=ACTION.curie('rate'),
                   model_uri=ANALYSIS.ActionFrequencyFacet_rate, domain=ActionFrequencyFacet, range=Union[Decimal, DecimalType])

slots.ActionFrequencyFacet_scale = Slot(uri=ACTION.scale, name="ActionFrequencyFacet_scale", curie=ACTION.curie('scale'),
                   model_uri=ANALYSIS.ActionFrequencyFacet_scale, domain=ActionFrequencyFacet, range=str)

slots.ActionFrequencyFacet_units = Slot(uri=ACTION.units, name="ActionFrequencyFacet_units", curie=ACTION.curie('units'),
                   model_uri=ANALYSIS.ActionFrequencyFacet_units, domain=ActionFrequencyFacet, range=str)

slots.ActionFrequencyFacet_trend = Slot(uri=ACTION.trend, name="ActionFrequencyFacet_trend", curie=ACTION.curie('trend'),
                   model_uri=ANALYSIS.ActionFrequencyFacet_trend, domain=ActionFrequencyFacet, range=Union[str, "TrendEnum"])

slots.ActionLifecycle_phase = Slot(uri=ACTION.phase, name="ActionLifecycle_phase", curie=ACTION.curie('phase'),
                   model_uri=ANALYSIS.ActionLifecycle_phase, domain=ActionLifecycle, range=Union[dict, "ArrayOfAction"])

slots.ActionLifecycle_error = Slot(uri=ACTION.error, name="ActionLifecycle_error", curie=ACTION.curie('error'),
                   model_uri=ANALYSIS.ActionLifecycle_error, domain=ActionLifecycle, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ActionLifecycle_endTime = Slot(uri=CORE.endTime, name="ActionLifecycle_endTime", curie=CORE.curie('endTime'),
                   model_uri=ANALYSIS.ActionLifecycle_endTime, domain=ActionLifecycle, range=Optional[Union[str, XSDDateTime]])

slots.ActionLifecycle_startTime = Slot(uri=CORE.startTime, name="ActionLifecycle_startTime", curie=CORE.curie('startTime'),
                   model_uri=ANALYSIS.ActionLifecycle_startTime, domain=ActionLifecycle, range=Optional[Union[str, XSDDateTime]])

slots.ActionLifecycle_actionCount = Slot(uri=ACTION.actionCount, name="ActionLifecycle_actionCount", curie=ACTION.curie('actionCount'),
                   model_uri=ANALYSIS.ActionLifecycle_actionCount, domain=ActionLifecycle, range=Optional[Union[int, NonNegativeIntegerType]])

slots.ActionLifecycle_actionStatus = Slot(uri=ACTION.actionStatus, name="ActionLifecycle_actionStatus", curie=ACTION.curie('actionStatus'),
                   model_uri=ANALYSIS.ActionLifecycle_actionStatus, domain=ActionLifecycle, range=Optional[Union[str, "ActionStatusTypeEnum"]])

slots.ArrayOfAction_action = Slot(uri=ACTION.action, name="ArrayOfAction_action", curie=ACTION.curie('action'),
                   model_uri=ANALYSIS.ArrayOfAction_action, domain=ArrayOfAction, range=Optional[Union[dict, Action]])

slots.Annotation_object = Slot(uri=CORE.object, name="Annotation_object", curie=CORE.curie('object'),
                   model_uri=ANALYSIS.Annotation_object, domain=Annotation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Assertion_statement = Slot(uri=CORE.statement, name="Assertion_statement", curie=CORE.curie('statement'),
                   model_uri=ANALYSIS.Assertion_statement, domain=Assertion, range=Optional[Union[str, List[str]]])

slots.AttributedName_namingAuthority = Slot(uri=CORE.namingAuthority, name="AttributedName_namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=ANALYSIS.AttributedName_namingAuthority, domain=AttributedName, range=Optional[str])

slots.ConfidenceFacet_confidence = Slot(uri=CORE.confidence, name="ConfidenceFacet_confidence", curie=CORE.curie('confidence'),
                   model_uri=ANALYSIS.ConfidenceFacet_confidence, domain=ConfidenceFacet, range=Union[int, NonNegativeIntegerType])

slots.ContextualCompilation_object = Slot(uri=CORE.object, name="ContextualCompilation_object", curie=CORE.curie('object'),
                   model_uri=ANALYSIS.ContextualCompilation_object, domain=ContextualCompilation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.ControlledVocabulary_constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="ControlledVocabulary_constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=ANALYSIS.ControlledVocabulary_constrainingVocabularyReference, domain=ControlledVocabulary, range=Optional[Union[str, IriType]])

slots.ControlledVocabulary_constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="ControlledVocabulary_constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=ANALYSIS.ControlledVocabulary_constrainingVocabularyName, domain=ControlledVocabulary, range=Optional[str])

slots.ControlledVocabulary_value = Slot(uri=CORE.value, name="ControlledVocabulary_value", curie=CORE.curie('value'),
                   model_uri=ANALYSIS.ControlledVocabulary_value, domain=ControlledVocabulary, range=str)

slots.EnclosingCompilation_object = Slot(uri=CORE.object, name="EnclosingCompilation_object", curie=CORE.curie('object'),
                   model_uri=ANALYSIS.EnclosingCompilation_object, domain=EnclosingCompilation, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ExternalReference_referenceURL = Slot(uri=CORE.referenceURL, name="ExternalReference_referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=ANALYSIS.ExternalReference_referenceURL, domain=ExternalReference, range=Optional[Union[str, IriType]])

slots.ExternalReference_definingContext = Slot(uri=CORE.definingContext, name="ExternalReference_definingContext", curie=CORE.curie('definingContext'),
                   model_uri=ANALYSIS.ExternalReference_definingContext, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_externalIdentifier = Slot(uri=CORE.externalIdentifier, name="ExternalReference_externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=ANALYSIS.ExternalReference_externalIdentifier, domain=ExternalReference, range=Optional[str])

slots.Grouping_context = Slot(uri=CORE.context, name="Grouping_context", curie=CORE.curie('context'),
                   model_uri=ANALYSIS.Grouping_context, domain=Grouping, range=Optional[Union[str, List[str]]])

slots.Relationship_endTime = Slot(uri=CORE.endTime, name="Relationship_endTime", curie=CORE.curie('endTime'),
                   model_uri=ANALYSIS.Relationship_endTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.Relationship_isDirectional = Slot(uri=CORE.isDirectional, name="Relationship_isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=ANALYSIS.Relationship_isDirectional, domain=Relationship, range=Union[bool, BooleanType])

slots.Relationship_kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="Relationship_kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=ANALYSIS.Relationship_kindOfRelationship, domain=Relationship, range=Optional[str])

slots.Relationship_target = Slot(uri=CORE.target, name="Relationship_target", curie=CORE.curie('target'),
                   model_uri=ANALYSIS.Relationship_target, domain=Relationship, range=Union[dict, "UcoObject"])

slots.Relationship_source = Slot(uri=CORE.source, name="Relationship_source", curie=CORE.curie('source'),
                   model_uri=ANALYSIS.Relationship_source, domain=Relationship, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Relationship_startTime = Slot(uri=CORE.startTime, name="Relationship_startTime", curie=CORE.curie('startTime'),
                   model_uri=ANALYSIS.Relationship_startTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_description = Slot(uri=DCTERMS.description, name="UcoObject_description", curie=DCTERMS.curie('description'),
                   model_uri=ANALYSIS.UcoObject_description, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_createdBy = Slot(uri=CORE.createdBy, name="UcoObject_createdBy", curie=CORE.curie('createdBy'),
                   model_uri=ANALYSIS.UcoObject_createdBy, domain=UcoObject, range=Optional[str])

slots.UcoObject_externalReference = Slot(uri=CORE.externalReference, name="UcoObject_externalReference", curie=CORE.curie('externalReference'),
                   model_uri=ANALYSIS.UcoObject_externalReference, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_hasFacet = Slot(uri=CORE.hasFacet, name="UcoObject_hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=ANALYSIS.UcoObject_hasFacet, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_modifiedTime = Slot(uri=CORE.modifiedTime, name="UcoObject_modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=ANALYSIS.UcoObject_modifiedTime, domain=UcoObject, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_name = Slot(uri=RDFS.label, name="UcoObject_name", curie=RDFS.curie('label'),
                   model_uri=ANALYSIS.UcoObject_name, domain=UcoObject, range=Optional[str])

slots.UcoObject_objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="UcoObject_objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=ANALYSIS.UcoObject_objectCreatedTime, domain=UcoObject, range=Optional[Union[str, XSDDateTime]])

slots.UcoObject_objectMarking = Slot(uri=CORE.objectMarking, name="UcoObject_objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=ANALYSIS.UcoObject_objectMarking, domain=UcoObject, range=Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]])

slots.UcoObject_specVersion = Slot(uri=CORE.specVersion, name="UcoObject_specVersion", curie=CORE.curie('specVersion'),
                   model_uri=ANALYSIS.UcoObject_specVersion, domain=UcoObject, range=Optional[str])

slots.UcoObject_tag = Slot(uri=CORE.tag, name="UcoObject_tag", curie=CORE.curie('tag'),
                   model_uri=ANALYSIS.UcoObject_tag, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.GPSCoordinatesFacet_hdop = Slot(uri=LOCATION.hdop, name="GPSCoordinatesFacet_hdop", curie=LOCATION.curie('hdop'),
                   model_uri=ANALYSIS.GPSCoordinatesFacet_hdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.GPSCoordinatesFacet_pdop = Slot(uri=LOCATION.pdop, name="GPSCoordinatesFacet_pdop", curie=LOCATION.curie('pdop'),
                   model_uri=ANALYSIS.GPSCoordinatesFacet_pdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.GPSCoordinatesFacet_tdop = Slot(uri=LOCATION.tdop, name="GPSCoordinatesFacet_tdop", curie=LOCATION.curie('tdop'),
                   model_uri=ANALYSIS.GPSCoordinatesFacet_tdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.GPSCoordinatesFacet_vdop = Slot(uri=LOCATION.vdop, name="GPSCoordinatesFacet_vdop", curie=LOCATION.curie('vdop'),
                   model_uri=ANALYSIS.GPSCoordinatesFacet_vdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.LatLongCoordinatesFacet_altitude = Slot(uri=LOCATION.altitude, name="LatLongCoordinatesFacet_altitude", curie=LOCATION.curie('altitude'),
                   model_uri=ANALYSIS.LatLongCoordinatesFacet_altitude, domain=LatLongCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.LatLongCoordinatesFacet_latitude = Slot(uri=LOCATION.latitude, name="LatLongCoordinatesFacet_latitude", curie=LOCATION.curie('latitude'),
                   model_uri=ANALYSIS.LatLongCoordinatesFacet_latitude, domain=LatLongCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.LatLongCoordinatesFacet_longitude = Slot(uri=LOCATION.longitude, name="LatLongCoordinatesFacet_longitude", curie=LOCATION.curie('longitude'),
                   model_uri=ANALYSIS.LatLongCoordinatesFacet_longitude, domain=LatLongCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.SimpleAddressFacet_addressType = Slot(uri=LOCATION.addressType, name="SimpleAddressFacet_addressType", curie=LOCATION.curie('addressType'),
                   model_uri=ANALYSIS.SimpleAddressFacet_addressType, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_country = Slot(uri=LOCATION.country, name="SimpleAddressFacet_country", curie=LOCATION.curie('country'),
                   model_uri=ANALYSIS.SimpleAddressFacet_country, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_locality = Slot(uri=LOCATION.locality, name="SimpleAddressFacet_locality", curie=LOCATION.curie('locality'),
                   model_uri=ANALYSIS.SimpleAddressFacet_locality, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_postalCode = Slot(uri=LOCATION.postalCode, name="SimpleAddressFacet_postalCode", curie=LOCATION.curie('postalCode'),
                   model_uri=ANALYSIS.SimpleAddressFacet_postalCode, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_region = Slot(uri=LOCATION.region, name="SimpleAddressFacet_region", curie=LOCATION.curie('region'),
                   model_uri=ANALYSIS.SimpleAddressFacet_region, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_street = Slot(uri=LOCATION.street, name="SimpleAddressFacet_street", curie=LOCATION.curie('street'),
                   model_uri=ANALYSIS.SimpleAddressFacet_street, domain=SimpleAddressFacet, range=Optional[str])

slots.LogicalPattern_patternExpression = Slot(uri=PATTERN.patternExpression, name="LogicalPattern_patternExpression", curie=PATTERN.curie('patternExpression'),
                   model_uri=ANALYSIS.LogicalPattern_patternExpression, domain=LogicalPattern, range=Optional[str])

slots.ControlledDictionary_entry = Slot(uri=TYPES.entry, name="ControlledDictionary_entry", curie=TYPES.curie('entry'),
                   model_uri=ANALYSIS.ControlledDictionary_entry, domain=ControlledDictionary, range=Optional[Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]]])

slots.Dictionary_entry = Slot(uri=TYPES.entry, name="Dictionary_entry", curie=TYPES.curie('entry'),
                   model_uri=ANALYSIS.Dictionary_entry, domain=Dictionary, range=Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]])

slots.DictionaryEntry_key = Slot(uri=TYPES.key, name="DictionaryEntry_key", curie=TYPES.curie('key'),
                   model_uri=ANALYSIS.DictionaryEntry_key, domain=DictionaryEntry, range=str)

slots.DictionaryEntry_value = Slot(uri=CORE.value, name="DictionaryEntry_value", curie=CORE.curie('value'),
                   model_uri=ANALYSIS.DictionaryEntry_value, domain=DictionaryEntry, range=str)

slots.Hash_hashValue = Slot(uri=TYPES.hashValue, name="Hash_hashValue", curie=TYPES.curie('hashValue'),
                   model_uri=ANALYSIS.Hash_hashValue, domain=Hash, range=hex)

slots.Hash_hashMethod = Slot(uri=TYPES.hashMethod, name="Hash_hashMethod", curie=TYPES.curie('hashMethod'),
                   model_uri=ANALYSIS.Hash_hashMethod, domain=Hash, range=str)

slots.Thread_item = Slot(uri=COLLECTIONS.item, name="Thread_item", curie=COLLECTIONS.curie('item'),
                   model_uri=ANALYSIS.Thread_item, domain=Thread, range=Optional[Union[Union[dict, "ThreadItem"], List[Union[dict, "ThreadItem"]]]])

slots.ThreadItem_itemContent = Slot(uri=COLLECTIONS.itemContent, name="ThreadItem_itemContent", curie=COLLECTIONS.curie('itemContent'),
                   model_uri=ANALYSIS.ThreadItem_itemContent, domain=ThreadItem, range=Optional[Union[Union[dict, "CoItem"], List[Union[dict, "CoItem"]]]])

slots.Collection_element = Slot(uri=COLLECTIONS.element, name="Collection_element", curie=COLLECTIONS.curie('element'),
                   model_uri=ANALYSIS.Collection_element, domain=Collection, range=Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]])

slots.Collection_size = Slot(uri=COLLECTIONS.size, name="Collection_size", curie=COLLECTIONS.curie('size'),
                   model_uri=ANALYSIS.Collection_size, domain=Collection, range=Optional[Union[int, PositiveInteger]])

slots.List_lastItem = Slot(uri=COLLECTIONS.lastItem, name="List_lastItem", curie=COLLECTIONS.curie('lastItem'),
                   model_uri=ANALYSIS.List_lastItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.List_firstItem = Slot(uri=COLLECTIONS.firstItem, name="List_firstItem", curie=COLLECTIONS.curie('firstItem'),
                   model_uri=ANALYSIS.List_firstItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.List_item = Slot(uri=COLLECTIONS.item, name="List_item", curie=COLLECTIONS.curie('item'),
                   model_uri=ANALYSIS.List_item, domain=List, range=Optional[Union[Union[dict, "ListItem"], List[Union[dict, "ListItem"]]]])

slots.ListItem__index = Slot(uri=COLLECTIONS._index, name="ListItem__index", curie=COLLECTIONS.curie('_index'),
                   model_uri=ANALYSIS.ListItem__index, domain=ListItem, range=Union[int, PositiveInteger])