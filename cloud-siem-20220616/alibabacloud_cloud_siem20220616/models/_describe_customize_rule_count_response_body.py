# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomizeRuleCountResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeCustomizeRuleCountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeCustomizeRuleCountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCustomizeRuleCountResponseBodyData(DaraModel):
    def __init__(
        self,
        aggregation_rule_num: int = None,
        customize_rule_num: int = None,
        expert_rule_num: int = None,
        graph_computing_rule_num: int = None,
        high_rule_num: int = None,
        in_use_rule_num: int = None,
        low_rule_num: int = None,
        medium_rule_num: int = None,
        predefined_rule_num: int = None,
        single_alert_rule_num: int = None,
        total_rule_num: int = None,
        un_event_rule_num: int = None,
    ):
        # 同类聚合规则数。
        self.aggregation_rule_num = aggregation_rule_num
        # 自定义规则数。
        self.customize_rule_num = customize_rule_num
        # 专家规则数。
        self.expert_rule_num = expert_rule_num
        # 图计算规则数。
        self.graph_computing_rule_num = graph_computing_rule_num
        # The number of rules that are used to identify high-risk threats.
        self.high_rule_num = high_rule_num
        # The total number of rules.
        self.in_use_rule_num = in_use_rule_num
        # The number of rules that are used to identify low-risk threats.
        self.low_rule_num = low_rule_num
        # The number of rules that are used to identify medium-risk threats.
        self.medium_rule_num = medium_rule_num
        # 预定义规则数。
        self.predefined_rule_num = predefined_rule_num
        # 告警透传规则数。
        self.single_alert_rule_num = single_alert_rule_num
        # 总规则数。
        self.total_rule_num = total_rule_num
        # 不产生事件规则数。
        self.un_event_rule_num = un_event_rule_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregation_rule_num is not None:
            result['AggregationRuleNum'] = self.aggregation_rule_num

        if self.customize_rule_num is not None:
            result['CustomizeRuleNum'] = self.customize_rule_num

        if self.expert_rule_num is not None:
            result['ExpertRuleNum'] = self.expert_rule_num

        if self.graph_computing_rule_num is not None:
            result['GraphComputingRuleNum'] = self.graph_computing_rule_num

        if self.high_rule_num is not None:
            result['HighRuleNum'] = self.high_rule_num

        if self.in_use_rule_num is not None:
            result['InUseRuleNum'] = self.in_use_rule_num

        if self.low_rule_num is not None:
            result['LowRuleNum'] = self.low_rule_num

        if self.medium_rule_num is not None:
            result['MediumRuleNum'] = self.medium_rule_num

        if self.predefined_rule_num is not None:
            result['PredefinedRuleNum'] = self.predefined_rule_num

        if self.single_alert_rule_num is not None:
            result['SingleAlertRuleNum'] = self.single_alert_rule_num

        if self.total_rule_num is not None:
            result['TotalRuleNum'] = self.total_rule_num

        if self.un_event_rule_num is not None:
            result['UnEventRuleNum'] = self.un_event_rule_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationRuleNum') is not None:
            self.aggregation_rule_num = m.get('AggregationRuleNum')

        if m.get('CustomizeRuleNum') is not None:
            self.customize_rule_num = m.get('CustomizeRuleNum')

        if m.get('ExpertRuleNum') is not None:
            self.expert_rule_num = m.get('ExpertRuleNum')

        if m.get('GraphComputingRuleNum') is not None:
            self.graph_computing_rule_num = m.get('GraphComputingRuleNum')

        if m.get('HighRuleNum') is not None:
            self.high_rule_num = m.get('HighRuleNum')

        if m.get('InUseRuleNum') is not None:
            self.in_use_rule_num = m.get('InUseRuleNum')

        if m.get('LowRuleNum') is not None:
            self.low_rule_num = m.get('LowRuleNum')

        if m.get('MediumRuleNum') is not None:
            self.medium_rule_num = m.get('MediumRuleNum')

        if m.get('PredefinedRuleNum') is not None:
            self.predefined_rule_num = m.get('PredefinedRuleNum')

        if m.get('SingleAlertRuleNum') is not None:
            self.single_alert_rule_num = m.get('SingleAlertRuleNum')

        if m.get('TotalRuleNum') is not None:
            self.total_rule_num = m.get('TotalRuleNum')

        if m.get('UnEventRuleNum') is not None:
            self.un_event_rule_num = m.get('UnEventRuleNum')

        return self

