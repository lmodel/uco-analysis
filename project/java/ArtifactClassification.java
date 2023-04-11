package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  "An artifact classification is a single specific assertion that a particular class of a classification taxonomy applies to something."
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArtifactClassification extends UcoInherentCharacterizationThing {

  private BigDecimal classificationConfidence;
  private String class;

}