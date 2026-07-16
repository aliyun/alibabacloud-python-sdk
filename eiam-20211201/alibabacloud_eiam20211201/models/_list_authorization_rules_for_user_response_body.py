# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizationRulesForUserResponseBody(DaraModel):
    def __init__(
        self,
        authorization_rules: List[main_models.ListAuthorizationRulesForUserResponseBodyAuthorizationRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of authorization rules.
        self.authorization_rules = authorization_rules
        # The maximum number of entries per page in a paged query. This parameter indicates the paging size.
        self.max_results = max_results
        # The pagination token returned in this call. Use this token to query the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
                temp_model = main_models.ListAuthorizationRulesForUserResponseBodyAuthorizationRules()
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

class ListAuthorizationRulesForUserResponseBodyAuthorizationRules(DaraModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        instance_id: str = None,
        validity_period: main_models.ListAuthorizationRulesForUserResponseBodyAuthorizationRulesValidityPeriod = None,
        validity_type: str = None,
    ):
        # The authorization rule ID.
        self.authorization_rule_id = authorization_rule_id
        # The instance ID.
        self.instance_id = instance_id
        # The time range of the validity period. This parameter takes effect only when ValidityType is set to time_bound.
        self.validity_period = validity_period
        # The validity type of the relationship. Valid values:
        # - permanent: permanent
        # - time_bound: custom time range.
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
            temp_model = main_models.ListAuthorizationRulesForUserResponseBodyAuthorizationRulesValidityPeriod()
            self.validity_period = temp_model.from_map(m.get('ValidityPeriod'))

        if m.get('ValidityType') is not None:
            self.validity_type = m.get('ValidityType')

        return self

class ListAuthorizationRulesForUserResponseBodyAuthorizationRulesValidityPeriod(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end time of the validity period, in UNIX timestamp format. Unit: milliseconds.
        self.end_time = end_time
        # The start time of the validity period, in UNIX timestamp format. Unit: milliseconds.
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

