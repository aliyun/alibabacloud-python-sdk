# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWafRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        config_shrink: str = None,
        id: int = None,
        position: int = None,
        site_id: int = None,
        site_version: int = None,
        status: str = None,
    ):
        # The configuration of the rule.
        self.config_shrink = config_shrink
        # The ID of the WAF rule. To obtain the rule ID, call the [ListWafRules](https://help.aliyun.com/document_detail/2878257.html) operation.
        # 
        # This parameter is required.
        self.id = id
        # The position of the rule within the rule set.
        self.position = position
        # The ID of the site. To obtain the site ID, call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site configuration. For sites with configuration version management enabled, use this parameter to specify the effective configuration version. The default is version 0.
        self.site_version = site_version
        # The status of the rule.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink

        if self.id is not None:
            result['Id'] = self.id

        if self.position is not None:
            result['Position'] = self.position

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

