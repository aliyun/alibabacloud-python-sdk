# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddCasterEpisodeRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        component_id: List[str] = None,
        end_time: str = None,
        episode_name: str = None,
        episode_type: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: str = None,
        start_time: str = None,
        switch_type: str = None,
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
        # The components. Components in the production studio are listed from the bottom to the top in an array.
        # 
        # If a component was added by calling the [AddCasterComponent](https://help.aliyun.com/document_detail/2848030.html) operation, check the value of the response parameter ComponentId to obtain the component ID.
        # 
        # *   This parameter takes effect and is required when the EpisodeType parameter is set to **Component**.
        # *   This parameter is optional when the EpisodeType parameter is set to **Resource**. In this case, if this parameter is specified, the components are bound to and switched together with video resources.
        # 
        # >  The variable N specifies the sequence number of the component. For example, **ComponentId.1** specifies the ID of the first component and **ComponentId.2** specifies the ID of the second component.
        self.component_id = component_id
        # The time when the episode ends. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the episode.
        self.episode_name = episode_name
        # The type of the episode. Valid values:
        # 
        # *   **Resource**: a video resource.
        # *   **Component**: a component.
        # 
        # This parameter is required.
        self.episode_type = episode_type
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the video resource.
        # 
        # >  This parameter takes effect and is required when the EpisodeType parameter is set to Resource.
        # 
        # \\
        # If the video resource was added by calling the [AddCasterVideoResource](https://help.aliyun.com/document_detail/2848020.html) operation, check the value of the response parameter ResourceId to obtain the ID.
        self.resource_id = resource_id
        # The time when the episode starts. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The policy for switching episodes. Valid values:
        # 
        # *   **TimeFirst**: The episode starts when the preceding episode ends and ends when the next episode starts. If no next episode exists, the episode keeps repeating until a new episode is added or the production studio stops.
        # *   **ContentFirst**: The episode starts and ends as scheduled.
        # 
        # This parameter takes effect only when the EpisodeType parameter is set to Resource.
        # 
        # >  This parameter must be set to TimeFirst when the video resource is a live stream.
        # 
        # This parameter is required.
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

        if self.episode_name is not None:
            result['EpisodeName'] = self.episode_name

        if self.episode_type is not None:
            result['EpisodeType'] = self.episode_type

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

        if m.get('EpisodeName') is not None:
            self.episode_name = m.get('EpisodeName')

        if m.get('EpisodeType') is not None:
            self.episode_type = m.get('EpisodeType')

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

