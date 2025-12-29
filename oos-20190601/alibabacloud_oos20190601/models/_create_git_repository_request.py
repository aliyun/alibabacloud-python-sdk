# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGitRepositoryRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        is_private: bool = None,
        org_id: str = None,
        owner: str = None,
        platform: str = None,
        region_id: str = None,
        source_repo_branch: str = None,
        source_repo_name: str = None,
        source_repo_owner: str = None,
        target_repo_name: str = None,
        target_repo_owner: str = None,
    ):
        self.client_token = client_token
        self.is_private = is_private
        self.org_id = org_id
        # This parameter is required.
        self.owner = owner
        # This parameter is required.
        self.platform = platform
        self.region_id = region_id
        self.source_repo_branch = source_repo_branch
        self.source_repo_name = source_repo_name
        self.source_repo_owner = source_repo_owner
        self.target_repo_name = target_repo_name
        self.target_repo_owner = target_repo_owner

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.is_private is not None:
            result['IsPrivate'] = self.is_private

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_repo_branch is not None:
            result['SourceRepoBranch'] = self.source_repo_branch

        if self.source_repo_name is not None:
            result['SourceRepoName'] = self.source_repo_name

        if self.source_repo_owner is not None:
            result['SourceRepoOwner'] = self.source_repo_owner

        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name

        if self.target_repo_owner is not None:
            result['TargetRepoOwner'] = self.target_repo_owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('IsPrivate') is not None:
            self.is_private = m.get('IsPrivate')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceRepoBranch') is not None:
            self.source_repo_branch = m.get('SourceRepoBranch')

        if m.get('SourceRepoName') is not None:
            self.source_repo_name = m.get('SourceRepoName')

        if m.get('SourceRepoOwner') is not None:
            self.source_repo_owner = m.get('SourceRepoOwner')

        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')

        if m.get('TargetRepoOwner') is not None:
            self.target_repo_owner = m.get('TargetRepoOwner')

        return self

