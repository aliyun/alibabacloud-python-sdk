# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWafRulesetRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        phase: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The name of the WAF ruleset.
        self.name = name
        # The WAF rule execution phase. Valid values:
        # 
        # - http_whitelist
        # 
        # - http_custom
        # 
        # - http_managed
        # 
        # - http_anti_scan
        # 
        # - http_ratelimit
        # 
        # - ip_access_rule
        # 
        # - http_bot
        # 
        # - http_security_level_rule
        # 
        # This parameter is required.
        self.phase = phase
        # The site ID. To get this ID, call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The site configuration version. This parameter applies only if versioning is enabled for the site. The default is 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

