# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeRuleSnapshotResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeRuleSnapshotResponseBodyResultObject = None,
    ):
        # Request ID
        self.request_id = request_id
        # Returned object
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
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeRuleSnapshotResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeRuleSnapshotResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_version: str = None,
        event_code: str = None,
        event_name: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        logic_expression: str = None,
        memo: str = None,
        rule_actions: str = None,
        rule_body: str = None,
        rule_expressions: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_status: str = None,
        rule_type: str = None,
    ):
        # Business version.
        self.biz_version = biz_version
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Expression for analysis results.
        self.logic_expression = logic_expression
        # Memo.
        self.memo = memo
        # Rule actions.
        self.rule_actions = rule_actions
        # DSL rule expression. This field is required when ruleType is DSL.
        self.rule_body = rule_body
        # Expression.
        self.rule_expressions = rule_expressions
        # Policy ID
        self.rule_id = rule_id
        # Policy name
        self.rule_name = rule_name
        # Policy status
        self.rule_status = rule_status
        # Rule type.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_version is not None:
            result['bizVersion'] = self.biz_version

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.logic_expression is not None:
            result['logicExpression'] = self.logic_expression

        if self.memo is not None:
            result['memo'] = self.memo

        if self.rule_actions is not None:
            result['ruleActions'] = self.rule_actions

        if self.rule_body is not None:
            result['ruleBody'] = self.rule_body

        if self.rule_expressions is not None:
            result['ruleExpressions'] = self.rule_expressions

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        if self.rule_type is not None:
            result['ruleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizVersion') is not None:
            self.biz_version = m.get('bizVersion')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('logicExpression') is not None:
            self.logic_expression = m.get('logicExpression')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('ruleActions') is not None:
            self.rule_actions = m.get('ruleActions')

        if m.get('ruleBody') is not None:
            self.rule_body = m.get('ruleBody')

        if m.get('ruleExpressions') is not None:
            self.rule_expressions = m.get('ruleExpressions')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')

        return self

