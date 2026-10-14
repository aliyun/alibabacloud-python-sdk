# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebCCRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        web_ccrules: List[main_models.DescribeWebCCRulesResponseBodyWebCCRules] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of frequency control (HTTP flood mitigation) custom rules.
        self.total_count = total_count
        # The frequency control (HTTP flood mitigation) custom rules.
        self.web_ccrules = web_ccrules

    def validate(self):
        if self.web_ccrules:
            for v1 in self.web_ccrules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WebCCRules'] = []
        if self.web_ccrules is not None:
            for k1 in self.web_ccrules:
                result['WebCCRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.web_ccrules = []
        if m.get('WebCCRules') is not None:
            for k1 in m.get('WebCCRules'):
                temp_model = main_models.DescribeWebCCRulesResponseBodyWebCCRules()
                self.web_ccrules.append(temp_model.from_map(k1))

        return self

class DescribeWebCCRulesResponseBodyWebCCRules(DaraModel):
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
        # The blocking type. Valid values:
        # - **close**: blocks the request.
        # - **captcha**: implements CAPTCHA verification.
        self.act = act
        # The number of visits from a single IP address. Valid values: **2** to **2000**.
        self.count = count
        # The detection interval. Valid values: **5** to **10800**. Unit: seconds.
        self.interval = interval
        # The matching mode. Valid values:
        # - **prefix**: prefix match.
        # - **match**: exact match.
        self.mode = mode
        # The rule name.
        self.name = name
        # The blocking duration. Valid values: **1** to **1440**. Unit: minutes.
        self.ttl = ttl
        # The detection path.
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

