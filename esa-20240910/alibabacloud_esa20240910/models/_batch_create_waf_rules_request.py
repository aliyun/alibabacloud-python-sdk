# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class BatchCreateWafRulesRequest(DaraModel):
    def __init__(
        self,
        configs: List[main_models.WafRuleConfig] = None,
        phase: str = None,
        ruleset_id: int = None,
        shared: main_models.WafBatchRuleShared = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # A list of configurations for each rule, specifying detailed configurations for each rule.
        self.configs = configs
        # WAF rule type, with values:
        # 
        # - **http_anti_scan**: Scan protection.
        # - **http_bot**: Bots.
        self.phase = phase
        # Ruleset ID.
        self.ruleset_id = ruleset_id
        # Shared configuration for multiple rules, specifying common attributes of multiple rules.
        self.shared = shared
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) interface.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Site version.
        self.site_version = site_version

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()
        if self.shared:
            self.shared.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id

        if self.shared is not None:
            result['Shared'] = self.shared.to_map()

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.WafRuleConfig()
                self.configs.append(temp_model.from_map(k1))

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')

        if m.get('Shared') is not None:
            temp_model = main_models.WafBatchRuleShared()
            self.shared = temp_model.from_map(m.get('Shared'))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

