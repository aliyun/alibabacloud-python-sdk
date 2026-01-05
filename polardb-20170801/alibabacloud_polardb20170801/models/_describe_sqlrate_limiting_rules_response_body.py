# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLRateLimitingRulesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSQLRateLimitingRulesResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.max_results = max_results
        self.message = message
        # nextToken
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSQLRateLimitingRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSQLRateLimitingRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        rule_list: List[str] = None,
    ):
        self.rule_list = rule_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleList') is not None:
            self.rule_list = m.get('RuleList')

        return self

