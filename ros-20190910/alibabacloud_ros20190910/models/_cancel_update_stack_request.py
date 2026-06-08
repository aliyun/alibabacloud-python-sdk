# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelUpdateStackRequest(DaraModel):
    def __init__(
        self,
        cancel_type: str = None,
        region_id: str = None,
        stack_id: str = None,
    ):
        # The method to cancel the update operation. Valid values:
        # 
        # *   Quick: cancels the update of a stack as soon as possible.
        # *   Safe: cancels the update of a stack as safely as possible.
        self.cancel_type = cancel_type
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the stack.
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
        if self.cancel_type is not None:
            result['CancelType'] = self.cancel_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelType') is not None:
            self.cancel_type = m.get('CancelType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

