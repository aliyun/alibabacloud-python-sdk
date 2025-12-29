# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ForeignInstance(DaraModel):
    def __init__(
        self,
        data_link_name: str = None,
        host: str = None,
        instance_source: str = None,
        instance_type: str = None,
        port: int = None,
        properties: Dict[str, str] = None,
        region_id: str = None,
        sid: str = None,
    ):
        self.data_link_name = data_link_name
        self.host = host
        self.instance_source = instance_source
        self.instance_type = instance_type
        self.port = port
        self.properties = properties
        self.region_id = region_id
        self.sid = sid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.port is not None:
            result['Port'] = self.port

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sid is not None:
            result['Sid'] = self.sid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        return self

