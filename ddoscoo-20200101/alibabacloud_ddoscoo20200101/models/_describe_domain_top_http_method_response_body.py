# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainTopHttpMethodResponseBody(DaraModel):
    def __init__(
        self,
        domain_top_method: List[main_models.DescribeDomainTopHttpMethodResponseBodyDomainTopMethod] = None,
        request_id: str = None,
    ):
        # The information about top HTTP methods.
        self.domain_top_method = domain_top_method
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_top_method:
            for v1 in self.domain_top_method:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainTopMethod'] = []
        if self.domain_top_method is not None:
            for k1 in self.domain_top_method:
                result['DomainTopMethod'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_top_method = []
        if m.get('DomainTopMethod') is not None:
            for k1 in m.get('DomainTopMethod'):
                temp_model = main_models.DescribeDomainTopHttpMethodResponseBodyDomainTopMethod()
                self.domain_top_method.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainTopHttpMethodResponseBodyDomainTopMethod(DaraModel):
    def __init__(
        self,
        domain: str = None,
        http_method: str = None,
        pv: int = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The HTTP method.
        self.http_method = http_method
        # The page views.
        self.pv = pv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.pv is not None:
            result['Pv'] = self.pv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('Pv') is not None:
            self.pv = m.get('Pv')

        return self

