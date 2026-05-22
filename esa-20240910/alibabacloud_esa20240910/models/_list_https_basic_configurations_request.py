# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHttpsBasicConfigurationsRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_name: str = None,
        site_id: int = None,
    ):
        # Configuration ID.
        self.config_id = config_id
        # Configuration type, which can be used to query global or rule configurations. Value range:
        # - global: Query global configuration.
        # - rule: Query rule configuration.
        # 
        # This parameter is optional. If not provided, it does not distinguish between global and rule configurations.
        self.config_type = config_type
        # Page number, default is 1 if not provided.
        self.page_number = page_number
        # Number of items per page, maximum is 500, default is 500 if not provided.
        self.page_size = page_size
        # Rule name, which can be used to find the rule with the specified name.
        self.rule_name = rule_name
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) interface.
        # 
        # This parameter is required.
        self.site_id = site_id

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

        return self

