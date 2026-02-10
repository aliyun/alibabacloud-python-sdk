# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetAssetsPropertyDetailRequest(DaraModel):
    def __init__(
        self,
        biz: str = None,
        current_page: int = None,
        item_name: str = None,
        lang: str = None,
        next_token: str = None,
        page_size: int = None,
        remark: str = None,
        search_criteria_list: List[main_models.GetAssetsPropertyDetailRequestSearchCriteriaList] = None,
        use_next_token: bool = None,
        uuid: str = None,
    ):
        # The type of asset fingerprint to be queried, with a default value of **sca**. Values:
        # 
        # - **lkm**: Kernel module
        # - **autorun**: Startup item
        # - **web_server**: Web site
        # 
        # This parameter is required.
        self.biz = biz
        # Set the page number from which to start displaying the query results. The default value is **1**, indicating that the display starts from the first page.
        self.current_page = current_page
        # The aggregated item name of the asset fingerprint to be queried.
        # > Call the [GetAssetsPropertyItem](~~GetAssetsPropertyItem~~) API to obtain this parameter.
        self.item_name = item_name
        # The language type for the request and response. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Used to mark the current read position. Leave it empty to start from the beginning.
        # > Do not fill in for the first call; the response will include the NextToken for the second call. Each subsequent call\\"s response will contain the NextToken for the next call.
        self.next_token = next_token
        # Specify the maximum number of data entries per page in a paginated query. The default number of data entries per page is 20. If the PageSize parameter is empty, 20 data entries will be returned by default.
        # > It is recommended that the PageSize value is not empty.
        self.page_size = page_size
        # Server name or IP.
        self.remark = remark
        # A set of conditions for querying asset fingerprint details.
        self.search_criteria_list = search_criteria_list
        # Whether to use the NextToken method to fetch the list of vulnerabilities. If this parameter is used, TotalCount will not be returned. Values:
        # 
        # - **true**: Use the NextToken method.
        # - **false**: Do not use the NextToken method.
        self.use_next_token = use_next_token
        # The UUID of the asset to be queried.
        # > Call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) API to obtain this parameter.
        self.uuid = uuid

    def validate(self):
        if self.search_criteria_list:
            for v1 in self.search_criteria_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        result['SearchCriteriaList'] = []
        if self.search_criteria_list is not None:
            for k1 in self.search_criteria_list:
                result['SearchCriteriaList'].append(k1.to_map() if k1 else None)

        if self.use_next_token is not None:
            result['UseNextToken'] = self.use_next_token

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        self.search_criteria_list = []
        if m.get('SearchCriteriaList') is not None:
            for k1 in m.get('SearchCriteriaList'):
                temp_model = main_models.GetAssetsPropertyDetailRequestSearchCriteriaList()
                self.search_criteria_list.append(temp_model.from_map(k1))

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class GetAssetsPropertyDetailRequestSearchCriteriaList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the condition to be queried. Values are as follows:
        # - **remarkItemName**: The aggregated item name of the asset fingerprint, supporting fuzzy matching
        # 
        # 
        # >-   - When **Biz** is **web_server**, **remarkItemName** represents the domain name as the search condition.
        # >-   - When **Biz** is **lkm**, **remarkItemName** represents the module name as the search condition.
        # >-   - When **Biz** is **autorun**, **remarkItemName** represents the startup item path as the search condition.
        self.name = name
        # The value of the condition to be queried.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

