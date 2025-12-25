# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiInfoByName(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
        type: str = None,
        version_enabled: bool = None,
        versioned_http_apis: List[main_models.HttpApiApiInfo] = None,
    ):
        self.gateway_id = gateway_id
        self.name = name
        self.type = type
        self.version_enabled = version_enabled
        self.versioned_http_apis = versioned_http_apis

    def validate(self):
        if self.versioned_http_apis:
            for v1 in self.versioned_http_apis:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.version_enabled is not None:
            result['versionEnabled'] = self.version_enabled

        result['versionedHttpApis'] = []
        if self.versioned_http_apis is not None:
            for k1 in self.versioned_http_apis:
                result['versionedHttpApis'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('versionEnabled') is not None:
            self.version_enabled = m.get('versionEnabled')

        self.versioned_http_apis = []
        if m.get('versionedHttpApis') is not None:
            for k1 in m.get('versionedHttpApis'):
                temp_model = main_models.HttpApiApiInfo()
                self.versioned_http_apis.append(temp_model.from_map(k1))

        return self

