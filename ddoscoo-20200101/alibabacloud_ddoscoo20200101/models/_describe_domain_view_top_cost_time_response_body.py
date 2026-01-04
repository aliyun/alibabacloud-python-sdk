# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainViewTopCostTimeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        url_list: List[main_models.DescribeDomainViewTopCostTimeResponseBodyUrlList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The URLs which require the longest time to respond to requests.
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for v1 in self.url_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UrlList'] = []
        if self.url_list is not None:
            for k1 in self.url_list:
                result['UrlList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.url_list = []
        if m.get('UrlList') is not None:
            for k1 in m.get('UrlList'):
                temp_model = main_models.DescribeDomainViewTopCostTimeResponseBodyUrlList()
                self.url_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainViewTopCostTimeResponseBodyUrlList(DaraModel):
    def __init__(
        self,
        cost_time: float = None,
        domain: str = None,
        url: str = None,
    ):
        # The response duration. Unit: milliseconds.
        self.cost_time = cost_time
        # The domain name of the website.
        self.domain = domain
        # The URL that is Base64-encoded.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

