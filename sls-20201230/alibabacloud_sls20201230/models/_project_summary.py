# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProjectSummary(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        project_name: str = None,
        region: str = None,
        resource_group_id: str = None,
        update_time: int = None,
    ):
        # This parameter is required.
        self.create_time = create_time
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.region is not None:
            result['region'] = self.region

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

