# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGitBranchRequest(DaraModel):
    def __init__(
        self,
        branch: str = None,
        org_id: str = None,
        owner: str = None,
        platform: str = None,
        region_id: str = None,
        repo_full_name: str = None,
        repo_id: int = None,
    ):
        # This parameter is required.
        self.branch = branch
        self.org_id = org_id
        self.owner = owner
        # This parameter is required.
        self.platform = platform
        self.region_id = region_id
        # This parameter is required.
        self.repo_full_name = repo_full_name
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch is not None:
            result['Branch'] = self.branch

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_full_name is not None:
            result['RepoFullName'] = self.repo_full_name

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoFullName') is not None:
            self.repo_full_name = m.get('RepoFullName')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        return self

