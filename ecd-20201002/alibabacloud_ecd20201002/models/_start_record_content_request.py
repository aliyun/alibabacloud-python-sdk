# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartRecordContentRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_version: str = None,
        desktop_id: str = None,
        file_path: str = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.client_os = client_os
        self.client_version = client_version
        # This parameter is required.
        self.desktop_id = desktop_id
        self.file_path = file_path
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.session_id = session_id

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

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

