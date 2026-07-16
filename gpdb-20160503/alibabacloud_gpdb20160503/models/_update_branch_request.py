# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class UpdateBranchRequest(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        branch_name: str = None,
        clear_expires_at: bool = None,
        description: str = None,
        expires_at: str = None,
        project_id: str = None,
        protected: bool = None,
        region_id: str = None,
        tag: List[main_models.UpdateBranchRequestTag] = None,
    ):
        # The branch ID that uniquely identifies a Supabase branch.
        # 
        # This parameter is required.
        self.branch_id = branch_id
        # The branch name.
        # 
        # This parameter is required.
        self.branch_name = branch_name
        # Specifies whether to clear the branch expiration time.
        # 
        # Valid values:
        # - true: Clears ExpiresAt.
        # - false: Does not clear ExpiresAt.
        # 
        # If this parameter is not specified, the existing expiration time remains unchanged.
        self.clear_expires_at = clear_expires_at
        # The branch description.
        self.description = description
        # The time when the branch automatically expires and is deleted. The value is in ISO 8601 UTC format.
        self.expires_at = expires_at
        # The Supabase project ID that corresponds to the primary branch.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Specifies whether to enable branch protection.
        # 
        # Valid values:
        # - true: Branch protection is enabled.
        # - false: Branch protection is disabled. This is the default value.
        self.protected = protected
        # The region ID. This parameter is required when you create a primary branch. When you create a sub-branch, the region of the primary branch is inherited by default.
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
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.clear_expires_at is not None:
            result['ClearExpiresAt'] = self.clear_expires_at

        if self.description is not None:
            result['Description'] = self.description

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

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
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('ClearExpiresAt') is not None:
            self.clear_expires_at = m.get('ClearExpiresAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Protected') is not None:
            self.protected = m.get('Protected')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.UpdateBranchRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class UpdateBranchRequestTag(DaraModel):
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

