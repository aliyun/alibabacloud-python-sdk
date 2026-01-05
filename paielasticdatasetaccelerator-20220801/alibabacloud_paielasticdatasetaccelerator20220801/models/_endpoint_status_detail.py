# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from darabonba.model import DaraModel

class EndpointStatusDetail(DaraModel):
    def __init__(
        self,
        ip_port_mapping: Dict[str, main_models.IpPort] = None,
    ):
        self.ip_port_mapping = ip_port_mapping

    def validate(self):
        if self.ip_port_mapping:
            for v1 in self.ip_port_mapping.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpPortMapping'] = {}
        if self.ip_port_mapping is not None:
            for k1, v1 in self.ip_port_mapping.items():
                result['IpPortMapping'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_port_mapping = {}
        if m.get('IpPortMapping') is not None:
            for k1, v1 in m.get('IpPortMapping').items():
                temp_model = main_models.IpPort()
                self.ip_port_mapping[k1] = temp_model.from_map(v1)

        return self

