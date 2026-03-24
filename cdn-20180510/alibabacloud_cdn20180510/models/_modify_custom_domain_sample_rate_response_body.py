# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class ModifyCustomDomainSampleRateResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.ModifyCustomDomainSampleRateResponseBodyContent = None,
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
            temp_model = main_models.ModifyCustomDomainSampleRateResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyCustomDomainSampleRateResponseBodyContent(DaraModel):
    def __init__(
        self,
        content: List[main_models.ModifyCustomDomainSampleRateResponseBodyContentContent] = None,
    ):
        self.content = content

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ModifyCustomDomainSampleRateResponseBodyContentContent()
                self.content.append(temp_model.from_map(k1))

        return self

class ModifyCustomDomainSampleRateResponseBodyContentContent(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        err_message: str = None,
        sample_rate: float = None,
    ):
        self.domain_name = domain_name
        self.err_message = err_message
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

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        return self

