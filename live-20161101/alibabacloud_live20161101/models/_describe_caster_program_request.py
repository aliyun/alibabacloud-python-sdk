# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCasterProgramRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        end_time: str = None,
        episode_id: str = None,
        episode_type: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
        status: int = None,
    ):
        # The ID of the production studio.
        # 
        # - If you create a production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value that is returned in the response.
        # 
        # - If you create a production studio in the LIVE console, find the ID on the Cloud Production Studio page. To go to this page, choose **LIVE** > **Production Studio** > **Cloud Production Studio**.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is its ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The end time. The time must be in the *yyyy-MM-dd*T*HH:mm:ss*Z format and in UTC.
        self.end_time = end_time
        # The ID of the program.
        self.episode_id = episode_id
        # The type of the node. Valid values:
        # 
        # - **Resource**: video source.
        # 
        # - **Component**: component.
        self.episode_type = episode_type
        self.owner_id = owner_id
        # The page number.
        self.page_num = page_num
        # The number of programs on each page.
        self.page_size = page_size
        # The ID of the region.
        self.region_id = region_id
        # The start time. The time must be in the *yyyy-MM-dd*T*HH:mm:ss*Z format and in UTC.
        self.start_time = start_time
        # The status of the program. Valid values:
        # 
        # - **0**: not started
        # 
        # - **1**: playing
        # 
        # - **2**: finished
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.episode_id is not None:
            result['EpisodeId'] = self.episode_id

        if self.episode_type is not None:
            result['EpisodeType'] = self.episode_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EpisodeId') is not None:
            self.episode_id = m.get('EpisodeId')

        if m.get('EpisodeType') is not None:
            self.episode_type = m.get('EpisodeType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

