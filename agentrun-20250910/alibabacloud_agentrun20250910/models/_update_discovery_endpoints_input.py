# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateDiscoveryEndpointsInput(DaraModel):
    def __init__(
        self,
        discovery_endpoints: List[main_models.DiscoveryEndpoint] = None,
    ):
        self.discovery_endpoints = discovery_endpoints

    def validate(self):
        if self.discovery_endpoints:
            for v1 in self.discovery_endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['discoveryEndpoints'] = []
        if self.discovery_endpoints is not None:
            for k1 in self.discovery_endpoints:
                result['discoveryEndpoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovery_endpoints = []
        if m.get('discoveryEndpoints') is not None:
            for k1 in m.get('discoveryEndpoints'):
                temp_model = main_models.DiscoveryEndpoint()
                self.discovery_endpoints.append(temp_model.from_map(k1))

        return self

