# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApproveFotaUpdateRequest(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        client_id: str = None,
        desktop_id: str = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
        target_status: str = None,
        uuid: str = None,
    ):
        # The application version.
        # 
        # This parameter is required.
        self.app_version = app_version
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id
        # The state of the cloud computer after the OTA update.
        # 
        # >  This parameter is not publicly available. After the OTA update is complete, the state of the cloud computer changes to `RUNNING`.
        # 
        # *   Set the value to running.
        self.target_status = target_status
        # The unique identifier of the client. To view the unique identifier of an Alibaba Cloud Workspace client, go to the client logon page and click on "About."
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.target_status is not None:
            result['TargetStatus'] = self.target_status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TargetStatus') is not None:
            self.target_status = m.get('TargetStatus')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

