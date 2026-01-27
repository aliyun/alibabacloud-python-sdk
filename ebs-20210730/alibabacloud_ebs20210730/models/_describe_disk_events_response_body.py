# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeDiskEventsResponseBody(DaraModel):
    def __init__(
        self,
        disk_events: List[main_models.DescribeDiskEventsResponseBodyDiskEvents] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The risk events of the disk.
        self.disk_events = disk_events
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.disk_events:
            for v1 in self.disk_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiskEvents'] = []
        if self.disk_events is not None:
            for k1 in self.disk_events:
                result['DiskEvents'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk_events = []
        if m.get('DiskEvents') is not None:
            for k1 in m.get('DiskEvents'):
                temp_model = main_models.DescribeDiskEventsResponseBodyDiskEvents()
                self.disk_events.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiskEventsResponseBodyDiskEvents(DaraModel):
    def __init__(
        self,
        description: str = None,
        disk_id: str = None,
        recommend_action: str = None,
        region_id: str = None,
        status: str = None,
        timestamp: str = None,
        type: str = None,
    ):
        # The description of the event.
        self.description = description
        # The ID of the disk.
        self.disk_id = disk_id
        # The recommended action after the event occurred. Valid values:
        # 
        # *   Resize: resizes the disk.
        # *   ModifyDiskSpec: changes the category of the disk.
        # *   NoAction: performs no operation.
        self.recommend_action = recommend_action
        # The region ID of the disk.
        self.region_id = region_id
        # The state of the event. Valid values:
        # 
        # *   Solved
        # *   UnSolved
        self.status = status
        # The time when the event occurred. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.timestamp = timestamp
        # The type of the event. Only DataNeedProtect can be returned.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.recommend_action is not None:
            result['RecommendAction'] = self.recommend_action

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('RecommendAction') is not None:
            self.recommend_action = m.get('RecommendAction')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

