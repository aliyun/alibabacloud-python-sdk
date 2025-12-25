# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeVisitUasResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        uas: List[main_models.DescribeVisitUasResponseBodyUas] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The array of the top 10 user agents that are used to initiate requests.
        self.uas = uas

    def validate(self):
        if self.uas:
            for v1 in self.uas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Uas'] = []
        if self.uas is not None:
            for k1 in self.uas:
                result['Uas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.uas = []
        if m.get('Uas') is not None:
            for k1 in m.get('Uas'):
                temp_model = main_models.DescribeVisitUasResponseBodyUas()
                self.uas.append(temp_model.from_map(k1))

        return self

class DescribeVisitUasResponseBodyUas(DaraModel):
    def __init__(
        self,
        count: int = None,
        ua: str = None,
    ):
        # The number of requests that use the user agent.
        self.count = count
        # The user agent.
        self.ua = ua

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.ua is not None:
            result['Ua'] = self.ua

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Ua') is not None:
            self.ua = m.get('Ua')

        return self

