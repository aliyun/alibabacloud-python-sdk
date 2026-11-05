# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListApplicationAssignmentsResponseBody(DaraModel):
    def __init__(
        self,
        application_assignment: main_models.ListApplicationAssignmentsResponseBodyApplicationAssignment = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.application_assignment = application_assignment
        # The maximum number of items per page.
        self.max_results = max_results
        # This parameter is returned only when the response is truncated. To retrieve the remaining content in subsequent API calls, use the NextToken value.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application_assignment:
            self.application_assignment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_assignment is not None:
            result['ApplicationAssignment'] = self.application_assignment.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationAssignment') is not None:
            temp_model = main_models.ListApplicationAssignmentsResponseBodyApplicationAssignment()
            self.application_assignment = temp_model.from_map(m.get('ApplicationAssignment'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListApplicationAssignmentsResponseBodyApplicationAssignment(DaraModel):
    def __init__(
        self,
        application_assignment_info: List[main_models.ListApplicationAssignmentsResponseBodyApplicationAssignmentApplicationAssignmentInfo] = None,
    ):
        self.application_assignment_info = application_assignment_info

    def validate(self):
        if self.application_assignment_info:
            for v1 in self.application_assignment_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationAssignmentInfo'] = []
        if self.application_assignment_info is not None:
            for k1 in self.application_assignment_info:
                result['ApplicationAssignmentInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_assignment_info = []
        if m.get('ApplicationAssignmentInfo') is not None:
            for k1 in m.get('ApplicationAssignmentInfo'):
                temp_model = main_models.ListApplicationAssignmentsResponseBodyApplicationAssignmentApplicationAssignmentInfo()
                self.application_assignment_info.append(temp_model.from_map(k1))

        return self

class ListApplicationAssignmentsResponseBodyApplicationAssignmentApplicationAssignmentInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: str = None,
        principal_name: str = None,
        principal_type: str = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.principal_name = principal_name
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

