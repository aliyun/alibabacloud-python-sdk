# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainSuffixResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        suffix_list: main_models.QueryDomainSuffixResponseBodySuffixList = None,
    ):
        self.request_id = request_id
        self.suffix_list = suffix_list

    def validate(self):
        if self.suffix_list:
            self.suffix_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.suffix_list is not None:
            result['SuffixList'] = self.suffix_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuffixList') is not None:
            temp_model = main_models.QueryDomainSuffixResponseBodySuffixList()
            self.suffix_list = temp_model.from_map(m.get('SuffixList'))

        return self

class QueryDomainSuffixResponseBodySuffixList(DaraModel):
    def __init__(
        self,
        suffix: List[str] = None,
    ):
        self.suffix = suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.suffix is not None:
            result['Suffix'] = self.suffix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        return self

