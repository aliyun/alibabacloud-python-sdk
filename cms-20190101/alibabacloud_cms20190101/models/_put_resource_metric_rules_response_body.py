# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutResourceMetricRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        failed_list_result: main_models.PutResourceMetricRulesResponseBodyFailedListResult = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The alert rules that failed to be created for the resource.
        self.failed_list_result = failed_list_result
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.failed_list_result:
            self.failed_list_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.failed_list_result is not None:
            result['FailedListResult'] = self.failed_list_result.to_map()

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

        if m.get('FailedListResult') is not None:
            temp_model = main_models.PutResourceMetricRulesResponseBodyFailedListResult()
            self.failed_list_result = temp_model.from_map(m.get('FailedListResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PutResourceMetricRulesResponseBodyFailedListResult(DaraModel):
    def __init__(
        self,
        target: List[main_models.PutResourceMetricRulesResponseBodyFailedListResultTarget] = None,
    ):
        self.target = target

    def validate(self):
        if self.target:
            for v1 in self.target:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Target'] = []
        if self.target is not None:
            for k1 in self.target:
                result['Target'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target = []
        if m.get('Target') is not None:
            for k1 in m.get('Target'):
                temp_model = main_models.PutResourceMetricRulesResponseBodyFailedListResultTarget()
                self.target.append(temp_model.from_map(k1))

        return self

class PutResourceMetricRulesResponseBodyFailedListResultTarget(DaraModel):
    def __init__(
        self,
        result: main_models.PutResourceMetricRulesResponseBodyFailedListResultTargetResult = None,
        rule_id: str = None,
    ):
        # The alert rule that failed to be created.
        self.result = result
        # The ID of the alert rule.
        self.rule_id = rule_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = main_models.PutResourceMetricRulesResponseBodyFailedListResultTargetResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class PutResourceMetricRulesResponseBodyFailedListResultTargetResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The error message returned.
        self.message = message
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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

