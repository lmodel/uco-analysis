package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  "An analytic result is a characterization of the understanding resulting from an analysis action."
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AnalyticResult extends Assertion {

  private Analysis originatingAnalysis;
  private List<UcoObject> resultContent;

}