# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListProvisionedProductsRequest(DaraModel):
    def __init__(
        self,
        access_level_filter: str = None,
        filters: List[main_models.ListProvisionedProductsRequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # The access filter. Valid values:
        # 
        # *   User: queries the product instances that are created by the current requester. This is the default value.
        # *   Account: queries the product instances that belong to the current Alibaba Cloud account.
        self.access_level_filter = access_level_filter
        # The filter conditions.
        self.filters = filters
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The field that is used to sort the queried data.
        # 
        # Set the value to CreateTime, which specifies the time when the product instance was created.
        self.sort_by = sort_by
        # The sorting method. Valid values:
        # 
        # *   Asc: the ascending order.
        # *   Desc (default): the descending order.
        self.sort_order = sort_order

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_level_filter is not None:
            result['AccessLevelFilter'] = self.access_level_filter

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

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
        if m.get('AccessLevelFilter') is not None:
            self.access_level_filter = m.get('AccessLevelFilter')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ListProvisionedProductsRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

class ListProvisionedProductsRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the filter condition. Valid values:
        # 
        # *   ProvisionedProductName: performs exact matches by product instance name. Product instance names are not case-sensitive.
        # *   FullTextSearch: performs full-text searches by product instance name. Fuzzy match is supported.
        self.key = key
        # The value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

