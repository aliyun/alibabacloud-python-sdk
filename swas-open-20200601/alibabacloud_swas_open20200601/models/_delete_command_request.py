# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCommandRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        region_id: str = None,
    ):
        # The command ID. You can call the [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) operation to query all available command IDs.
        # 
        # This parameter is required.
        self.command_id = command_id
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the available regions for Simple Application Server.
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
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

