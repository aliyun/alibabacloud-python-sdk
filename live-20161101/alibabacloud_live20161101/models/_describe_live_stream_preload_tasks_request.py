# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamPreloadTasksRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        play_url: str = None,
        region_id: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end time in ISO 8601 format in UTC. Format: yyyy-MM-ddTHH:mm:ssZ. The interval between EndTime and StartTime cannot exceed 3 days.
        self.end_time = end_time
        self.owner_id = owner_id
        # The page number to return. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Maximum value: 100. Valid values: any integer from 1 to 100.
        self.page_size = page_size
        # The live streaming URL. You can specify multiple URLs separated by commas (,), up to 100.
        self.play_url = play_url
        # The region ID.
        self.region_id = region_id
        # The start time in ISO 8601 format in UTC. Format: yyyy-MM-ddTHH:mm:ssZ. The start time must be within the last 3 days.
        self.start_time = start_time
        # The task status. Valid values:
        # - complete: completed.
        # - pending: waiting for preload.
        # - preloading: preloading in progress.
        # - failed: preload failed.
        self.status = status
        # The task ID. You can obtain the preload task ID by calling the [SetLiveStreamPreloadTasks](https://help.aliyun.com/document_detail/2519938.html) operation.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.play_url is not None:
            result['PlayUrl'] = self.play_url

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlayUrl') is not None:
            self.play_url = m.get('PlayUrl')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

