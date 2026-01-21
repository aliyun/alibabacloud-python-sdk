# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyInstanceLDAPAuthServerRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        filter: str = None,
        instance_id: str = None,
        is_ssl: str = None,
        password: str = None,
        port: str = None,
        region_id: str = None,
        server: str = None,
        standby_server: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.base_dn = base_dn
        self.filter = filter
        # This parameter is required.
        self.instance_id = instance_id
        self.is_ssl = is_ssl
        self.password = password
        # This parameter is required.
        self.port = port
        self.region_id = region_id
        # This parameter is required.
        self.server = server
        self.standby_server = standby_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.server is not None:
            result['Server'] = self.server

        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Server') is not None:
            self.server = m.get('Server')

        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')

        return self

