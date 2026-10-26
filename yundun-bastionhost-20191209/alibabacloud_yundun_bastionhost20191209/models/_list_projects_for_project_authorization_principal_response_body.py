# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListProjectsForProjectAuthorizationPrincipalResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        projects: List[main_models.ListProjectsForProjectAuthorizationPrincipalResponseBodyProjects] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned per page. If a valid MaxResults request parameter is passed, the specified value is returned. Otherwise, the default value is returned.
        self.max_results = max_results
        # The token for the next request, used for paging. You can specify this token in the NextToken request parameter for the next paged query. If this field is empty in the response, no more data is available.
        self.next_token = next_token
        # The list of projects.
        self.projects = projects
        # The ID of the request.
        self.request_id = request_id
        # The total number of queried projects.
        self.total_count = total_count

    def validate(self):
        if self.projects:
            for v1 in self.projects:
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

        result['Projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['Projects'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.projects = []
        if m.get('Projects') is not None:
            for k1 in m.get('Projects'):
                temp_model = main_models.ListProjectsForProjectAuthorizationPrincipalResponseBodyProjects()
                self.projects.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProjectsForProjectAuthorizationPrincipalResponseBodyProjects(DaraModel):
    def __init__(
        self,
        description: str = None,
        is_default: bool = None,
        name: str = None,
        project_id: int = None,
    ):
        # The description of the project.
        self.description = description
        # Specifies whether the project is the default project. Valid values:
        # - **true**: Yes.
        # 
        # - **false**: No.
        self.is_default = is_default
        # The name of the project.
        self.name = name
        # The ID of the project.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

