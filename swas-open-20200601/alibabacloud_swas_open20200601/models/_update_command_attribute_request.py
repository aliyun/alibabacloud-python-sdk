# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCommandAttributeRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        timeout: int = None,
        working_dir: str = None,
    ):
        # The command ID. You can call the [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) operation to query all available command IDs.
        # 
        # This parameter is required.
        self.command_id = command_id
        # The description of the command. The description supports all character sets and can be up to 512 characters in length.
        self.description = description
        # The name of the command. The name supports all character sets and can be up to 128 characters in length.
        self.name = name
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The maximum timeout period for the command execution on the ECS instance. Unit: seconds. When a command that you created cannot be run, the command execution times out. When the execution times out, the command process is forcefully terminated and the PID of the command is canceled. Default value: 60.
        self.timeout = timeout
        # The working directory of the command. The directory can be up to 200 characters in length.
        self.working_dir = working_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

