# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DeepCopyRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DeepCopyRuleResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DeepCopyRuleResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DeepCopyRuleResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        batch_copy_flag: bool = None,
        console_rule_id: int = None,
        rule_id: str = None,
        rule_version_id: int = None,
    ):
        # Whether to redirect to details
        self.batch_copy_flag = batch_copy_flag
        # Primary key of the policy
        self.console_rule_id = console_rule_id
        # Policy ID
        self.rule_id = rule_id
        # Primary key of the policy version
        self.rule_version_id = rule_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_copy_flag is not None:
            result['BatchCopyFlag'] = self.batch_copy_flag

        if self.console_rule_id is not None:
            result['ConsoleRuleId'] = self.console_rule_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_version_id is not None:
            result['RuleVersionId'] = self.rule_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchCopyFlag') is not None:
            self.batch_copy_flag = m.get('BatchCopyFlag')

        if m.get('ConsoleRuleId') is not None:
            self.console_rule_id = m.get('ConsoleRuleId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleVersionId') is not None:
            self.rule_version_id = m.get('RuleVersionId')

        return self

