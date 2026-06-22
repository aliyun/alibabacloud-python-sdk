# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class Operation(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        create_time: int = None,
        description: str = None,
        end_time: int = None,
        operation_id: str = None,
        operation_state: str = None,
        operation_type: str = None,
        start_time: int = None,
        state_change_reason: main_models.OperationStateChangeReason = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The time when the operation was created. This value is a UNIX timestamp, measured in milliseconds.
        self.create_time = create_time
        # The description of the operation.
        self.description = description
        # The time when the operation ended. This value is a UNIX timestamp, measured in milliseconds.
        self.end_time = end_time
        # The operation ID.
        self.operation_id = operation_id
        # The operation state. Valid values:
        # 
        # - `IN_PROGRESS`: The operation is in progress.
        # 
        # - `COMPLETED`: The operation completed.
        # 
        # - `HUMAN_PROCESSING`: The operation requires manual intervention.
        # 
        # - `FAILED`: The operation failed.
        self.operation_state = operation_state
        # The operation type.
        self.operation_type = operation_type
        # The time when the operation started. This value is a UNIX timestamp, measured in milliseconds.
        self.start_time = start_time
        # The reason for the state change.
        self.state_change_reason = state_change_reason

    def validate(self):
        if self.state_change_reason:
            self.state_change_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.operation_state is not None:
            result['OperationState'] = self.operation_state

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('OperationState') is not None:
            self.operation_state = m.get('OperationState')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StateChangeReason') is not None:
            temp_model = main_models.OperationStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('StateChangeReason'))

        return self

