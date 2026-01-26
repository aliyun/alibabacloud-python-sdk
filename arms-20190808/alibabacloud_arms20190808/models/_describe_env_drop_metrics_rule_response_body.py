# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeEnvDropMetricsRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeEnvDropMetricsRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeEnvDropMetricsRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnvDropMetricsRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        drop_metrics: str = None,
        rule_name: str = None,
    ):
        # The list of discarded metrics. Separate multiple metrics with line feeds.
        self.drop_metrics = drop_metrics
        # The name of the discarded metric rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drop_metrics is not None:
            result['DropMetrics'] = self.drop_metrics

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DropMetrics') is not None:
            self.drop_metrics = m.get('DropMetrics')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

