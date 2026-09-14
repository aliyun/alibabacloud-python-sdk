# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCrossProjectDeploymentCandidatesRequest(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        commit_time_from: int = None,
        commit_time_to: int = None,
        commit_user: str = None,
        deployment_environment_id: int = None,
        keyword: str = None,
        object_id: str = None,
        object_type: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
    ):
        # The change type.
        self.change_type = change_type
        # The start of the commit time range. This value is a UNIX timestamp in milliseconds.
        self.commit_time_from = commit_time_from
        # The end of the commit time range. This value is a UNIX timestamp in milliseconds.
        self.commit_time_to = commit_time_to
        # The committer.
        self.commit_user = commit_user
        # The cross-workspace deployment environment ID.
        # 
        # This parameter is required.
        self.deployment_environment_id = deployment_environment_id
        # The search keyword.
        self.keyword = keyword
        # The candidate object ID.
        self.object_id = object_id
        # The candidate object type.
        self.object_type = object_type
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.commit_time_from is not None:
            result['CommitTimeFrom'] = self.commit_time_from

        if self.commit_time_to is not None:
            result['CommitTimeTo'] = self.commit_time_to

        if self.commit_user is not None:
            result['CommitUser'] = self.commit_user

        if self.deployment_environment_id is not None:
            result['DeploymentEnvironmentId'] = self.deployment_environment_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('CommitTimeFrom') is not None:
            self.commit_time_from = m.get('CommitTimeFrom')

        if m.get('CommitTimeTo') is not None:
            self.commit_time_to = m.get('CommitTimeTo')

        if m.get('CommitUser') is not None:
            self.commit_user = m.get('CommitUser')

        if m.get('DeploymentEnvironmentId') is not None:
            self.deployment_environment_id = m.get('DeploymentEnvironmentId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

