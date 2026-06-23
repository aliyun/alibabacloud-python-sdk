# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUploadTasksRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        site_id: int = None,
        start_time: str = None,
        type: str = None,
    ):
        # The end time in ISO 8601 format (for example, 2024-01-01T00:00:00+Z).
        # >Notice: StartTime and EndTime must be provided together to define the query time window. An error is returned if either one is missing..
        self.end_time = end_time
        # The site ID. You can obtain this value by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # >Notice: This parameter is required when you call the ListUploadTasks operation..
        self.site_id = site_id
        # The start time in ISO 8601 format (for example, 2024-01-01T00:00:00+Z).
        # >Notice: StartTime and EndTime must be provided together to define the query time window. An error is returned if either one is missing..
        self.start_time = start_time
        # The task type. Valid values:
        # 
        # - **file**: URL file purge.
        # - **preload**: resource prefetch.
        # - **directory**: directory purge.
        # - **ignoreparams**: purge with parameters ignored.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

