# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectionTicketRequest(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        desktop_id: str = None,
        end_user_id: str = None,
        owner_id: int = None,
        password: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
        uuid: str = None,
    ):
        # The command that you want to run to configure a custom application in user mode. After you obtain the credential, the application is automatically started. Parameter description in the command:
        # 
        # *   appPath: the path of the application startup file. Example: `"C:\\\\Program Files (x86)\\\\000\\\\000.exe"`. Use double slashes (\\\\\\) as the delimiter. Type of the parameter value: string.
        # *   appParameter: the startup arguments of the application. Example: `"meetingid 000 meetingname aaa"`. Separate multiple arguments with spaces. Type of the parameter value: string.
        self.command_content = command_content
        # The ID of the cloud computer for which you want to generate a connection credential. This parameter is required.
        self.desktop_id = desktop_id
        # The ID of the end user of the cloud computer. The end user must be the current end user of the cloud computer.
        self.end_user_id = end_user_id
        self.owner_id = owner_id
        # The password of the current end user of the cloud computer.
        self.password = password
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the cloud computer connection task.
        self.task_id = task_id
        # The unique identifier of the client. If you use an Alibaba Cloud Workspace client, click **About** on the client logon page to view the identifier of the client.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

