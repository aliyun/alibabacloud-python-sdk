# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class ListAliasesByKeyIdResponseBody(DaraModel):
    def __init__(
        self,
        aliases: main_models.ListAliasesByKeyIdResponseBodyAliases = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.aliases = aliases
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of returned CMKs.
        self.total_count = total_count

    def validate(self):
        if self.aliases:
            self.aliases.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliases is not None:
            result['Aliases'] = self.aliases.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliases') is not None:
            temp_model = main_models.ListAliasesByKeyIdResponseBodyAliases()
            self.aliases = temp_model.from_map(m.get('Aliases'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAliasesByKeyIdResponseBodyAliases(DaraModel):
    def __init__(
        self,
        alias: List[main_models.ListAliasesByKeyIdResponseBodyAliasesAlias] = None,
    ):
        self.alias = alias

    def validate(self):
        if self.alias:
            for v1 in self.alias:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Alias'] = []
        if self.alias is not None:
            for k1 in self.alias:
                result['Alias'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alias = []
        if m.get('Alias') is not None:
            for k1 in m.get('Alias'):
                temp_model = main_models.ListAliasesByKeyIdResponseBodyAliasesAlias()
                self.alias.append(temp_model.from_map(k1))

        return self

class ListAliasesByKeyIdResponseBodyAliasesAlias(DaraModel):
    def __init__(
        self,
        alias_arn: str = None,
        alias_name: str = None,
        key_id: str = None,
    ):
        self.alias_arn = alias_arn
        self.alias_name = alias_name
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_arn is not None:
            result['AliasArn'] = self.alias_arn

        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasArn') is not None:
            self.alias_arn = m.get('AliasArn')

        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        return self

