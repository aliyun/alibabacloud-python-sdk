# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetDetectionStatisticResponseBody(DaraModel):
    def __init__(
        self,
        detection_statistic: main_models.GetDetectionStatisticResponseBodyDetectionStatistic = None,
        request_id: str = None,
    ):
        self.detection_statistic = detection_statistic
        self.request_id = request_id

    def validate(self):
        if self.detection_statistic:
            self.detection_statistic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detection_statistic is not None:
            result['DetectionStatistic'] = self.detection_statistic.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectionStatistic') is not None:
            temp_model = main_models.GetDetectionStatisticResponseBodyDetectionStatistic()
            self.detection_statistic = temp_model.from_map(m.get('DetectionStatistic'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDetectionStatisticResponseBodyDetectionStatistic(DaraModel):
    def __init__(
        self,
        detection_rule_online_count: int = None,
        detection_rule_template_count: int = None,
        detection_rule_test_count: int = None,
        graph_compute_rule_count: int = None,
        passthrough_rule_count: int = None,
        window_rule_count: int = None,
    ):
        self.detection_rule_online_count = detection_rule_online_count
        self.detection_rule_template_count = detection_rule_template_count
        self.detection_rule_test_count = detection_rule_test_count
        self.graph_compute_rule_count = graph_compute_rule_count
        self.passthrough_rule_count = passthrough_rule_count
        self.window_rule_count = window_rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detection_rule_online_count is not None:
            result['DetectionRuleOnlineCount'] = self.detection_rule_online_count

        if self.detection_rule_template_count is not None:
            result['DetectionRuleTemplateCount'] = self.detection_rule_template_count

        if self.detection_rule_test_count is not None:
            result['DetectionRuleTestCount'] = self.detection_rule_test_count

        if self.graph_compute_rule_count is not None:
            result['GraphComputeRuleCount'] = self.graph_compute_rule_count

        if self.passthrough_rule_count is not None:
            result['PassthroughRuleCount'] = self.passthrough_rule_count

        if self.window_rule_count is not None:
            result['WindowRuleCount'] = self.window_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectionRuleOnlineCount') is not None:
            self.detection_rule_online_count = m.get('DetectionRuleOnlineCount')

        if m.get('DetectionRuleTemplateCount') is not None:
            self.detection_rule_template_count = m.get('DetectionRuleTemplateCount')

        if m.get('DetectionRuleTestCount') is not None:
            self.detection_rule_test_count = m.get('DetectionRuleTestCount')

        if m.get('GraphComputeRuleCount') is not None:
            self.graph_compute_rule_count = m.get('GraphComputeRuleCount')

        if m.get('PassthroughRuleCount') is not None:
            self.passthrough_rule_count = m.get('PassthroughRuleCount')

        if m.get('WindowRuleCount') is not None:
            self.window_rule_count = m.get('WindowRuleCount')

        return self

