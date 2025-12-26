# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_datahub20240620 import models as main_models
from darabonba.model import DaraModel

class ListProjectsResponseBody(DaraModel):
    def __init__(
        self,
        list: main_models.ListProjectsResponseBodyList = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.list = list
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list is not None:
            result['List'] = self.list.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = main_models.ListProjectsResponseBodyList()
            self.list = temp_model.from_map(m.get('List'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProjectsResponseBodyList(DaraModel):
    def __init__(
        self,
        project: List[main_models.ListProjectsResponseBodyListProject] = None,
    ):
        self.project = project

    def validate(self):
        if self.project:
            for v1 in self.project:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Project'] = []
        if self.project is not None:
            for k1 in self.project:
                result['Project'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.project = []
        if m.get('Project') is not None:
            for k1 in m.get('Project'):
                temp_model = main_models.ListProjectsResponseBodyListProject()
                self.project.append(temp_model.from_map(k1))

        return self



class ListProjectsResponseBodyListProject(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        creator: str = None,
        project_name: str = None,
        update_time: int = None,
    ):
        self.comment = comment
        self.create_time = create_time
        self.creator = creator
        self.project_name = project_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

