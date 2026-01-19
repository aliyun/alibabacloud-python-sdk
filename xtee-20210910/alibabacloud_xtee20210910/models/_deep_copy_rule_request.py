# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeepCopyRuleRequest(DaraModel):
    def __init__(
        self,
        create_type: str = None,
        cust_insert_info: str = None,
        cust_write_info: str = None,
        expression_variable_info: str = None,
        lang: str = None,
        query_expression_variable_info: str = None,
        reg_id: str = None,
        source_rule_id: str = None,
        source_rule_ids: str = None,
        target_event_code: str = None,
        target_event_name: str = None,
    ):
        # Creation type
        self.create_type = create_type
        # Newly added cumulative variable
        self.cust_insert_info = cust_insert_info
        # Read cumulative variable
        self.cust_write_info = cust_write_info
        # Custom variables to be added
        self.expression_variable_info = expression_variable_info
        # Sets the language type for requests and received messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Custom query variables to be added
        self.query_expression_variable_info = query_expression_variable_info
        # Region code
        self.reg_id = reg_id
        # Source policy ID
        self.source_rule_id = source_rule_id
        # Target policy ID
        self.source_rule_ids = source_rule_ids
        # Target event
        self.target_event_code = target_event_code
        # Target event name
        self.target_event_name = target_event_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_type is not None:
            result['CreateType'] = self.create_type

        if self.cust_insert_info is not None:
            result['CustInsertInfo'] = self.cust_insert_info

        if self.cust_write_info is not None:
            result['CustWriteInfo'] = self.cust_write_info

        if self.expression_variable_info is not None:
            result['ExpressionVariableInfo'] = self.expression_variable_info

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.query_expression_variable_info is not None:
            result['QueryExpressionVariableInfo'] = self.query_expression_variable_info

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.source_rule_id is not None:
            result['SourceRuleId'] = self.source_rule_id

        if self.source_rule_ids is not None:
            result['SourceRuleIds'] = self.source_rule_ids

        if self.target_event_code is not None:
            result['TargetEventCode'] = self.target_event_code

        if self.target_event_name is not None:
            result['TargetEventName'] = self.target_event_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')

        if m.get('CustInsertInfo') is not None:
            self.cust_insert_info = m.get('CustInsertInfo')

        if m.get('CustWriteInfo') is not None:
            self.cust_write_info = m.get('CustWriteInfo')

        if m.get('ExpressionVariableInfo') is not None:
            self.expression_variable_info = m.get('ExpressionVariableInfo')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('QueryExpressionVariableInfo') is not None:
            self.query_expression_variable_info = m.get('QueryExpressionVariableInfo')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('SourceRuleId') is not None:
            self.source_rule_id = m.get('SourceRuleId')

        if m.get('SourceRuleIds') is not None:
            self.source_rule_ids = m.get('SourceRuleIds')

        if m.get('TargetEventCode') is not None:
            self.target_event_code = m.get('TargetEventCode')

        if m.get('TargetEventName') is not None:
            self.target_event_name = m.get('TargetEventName')

        return self

