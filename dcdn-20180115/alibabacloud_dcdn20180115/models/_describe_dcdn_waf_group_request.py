# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnWafGroupRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        query_args: str = None,
        scope: str = None,
    ):
        # The ID of the WAF rule group. You can query the ID by calling the [DescribeDcdnWafGroups](~~DescribeDcdnWafGroups~~) operation.
        # 
        # This parameter is required.
        self.id = id
        # The language of the response. Valid values:
        # 
        # *   **en**: English.
        # *   **zh**: Chinese.
        # 
        # This parameter is required.
        self.language = language
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The query conditions. The value is a JSON string in the following format:
        # 
        # `QueryArgs={"PolicyIds":"The range of protection policy IDs","RuleIds":"The range of protection rule IDs","RuleNameLike":"The name of the protection rule","DomainNames":"The protected domain names","DefenseScenes":"waf_group","RuleStatus":"on","OrderBy":"GmtModified","Desc":"false"}`
        # 
        # >  If you do not specify this parameter, all protection rules are queried.
        self.query_args = query_args
        # The range of the rule group to be queried.
        # 
        # *   **in**: Rules in the rule group are returned.
        # *   **out**: Rules that are in the full rule set but are not in the rule group are returned.
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.language is not None:
            result['Language'] = self.language

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_args is not None:
            result['QueryArgs'] = self.query_args

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryArgs') is not None:
            self.query_args = m.get('QueryArgs')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

