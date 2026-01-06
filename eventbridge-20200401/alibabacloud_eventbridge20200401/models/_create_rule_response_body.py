# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
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
            temp_model = main_models.CreateRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        rule_arn: str = None,
    ):
        # The ARN of the event rule. The ARN is used for authorization.
        self.rule_arn = rule_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')

        return self

