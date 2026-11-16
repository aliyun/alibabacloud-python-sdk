# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetProjectResponseBody(DaraModel):
    def __init__(
        self,
        project: main_models.GetProjectResponseBodyProject = None,
        request_id: str = None,
    ):
        # The project details.
        self.project = project
        # The request ID, used to trace and troubleshoot the request.
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project is not None:
            result['Project'] = self.project.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = main_models.GetProjectResponseBodyProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProjectResponseBodyProject(DaraModel):
    def __init__(
        self,
        auth: str = None,
        cover_url: str = None,
        create_time: str = None,
        create_user_name: str = None,
        description: str = None,
        project_id: str = None,
        title: str = None,
        workspace_id: str = None,
    ):
        # The permissions of the current caller in the project. For example, Manage indicates management permissions.
        self.auth = auth
        # The URL of the cover image.
        self.cover_url = cover_url
        # The creation time, in ISO 8601 UTC format ending with Z.
        self.create_time = create_time
        # The username of the user who created the project.
        self.create_user_name = create_user_name
        # The project description.
        self.description = description
        # The project ID.
        self.project_id = project_id
        # The project name.
        self.title = title
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['Auth'] = self.auth

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.description is not None:
            result['Description'] = self.description

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.title is not None:
            result['Title'] = self.title

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

