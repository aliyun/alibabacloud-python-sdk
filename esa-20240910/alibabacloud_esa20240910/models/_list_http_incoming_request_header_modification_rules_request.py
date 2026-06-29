# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHttpIncomingRequestHeaderModificationRulesRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_name: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The configuration ID. You can call the ListHttpIncomingRequestHeaderModificationRules operation to obtain the configuration ID.
        self.config_id = config_id
        # The configuration type. You can use this parameter to query global or rule configurations. Valid values:
        # 
        # - global: queries global configurations.
        # - rule: queries rule configurations.
        self.config_type = config_type
        # The page number for a paged query. The value must be greater than or equal to 1.
        self.page_number = page_number
        # The number of entries per page for a paged query. Valid values: 1 to 500.
        self.page_size = page_size
        # The rule name.
        self.rule_name = rule_name
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site configuration. For sites with version management enabled, you can use this parameter to specify the site version for which the configuration takes effect. The default value is version 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

