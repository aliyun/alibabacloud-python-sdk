# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateGroupMetricRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        resources: main_models.CreateGroupMetricRulesResponseBodyResources = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the call is successful.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The details of the alert rules.
        self.resources = resources
        # Indicates whether the call is successful. Valid value:
        # 
        # - true: The call is successful.
        # - false: The call fails.
        self.success = success

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            temp_model = main_models.CreateGroupMetricRulesResponseBodyResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateGroupMetricRulesResponseBodyResources(DaraModel):
    def __init__(
        self,
        alert_result: List[main_models.CreateGroupMetricRulesResponseBodyResourcesAlertResult] = None,
    ):
        self.alert_result = alert_result

    def validate(self):
        if self.alert_result:
            for v1 in self.alert_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertResult'] = []
        if self.alert_result is not None:
            for k1 in self.alert_result:
                result['AlertResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_result = []
        if m.get('AlertResult') is not None:
            for k1 in m.get('AlertResult'):
                temp_model = main_models.CreateGroupMetricRulesResponseBodyResourcesAlertResult()
                self.alert_result.append(temp_model.from_map(k1))

        return self

class CreateGroupMetricRulesResponseBodyResourcesAlertResult(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        rule_id: str = None,
        rule_name: str = None,
        success: bool = None,
    ):
        # The status code that is returned for the alert rule.
        # 
        # >  The status code 200 indicates that the call is successful.
        self.code = code
        # The error message that is returned for the alert rule.
        self.message = message
        # The ID of the alert rule.
        self.rule_id = rule_id
        # The name of the alert rule.
        self.rule_name = rule_name
        # Indicates whether the alert rule was created. Valid value:
        # 
        # - true: The alert rule was created.
        # - false: The alert rule failed to be created.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

