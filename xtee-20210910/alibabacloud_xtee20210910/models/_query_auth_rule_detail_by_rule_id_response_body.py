# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class QueryAuthRuleDetailByRuleIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.QueryAuthRuleDetailByRuleIdResponseBodyResultObject = None,
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
            temp_model = main_models.QueryAuthRuleDetailByRuleIdResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class QueryAuthRuleDetailByRuleIdResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        audit_id: int = None,
        auth_type: str = None,
        auth_users: str = None,
        console_rule_id: int = None,
        event_code: str = None,
        event_name: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        logic_expression: str = None,
        memo: str = None,
        priority: int = None,
        rule_action_map: Dict[str, str] = None,
        rule_actions: str = None,
        rule_auth_type: str = None,
        rule_expressions: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_status: str = None,
        rule_type: str = None,
        rule_version_id: int = None,
        template_type: str = None,
        version: int = None,
    ):
        # Audit ID
        self.audit_id = audit_id
        # Authorization type
        self.auth_type = auth_type
        # Authorized user UID
        self.auth_users = auth_users
        # Primary key ID of the strategy
        self.console_rule_id = console_rule_id
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time
        self.gmt_modified = gmt_modified
        # Execution logic
        self.logic_expression = logic_expression
        # Description
        self.memo = memo
        # Rule priority, the higher the number, the higher the priority.
        self.priority = priority
        # Returned rule action structure.
        self.rule_action_map = rule_action_map
        # Output actions
        self.rule_actions = rule_actions
        # Rule authorization type
        self.rule_auth_type = rule_auth_type
        # Rule expressions.
        self.rule_expressions = rule_expressions
        # Strategy ID
        self.rule_id = rule_id
        # Strategy name
        self.rule_name = rule_name
        # Strategy status
        self.rule_status = rule_status
        # Rule type
        self.rule_type = rule_type
        # Primary key ID of the strategy version
        self.rule_version_id = rule_version_id
        # Template type
        self.template_type = template_type
        # Version number
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

        if self.auth_users is not None:
            result['authUsers'] = self.auth_users

        if self.console_rule_id is not None:
            result['consoleRuleId'] = self.console_rule_id

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

        if self.priority is not None:
            result['priority'] = self.priority

        if self.rule_action_map is not None:
            result['ruleActionMap'] = self.rule_action_map

        if self.rule_actions is not None:
            result['ruleActions'] = self.rule_actions

        if self.rule_auth_type is not None:
            result['ruleAuthType'] = self.rule_auth_type

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

        if self.template_type is not None:
            result['templateType'] = self.template_type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditId') is not None:
            self.audit_id = m.get('auditId')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('authUsers') is not None:
            self.auth_users = m.get('authUsers')

        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

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

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('ruleActionMap') is not None:
            self.rule_action_map = m.get('ruleActionMap')

        if m.get('ruleActions') is not None:
            self.rule_actions = m.get('ruleActions')

        if m.get('ruleAuthType') is not None:
            self.rule_auth_type = m.get('ruleAuthType')

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

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

