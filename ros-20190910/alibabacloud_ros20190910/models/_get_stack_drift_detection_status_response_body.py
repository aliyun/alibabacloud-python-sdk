# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackDriftDetectionStatusResponseBody(DaraModel):
    def __init__(
        self,
        drift_detection_id: str = None,
        drift_detection_status: str = None,
        drift_detection_status_reason: str = None,
        drift_detection_time: str = None,
        drifted_stack_resource_count: int = None,
        request_id: str = None,
        stack_drift_status: str = None,
        stack_id: str = None,
    ):
        # The ID of the drift detection operation.
        self.drift_detection_id = drift_detection_id
        # The drift detection status. Valid values:
        # 
        # *   DETECTION_COMPLETE: The drift detection operation has been completed for all resources that support drift detection in the stack.
        # *   DETECTION_FAILED: The stack drift detection operation has failed for at least one resource in the stack.
        # *   DETECTION_IN_PROGRESS: The stack drift detection operation is in progress.
        self.drift_detection_status = drift_detection_status
        # The reason why the stack drift detection operation has its current status.
        self.drift_detection_status_reason = drift_detection_status_reason
        # The time when the stack drift detection operation was initiated.
        self.drift_detection_time = drift_detection_time
        # The total number of stack resources that have drifted.
        self.drifted_stack_resource_count = drifted_stack_resource_count
        # The ID of the request.
        self.request_id = request_id
        # The drift status of the stack. Valid values:
        # 
        # *   DRIFTED: The actual configuration of the stack differs, or has drifted, from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.
        # *   NOT_CHECKED: Resource Orchestration Service (ROS) has not checked whether the actual configuration of the resource differs from its expected template configuration.
        # *   IN_SYNC: The current configuration of each supported resource matches its expected template configuration. A stack with no resources that support drift detection also has a status of IN_SYNC.
        self.stack_drift_status = stack_drift_status
        # The ID of the stack.
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id

        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status

        if self.drift_detection_status_reason is not None:
            result['DriftDetectionStatusReason'] = self.drift_detection_status_reason

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.drifted_stack_resource_count is not None:
            result['DriftedStackResourceCount'] = self.drifted_stack_resource_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')

        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')

        if m.get('DriftDetectionStatusReason') is not None:
            self.drift_detection_status_reason = m.get('DriftDetectionStatusReason')

        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')

        if m.get('DriftedStackResourceCount') is not None:
            self.drifted_stack_resource_count = m.get('DriftedStackResourceCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

