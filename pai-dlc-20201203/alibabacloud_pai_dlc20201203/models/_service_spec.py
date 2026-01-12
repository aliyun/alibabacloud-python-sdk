# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ServiceSpec(DaraModel):
    def __init__(
        self,
        default_port: int = None,
        extra_ports: List[int] = None,
        service_mode: str = None,
    ):
        self.default_port = default_port
        self.extra_ports = extra_ports
        self.service_mode = service_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_port is not None:
            result['DefaultPort'] = self.default_port

        if self.extra_ports is not None:
            result['ExtraPorts'] = self.extra_ports

        if self.service_mode is not None:
            result['ServiceMode'] = self.service_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultPort') is not None:
            self.default_port = m.get('DefaultPort')

        if m.get('ExtraPorts') is not None:
            self.extra_ports = m.get('ExtraPorts')

        if m.get('ServiceMode') is not None:
            self.service_mode = m.get('ServiceMode')

        return self

