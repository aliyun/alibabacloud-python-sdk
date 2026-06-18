# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeBranchResponseBody(DaraModel):
    def __init__(
        self,
        branch: main_models.DescribeBranchResponseBodyBranch = None,
        request_id: str = None,
    ):
        # The branch list. Each element represents a Supabase branch.
        self.branch = branch
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.branch:
            self.branch.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch is not None:
            result['Branch'] = self.branch.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Branch') is not None:
            temp_model = main_models.DescribeBranchResponseBodyBranch()
            self.branch = temp_model.from_map(m.get('Branch'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBranchResponseBodyBranch(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        branch_name: str = None,
        compute_endpoint: str = None,
        create_time: str = None,
        description: str = None,
        expires_at: str = None,
        init_source: str = None,
        is_default: bool = None,
        parent_branch_id: str = None,
        parent_branch_name: str = None,
        parent_lsn: str = None,
        parent_timestamp: str = None,
        project_id: str = None,
        protected: bool = None,
        service_type: str = None,
        status: str = None,
        tags: List[main_models.DescribeBranchResponseBodyBranchTags] = None,
    ):
        # The branch ID, which uniquely identifies a Supabase branch.
        self.branch_id = branch_id
        # The branch name.
        self.branch_name = branch_name
        # The connection information of the compute node associated with the branch.
        self.compute_endpoint = compute_endpoint
        # The time when the branch was created, in ISO 8601 UTC format.
        self.create_time = create_time
        # The branch description.
        self.description = description
        # The time when the branch expires and is automatically deleted, in ISO 8601 UTC format.
        self.expires_at = expires_at
        # The initialization source of the branch.
        # 
        # Valid values:
        # - ParentData: Copies the schema and data from the parent branch. This is the default value.
        # - SchemaOnly: Copies only the schema structure.
        self.init_source = init_source
        # Indicates whether this is the default branch.
        self.is_default = is_default
        # The parent branch ID, which specifies the parent branch of a new branch or a query condition.
        self.parent_branch_id = parent_branch_id
        # The parent branch name. This value is empty or displayed as - for the primary branch.
        self.parent_branch_name = parent_branch_name
        # The Log Sequence Number (LSN) of the parent branch at the time this branch was created.
        self.parent_lsn = parent_lsn
        # The data synchronization point in time selected from the parent branch when this branch was created, in ISO 8601 UTC format.
        # 
        # Note:
        # - For child branches, this value indicates the point in time of the parent branch selected during creation.
        # - If no parent branch exists, the value 1970-01-01T00:00:00.000Z is returned.
        self.parent_timestamp = parent_timestamp
        # The Supabase project ID that corresponds to the primary branch.
        self.project_id = project_id
        # Indicates whether branch protection is enabled. A value of true indicates that branch protection is enabled. A value of false indicates that branch protection is disabled.
        self.protected = protected
        # The service type.
        # 
        # Valid values:
        # - Supabase: Supabase service.
        # - Memory: Memory service.
        self.service_type = service_type
        # The branch status.
        self.status = status
        # The list of branch tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.compute_endpoint is not None:
            result['ComputeEndpoint'] = self.compute_endpoint

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.init_source is not None:
            result['InitSource'] = self.init_source

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.parent_branch_id is not None:
            result['ParentBranchId'] = self.parent_branch_id

        if self.parent_branch_name is not None:
            result['ParentBranchName'] = self.parent_branch_name

        if self.parent_lsn is not None:
            result['ParentLSN'] = self.parent_lsn

        if self.parent_timestamp is not None:
            result['ParentTimestamp'] = self.parent_timestamp

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.protected is not None:
            result['Protected'] = self.protected

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('ComputeEndpoint') is not None:
            self.compute_endpoint = m.get('ComputeEndpoint')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('InitSource') is not None:
            self.init_source = m.get('InitSource')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ParentBranchId') is not None:
            self.parent_branch_id = m.get('ParentBranchId')

        if m.get('ParentBranchName') is not None:
            self.parent_branch_name = m.get('ParentBranchName')

        if m.get('ParentLSN') is not None:
            self.parent_lsn = m.get('ParentLSN')

        if m.get('ParentTimestamp') is not None:
            self.parent_timestamp = m.get('ParentTimestamp')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Protected') is not None:
            self.protected = m.get('Protected')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeBranchResponseBodyBranchTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeBranchResponseBodyBranchTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

