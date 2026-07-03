# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetResponseRuleStatisticResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        response_statistic: main_models.GetResponseRuleStatisticResponseBodyResponseStatistic = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics of automated response rules.
        self.response_statistic = response_statistic

    def validate(self):
        if self.response_statistic:
            self.response_statistic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.response_statistic is not None:
            result['ResponseStatistic'] = self.response_statistic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResponseStatistic') is not None:
            temp_model = main_models.GetResponseRuleStatisticResponseBodyResponseStatistic()
            self.response_statistic = temp_model.from_map(m.get('ResponseStatistic'))

        return self

class GetResponseRuleStatisticResponseBodyResponseStatistic(DaraModel):
    def __init__(
        self,
        response_rule_all_count: int = None,
        response_rule_online_count: int = None,
    ):
        # The total number of automated response rules.
        self.response_rule_all_count = response_rule_all_count
        # The number of online automated response rules.
        self.response_rule_online_count = response_rule_online_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.response_rule_all_count is not None:
            result['ResponseRuleAllCount'] = self.response_rule_all_count

        if self.response_rule_online_count is not None:
            result['ResponseRuleOnlineCount'] = self.response_rule_online_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResponseRuleAllCount') is not None:
            self.response_rule_all_count = m.get('ResponseRuleAllCount')

        if m.get('ResponseRuleOnlineCount') is not None:
            self.response_rule_online_count = m.get('ResponseRuleOnlineCount')

        return self

