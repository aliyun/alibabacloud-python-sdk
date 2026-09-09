# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvokeDiagnosisRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        params: str = None,
        service_name: str = None,
    ):
        # The diagnostic channel. Currently fixed to the ECS channel.
        # 
        # This parameter is required.
        self.channel = channel
        # The diagnostic parameters. Different diagnostic types require different parameters. For the parameters required by each diagnostic type, see the supplementary description of request parameters below.
        # 
        # >Notice: Pass a JSON-formatted string.
        # 
        # This parameter is required.
        self.params = params
        # The diagnostic type. Specifies the type of diagnostic to perform.
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.params is not None:
            result['params'] = self.params

        if self.service_name is not None:
            result['service_name'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')

        return self

