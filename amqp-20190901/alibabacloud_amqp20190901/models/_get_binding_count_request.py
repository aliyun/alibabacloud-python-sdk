# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBindingCountRequest(DaraModel):
    def __init__(
        self,
        binding_type: int = None,
        console_session_id: str = None,
        instance_id: str = None,
        resource_name: str = None,
        upstream: bool = None,
        vhost_name: str = None,
    ):
        # This parameter is required.
        self.binding_type = binding_type
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        # This parameter is required.
        self.resource_name = resource_name
        # This parameter is required.
        self.upstream = upstream
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.upstream is not None:
            result['Upstream'] = self.upstream

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Upstream') is not None:
            self.upstream = m.get('Upstream')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

