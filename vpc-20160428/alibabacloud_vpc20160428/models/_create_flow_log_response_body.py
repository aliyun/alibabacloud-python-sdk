# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFlowLogResponseBody(DaraModel):
    def __init__(
        self,
        flow_log_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        success: str = None,
    ):
        # The ID of the flow log.
        self.flow_log_id = flow_log_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

