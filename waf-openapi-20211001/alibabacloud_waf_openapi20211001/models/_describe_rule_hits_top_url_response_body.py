# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeRuleHitsTopUrlResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_hits_top_url: List[main_models.DescribeRuleHitsTopUrlResponseBodyRuleHitsTopUrl] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The top 10 URLs that match protection rules.
        self.rule_hits_top_url = rule_hits_top_url

    def validate(self):
        if self.rule_hits_top_url:
            for v1 in self.rule_hits_top_url:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleHitsTopUrl'] = []
        if self.rule_hits_top_url is not None:
            for k1 in self.rule_hits_top_url:
                result['RuleHitsTopUrl'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_hits_top_url = []
        if m.get('RuleHitsTopUrl') is not None:
            for k1 in m.get('RuleHitsTopUrl'):
                temp_model = main_models.DescribeRuleHitsTopUrlResponseBodyRuleHitsTopUrl()
                self.rule_hits_top_url.append(temp_model.from_map(k1))

        return self

class DescribeRuleHitsTopUrlResponseBodyRuleHitsTopUrl(DaraModel):
    def __init__(
        self,
        count: int = None,
        url: str = None,
    ):
        # The number of requests that match protection rules.
        self.count = count
        # The request URL.
        # 
        # >  The value is Base64-encoded.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

