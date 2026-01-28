# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizationRulesForGroupResponseBody(DaraModel):
    def __init__(
        self,
        authorization_rules: List[main_models.ListAuthorizationRulesForGroupResponseBodyAuthorizationRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authorization_rules = authorization_rules
        # 分页查询时每页行数。
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authorization_rules:
            for v1 in self.authorization_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizationRules'] = []
        if self.authorization_rules is not None:
            for k1 in self.authorization_rules:
                result['AuthorizationRules'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorization_rules = []
        if m.get('AuthorizationRules') is not None:
            for k1 in m.get('AuthorizationRules'):
                temp_model = main_models.ListAuthorizationRulesForGroupResponseBodyAuthorizationRules()
                self.authorization_rules.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAuthorizationRulesForGroupResponseBodyAuthorizationRules(DaraModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        instance_id: str = None,
        validity_period: main_models.ListAuthorizationRulesForGroupResponseBodyAuthorizationRulesValidityPeriod = None,
        validity_type: str = None,
    ):
        # 授权规则标识。
        self.authorization_rule_id = authorization_rule_id
        # 实例ID。
        self.instance_id = instance_id
        # 有效周期。
        self.validity_period = validity_period
        # 有效期类型，枚举值：permanent（永久），time_bound（自定义时间范围）。
        self.validity_type = validity_type

    def validate(self):
        if self.validity_period:
            self.validity_period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.validity_period is not None:
            result['ValidityPeriod'] = self.validity_period.to_map()

        if self.validity_type is not None:
            result['ValidityType'] = self.validity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ValidityPeriod') is not None:
            temp_model = main_models.ListAuthorizationRulesForGroupResponseBodyAuthorizationRulesValidityPeriod()
            self.validity_period = temp_model.from_map(m.get('ValidityPeriod'))

        if m.get('ValidityType') is not None:
            self.validity_type = m.get('ValidityType')

        return self

class ListAuthorizationRulesForGroupResponseBodyAuthorizationRulesValidityPeriod(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # 授权生效结束时间。
        self.end_time = end_time
        # 授权生效开始时间。
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

