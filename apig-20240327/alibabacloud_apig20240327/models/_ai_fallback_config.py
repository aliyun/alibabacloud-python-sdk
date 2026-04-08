# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AiFallbackConfig(DaraModel):
    def __init__(
        self,
        only_redirect_upstream_code: bool = None,
        service_configs: List[main_models.AiFallbackConfigServiceConfigs] = None,
    ):
        self.only_redirect_upstream_code = only_redirect_upstream_code
        self.service_configs = service_configs

    def validate(self):
        if self.service_configs:
            for v1 in self.service_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.only_redirect_upstream_code is not None:
            result['onlyRedirectUpstreamCode'] = self.only_redirect_upstream_code

        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onlyRedirectUpstreamCode') is not None:
            self.only_redirect_upstream_code = m.get('onlyRedirectUpstreamCode')

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.AiFallbackConfigServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        return self

class AiFallbackConfigServiceConfigs(DaraModel):
    def __init__(
        self,
        name: str = None,
        pass_through_model_name: bool = None,
        service_id: str = None,
        target_model_name: str = None,
    ):
        self.name = name
        self.pass_through_model_name = pass_through_model_name
        self.service_id = service_id
        self.target_model_name = target_model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.pass_through_model_name is not None:
            result['passThroughModelName'] = self.pass_through_model_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.target_model_name is not None:
            result['targetModelName'] = self.target_model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('passThroughModelName') is not None:
            self.pass_through_model_name = m.get('passThroughModelName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('targetModelName') is not None:
            self.target_model_name = m.get('targetModelName')

        return self

