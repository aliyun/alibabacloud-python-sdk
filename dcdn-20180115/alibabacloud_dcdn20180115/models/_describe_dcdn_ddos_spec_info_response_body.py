# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDdosSpecInfoResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth_limit: str = None,
        edition: str = None,
        enable: str = None,
        is_special_port: str = None,
        protected_area: str = None,
        qps_limit: str = None,
        request_id: str = None,
        spec_infos: List[main_models.DescribeDcdnDdosSpecInfoResponseBodySpecInfos] = None,
    ):
        # The bandwidth limit of a single instance.
        self.bandwidth_limit = bandwidth_limit
        # The version. Valid values:
        # 
        # * **poc**: POC Edition
        # * **basic**: Basic Edition
        # * **insurance**: Insurance Edition
        # * **unlimited**: Unlimited Edition
        # * **port_enhancement**: Special Port Enhanced Edition
        self.edition = edition
        # Specifies whether to enable DDoS mitigation. Valid values:
        # 
        # *   **on:**
        # *   **off**.
        self.enable = enable
        # Specifies whether custom ports are supported. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.is_special_port = is_special_port
        # Protected region. Valid values:
        # 
        # * **global**: global
        # * **chinese_mainland**: Chinese mainland
        # * **global_excluding_the_chinese_mainland**: outside the Chinese mainland
        self.protected_area = protected_area
        # The QPS limit.
        self.qps_limit = qps_limit
        # The ID of the request.
        self.request_id = request_id
        # The code and configurations of the security rules.
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
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.is_special_port is not None:
            result['IsSpecialPort'] = self.is_special_port

        if self.protected_area is not None:
            result['ProtectedArea'] = self.protected_area

        if self.qps_limit is not None:
            result['QpsLimit'] = self.qps_limit

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SpecInfos'] = []
        if self.spec_infos is not None:
            for k1 in self.spec_infos:
                result['SpecInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('IsSpecialPort') is not None:
            self.is_special_port = m.get('IsSpecialPort')

        if m.get('ProtectedArea') is not None:
            self.protected_area = m.get('ProtectedArea')

        if m.get('QpsLimit') is not None:
            self.qps_limit = m.get('QpsLimit')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.spec_infos = []
        if m.get('SpecInfos') is not None:
            for k1 in m.get('SpecInfos'):
                temp_model = main_models.DescribeDcdnDdosSpecInfoResponseBodySpecInfos()
                self.spec_infos.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDdosSpecInfoResponseBodySpecInfos(DaraModel):
    def __init__(
        self,
        configs: List[main_models.DescribeDcdnDdosSpecInfoResponseBodySpecInfosConfigs] = None,
        rule: str = None,
    ):
        # The configurations of the version rule.
        self.configs = configs
        # The version rule. Valid values:
        # 
        # *   **version_defense_num**: the rule for the number of version mitigation sessions
        # *   **domain_num**: the rule for the limit on the number of domain names
        # *   **defence_package_num**: the rule for extra mitigation session plans
        self.rule = rule

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

        if self.rule is not None:
            result['Rule'] = self.rule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.DescribeDcdnDdosSpecInfoResponseBodySpecInfosConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        return self

class DescribeDcdnDdosSpecInfoResponseBodySpecInfosConfigs(DaraModel):
    def __init__(
        self,
        config: str = None,
        expr: str = None,
        value: str = None,
    ):
        # The configuration code of the version rule. Valid values:
        # 
        # *   **total_defense_num**: the total number of mitigation sessions of the version.
        # *   **consume_defense_num**: the number of used mitigation sessions of the version.
        # *   **max_domain_num**: the limit on the number of added domain names.
        # *   **emain_domain_num**: the number of added domain names.
        # *   **defence_package_num**: the total number of purchased additional mitigation sessions.
        # *   **consume_defence_package_num**: the number of used additional mitigation sessions.
        self.config = config
        # The configuration expression of the version rule.
        self.expr = expr
        # The value of the configuration expression of the version rule.
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

