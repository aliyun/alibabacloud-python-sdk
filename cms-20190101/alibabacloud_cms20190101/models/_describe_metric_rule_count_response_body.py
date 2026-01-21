# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricRuleCountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        metric_rule_count: main_models.DescribeMetricRuleCountResponseBodyMetricRuleCount = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The responses code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The number of alert rules in each state.
        self.metric_rule_count = metric_rule_count
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.metric_rule_count:
            self.metric_rule_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.metric_rule_count is not None:
            result['MetricRuleCount'] = self.metric_rule_count.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MetricRuleCount') is not None:
            temp_model = main_models.DescribeMetricRuleCountResponseBodyMetricRuleCount()
            self.metric_rule_count = temp_model.from_map(m.get('MetricRuleCount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeMetricRuleCountResponseBodyMetricRuleCount(DaraModel):
    def __init__(
        self,
        alarm: int = None,
        disable: int = None,
        nodata: int = None,
        ok: int = None,
        total: int = None,
    ):
        # The number of alert rules with active alerts.
        self.alarm = alarm
        # The number of disabled alert rules.
        self.disable = disable
        # The number of alert rules without data.
        self.nodata = nodata
        # The number of alert rules without active alerts.
        self.ok = ok
        # The total number of alert rules.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm is not None:
            result['Alarm'] = self.alarm

        if self.disable is not None:
            result['Disable'] = self.disable

        if self.nodata is not None:
            result['Nodata'] = self.nodata

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alarm') is not None:
            self.alarm = m.get('Alarm')

        if m.get('Disable') is not None:
            self.disable = m.get('Disable')

        if m.get('Nodata') is not None:
            self.nodata = m.get('Nodata')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

