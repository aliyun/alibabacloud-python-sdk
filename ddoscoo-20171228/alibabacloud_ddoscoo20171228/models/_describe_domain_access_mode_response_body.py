# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainAccessModeResponseBody(DaraModel):
    def __init__(
        self,
        domain_mode_list: List[main_models.DescribeDomainAccessModeResponseBodyDomainModeList] = None,
        request_id: str = None,
    ):
        self.domain_mode_list = domain_mode_list
        self.request_id = request_id

    def validate(self):
        if self.domain_mode_list:
            for v1 in self.domain_mode_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainModeList'] = []
        if self.domain_mode_list is not None:
            for k1 in self.domain_mode_list:
                result['DomainModeList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_mode_list = []
        if m.get('DomainModeList') is not None:
            for k1 in m.get('DomainModeList'):
                temp_model = main_models.DescribeDomainAccessModeResponseBodyDomainModeList()
                self.domain_mode_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainAccessModeResponseBodyDomainModeList(DaraModel):
    def __init__(
        self,
        access_mode: int = None,
        domain: str = None,
    ):
        self.access_mode = access_mode
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

