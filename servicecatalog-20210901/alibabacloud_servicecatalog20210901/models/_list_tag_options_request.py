# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListTagOptionsRequest(DaraModel):
    def __init__(
        self,
        filters: main_models.ListTagOptionsRequestFilters = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # The filter condition.
        self.filters = filters
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size
        # The information based on which you want to sort the query results.
        # 
        # Set the value to CreateTime, which specifies the creation time of tag options.
        self.sort_by = sort_by
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   Asc: the ascending order
        # *   Desc (default): the descending order
        self.sort_order = sort_order

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filters is not None:
            result['Filters'] = self.filters.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filters') is not None:
            temp_model = main_models.ListTagOptionsRequestFilters()
            self.filters = temp_model.from_map(m.get('Filters'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

class ListTagOptionsRequestFilters(DaraModel):
    def __init__(
        self,
        active: bool = None,
        full_text_search: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether to enable the tag option. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active
        # The full-text search method.
        self.full_text_search = full_text_search
        # The key of the tag option.
        self.key = key
        # The value of the tag option.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.full_text_search is not None:
            result['FullTextSearch'] = self.full_text_search

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('FullTextSearch') is not None:
            self.full_text_search = m.get('FullTextSearch')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

