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
        # The ID of the WAF ruleset. You can call the [ListWafRulesets](https://help.aliyun.com/document_detail/2878359.html) operation to obtain the ID.
        self.id = id
        # The WAF rule execution phase. Valid values:
        # - http_whitelist: whitelist rules
        # - http_custom: custom rules
        # - http_managed: managed rules
        # - http_anti_scan: scan protection rules
        # - http_ratelimit: rate limiting rules
        # - ip_access_rule: IP access rules
        # - http_bot: advanced mode bots
        # - http_security_level_rule: security rules
        self.phase = phase
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
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

