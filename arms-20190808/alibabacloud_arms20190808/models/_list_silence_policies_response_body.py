# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListSilencePoliciesResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.ListSilencePoliciesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned pages.
        self.page_bean = page_bean
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.ListSilencePoliciesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSilencePoliciesResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        page: int = None,
        silence_policies: List[main_models.ListSilencePoliciesResponseBodyPageBeanSilencePolicies] = None,
        size: int = None,
        total: int = None,
    ):
        # The number of the page returned.
        self.page = page
        # The queried silence policies.
        self.silence_policies = silence_policies
        # The number of entries returned per page.
        self.size = size
        # The number of silence policies that were returned.
        self.total = total

    def validate(self):
        if self.silence_policies:
            for v1 in self.silence_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        result['SilencePolicies'] = []
        if self.silence_policies is not None:
            for k1 in self.silence_policies:
                result['SilencePolicies'].append(k1.to_map() if k1 else None)

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        self.silence_policies = []
        if m.get('SilencePolicies') is not None:
            for k1 in m.get('SilencePolicies'):
                temp_model = main_models.ListSilencePoliciesResponseBodyPageBeanSilencePolicies()
                self.silence_policies.append(temp_model.from_map(k1))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSilencePoliciesResponseBodyPageBeanSilencePolicies(DaraModel):
    def __init__(
        self,
        effective_time_type: str = None,
        id: int = None,
        matching_rules: List[main_models.ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules] = None,
        name: str = None,
        state: str = None,
        time_period: str = None,
        time_slots: str = None,
    ):
        # The effective type. Valid values: PERMANENT: The policy is effective permanently. CYCLE_EFFECT: The policy is effective cyclically. CUSTOM_TIME: The policy is effective during a custom time period.
        self.effective_time_type = effective_time_type
        # The ID of the silence policy.
        self.id = id
        # The matching rules.
        self.matching_rules = matching_rules
        # The name of the silence policy.
        self.name = name
        # Indicates whether the silence policy is enabled. Valid values: enable and disable.
        self.state = state
        # The effective time. Valid values: WEEK: weekly DAY: daily
        self.time_period = time_period
        # Effective period.
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
                temp_model = main_models.ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules()
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

class ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules(DaraModel):
    def __init__(
        self,
        matching_conditions: List[main_models.ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions] = None,
    ):
        # The matching conditions.
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
                temp_model = main_models.ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k1))

        return self

class ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions(DaraModel):
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

