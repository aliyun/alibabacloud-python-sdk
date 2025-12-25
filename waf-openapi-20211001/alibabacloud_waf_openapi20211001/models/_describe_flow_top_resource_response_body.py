# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowTopResourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_hits_top_resource: List[main_models.DescribeFlowTopResourceResponseBodyRuleHitsTopResource] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The array of the top 10 protected objects that receive requests.
        self.rule_hits_top_resource = rule_hits_top_resource

    def validate(self):
        if self.rule_hits_top_resource:
            for v1 in self.rule_hits_top_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleHitsTopResource'] = []
        if self.rule_hits_top_resource is not None:
            for k1 in self.rule_hits_top_resource:
                result['RuleHitsTopResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_hits_top_resource = []
        if m.get('RuleHitsTopResource') is not None:
            for k1 in m.get('RuleHitsTopResource'):
                temp_model = main_models.DescribeFlowTopResourceResponseBodyRuleHitsTopResource()
                self.rule_hits_top_resource.append(temp_model.from_map(k1))

        return self

class DescribeFlowTopResourceResponseBodyRuleHitsTopResource(DaraModel):
    def __init__(
        self,
        count: int = None,
        resource: str = None,
    ):
        # The total number of requests received by the protected object in a specified time range.
        self.count = count
        # The protected object.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.resource is not None:
            result['Resource'] = self.resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        return self

