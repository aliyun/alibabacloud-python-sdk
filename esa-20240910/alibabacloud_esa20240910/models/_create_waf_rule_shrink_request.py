# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWafRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        config_shrink: str = None,
        phase: str = None,
        ruleset_id: int = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The detailed configuration of the WAF rule.
        self.config_shrink = config_shrink
        # The phase in which the WAF rule runs.
        # 
        # - `http_whitelist`: whitelist rule
        # 
        # - `http_custom`: custom rule
        # 
        # - `http_managed`: managed rule
        # 
        # - `http_anti_scan`: anti-scan rule
        # 
        # - `http_ratelimit`: rate limit rule
        # 
        # - `ip_access_rule`: IP access rule
        # 
        # - `http_bot`: Advanced Mode Bots
        # 
        # - `http_security_level_rule`: Security Rule
        # 
        # This parameter is required.
        self.phase = phase
        # The ID of the WAF ruleset. You can obtain this ID by calling the [ListWafRulesets](https://help.aliyun.com/document_detail/2878359.html) operation.
        self.ruleset_id = ruleset_id
        # The ID of the site. You can obtain this ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # If version management is enabled for the site, use this parameter to specify the version to which the configuration applies. The default is 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

