from dataclasses import dataclass
from typing import Optional

from argo_workflows.models import IoArgoprojWorkflowV1alpha1PodGC
from argo_workflows.models import LabelSelector

@dataclass
class PodGC:
    """Specification of podGC strategy for workflows.

    https://argoproj.github.io/argo-workflows/fields/#podgc

    Delete completed workflows.

    Attributes
    ----------
    label_selector: LabelSelector
        Check if the pods match the labels before being added to the pod GC queue.
    strategy: string
        One of "OnPodCompletion", "OnPodSuccess", "OnWorkflowCompletion", "OnWorkflowSuccess".

    """

    label_selector: Optional[LabelSelector]
    strategy: str

    def build(self) -> IoArgoprojWorkflowV1alpha1PodGC:
        """Constructs and returns the pod_gc strategy."""

        return IoArgoprojWorkflowV1alpha1PodGC(
            label_selector=self.label_selector,
            strategy=self.strategy
        )
