# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class AddCasterProgramRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        episode: List[main_models.AddCasterProgramRequestEpisode] = None,
        owner_id: int = None,
        region_id: str = None,
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
        # The information about episodes in the episode list.
        # 
        # This parameter is required.
        self.episode = episode
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        if self.episode:
            for v1 in self.episode:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        result['Episode'] = []
        if self.episode is not None:
            for k1 in self.episode:
                result['Episode'].append(k1.to_map() if k1 else None)

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        self.episode = []
        if m.get('Episode') is not None:
            for k1 in m.get('Episode'):
                temp_model = main_models.AddCasterProgramRequestEpisode()
                self.episode.append(temp_model.from_map(k1))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class AddCasterProgramRequestEpisode(DaraModel):
    def __init__(
        self,
        component_id: List[str] = None,
        end_time: str = None,
        episode_name: str = None,
        episode_type: str = None,
        resource_id: str = None,
        start_time: str = None,
        switch_type: str = None,
    ):
        # The components. Components in the production studio are listed from the bottom to the top in an array.
        # 
        # >  This parameter is required and takes effect when the Episode.N.EpisodeType parameter is set to Component.
        # 
        # This parameter is optional when the Episode.N.EpisodeType parameter is set to **Resource**. In this case, if this parameter is specified, the components are bound to and switched together with video resources.
        self.component_id = component_id
        # The end time of the episode. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.end_time = end_time
        # The name of the episode.
        self.episode_name = episode_name
        # The type of the episode.
        # 
        # *   **Resource**: a video resource If you set this parameter to Resource, you must specify the Episode.N.ResourceId and Episode.N.SwitchType parameters.
        # *   **Component**: a component If you set this parameter to Component, you must specify the Episode.N.ComponentId.N parameter.
        self.episode_type = episode_type
        # The ID of the video resource.
        # 
        # >  This parameter takes effect and is required when the Episode.N.EpisodeType parameter is set to Resource.
        # 
        # \\
        # This parameter is invalid if you set the Episode.N.EpisodeType parameter to **Component**.
        # 
        # If the video resource was added by calling the [AddCasterVideoResource](https://help.aliyun.com/document_detail/60250.html) operation, check the value of the response parameter ResourceId to obtain the ID.
        self.resource_id = resource_id
        # The start time of the episode. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time
        # The policy for switching episodes. Valid values:
        # 
        # >  This parameter takes effect only when the Episode.N.EpisodeType parameter is set to Resource.
        # 
        # *   **TimeFirst**: The episode starts when the previous episode ends and ends when the next episode starts. If no next episode exists, the episode keeps repeating until a new episode is added or the production studio stops. This value is required for live video resources.
        # *   **ContentFirst**: The episode starts and ends as scheduled.
        self.switch_type = switch_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.episode_name is not None:
            result['EpisodeName'] = self.episode_name

        if self.episode_type is not None:
            result['EpisodeType'] = self.episode_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EpisodeName') is not None:
            self.episode_name = m.get('EpisodeName')

        if m.get('EpisodeType') is not None:
            self.episode_type = m.get('EpisodeType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')

        return self

