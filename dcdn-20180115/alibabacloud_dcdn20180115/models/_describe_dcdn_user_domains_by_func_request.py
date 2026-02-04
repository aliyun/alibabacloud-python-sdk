# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnUserDomainsByFuncRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        func_filter: str = None,
        func_id: int = None,
        match_type: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The accelerated domain name whose ICP filing status you want to update.
        self.domain_name = domain_name
        # Specifies whether the feature that is specified by the FuncId parameter is enabled.
        # 
        # *   **config**: enabled
        # *   **unconfig**: not enabled
        self.func_filter = func_filter
        # The ID of the feature. For more information about how to query feature IDs, see [Parameters for configuring features for domain names](https://help.aliyun.com/document_detail/410622.html). For example, the ID of the origin host feature (set_req_host_header) is 18.
        # 
        # This parameter is required.
        self.func_id = func_id
        # The type of the search. Default value: exact_match. Valid values:
        # 
        # *   fuzzy_match: fuzzy search.
        # *   exact_match: exact search.
        self.match_type = match_type
        # The number of the page to return. Default value: **1**. Valid values: **1 to 100000**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **20**. Valid values: **1 to 500**.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.func_filter is not None:
            result['FuncFilter'] = self.func_filter

        if self.func_id is not None:
            result['FuncId'] = self.func_id

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FuncFilter') is not None:
            self.func_filter = m.get('FuncFilter')

        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

