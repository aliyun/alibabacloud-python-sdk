# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class SearchEditingProjectResponseBody(DaraModel):
    def __init__(
        self,
        project_list: main_models.SearchEditingProjectResponseBodyProjectList = None,
        request_id: str = None,
        total: int = None,
    ):
        self.project_list = project_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of online editing projects returned.
        self.total = total

    def validate(self):
        if self.project_list:
            self.project_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_list is not None:
            result['ProjectList'] = self.project_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectList') is not None:
            temp_model = main_models.SearchEditingProjectResponseBodyProjectList()
            self.project_list = temp_model.from_map(m.get('ProjectList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class SearchEditingProjectResponseBodyProjectList(DaraModel):
    def __init__(
        self,
        project: List[main_models.SearchEditingProjectResponseBodyProjectListProject] = None,
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
                temp_model = main_models.SearchEditingProjectResponseBodyProjectListProject()
                self.project.append(temp_model.from_map(k1))

        return self

class SearchEditingProjectResponseBodyProjectListProject(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        duration: float = None,
        modified_time: str = None,
        project_id: str = None,
        region_id: str = None,
        status: str = None,
        storage_location: str = None,
        title: str = None,
    ):
        self.cover_url = cover_url
        self.creation_time = creation_time
        self.description = description
        self.duration = duration
        self.modified_time = modified_time
        self.project_id = project_id
        self.region_id = region_id
        self.status = status
        self.storage_location = storage_location
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

