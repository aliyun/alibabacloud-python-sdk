# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeLangfuseProjectsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeLangfuseProjectsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeLangfuseProjectsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLangfuseProjectsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        projects: List[main_models.DescribeLangfuseProjectsResponseBodyDataProjects] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The list of Langfuse projects.
        self.projects = projects
        # The total number of records.
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['Projects'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.projects = []
        if m.get('Projects') is not None:
            for k1 in m.get('Projects'):
                temp_model = main_models.DescribeLangfuseProjectsResponseBodyDataProjects()
                self.projects.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLangfuseProjectsResponseBodyDataProjects(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        organization_id: str = None,
        project_id: str = None,
        updated_at: str = None,
    ):
        # The time when the Langfuse project was created.
        self.created_at = created_at
        # The Langfuse project name.
        self.name = name
        # The organization ID to which the Langfuse project belongs.
        self.organization_id = organization_id
        # The Langfuse project ID.
        self.project_id = project_id
        # The time when the Langfuse project was last updated.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.name is not None:
            result['Name'] = self.name

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

