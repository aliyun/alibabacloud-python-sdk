# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class QueryAliasesResponseBody(DaraModel):
    def __init__(
        self,
        alias_infos: main_models.QueryAliasesResponseBodyAliasInfos = None,
        request_id: str = None,
    ):
        self.alias_infos = alias_infos
        self.request_id = request_id

    def validate(self):
        if self.alias_infos:
            self.alias_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_infos is not None:
            result['AliasInfos'] = self.alias_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasInfos') is not None:
            temp_model = main_models.QueryAliasesResponseBodyAliasInfos()
            self.alias_infos = temp_model.from_map(m.get('AliasInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryAliasesResponseBodyAliasInfos(DaraModel):
    def __init__(
        self,
        alias_info: List[main_models.QueryAliasesResponseBodyAliasInfosAliasInfo] = None,
    ):
        self.alias_info = alias_info

    def validate(self):
        if self.alias_info:
            for v1 in self.alias_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AliasInfo'] = []
        if self.alias_info is not None:
            for k1 in self.alias_info:
                result['AliasInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alias_info = []
        if m.get('AliasInfo') is not None:
            for k1 in m.get('AliasInfo'):
                temp_model = main_models.QueryAliasesResponseBodyAliasInfosAliasInfo()
                self.alias_info.append(temp_model.from_map(k1))

        return self

class QueryAliasesResponseBodyAliasInfosAliasInfo(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
    ):
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        return self

