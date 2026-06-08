# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CancelStackOperationRequest(DaraModel):
    def __init__(
        self,
        allowed_stack_operations: List[str] = None,
        cancel_type: str = None,
        region_id: str = None,
        stack_id: str = None,
    ):
        # The operations that you want to cancel on the stack.
        self.allowed_stack_operations = allowed_stack_operations
        # The method that you want to use to cancel the operations. Valid values:
        # 
        # *   Quick: cancels the operations on the stack at the earliest opportunity. In this case, Resource Orchestration Service (ROS) stops scheduling new resources and stops running resources at the earliest opportunity. If you use this method, the resource status may become invalid and subsequent stack operations may be affected.
        # *   Safe (default): cancels the operations on the stack in a secure manner. In this case, ROS stops scheduling new resources and waits for running resources to be stopped.
        self.cancel_type = cancel_type
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The stack ID.
        # 
        # This parameter is required.
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_stack_operations is not None:
            result['AllowedStackOperations'] = self.allowed_stack_operations

        if self.cancel_type is not None:
            result['CancelType'] = self.cancel_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedStackOperations') is not None:
            self.allowed_stack_operations = m.get('AllowedStackOperations')

        if m.get('CancelType') is not None:
            self.cancel_type = m.get('CancelType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

