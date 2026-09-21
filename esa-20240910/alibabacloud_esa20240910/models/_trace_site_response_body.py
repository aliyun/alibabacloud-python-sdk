# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class TraceSiteResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status_code: int = None,
        success: bool = None,
        trace: List[main_models.TraceSiteResponseBodyTrace] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The HTTP status code of the request.
        self.status_code = status_code
        # Indicates whether the request was successful.
        self.success = success
        # The trace information of the call chain.
        self.trace = trace

    def validate(self):
        if self.trace:
            for v1 in self.trace:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.success is not None:
            result['Success'] = self.success

        result['Trace'] = []
        if self.trace is not None:
            for k1 in self.trace:
                result['Trace'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.trace = []
        if m.get('Trace') is not None:
            for k1 in m.get('Trace'):
                temp_model = main_models.TraceSiteResponseBodyTrace()
                self.trace.append(temp_model.from_map(k1))

        return self

class TraceSiteResponseBodyTrace(DaraModel):
    def __init__(
        self,
        matched: bool = None,
        step_module_name: str = None,
        trace: List[main_models.TraceSiteResponseBodyTraceTrace] = None,
    ):
        # Indicates whether the module is matched. Valid values: true and false.
        self.matched = matched
        # The feature module.
        self.step_module_name = step_module_name
        # The matching results of rules in the feature module.
        self.trace = trace

    def validate(self):
        if self.trace:
            for v1 in self.trace:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.matched is not None:
            result['Matched'] = self.matched

        if self.step_module_name is not None:
            result['StepModuleName'] = self.step_module_name

        result['Trace'] = []
        if self.trace is not None:
            for k1 in self.trace:
                result['Trace'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Matched') is not None:
            self.matched = m.get('Matched')

        if m.get('StepModuleName') is not None:
            self.step_module_name = m.get('StepModuleName')

        self.trace = []
        if m.get('Trace') is not None:
            for k1 in m.get('Trace'):
                temp_model = main_models.TraceSiteResponseBodyTraceTrace()
                self.trace.append(temp_model.from_map(k1))

        return self

class TraceSiteResponseBodyTraceTrace(DaraModel):
    def __init__(
        self,
        action: str = None,
        config_type: str = None,
        ddos_level_domestic: str = None,
        ddos_level_oversea: str = None,
        env_name: str = None,
        expression: str = None,
        level: str = None,
        load_balancer_name: str = None,
        origin_pool_name: str = None,
        routine_id: str = None,
        rule_id: int = None,
        rule_name: str = None,
        site_version: int = None,
        type: str = None,
        value: str = None,
    ):
        # The action to perform.
        self.action = action
        # The configuration type.
        self.config_type = config_type
        # The mitigation capability (China).
        self.ddos_level_domestic = ddos_level_domestic
        # The mitigation capability (global, excluding China).
        self.ddos_level_oversea = ddos_level_oversea
        # The environment.
        self.env_name = env_name
        # The rule expression.
        self.expression = expression
        # The mitigation capability.
        self.level = level
        # The load balancer domain name.
        self.load_balancer_name = load_balancer_name
        # The name of the origin pool.
        self.origin_pool_name = origin_pool_name
        # The routine ID.
        self.routine_id = routine_id
        # The security rule ID.
        self.rule_id = rule_id
        # The name of the matched rule.
        self.rule_name = rule_name
        # The version.
        self.site_version = site_version
        # The security-related rule type.
        self.type = type
        # The value specified in the IP access rule.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.ddos_level_domestic is not None:
            result['DdosLevelDomestic'] = self.ddos_level_domestic

        if self.ddos_level_oversea is not None:
            result['DdosLevelOversea'] = self.ddos_level_oversea

        if self.env_name is not None:
            result['EnvName'] = self.env_name

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.level is not None:
            result['Level'] = self.level

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.origin_pool_name is not None:
            result['OriginPoolName'] = self.origin_pool_name

        if self.routine_id is not None:
            result['RoutineId'] = self.routine_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('DdosLevelDomestic') is not None:
            self.ddos_level_domestic = m.get('DdosLevelDomestic')

        if m.get('DdosLevelOversea') is not None:
            self.ddos_level_oversea = m.get('DdosLevelOversea')

        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('OriginPoolName') is not None:
            self.origin_pool_name = m.get('OriginPoolName')

        if m.get('RoutineId') is not None:
            self.routine_id = m.get('RoutineId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

