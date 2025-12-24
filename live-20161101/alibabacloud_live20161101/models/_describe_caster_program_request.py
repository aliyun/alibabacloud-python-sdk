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
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.end_time = end_time
        # The ID of the episode.
        self.episode_id = episode_id
        # The type of the episode. Valid values:
        # 
        # *   **Resource**: a video resource
        # *   **Component**: a component
        self.episode_type = episode_type
        self.owner_id = owner_id
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time
        # The status of the episode. Valid values:
        # 
        # *   **0**: The episode is not played.
        # *   **1**: The episode is being played.
        # *   **2**: The playback of the episode is complete.
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

