# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainTopRefererResponseBody(DaraModel):
    def __init__(
        self,
        domain_top_referer: List[main_models.DescribeDomainTopRefererResponseBodyDomainTopReferer] = None,
        request_id: str = None,
    ):
        # The information about top referers.
        self.domain_top_referer = domain_top_referer
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_top_referer:
            for v1 in self.domain_top_referer:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainTopReferer'] = []
        if self.domain_top_referer is not None:
            for k1 in self.domain_top_referer:
                result['DomainTopReferer'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_top_referer = []
        if m.get('DomainTopReferer') is not None:
            for k1 in m.get('DomainTopReferer'):
                temp_model = main_models.DescribeDomainTopRefererResponseBodyDomainTopReferer()
                self.domain_top_referer.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainTopRefererResponseBodyDomainTopReferer(DaraModel):
    def __init__(
        self,
        domain: str = None,
        pv: int = None,
        referer: str = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The page views.
        self.pv = pv
        # The Base64-encoded referer.
        self.referer = referer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.pv is not None:
            result['Pv'] = self.pv

        if self.referer is not None:
            result['Referer'] = self.referer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Pv') is not None:
            self.pv = m.get('Pv')

        if m.get('Referer') is not None:
            self.referer = m.get('Referer')

        return self

