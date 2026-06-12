# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        fetch_quota: bool = None,
        offset: int = None,
        project_name: str = None,
        resource_group_id: str = None,
        size: int = None,
    ):
        self.description = description
        # Specifies whether to retrieve the quota information for the project.
        self.fetch_quota = fetch_quota
        # The line from which the query starts. The default value is 0.
        self.offset = offset
        # The name of the project. Fuzzy queries are supported.
        self.project_name = project_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The number of rows to return on each page for a paged query. The default value is 100. A maximum of 500 projects can be returned.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.fetch_quota is not None:
            result['fetchQuota'] = self.fetch_quota

        if self.offset is not None:
            result['offset'] = self.offset

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('fetchQuota') is not None:
            self.fetch_quota = m.get('fetchQuota')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

