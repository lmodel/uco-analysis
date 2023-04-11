package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  "An artifact classification result facet is a grouping of characteristics unique to the results of an artifact classification analysis action."
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArtifactClassificationResultFacet extends AnalyticResultFacet {

  private List<ArtifactClassification> classification;

}