# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafSpecInfoResponseBody(DaraModel):
    def __init__(
        self,
        edition: str = None,
        request_id: str = None,
        spec_infos: List[main_models.DescribeDcdnWafSpecInfoResponseBodySpecInfos] = None,
    ):
        # The version of WAF.
        self.edition = edition
        # The ID of the request.
        self.request_id = request_id
        # The supported types of protection policies and the configuration information of protection rules.
        self.spec_infos = spec_infos

    def validate(self):
        if self.spec_infos:
            for v1 in self.spec_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SpecInfos'] = []
        if self.spec_infos is not None:
            for k1 in self.spec_infos:
                result['SpecInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.spec_infos = []
        if m.get('SpecInfos') is not None:
            for k1 in m.get('SpecInfos'):
                temp_model = main_models.DescribeDcdnWafSpecInfoResponseBodySpecInfos()
                self.spec_infos.append(temp_model.from_map(k1))

        return self

class DescribeDcdnWafSpecInfoResponseBodySpecInfos(DaraModel):
    def __init__(
        self,
        configs: List[main_models.DescribeDcdnWafSpecInfoResponseBodySpecInfosConfigs] = None,
        defense_scene: str = None,
    ):
        # The configuration information of the protection rule.
        self.configs = configs
        # The type of the protection policy. Valid values:
        # 
        # *   waf_group: basic web protection
        # *   custom_acl: custom
        # *   whitelist: whitelist
        # *   ip_blacklist: IP address blacklist
        # *   region_block: region blacklist
        # *   bot: bot management
        self.defense_scene = defense_scene

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

        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.DescribeDcdnWafSpecInfoResponseBodySpecInfosConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        return self

class DescribeDcdnWafSpecInfoResponseBodySpecInfosConfigs(DaraModel):
    def __init__(
        self,
        config: str = None,
        expr: str = None,
        value: str = None,
    ):
        # The configuration code of the protection rule.
        self.config = config
        # The configuration expression of the protection rule.
        self.expr = expr
        # The value of the configuration expression of the protection rule.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.expr is not None:
            result['Expr'] = self.expr

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Expr') is not None:
            self.expr = m.get('Expr')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

