# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceRegistrationsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_registrations: List[main_models.ListServiceRegistrationsResponseBodyServiceRegistrations] = None,
        total_count: int = None,
    ):
        # Number of items per page in a paginated query. The maximum is 100, and the default is 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # Service registration information.
        self.service_registrations = service_registrations
        # Total number of records that meet the criteria.
        self.total_count = total_count

    def validate(self):
        if self.service_registrations:
            for v1 in self.service_registrations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServiceRegistrations'] = []
        if self.service_registrations is not None:
            for k1 in self.service_registrations:
                result['ServiceRegistrations'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.service_registrations = []
        if m.get('ServiceRegistrations') is not None:
            for k1 in m.get('ServiceRegistrations'):
                temp_model = main_models.ListServiceRegistrationsResponseBodyServiceRegistrations()
                self.service_registrations.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServiceRegistrationsResponseBodyServiceRegistrations(DaraModel):
    def __init__(
        self,
        comment: str = None,
        finish_time: str = None,
        registration_id: str = None,
        service_id: str = None,
        status: str = None,
        submit_time: str = None,
    ):
        # Comment.
        self.comment = comment
        # Finish time.
        self.finish_time = finish_time
        # Registration ID.
        self.registration_id = registration_id
        # Service ID.
        self.service_id = service_id
        # Registration status. Allowed values:
        # 
        # - Submitted
        # 
        # - Approved
        # 
        # - Rejected
        # 
        # - Canceled
        # 
        # - Executed
        # 
        # - Executed: Executed.
        self.status = status
        # Submit time.
        self.submit_time = submit_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        return self

