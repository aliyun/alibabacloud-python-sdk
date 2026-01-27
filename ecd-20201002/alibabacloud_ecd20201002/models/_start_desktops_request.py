# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartDesktopsRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_token: str = None,
        client_version: str = None,
        desktop_id: List[str] = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
        uuid: str = None,
    ):
        # The ID of the Alibaba Cloud Workspace client (hereinafter referred to as WUYING client). The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The operating system (OS) of the device that run the client.
        self.client_os = client_os
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The client version. If you use a WUYING client, you can click **About** on the client logon page to view the version of the client.
        self.client_version = client_version
        # The IDs of the cloud computers. You can specify the IDs of 1 to 20 cloud computers.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id
        # The UUID of the client.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_os is not None:
            result['ClientOS'] = self.client_os

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

