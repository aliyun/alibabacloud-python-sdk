# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class ListProjectsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        project_list: List[main_models.ListProjectsResponseBodyProjectList] = None,
        request_id: str = None,
    ):
        # A response field retained for backward compatibility. This field is not used for pagination. Do not rely on this field.
        self.max_results = max_results
        # A response field retained for backward compatibility. This field is not used for pagination. Do not rely on this field.
        self.next_token = next_token
        # The list of projects on the current page.
        self.project_list = project_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.project_list:
            for v1 in self.project_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ProjectList'] = []
        if self.project_list is not None:
            for k1 in self.project_list:
                result['ProjectList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.project_list = []
        if m.get('ProjectList') is not None:
            for k1 in m.get('ProjectList'):
                temp_model = main_models.ListProjectsResponseBodyProjectList()
                self.project_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProjectsResponseBodyProjectList(DaraModel):
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
        # The creation time. The time is in UTC and follows the ISO 8601 standard, ending with Z.
        self.create_time = create_time
        # The username of the user who created the project.
        self.create_user_name = create_user_name
        # The description of the project.
        self.description = description
        # The ID of the project.
        self.project_id = project_id
        # The name of the project.
        self.title = title
        # The ID of the workspace.
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

