# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCommandRequest(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        command_id: str = None,
        description: str = None,
        launcher: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        timeout: int = None,
        working_dir: str = None,
    ):
        # >  This parameter is no longer used and does not take effect.
        self.command_content = command_content
        # The command ID. You can call the [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) operation to query all available command IDs.
        # 
        # This parameter is required.
        self.command_id = command_id
        # The command description. The description supports all character sets and can be up to 512 characters in length.
        self.description = description
        # The launcher for script execution. The value cannot exceed 1 KB in length.
        self.launcher = launcher
        # The command name. The name supports all character sets and can be up to 128 characters in length.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the command. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum timeout period for the command to be run on the instance. Unit: seconds. When a command cannot run within the specified time range, the command times out. Then, the command process is forcibly terminated by canceling the process ID (PID) of the command.
        self.timeout = timeout
        # The working directory of the command. The value can be up to 200 characters in length.
        self.working_dir = working_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.description is not None:
            result['Description'] = self.description

        if self.launcher is not None:
            result['Launcher'] = self.launcher

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

