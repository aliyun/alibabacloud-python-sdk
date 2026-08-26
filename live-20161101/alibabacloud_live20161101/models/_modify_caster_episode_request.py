# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyCasterEpisodeRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        component_id: List[str] = None,
        end_time: str = None,
        episode_id: str = None,
        episode_name: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: str = None,
        start_time: str = None,
        switch_type: str = None,
    ):
        # The ID of the production studio.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value that is returned in the response.
        # 
        # - If you created the production studio in the LIVE console, find the ID on the Cloud Production Studio page. To go to the page, choose **LIVE Console** > **Production Studio** > **Cloud Production Studio**.
        # 
        # > The name of a production studio in the list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The IDs of the components. The components are arranged from bottom to top and are switched in sync with the video source.
        # 
        # - This parameter is required and takes effect only if EpisodeType is set to **Component**.
        # 
        # - If EpisodeType is set to **Resource**, this parameter specifies the components that are attached to the video source and switched in sync.
        # 
        # > N specifies the Nth component ID. For example, ComponentId.1 specifies the first component ID and ComponentId.2 specifies the second component ID.
        self.component_id = component_id
        # The end time. The time must be in UTC. The format is *yyyy-MM-dd*T*HH:mm:ss*Z.
        self.end_time = end_time
        # The ID of the episode.
        # 
        # This parameter is required.
        self.episode_id = episode_id
        # The name of the episode.
        self.episode_name = episode_name
        self.owner_id = owner_id
        # The ID of the region.
        self.region_id = region_id
        # The ID of the video source.
        # 
        # - This parameter is required and takes effect only if EpisodeType is set to **Resource**.
        # 
        # - This parameter is not available if EpisodeType is set to **Component**.
        self.resource_id = resource_id
        # The start time. The time must be in UTC. The format is *yyyy-MM-dd*T*HH:mm:ss*Z.
        self.start_time = start_time
        # The switch policy. This parameter takes effect only if EpisodeType is set to **Resource**.
        # 
        # - **TimeFirst**: time-priority. This is the only policy available for live stream video sources.
        # 
        # - **ContentFirst**: content-priority.
        self.switch_type = switch_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.episode_id is not None:
            result['EpisodeId'] = self.episode_id

        if self.episode_name is not None:
            result['EpisodeName'] = self.episode_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EpisodeId') is not None:
            self.episode_id = m.get('EpisodeId')

        if m.get('EpisodeName') is not None:
            self.episode_name = m.get('EpisodeName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')

        return self

