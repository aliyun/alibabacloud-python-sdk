# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class CreateBranchRequest(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        client_token: str = None,
        description: str = None,
        expires_at: str = None,
        init_source: str = None,
        parent_branch_id: str = None,
        parent_lsn: str = None,
        parent_timestamp: str = None,
        project_id: str = None,
        protected: bool = None,
        region_id: str = None,
        tag: List[main_models.CreateBranchRequestTag] = None,
    ):
        # The branch name.
        # 
        # This parameter is required.
        self.branch_name = branch_name
        # The client idempotency token. This token ensures the idempotence of retry requests.
        self.client_token = client_token
        # The branch description.
        self.description = description
        # The time at which the branch automatically expires and is deleted. The value is in ISO 8601 UTC format.
        self.expires_at = expires_at
        # The initialization source of the branch.
        # 
        # Valid values:
        # - ParentData: copies the schema and data from the parent branch. This is the default value.
        # - SchemaOnly: copies only the schema structure.
        self.init_source = init_source
        # The parent branch ID. This parameter specifies the parent branch for the new branch or query condition.
        # 
        # This parameter is required.
        self.parent_branch_id = parent_branch_id
        # The log sequence number (LSN) from the parent branch at which the branch is created.
        self.parent_lsn = parent_lsn
        # The point in time for data synchronization from the parent branch when creating the branch. The value is in ISO 8601 UTC format.
        # 
        # Default value: the current time.
        self.parent_timestamp = parent_timestamp
        # The Supabase project ID that corresponds to the primary branch.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Specifies whether to enable branch protection.
        # 
        # Valid values:
        # - true: Enables branch protection.
        # - false: Disables branch protection. This is the default value.
        self.protected = protected
        # The region ID. This parameter is required when you create a primary branch. When you create a child branch, the region is inherited from the primary branch by default.
        self.region_id = region_id
        # The list of branch tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.init_source is not None:
            result['InitSource'] = self.init_source

        if self.parent_branch_id is not None:
            result['ParentBranchId'] = self.parent_branch_id

        if self.parent_lsn is not None:
            result['ParentLsn'] = self.parent_lsn

        if self.parent_timestamp is not None:
            result['ParentTimestamp'] = self.parent_timestamp

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.protected is not None:
            result['Protected'] = self.protected

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('InitSource') is not None:
            self.init_source = m.get('InitSource')

        if m.get('ParentBranchId') is not None:
            self.parent_branch_id = m.get('ParentBranchId')

        if m.get('ParentLsn') is not None:
            self.parent_lsn = m.get('ParentLsn')

        if m.get('ParentTimestamp') is not None:
            self.parent_timestamp = m.get('ParentTimestamp')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Protected') is not None:
            self.protected = m.get('Protected')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateBranchRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateBranchRequestTag(DaraModel):
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

