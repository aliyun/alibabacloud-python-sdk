# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyParentPlatformRequest(DaraModel):
    def __init__(
        self,
        auto_start: bool = None,
        client_auth: bool = None,
        client_password: str = None,
        client_username: str = None,
        description: str = None,
        gb_id: str = None,
        id: str = None,
        ip: str = None,
        name: str = None,
        owner_id: int = None,
        port: int = None,
    ):
        self.auto_start = auto_start
        self.client_auth = client_auth
        self.client_password = client_password
        self.client_username = client_username
        self.description = description
        self.gb_id = gb_id
        # This parameter is required.
        self.id = id
        self.ip = ip
        self.name = name
        self.owner_id = owner_id
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start

        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth

        if self.client_password is not None:
            result['ClientPassword'] = self.client_password

        if self.client_username is not None:
            result['ClientUsername'] = self.client_username

        if self.description is not None:
            result['Description'] = self.description

        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.id is not None:
            result['Id'] = self.id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')

        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')

        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')

        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

