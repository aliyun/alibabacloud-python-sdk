# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class QueryAutoShutdownPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        auto_shutdown_policies: List[main_models.QueryAutoShutdownPoliciesResponseBodyAutoShutdownPolicies] = None,
        request_id: str = None,
    ):
        self.auto_shutdown_policies = auto_shutdown_policies
        self.request_id = request_id

    def validate(self):
        if self.auto_shutdown_policies:
            for v1 in self.auto_shutdown_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoShutdownPolicies'] = []
        if self.auto_shutdown_policies is not None:
            for k1 in self.auto_shutdown_policies:
                result['AutoShutdownPolicies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_shutdown_policies = []
        if m.get('AutoShutdownPolicies') is not None:
            for k1 in m.get('AutoShutdownPolicies'):
                temp_model = main_models.QueryAutoShutdownPoliciesResponseBodyAutoShutdownPolicies()
                self.auto_shutdown_policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryAutoShutdownPoliciesResponseBodyAutoShutdownPolicies(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.QueryAutoShutdownPoliciesResponseBodyAutoShutdownPoliciesConditions] = None,
        context: Dict[str, Any] = None,
        expression: str = None,
        instance_id: str = None,
        source_type: str = None,
    ):
        self.conditions = conditions
        self.context = context
        self.expression = expression
        self.instance_id = instance_id
        self.source_type = source_type

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.context is not None:
            result['Context'] = self.context

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.QueryAutoShutdownPoliciesResponseBodyAutoShutdownPoliciesConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class QueryAutoShutdownPoliciesResponseBodyAutoShutdownPoliciesConditions(DaraModel):
    def __init__(
        self,
        context: Dict[str, Any] = None,
        expression: str = None,
        source_type: str = None,
    ):
        self.context = context
        self.expression = expression
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

