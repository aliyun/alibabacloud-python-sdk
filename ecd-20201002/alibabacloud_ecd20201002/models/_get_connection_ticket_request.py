# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20201002 import models as main_models
from darabonba.model import DaraModel

class GetConnectionTicketRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        client_id: str = None,
        client_os: str = None,
        client_type: str = None,
        client_version: str = None,
        command_content: str = None,
        desktop_id: str = None,
        login_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        session_id: str = None,
        tag: List[main_models.GetConnectionTicketRequestTag] = None,
        task_id: str = None,
        ticket_black_list: List[str] = None,
        uuid: str = None,
    ):
        self.access_type = access_type
        # This parameter is required.
        self.client_id = client_id
        self.client_os = client_os
        # The type of the client.
        # 
        # Valid values:
        # 
        # *   html5: web client
        # *   Linux: self-developed hardware terminal
        # *   android: Android client
        # *   windows: Windows client
        # *   ios: iOS client
        # *   macos: macOS client
        self.client_type = client_type
        self.client_version = client_version
        self.command_content = command_content
        # The cloud compute ID.
        self.desktop_id = desktop_id
        # This parameter is required.
        self.login_token = login_token
        self.owner_id = owner_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.session_id = session_id
        # The tags. You can specify 1 to 20 tags.
        self.tag = tag
        # The ID of the cloud computer connection task.\\
        # The first time you call the GetConnectionTicket operation, you do not need to configure this parameter. When you call the GetConnectionTicket operation later, set this parameter to the value of the `TaskId` parameter returned from the previous invocation.
        self.task_id = task_id
        self.ticket_black_list = ticket_black_list
        self.uuid = uuid

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_os is not None:
            result['ClientOS'] = self.client_os

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.ticket_black_list is not None:
            result['TicketBlackList'] = self.ticket_black_list

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.GetConnectionTicketRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TicketBlackList') is not None:
            self.ticket_black_list = m.get('TicketBlackList')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class GetConnectionTicketRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. If you specify the `Tag` parameter, you must also specify the `Key` parameter. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun` and contain only spaces.
        self.key = key
        # The tag value. You can specify an empty string as a tag value. A tag value can be up to 128 characters in length and cannot start with `acs:`. It cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

