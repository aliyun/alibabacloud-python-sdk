# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartTerminalSessionRequest(DaraModel):
    def __init__(
        self,
        command_line: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The command to run after the session is started. The command can be up to 512 characters in length.
        self.command_line = command_line
        # The ID of the Simple Application Server instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the Simple Application Server instance. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent list of Alibaba Cloud regions.
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
        if self.command_line is not None:
            result['CommandLine'] = self.command_line

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

