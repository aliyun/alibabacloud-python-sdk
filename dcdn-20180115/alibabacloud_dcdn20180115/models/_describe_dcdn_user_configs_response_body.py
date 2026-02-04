# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnUserConfigsResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.DescribeDcdnUserConfigsResponseBodyConfigs] = None,
        request_id: str = None,
    ):
        # The user configurations.
        self.configs = configs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.DescribeDcdnUserConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnUserConfigsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
        function_name: str = None,
    ):
        # The name of the configuration.
        # 
        # The configuration is specified by enterprise users and public service sectors.
        self.arg_name = arg_name
        # The value of the configuration. Valid values:
        # 
        # *   cc_rule: HTTP flood protection
        # *   ddos_dispatch: DDoS mitigation
        # *   edge_safe: application security on points of presence (POPs)
        # *   blocked_regions: region blacklist
        # *   http_acl_policy: precise access control
        # *   bot_manager: bot traffic management
        # *   ip_reputation: IP reputation library
        self.arg_value = arg_value
        # The name of the feature.
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name

        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')

        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        return self

