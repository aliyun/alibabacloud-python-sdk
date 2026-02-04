# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnWafPoliciesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        query_args: str = None,
    ):
        # The number of the page to return. Valid values: **1** to **100000**. Default value: **1**.
        self.page_number = page_number
        # The number of protection policies to return on each page. Valid values: an integer from **1** to **500**. Default value: **20**.
        self.page_size = page_size
        # The query conditions. The value is a JSON string. The format is `QueryArgs={"PolicyIds":"The IDs of protection policies","RuleIds":"The IDs of protection rules","PolicyNameLike":"The name of the protection policy","DomainNames":"The protected domain names","PolicyType":"default","DefenseScenes":"waf_group","PolicyStatus":"on","OrderBy":"GmtModified","Desc":"false"}`
        # 
        # > If you do not set this parameter, all protection policies are queried.
        self.query_args = query_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_args is not None:
            result['QueryArgs'] = self.query_args

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryArgs') is not None:
            self.query_args = m.get('QueryArgs')

        return self

