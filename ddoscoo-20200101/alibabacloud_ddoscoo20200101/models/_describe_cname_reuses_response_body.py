# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeCnameReusesResponseBody(DaraModel):
    def __init__(
        self,
        cname_reuses: List[main_models.DescribeCnameReusesResponseBodyCnameReuses] = None,
        request_id: str = None,
    ):
        self.cname_reuses = cname_reuses
        self.request_id = request_id

    def validate(self):
        if self.cname_reuses:
            for v1 in self.cname_reuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CnameReuses'] = []
        if self.cname_reuses is not None:
            for k1 in self.cname_reuses:
                result['CnameReuses'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cname_reuses = []
        if m.get('CnameReuses') is not None:
            for k1 in m.get('CnameReuses'):
                temp_model = main_models.DescribeCnameReusesResponseBodyCnameReuses()
                self.cname_reuses.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCnameReusesResponseBodyCnameReuses(DaraModel):
    def __init__(
        self,
        cname: str = None,
        domain: str = None,
        enable: int = None,
    ):
        self.cname = cname
        self.domain = domain
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

