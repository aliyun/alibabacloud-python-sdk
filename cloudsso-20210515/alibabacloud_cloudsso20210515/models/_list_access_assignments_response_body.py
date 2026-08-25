# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListAccessAssignmentsResponseBody(DaraModel):
    def __init__(
        self,
        access_assignments: List[main_models.ListAccessAssignmentsResponseBodyAccessAssignments] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # The access permissions that are assigned.
        self.access_assignments = access_assignments
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # - true
        # 
        # - false
        self.is_truncated = is_truncated
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        # 
        # > This parameter is returned only when the value of IsTruncated is `true`.\\`\\`
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_counts = total_counts

    def validate(self):
        if self.access_assignments:
            for v1 in self.access_assignments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessAssignments'] = []
        if self.access_assignments is not None:
            for k1 in self.access_assignments:
                result['AccessAssignments'].append(k1.to_map() if k1 else None)

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_assignments = []
        if m.get('AccessAssignments') is not None:
            for k1 in m.get('AccessAssignments'):
                temp_model = main_models.ListAccessAssignmentsResponseBodyAccessAssignments()
                self.access_assignments.append(temp_model.from_map(k1))

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ListAccessAssignmentsResponseBodyAccessAssignments(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        create_time: str = None,
        origin_target_id: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
    ):
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The time when the access permissions were assigned.
        self.create_time = create_time
        self.origin_target_id = origin_target_id
        # The ID of the CloudSSO identity.
        self.principal_id = principal_id
        # The name of the CloudSSO identity.
        self.principal_name = principal_name
        # The type of the CloudSSO identity. Valid values:
        # 
        # - User
        # 
        # - Group
        self.principal_type = principal_type
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object.
        # 
        # The value is fixed as RD-Account, which indicates the accounts in the resource directory.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id

        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.origin_target_id is not None:
            result['OriginTargetId'] = self.origin_target_id

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('OriginTargetId') is not None:
            self.origin_target_id = m.get('OriginTargetId')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

