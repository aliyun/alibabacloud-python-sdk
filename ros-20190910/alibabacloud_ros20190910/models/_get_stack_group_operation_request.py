# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackGroupOperationRequest(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
        region_id: str = None,
    ):
        # The operation ID. You can call the [ListStackGroupOperations](https://help.aliyun.com/document_detail/151342.html) operation to query the operation ID.
        # 
        # This parameter is required.
        self.operation_id = operation_id
        # The region ID of the stack group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

