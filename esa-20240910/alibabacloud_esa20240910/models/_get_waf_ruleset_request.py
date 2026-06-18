# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWafRulesetRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        phase: str = None,
        site_id: int = None,
    ):
        # The ID of the WAF ruleset. You can obtain this ID by calling the [ListWafRulesets](https://help.aliyun.com/document_detail/2878359.html) operation.
        self.id = id
        # The execution phase of the WAF ruleset. Valid values:
        # 
        # - `http_whitelist`: A whitelist rule
        # 
        # - `http_custom`: A custom rule
        # 
        # - `http_managed`: A managed rule
        # 
        # - `http_anti_scan`: A scan protection rule
        # 
        # - `http_ratelimit`: A rate limit rule
        # 
        # - `ip_access_rule`: An IP access rule
        # 
        # - `http_bot`: A bot rule
        # 
        # - `http_security_level_rule`: A security rule
        self.phase = phase
        # The site ID. You can obtain this ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

