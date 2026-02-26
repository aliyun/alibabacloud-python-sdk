# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class SearchMultiAccountResourcesRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.SearchMultiAccountResourcesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
        sort_criterion: main_models.SearchMultiAccountResourcesRequestSortCriterion = None,
    ):
        # The filter conditions.
        self.filter = filter
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        # The scope of the accounts in which you want to search for resources. Valid values:
        # 
        # - The ID of a resource directory: Searches for resources in the management account and all its member accounts. For more information, see [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html).
        # 
        # - The ID of the Root folder: Searches for resources in all member accounts under the Root folder and its subfolders. For more information, see [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html).
        # 
        # - The ID of a folder: Searches for resources in all member accounts under the folder. For more information, see [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html).
        # 
        # - The ID of a member account: Searches for resources in the member account. For more information, see [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        # 
        # This parameter is required.
        self.scope = scope
        # The sorting parameters.
        self.sort_criterion = sort_criterion

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.sort_criterion:
            self.sort_criterion.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.sort_criterion is not None:
            result['SortCriterion'] = self.sort_criterion.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.SearchMultiAccountResourcesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SortCriterion') is not None:
            temp_model = main_models.SearchMultiAccountResourcesRequestSortCriterion()
            self.sort_criterion = temp_model.from_map(m.get('SortCriterion'))

        return self

class SearchMultiAccountResourcesRequestSortCriterion(DaraModel):
    def __init__(
        self,
        key: str = None,
        order: str = None,
    ):
        # The sort key.
        # 
        # Set this parameter to `CreateTime`, which means the results are sorted by resource creation time.
        self.key = key
        # The sort order. Valid values:
        # 
        # - ASC: Ascending order.
        # 
        # - DESC: Descending order.
        # 
        # Default value: ASC.
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.order is not None:
            result['Order'] = self.order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        return self

class SearchMultiAccountResourcesRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see the "`Supported filter parameters`" section below.
        self.key = key
        # The matching method.
        # 
        # Set this parameter to `Equals`, which means an exact match.
        self.match_type = match_type
        # The values of the filter condition.
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

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

