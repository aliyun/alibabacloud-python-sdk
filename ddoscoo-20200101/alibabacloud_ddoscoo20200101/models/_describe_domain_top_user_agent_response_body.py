# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainTopUserAgentResponseBody(DaraModel):
    def __init__(
        self,
        domain_top_ua: List[main_models.DescribeDomainTopUserAgentResponseBodyDomainTopUa] = None,
        request_id: str = None,
    ):
        # The information about the user agents.
        self.domain_top_ua = domain_top_ua
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_top_ua:
            for v1 in self.domain_top_ua:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainTopUa'] = []
        if self.domain_top_ua is not None:
            for k1 in self.domain_top_ua:
                result['DomainTopUa'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_top_ua = []
        if m.get('DomainTopUa') is not None:
            for k1 in m.get('DomainTopUa'):
                temp_model = main_models.DescribeDomainTopUserAgentResponseBodyDomainTopUa()
                self.domain_top_ua.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainTopUserAgentResponseBodyDomainTopUa(DaraModel):
    def __init__(
        self,
        domain: str = None,
        pv: int = None,
        user_agent: str = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The page views.
        self.pv = pv
        # The Base64-encoded user agent.
        self.user_agent = user_agent

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

        if self.user_agent is not None:
            result['UserAgent'] = self.user_agent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Pv') is not None:
            self.pv = m.get('Pv')

        if m.get('UserAgent') is not None:
            self.user_agent = m.get('UserAgent')

        return self

