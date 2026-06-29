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
        # The configuration ID.
        self.config_id = config_id
        # The configuration type. You can use this parameter to query global or rule configurations. Valid values:
        # - global: queries global configurations.
        # - rule: queries rule configurations.
        # 
        # This parameter is optional. If you do not specify this parameter, both global and rule configurations are returned.
        self.config_type = config_type
        # The page number for a paged query. The value must be greater than or equal to 1.
        self.page_number = page_number
        # The number of entries per page for a paged query. Valid values: 1 to 500.
        self.page_size = page_size
        # The rule name. You can use this parameter to query the rule that matches the specified name.
        self.rule_name = rule_name
        # The site ID, which can be obtained by calling the [ListSites](~~ListSites~~) operation.
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

