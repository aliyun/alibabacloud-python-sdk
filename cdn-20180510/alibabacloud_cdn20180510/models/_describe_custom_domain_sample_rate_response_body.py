# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomDomainSampleRateResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeCustomDomainSampleRateResponseBodyContent = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.DescribeCustomDomainSampleRateResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCustomDomainSampleRateResponseBodyContent(DaraModel):
    def __init__(
        self,
        domain_content: List[main_models.DescribeCustomDomainSampleRateResponseBodyContentDomainContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.domain_content = domain_content
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.domain_content:
            for v1 in self.domain_content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainContent'] = []
        if self.domain_content is not None:
            for k1 in self.domain_content:
                result['DomainContent'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_content = []
        if m.get('DomainContent') is not None:
            for k1 in m.get('DomainContent'):
                temp_model = main_models.DescribeCustomDomainSampleRateResponseBodyContentDomainContent()
                self.domain_content.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCustomDomainSampleRateResponseBodyContentDomainContent(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        sample_rate: float = None,
    ):
        self.domain_name = domain_name
        self.sample_rate = sample_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        return self

