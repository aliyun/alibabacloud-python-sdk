# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class ApplyMetricRuleTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        resource: main_models.ApplyMetricRuleTemplateResponseBodyResource = None,
        success: bool = None,
    ):
        # The responses code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The resources that are affected by the alert rule.
        self.resource = resource
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.resource:
            self.resource.validate()

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

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

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

        if m.get('Resource') is not None:
            temp_model = main_models.ApplyMetricRuleTemplateResponseBodyResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ApplyMetricRuleTemplateResponseBodyResource(DaraModel):
    def __init__(
        self,
        alert_results: List[main_models.ApplyMetricRuleTemplateResponseBodyResourceAlertResults] = None,
        group_id: int = None,
    ):
        # The details of the generated alert rule.
        self.alert_results = alert_results
        # The ID of the application group.
        self.group_id = group_id

    def validate(self):
        if self.alert_results:
            for v1 in self.alert_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertResults'] = []
        if self.alert_results is not None:
            for k1 in self.alert_results:
                result['AlertResults'].append(k1.to_map() if k1 else None)

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_results = []
        if m.get('AlertResults') is not None:
            for k1 in m.get('AlertResults'):
                temp_model = main_models.ApplyMetricRuleTemplateResponseBodyResourceAlertResults()
                self.alert_results.append(temp_model.from_map(k1))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        return self

class ApplyMetricRuleTemplateResponseBodyResourceAlertResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        rule_id: str = None,
        rule_name: str = None,
        success: bool = None,
    ):
        # The responses code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the alert rule.
        self.rule_id = rule_id
        # The name of the alert rule.
        self.rule_name = rule_name
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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

