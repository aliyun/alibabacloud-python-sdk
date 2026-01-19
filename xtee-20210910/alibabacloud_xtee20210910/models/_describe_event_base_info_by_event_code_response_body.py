# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventBaseInfoByEventCodeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeEventBaseInfoByEventCodeResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
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
            temp_model = main_models.DescribeEventBaseInfoByEventCodeResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeEventBaseInfoByEventCodeResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_version: int = None,
        event_code: str = None,
        event_name: str = None,
        event_stauts: str = None,
        input_fields: List[main_models.DescribeEventBaseInfoByEventCodeResponseBodyResultObjectInputFields] = None,
        memo: str = None,
        rule_details: List[main_models.DescribeEventBaseInfoByEventCodeResponseBodyResultObjectRuleDetails] = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # Business version number
        self.biz_version = biz_version
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Event status.
        self.event_stauts = event_stauts
        # Field list.
        self.input_fields = input_fields
        # Memo.
        self.memo = memo
        # Policy Information
        self.rule_details = rule_details
        # Operation template code
        self.template_code = template_code
        # Template name
        self.template_name = template_name
        # Template type.
        self.template_type = template_type

    def validate(self):
        if self.input_fields:
            for v1 in self.input_fields:
                 if v1:
                    v1.validate()
        if self.rule_details:
            for v1 in self.rule_details:
                 if v1:
                    v1.validate()

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

        if self.event_stauts is not None:
            result['eventStauts'] = self.event_stauts

        result['inputFields'] = []
        if self.input_fields is not None:
            for k1 in self.input_fields:
                result['inputFields'].append(k1.to_map() if k1 else None)

        if self.memo is not None:
            result['memo'] = self.memo

        result['ruleDetails'] = []
        if self.rule_details is not None:
            for k1 in self.rule_details:
                result['ruleDetails'].append(k1.to_map() if k1 else None)

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.template_type is not None:
            result['templateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizVersion') is not None:
            self.biz_version = m.get('bizVersion')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('eventStauts') is not None:
            self.event_stauts = m.get('eventStauts')

        self.input_fields = []
        if m.get('inputFields') is not None:
            for k1 in m.get('inputFields'):
                temp_model = main_models.DescribeEventBaseInfoByEventCodeResponseBodyResultObjectInputFields()
                self.input_fields.append(temp_model.from_map(k1))

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        self.rule_details = []
        if m.get('ruleDetails') is not None:
            for k1 in m.get('ruleDetails'):
                temp_model = main_models.DescribeEventBaseInfoByEventCodeResponseBodyResultObjectRuleDetails()
                self.rule_details.append(temp_model.from_map(k1))

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        return self

class DescribeEventBaseInfoByEventCodeResponseBodyResultObjectRuleDetails(DaraModel):
    def __init__(
        self,
        logic_expression: str = None,
        memo: str = None,
        rule_actions: str = None,
        rule_auth_type: str = None,
        rule_expressions: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_status: str = None,
    ):
        # Policy Execution Logic
        self.logic_expression = logic_expression
        # Memo
        self.memo = memo
        # Rule Actions
        self.rule_actions = rule_actions
        # Policy Type
        self.rule_auth_type = rule_auth_type
        # Event Expressions.
        self.rule_expressions = rule_expressions
        # Policy ID
        self.rule_id = rule_id
        # Policy Name
        self.rule_name = rule_name
        # Policy Status
        self.rule_status = rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logic_expression is not None:
            result['logicExpression'] = self.logic_expression

        if self.memo is not None:
            result['memo'] = self.memo

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logicExpression') is not None:
            self.logic_expression = m.get('logicExpression')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

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

        return self

class DescribeEventBaseInfoByEventCodeResponseBodyResultObjectInputFields(DaraModel):
    def __init__(
        self,
        description: str = None,
        field_code: str = None,
        field_rank: str = None,
        field_source: str = None,
        field_type: str = None,
        title: str = None,
    ):
        # Field description.
        self.description = description
        # Field code
        self.field_code = field_code
        # Field ranking
        self.field_rank = field_rank
        # Field source.
        self.field_source = field_source
        # Field type.
        self.field_type = field_type
        # Field name.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.field_code is not None:
            result['fieldCode'] = self.field_code

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('fieldCode') is not None:
            self.field_code = m.get('fieldCode')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

