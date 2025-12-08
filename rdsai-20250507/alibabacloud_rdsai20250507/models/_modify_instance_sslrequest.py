# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceSSLRequest(DaraModel):
    def __init__(
        self,
        catype: str = None,
        instance_name: str = None,
        region_id: str = None,
        sslenabled: int = None,
        server_cert: str = None,
        server_key: str = None,
    ):
        self.catype = catype
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id
        # This parameter is required.
        self.sslenabled = sslenabled
        self.server_cert = server_cert
        self.server_key = server_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catype is not None:
            result['CAType'] = self.catype

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        if self.server_cert is not None:
            result['ServerCert'] = self.server_cert

        if self.server_key is not None:
            result['ServerKey'] = self.server_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CAType') is not None:
            self.catype = m.get('CAType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('ServerCert') is not None:
            self.server_cert = m.get('ServerCert')

        if m.get('ServerKey') is not None:
            self.server_key = m.get('ServerKey')

        return self

