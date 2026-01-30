# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListRenderingProjectsResponseBody(DaraModel):
    def __init__(
        self,
        projects: List[main_models.ListRenderingProjectsResponseBodyProjects] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.projects = projects
        self.request_id = request_id
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
        self.projects = []
        if m.get('Projects') is not None:
            for k1 in m.get('Projects'):
                temp_model = main_models.ListRenderingProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRenderingProjectsResponseBodyProjects(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        project_id: str = None,
        project_name: str = None,
        session_attribs: main_models.ListRenderingProjectsResponseBodyProjectsSessionAttribs = None,
        update_time: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.project_id = project_id
        self.project_name = project_name
        self.session_attribs = session_attribs
        self.update_time = update_time

    def validate(self):
        if self.session_attribs:
            self.session_attribs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.session_attribs is not None:
            result['SessionAttribs'] = self.session_attribs.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SessionAttribs') is not None:
            temp_model = main_models.ListRenderingProjectsResponseBodyProjectsSessionAttribs()
            self.session_attribs = temp_model.from_map(m.get('SessionAttribs'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListRenderingProjectsResponseBodyProjectsSessionAttribs(DaraModel):
    def __init__(
        self,
        start_mode: str = None,
    ):
        self.start_mode = start_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.start_mode is not None:
            result['StartMode'] = self.start_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartMode') is not None:
            self.start_mode = m.get('StartMode')

        return self

