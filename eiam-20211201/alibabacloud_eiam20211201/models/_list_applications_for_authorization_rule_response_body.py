# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsForAuthorizationRuleResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListApplicationsForAuthorizationRuleResponseBodyApplications] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of applications.
        self.applications = applications
        # The number of entries per page in a paging query.
        self.max_results = max_results
        # The pagination token returned in this call. Use this token for the next paged query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the list.
        self.total_count = total_count

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

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
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListApplicationsForAuthorizationRuleResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationsForAuthorizationRuleResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        instance_id: str = None,
        validity_period: main_models.ListApplicationsForAuthorizationRuleResponseBodyApplicationsValidityPeriod = None,
        validity_type: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The instance ID.
        self.instance_id = instance_id
        # The time range of the validity period. This parameter takes effect only when ValidityType is set to time_bound.
        self.validity_period = validity_period
        # The validity type of the association. Valid values:
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.validity_period is not None:
            result['ValidityPeriod'] = self.validity_period.to_map()

        if self.validity_type is not None:
            result['ValidityType'] = self.validity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ValidityPeriod') is not None:
            temp_model = main_models.ListApplicationsForAuthorizationRuleResponseBodyApplicationsValidityPeriod()
            self.validity_period = temp_model.from_map(m.get('ValidityPeriod'))

        if m.get('ValidityType') is not None:
            self.validity_type = m.get('ValidityType')

        return self

class ListApplicationsForAuthorizationRuleResponseBodyApplicationsValidityPeriod(DaraModel):
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

