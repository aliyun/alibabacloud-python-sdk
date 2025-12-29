# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListWebApplicationInstancesRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_ids: List[str] = None,
        limit: str = None,
        namespace_id: str = None,
        start_time: int = None,
        statuses: List[str] = None,
        version_ids: List[str] = None,
    ):
        # The time when the operation ended.
        self.end_time = end_time
        # The instance ID.
        self.instance_ids = instance_ids
        # The number of application instances returned.
        self.limit = limit
        # The namespace ID.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The time when the task was created.
        self.start_time = start_time
        # The status of the application instance.
        self.statuses = statuses
        # The ID of the application version.
        self.version_ids = version_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        if self.version_ids is not None:
            result['VersionIds'] = self.version_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        if m.get('VersionIds') is not None:
            self.version_ids = m.get('VersionIds')

        return self

