# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ActiveAggregateConfigRulesResponseBody(DaraModel):
    def __init__(
        self,
        operate_rule_result: main_models.ActiveAggregateConfigRulesResponseBodyOperateRuleResult = None,
        request_id: str = None,
    ):
        # The results of the operations.
        self.operate_rule_result = operate_rule_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateRuleResult') is not None:
            temp_model = main_models.ActiveAggregateConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m.get('OperateRuleResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ActiveAggregateConfigRulesResponseBodyOperateRuleResult(DaraModel):
    def __init__(
        self,
        operate_rule_item_list: List[main_models.ActiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        # The result information about the operation.
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for v1 in self.operate_rule_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k1 in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k1 in m.get('OperateRuleItemList'):
                temp_model = main_models.ActiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k1))

        return self



class ActiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(DaraModel):
    def __init__(
        self,
        config_rule_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        # The rule ID.
        self.config_rule_id = config_rule_id
        # The error code.
        self.error_code = error_code
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
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

