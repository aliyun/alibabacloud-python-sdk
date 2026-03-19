# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeLayer7CCRulesResponseBody(DaraModel):
    def __init__(
        self,
        layer_7ccrules: List[main_models.DescribeLayer7CCRulesResponseBodyLayer7CCRules] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.layer_7ccrules = layer_7ccrules
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.layer_7ccrules:
            for v1 in self.layer_7ccrules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Layer7CCRules'] = []
        if self.layer_7ccrules is not None:
            for k1 in self.layer_7ccrules:
                result['Layer7CCRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layer_7ccrules = []
        if m.get('Layer7CCRules') is not None:
            for k1 in m.get('Layer7CCRules'):
                temp_model = main_models.DescribeLayer7CCRulesResponseBodyLayer7CCRules()
                self.layer_7ccrules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeLayer7CCRulesResponseBodyLayer7CCRules(DaraModel):
    def __init__(
        self,
        act: str = None,
        count: int = None,
        interval: int = None,
        mode: str = None,
        name: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        self.act = act
        self.count = count
        self.interval = interval
        self.mode = mode
        self.name = name
        self.ttl = ttl
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.act is not None:
            result['Act'] = self.act

        if self.count is not None:
            result['Count'] = self.count

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Act') is not None:
            self.act = m.get('Act')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

