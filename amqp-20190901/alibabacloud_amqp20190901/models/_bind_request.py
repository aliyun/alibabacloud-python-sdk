# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindRequest(DaraModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: int = None,
        console_session_id: str = None,
        dst_name: str = None,
        instance_id: str = None,
        src_name: str = None,
        vhost_name: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        # This parameter is required.
        self.binding_type = binding_type
        self.console_session_id = console_session_id
        # This parameter is required.
        self.dst_name = dst_name
        self.instance_id = instance_id
        # This parameter is required.
        self.src_name = src_name
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.argument is not None:
            result['Argument'] = self.argument

        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key

        if self.binding_type is not None:
            result['BindingType'] = self.binding_type

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.dst_name is not None:
            result['DstName'] = self.dst_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.src_name is not None:
            result['SrcName'] = self.src_name

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')

        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')

        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('DstName') is not None:
            self.dst_name = m.get('DstName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SrcName') is not None:
            self.src_name = m.get('SrcName')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

