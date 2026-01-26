# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateSilencePolicyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        silence_policy: main_models.CreateOrUpdateSilencePolicyResponseBodySilencePolicy = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The silence policy.
        self.silence_policy = silence_policy

    def validate(self):
        if self.silence_policy:
            self.silence_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.silence_policy is not None:
            result['SilencePolicy'] = self.silence_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SilencePolicy') is not None:
            temp_model = main_models.CreateOrUpdateSilencePolicyResponseBodySilencePolicy()
            self.silence_policy = temp_model.from_map(m.get('SilencePolicy'))

        return self

class CreateOrUpdateSilencePolicyResponseBodySilencePolicy(DaraModel):
    def __init__(
        self,
        effective_time_type: str = None,
        id: int = None,
        matching_rules: List[main_models.CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules] = None,
        name: str = None,
        state: str = None,
        time_period: str = None,
        time_slots: str = None,
    ):
        # The effective type. Valid values: PERMANENT: The policy is effective permanently. CYCLE_EFFECT: The policy is effective cyclically. CUSTOM_TIME: The policy is effective during a custom time period.
        self.effective_time_type = effective_time_type
        # The ID of the silence policy.
        self.id = id
        # A list of matching rules.
        self.matching_rules = matching_rules
        # The name of the silence policy.
        self.name = name
        # Specifies whether to enable the silence policy. Valid values: enable and disable.
        self.state = state
        # Effective period. Valid values: DAY: daily WEEK: weekly
        self.time_period = time_period
        # The time period during which the silence policy is effective.
        self.time_slots = time_slots

    def validate(self):
        if self.matching_rules:
            for v1 in self.matching_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_time_type is not None:
            result['EffectiveTimeType'] = self.effective_time_type

        if self.id is not None:
            result['Id'] = self.id

        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k1 in self.matching_rules:
                result['MatchingRules'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.state is not None:
            result['State'] = self.state

        if self.time_period is not None:
            result['TimePeriod'] = self.time_period

        if self.time_slots is not None:
            result['TimeSlots'] = self.time_slots

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveTimeType') is not None:
            self.effective_time_type = m.get('EffectiveTimeType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k1 in m.get('MatchingRules'):
                temp_model = main_models.CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules()
                self.matching_rules.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TimePeriod') is not None:
            self.time_period = m.get('TimePeriod')

        if m.get('TimeSlots') is not None:
            self.time_slots = m.get('TimeSlots')

        return self

class CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules(DaraModel):
    def __init__(
        self,
        matching_conditions: List[main_models.CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions] = None,
    ):
        # A list of matching conditions.
        self.matching_conditions = matching_conditions

    def validate(self):
        if self.matching_conditions:
            for v1 in self.matching_conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k1 in self.matching_conditions:
                result['MatchingConditions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k1 in m.get('MatchingConditions'):
                temp_model = main_models.CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k1))

        return self

class CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The key of the matching condition.
        self.key = key
        # The logical operator of the matching condition. Valid values:
        # 
        # *   `eq`: equal to
        # *   `neq`: not equal to
        # *   `in`: contains
        # *   `nin`: does not contain
        # *   `re`: regular expression match
        # *   `nre`: regular expression mismatch
        self.operator = operator
        # The value of the matching condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

