# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CollectorKibanaInstance(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        host: str = None,
        instance_id: str = None,
        kibana_host: str = None,
        password: str = None,
        protocol: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.config_type = config_type
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.kibana_host = kibana_host
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.protocol = protocol
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.host is not None:
            result['host'] = self.host

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.kibana_host is not None:
            result['kibanaHost'] = self.kibana_host

        if self.password is not None:
            result['password'] = self.password

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('kibanaHost') is not None:
            self.kibana_host = m.get('kibanaHost')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

