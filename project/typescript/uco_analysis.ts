/**
 * "An analysis is an action of detailed examination of something in order to understand its nature, context or essential features."
 */
export interface Analysis  extends Action  {
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An analytic result is a characterization of the understanding resulting from an analysis action."
 */
export interface AnalyticResult  extends Assertion  {
    /**
     * "The analysis action that resulted in an analytic result."
     */originatingAnalysis?: Analysis,
    /**
     * "Structured content expressing the results of an analysis action."
     */resultContent?: UcoObject[],
    /**
     * A textual statement of an assertion.
     */statement?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An analytic result facet is a grouping of characteristics unique to the results of an analysis action."
 */
export interface AnalyticResultFacet  extends Facet  {
}
/**
 * "An artifact classification is a single specific assertion that a particular class of a classification taxonomy applies to something."
 */
export interface ArtifactClassification  extends UcoInherentCharacterizationThing  {
    /**
     * "The level of confidence that a classification assertion is correct."
     */classificationConfidence?: number,
    /**
     * "A specific classification class."
     */class?: string,
}
/**
 * "An artifact classification result facet is a grouping of characteristics unique to the results of an artifact classification analysis action."
 */
export interface ArtifactClassificationResultFacet  extends AnalyticResultFacet  {
    /**
     * "An asserted classification of an analyzed artifact resulting from the analysis."
     */classification?: ArtifactClassification[],
}
/**
 * An annotation is an assertion made in relation to one or more objects.
 */
export interface Annotation  extends Assertion  {
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * A textual statement of an assertion.
     */statement?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An assertion is a statement declared to be true.
 */
export interface Assertion  extends UcoObject  {
    /**
     * A textual statement of an assertion.
     */statement?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An attributed name is a name of an entity issued by some attributed naming authority.
 */
export interface AttributedName  extends UcoObject  {
    /**
     * Specifies the naming authority that issued the name of the entity.
     */namingAuthority?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A bundle is a container for a grouping of UCO content with no presumption of shared context.
 */
export interface Bundle  extends EnclosingCompilation  {
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A compilation is a grouping of things.
 */
export interface Compilation  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some information.
 */
export interface ConfidenceFacet  extends Facet  {
    /**
     * An asserted level of certainty in the accuracy of some information.
     */confidence?: string,
}
/**
 * A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed on a given day, all accounts associated with a given person).
 */
export interface ContextualCompilation  extends Compilation  {
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A controlled vocabulary is an explicitly constrained set of string values.
 */
export interface ControlledVocabulary  extends UcoObject  {
    /**
     * A reference to a specification for an explicitly constrained set of string values. The specification may be unstructured (e.g., web page listing string values) or structured (e.g. RDF/OWL enumeration).
     */constrainingVocabularyReference?: string,
    /**
     * The name of an explicitly constrained set of string values.
     */constrainingVocabularyName?: string,
    /**
     * A string value.
     */value?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An enclosing compilation is a container for a grouping of things.
 */
export interface EnclosingCompilation  extends Compilation  {
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * Characteristics of a reference to a resource outside of the UCO.
 */
export interface ExternalReference  extends UcoInherentCharacterizationThing  {
    /**
     * A URL for some information defined external to the UCO context.
     */referenceURL?: string,
    /**
     * A description of the context relevant to the definition of a particular external reference identifier.
     */definingContext?: string,
    /**
     * An identifier for some information defined external to the UCO context.
     */externalIdentifier?: string,
}
/**
 * A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.
 */
export interface Facet  extends UcoInherentCharacterizationThing  {
}
/**
 * A grouping is a compilation of referenced UCO content with a shared context.
 */
export interface Grouping  extends ContextualCompilation  {
    /**
     * A description of particular contextual affinity.
     */context?: string,
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This class is an ontological structural abstraction for this concept. Implementations of this concept should utilize the identity:Identity class.
 */
export interface IdentityAbstraction  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An item is a distinct article or unit.
 */
export interface Item  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This class is an ontological structural abstraction for this concept. Implementations of this concept should utilize the marking MarkingDefinition class.
 */
export interface MarkingDefinitionAbstraction  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).
 */
export interface ModusOperandi  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to another object in some way.
 */
export interface Relationship  extends UcoObject  {
    /**
     * The ending time of a time range.
     */endTime?: string,
    /**
     * A specification whether or not a relationship assertion is limited to the context FROM a source object(s) TO a target object.
     */isDirectional?: string,
    /**
     * A characterization of the nature of a relationship between objects.
     */kindOfRelationship?: string,
    /**
     * The originating node of a specified relationship.
     */source?: UcoObject[],
    /**
     * The initial time of a time range.
     */startTime?: string,
    /**
     * The terminating node of a specified relationship.
     */target?: UcoObject,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a UCO domain object.
 */
export interface UcoInherentCharacterizationThing  extends UcoThing  {
}
/**
 * A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent, unifying and interoperable foundation for all explicit and inter-relatable content objects.
 */
export interface UcoObject  extends UcoThing  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * UcoThing is the top-level class within UCO.
 */
export interface UcoThing  {
}
/**
 * "An action is something that may be done or performed."
 */
export interface Action  extends UcoObject  {
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An action argument facet is a grouping of characteristics unique to a single parameter of an action."
 */
export interface ActionArgumentFacet  extends Facet  {
    /**
     * "The identifying label of an argument."
     */argumentName?: string,
    /**
     * "The value of an action parameter."
     */value?: string,
}
/**
 * "An action estimation facet is a grouping of characteristics unique to decision-focused approximation aspects for an action that may potentially be performed."
 */
export interface ActionEstimationFacet  extends Facet  {
    /**
     * "An estimation of the cost if the action is performed."
     */estimatedCost?: string,
    /**
     * "An estimation of the effectiveness of the action at achieving its objective if the action is performed."
     */estimatedEfficacy?: string,
    /**
     * "An estimation of the impact if the action is performed."
     */estimatedImpact?: string,
    /**
     * "The intended purpose for performing the action."
     */objective?: string,
}
/**
 * "An action frequency facet is a grouping of characteristics unique to the frequency of occurrence for an action."
 */
export interface ActionFrequencyFacet  extends Facet  {
    /**
     * "The frequency rate for the occurence of an action."
     */rate?: number,
    /**
     * "The time scale utilized for the frequency rate count for the occurence of an action."
     */scale?: string,
    /**
     * "The units of measure utilized for the frequency rate count for the occurence of an action."
     */units?: string,
    /**
     * "A characterization of the frequency trend for the occurence of an action."
     */trend?: string,
}
/**
 * "An action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action lifecycles."
 */
export interface ActionLifecycle  extends Action  {
    /**
     * "The ordered set of actions or sub action-lifecycles that represent the action lifecycle."
     */phase?: ArrayOfAction,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An action pattern is a grouping of characteristics unique to a combination of actions forming a consistent or characteristic arrangement."
 */
export interface ActionPattern  extends Action, Pattern  {
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An array of action is an ordered list of references to things that may be done or performed."
 */
export interface ArrayOfAction  extends UcoInherentCharacterizationThing  {
    /**
     * "A characterization of a single action."
     */action?: Action,
}
/**
 * "A controlled dictionary is a list of (term/key, value) pairs where each term/key exists no more than once and is constrained to an explicitly defined set of values."
 */
export interface ControlledDictionary  extends Dictionary  {
    /**
     * "A dictionary entry."
     */entry?: DictionaryEntry[],
}
/**
 * "A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an explicitly defined set of values."
 */
export interface ControlledDictionaryEntry  extends DictionaryEntry  {
    /**
     * "A key property of a single dictionary entry."
     */key?: string,
    /**
     * A string value.
     */value?: string,
}
/**
 * "A dictionary is list of (term/key, value) pairs with each term/key existing no more than once."
 */
export interface Dictionary  extends UcoInherentCharacterizationThing  {
    /**
     * "A dictionary entry."
     */entry?: DictionaryEntry[],
}
/**
 * "A dictionary entry is a single (term/key, value) pair."
 */
export interface DictionaryEntry  extends UcoInherentCharacterizationThing  {
    /**
     * "A key property of a single dictionary entry."
     */key?: string,
    /**
     * A string value.
     */value?: string,
}
/**
 * "A hash is a grouping of characteristics unique to the result of applying a mathematical algorithm that maps data of arbitrary size to a bit string (the 'hash') and is a one-way function, that is, a function which is practically infeasible to invert. This is commonly used for integrity checking of data. [based on https://en.wikipedia.org/wiki/Cryptographic_hash_function]"
 */
export interface Hash  extends UcoInherentCharacterizationThing  {
    /**
     * "A cryptographic hash value."
     */hashValue?: string,
    /**
     * "A particular cryptographic hashing method (e.g., MD5)."
     */hashMethod?: string,
}
/**
 * "A semi-ordered array of items, that can be present in multiple copies.  Implemetation of a UCO Thread is similar to a Collections Ontology List, except a Thread may fork and merge - that is, one of its members may have two or more direct successors, and two or more direct predecessors."
 */
export interface Thread  extends Bag, UcoThing  {
    /**
     * The link to every item of the bag
     */item?: ThreadItem[],
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * "A ThreadItem is a member of a thread."
 */
export interface ThreadItem  extends UcoThing  {
    /**
     * The link to the actual resource to which the item refers.
     */itemContent?: CoItem[],
}
/**
 * Collection that can have a number of copies of each object
 */
export interface Bag  extends Collection  {
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * A group of objects that can be considered as a whole.
 */
export interface Collection  extends Thing  {
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * Element belonging to a bag
 */
export interface CoItem  extends Thing  {
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
}
/**
 * An ordered array of items, that can be present in multiple copies
 */
export interface List  extends Bag  {
    /**
     * The link to every item of the bag
     */item?: ListItem[],
    /**
     * The link to the last item of the list.
     */lastItem?: ListItem,
    /**
     * The link to the first item of the list.
     */firstItem?: ListItem,
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * element belonging to a list
 */
export interface ListItem  extends CoItem  {
    /**
     * A number identifying the position, starting from 1, of a particular list item within a list.
     */_index?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
}
/**
 * A collection that cannot contain duplicate elements.
 */
export interface Set  extends Collection  {
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}

export interface Thing  {
}
/**
 * A logical pattern is a grouping of characteristics unique to an informational pattern expressed via a structured pattern expression following the rules of logic.
 */
export interface LogicalPattern  extends Pattern  {
    /**
     * An explicit logical pattern expression.
     */patternExpression?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A pattern is a combination of properties, acts, tendencies, etc., forming a consistent or characteristic arrangement.
 */
export interface Pattern  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A pattern expression is a grouping of characteristics unique to an explicit logical expression defining a pattern (e.g., regular expression, SQL Select expression, etc.).
 */
export interface PatternExpression  extends UcoInherentCharacterizationThing  {
}
/**
 * A GPS coordinates facet is a grouping of characteristics unique to the expression of quantified dilution of precision (DOP) for an asserted set of geolocation coordinates typically associated with satellite navigation such as the Global Positioning System (GPS).
 */
export interface GPSCoordinatesFacet  extends Facet  {
    /**
     * The horizontal dilution of precision of the GPS location.
     */hdop?: number,
    /**
     * The positional (3D) dilution of precision of the GPS location.
     */pdop?: number,
    /**
     * The temporal dilution of precision of the GPS location.
     */tdop?: number,
    /**
     * The vertical dilution of precision of the GPS location.
     */vdop?: number,
}
/**
 * A lat long coordinates facet is a grouping of characteristics unique to the expression of a geolocation as the intersection of specific latitude, longitude, and altitude values.
 */
export interface LatLongCoordinatesFacet  extends Facet  {
    /**
     * The altitude coordinate of a geolocation.
     */altitude?: number,
    /**
     * The latitude coordinate of a geolocation.
     */latitude?: number,
    /**
     * The longitude coordinate of a geolocation.
     */longitude?: number,
}
/**
 * A location is a geospatial place, site, or position.
 */
export interface Location  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A simple address facet is a grouping of characteristics unique to a geolocation expressed as an administrative address.
 */
export interface SimpleAddressFacet  extends Facet  {
    /**
     * The type of the address, for instance home or work.
     */addressType?: string,
    /**
     * The name of the geolocation country.
     */country?: string,
    /**
     * The name of the geolocation locality (e.g., city).
     */locality?: string,
    /**
     * The zip-code.
     */postalCode?: string,
    /**
     * The name of the geolocation region (e.g., state).
     */region?: string,
    /**
     * The name of the street.
     */street?: string,
}

