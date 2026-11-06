# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSourceTemplatesShrinkRequest(DaraModel):
    def __init__(
        self,
        data_source_template_ids_shrink: str = None,
        lang: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_template_ids_shrink = data_source_template_ids_shrink
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_template_ids_shrink is not None:
            result['DataSourceTemplateIds'] = self.data_source_template_ids_shrink

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceTemplateIds') is not None:
            self.data_source_template_ids_shrink = m.get('DataSourceTemplateIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

