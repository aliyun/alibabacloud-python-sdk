# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigHealthCheckRequest(DaraModel):
    def __init__(
        self,
        forward_protocol: str = None,
        frontend_port: int = None,
        health_check: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.forward_protocol = forward_protocol
        # This parameter is required.
        self.frontend_port = frontend_port
        # This parameter is required.
        self.health_check = health_check
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol

        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

