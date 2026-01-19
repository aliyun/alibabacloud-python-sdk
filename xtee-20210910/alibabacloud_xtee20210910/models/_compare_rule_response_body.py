# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class CompareRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.CompareRuleResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned object.
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
            temp_model = main_models.CompareRuleResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class CompareRuleResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        new_rule: main_models.CompareRuleResponseBodyResultObjectNewRule = None,
        old_rule: main_models.CompareRuleResponseBodyResultObjectOldRule = None,
    ):
        # New policy object.
        self.new_rule = new_rule
        # Old policy object.
        self.old_rule = old_rule

    def validate(self):
        if self.new_rule:
            self.new_rule.validate()
        if self.old_rule:
            self.old_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_rule is not None:
            result['newRule'] = self.new_rule.to_map()

        if self.old_rule is not None:
            result['oldRule'] = self.old_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newRule') is not None:
            temp_model = main_models.CompareRuleResponseBodyResultObjectNewRule()
            self.new_rule = temp_model.from_map(m.get('newRule'))

        if m.get('oldRule') is not None:
            temp_model = main_models.CompareRuleResponseBodyResultObjectOldRule()
            self.old_rule = temp_model.from_map(m.get('oldRule'))

        return self

class CompareRuleResponseBodyResultObjectOldRule(DaraModel):
    def __init__(
        self,
        audit_id: int = None,
        auth_type: str = None,
        console_rule_id: int = None,
        create_type: str = None,
        event_code: str = None,
        event_name: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        logic_expression: str = None,
        main_event_code: str = None,
        memo: str = None,
        rule_action_map: Dict[str, Any] = None,
        rule_actions: str = None,
        rule_auth_type: str = None,
        rule_body: str = None,
        rule_expressions: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_status: str = None,
        rule_type: str = None,
        rule_version_id: int = None,
        user_id: int = None,
        version: int = None,
    ):
        # Audit ID.
        self.audit_id = audit_id
        # Authorization type.
        self.auth_type = auth_type
        # Primary key ID of the policy.
        self.console_rule_id = console_rule_id
        # Creation type.
        self.create_type = create_type
        # Event code.
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Execution logic of the policy expression.
        self.logic_expression = logic_expression
        # Main event code.
        self.main_event_code = main_event_code
        # Description.
        self.memo = memo
        # Returned rule action structure. Returned when the policy type is DEFAULT.
        self.rule_action_map = rule_action_map
        # Policy execution output actions. Returned when the policy type is DEFAULT.
        self.rule_actions = rule_actions
        # Policy authorization type.
        self.rule_auth_type = rule_auth_type
        # DSL policy execution logic. Returned when the policy type is DSL.
        self.rule_body = rule_body
        # Policy expression. Returned when the policy type is DEFAULT.
        self.rule_expressions = rule_expressions
        # Policy ID.
        self.rule_id = rule_id
        # Policy name.
        self.rule_name = rule_name
        # Policy status.
        self.rule_status = rule_status
        # Policy type.
        self.rule_type = rule_type
        # Primary key ID of the policy version.
        self.rule_version_id = rule_version_id
        # User UID.
        self.user_id = user_id
        # Version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_id is not None:
            result['auditId'] = self.audit_id

        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.console_rule_id is not None:
            result['consoleRuleId'] = self.console_rule_id

        if self.create_type is not None:
            result['createType'] = self.create_type

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

        if self.main_event_code is not None:
            result['mainEventCode'] = self.main_event_code

        if self.memo is not None:
            result['memo'] = self.memo

        if self.rule_action_map is not None:
            result['ruleActionMap'] = self.rule_action_map

        if self.rule_actions is not None:
            result['ruleActions'] = self.rule_actions

        if self.rule_auth_type is not None:
            result['ruleAuthType'] = self.rule_auth_type

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

        if self.rule_version_id is not None:
            result['ruleVersionId'] = self.rule_version_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditId') is not None:
            self.audit_id = m.get('auditId')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

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

        if m.get('mainEventCode') is not None:
            self.main_event_code = m.get('mainEventCode')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('ruleActionMap') is not None:
            self.rule_action_map = m.get('ruleActionMap')

        if m.get('ruleActions') is not None:
            self.rule_actions = m.get('ruleActions')

        if m.get('ruleAuthType') is not None:
            self.rule_auth_type = m.get('ruleAuthType')

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

        if m.get('ruleVersionId') is not None:
            self.rule_version_id = m.get('ruleVersionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class CompareRuleResponseBodyResultObjectNewRule(DaraModel):
    def __init__(
        self,
        audit_id: int = None,
        auth_type: str = None,
        console_rule_id: int = None,
        create_type: str = None,
        event_code: str = None,
        event_name: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        logic_expression: str = None,
        main_event_code: str = None,
        memo: str = None,
        rule_action_map: Dict[str, Any] = None,
        rule_actions: str = None,
        rule_auth_type: str = None,
        rule_body: str = None,
        rule_expressions: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_status: str = None,
        rule_type: str = None,
        rule_version_id: int = None,
        user_id: int = None,
        version: int = None,
    ):
        # Audit ID.
        self.audit_id = audit_id
        # Authorization type.
        self.auth_type = auth_type
        # Primary key ID of the rule.
        self.console_rule_id = console_rule_id
        # Creation type.
        self.create_type = create_type
        # Event code.
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Logic of the rule expression execution.
        self.logic_expression = logic_expression
        # Main event code.
        self.main_event_code = main_event_code
        # Memo.
        self.memo = memo
        # Returned rule action structure. Returned when the policy type is DEFAULT.
        self.rule_action_map = rule_action_map
        # Output actions of the rule execution. Returned when the rule type is DEFAULT.
        self.rule_actions = rule_actions
        # Authorization type of the rule.
        self.rule_auth_type = rule_auth_type
        # DSL logic for rule execution. Returned when the rule type is DSL.
        self.rule_body = rule_body
        # Policy expressions. Returned when the policy type is DEFAULT.
        self.rule_expressions = rule_expressions
        # Rule ID.
        self.rule_id = rule_id
        # Rule name.
        self.rule_name = rule_name
        # Policy status.
        self.rule_status = rule_status
        # Rule type.
        self.rule_type = rule_type
        # Primary key ID of the rule version.
        self.rule_version_id = rule_version_id
        # User UID.
        self.user_id = user_id
        # Version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_id is not None:
            result['auditId'] = self.audit_id

        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.console_rule_id is not None:
            result['consoleRuleId'] = self.console_rule_id

        if self.create_type is not None:
            result['createType'] = self.create_type

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

        if self.main_event_code is not None:
            result['mainEventCode'] = self.main_event_code

        if self.memo is not None:
            result['memo'] = self.memo

        if self.rule_action_map is not None:
            result['ruleActionMap'] = self.rule_action_map

        if self.rule_actions is not None:
            result['ruleActions'] = self.rule_actions

        if self.rule_auth_type is not None:
            result['ruleAuthType'] = self.rule_auth_type

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

        if self.rule_version_id is not None:
            result['ruleVersionId'] = self.rule_version_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditId') is not None:
            self.audit_id = m.get('auditId')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

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

        if m.get('mainEventCode') is not None:
            self.main_event_code = m.get('mainEventCode')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('ruleActionMap') is not None:
            self.rule_action_map = m.get('ruleActionMap')

        if m.get('ruleActions') is not None:
            self.rule_actions = m.get('ruleActions')

        if m.get('ruleAuthType') is not None:
            self.rule_auth_type = m.get('ruleAuthType')

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

        if m.get('ruleVersionId') is not None:
            self.rule_version_id = m.get('ruleVersionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

