# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListCrossProjectDeploymentCandidatesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListCrossProjectDeploymentCandidatesResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business response.
        self.data = data
        # The request ID, which is used to locate and troubleshoot this API call.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListCrossProjectDeploymentCandidatesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCrossProjectDeploymentCandidatesResponseBodyData(DaraModel):
    def __init__(
        self,
        deployment_candidates: List[main_models.ListCrossProjectDeploymentCandidatesResponseBodyDataDeploymentCandidates] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of candidate objects from the source workspace that are available for cross-workspace deployment.
        self.deployment_candidates = deployment_candidates
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.deployment_candidates:
            for v1 in self.deployment_candidates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeploymentCandidates'] = []
        if self.deployment_candidates is not None:
            for k1 in self.deployment_candidates:
                result['DeploymentCandidates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployment_candidates = []
        if m.get('DeploymentCandidates') is not None:
            for k1 in m.get('DeploymentCandidates'):
                temp_model = main_models.ListCrossProjectDeploymentCandidatesResponseBodyDataDeploymentCandidates()
                self.deployment_candidates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCrossProjectDeploymentCandidatesResponseBodyDataDeploymentCandidates(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        commit_time: int = None,
        commit_user: str = None,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
        object_version: str = None,
    ):
        # The change type.
        self.change_type = change_type
        # The commit time. This value is a UNIX timestamp in milliseconds.
        self.commit_time = commit_time
        # The committer.
        self.commit_user = commit_user
        # The candidate object ID.
        self.object_id = object_id
        # The candidate object name.
        self.object_name = object_name
        # The candidate object type.
        self.object_type = object_type
        # The candidate object version.
        self.object_version = object_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.commit_time is not None:
            result['CommitTime'] = self.commit_time

        if self.commit_user is not None:
            result['CommitUser'] = self.commit_user

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.object_version is not None:
            result['ObjectVersion'] = self.object_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('CommitTime') is not None:
            self.commit_time = m.get('CommitTime')

        if m.get('CommitUser') is not None:
            self.commit_user = m.get('CommitUser')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('ObjectVersion') is not None:
            self.object_version = m.get('ObjectVersion')

        return self

