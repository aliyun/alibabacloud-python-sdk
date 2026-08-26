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
        # - If you create a production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the CasterId parameter that is returned.
        # 
        # - If you create a production studio in the LIVE console, go to the **LIVE Console**> **Production Studio** > **Production Studio** page to view the ID.
        # 
        # > The name of the production studio in the production studio list serves as the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # A list of component IDs. The components are layered from bottom to top in the specified order.
        # 
        # If you add a component by calling the [AddCasterComponent](https://help.aliyun.com/document_detail/2848030.html) operation, check the value of the ComponentId parameter that is returned.
        # 
        # - This parameter is required and applies only when the resource type is **Component**.
        # 
        # - This parameter is optional when the resource type is **Resource**. If you specify this parameter, the component is attached to the video source and they are switched synchronously.
        # 
        # > N specifies the sequence number of a component ID. For example, **ComponentId.1** specifies the first component ID and **ComponentId.2** specifies the second component ID.
        self.component_id = component_id
        # The end time. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the episode.
        self.episode_name = episode_name
        # The node type. Valid values:
        # 
        # - **Resource**: A video source. If you set this parameter to Resource, you must also specify the ResourceId and SwitchType parameters.
        # 
        # - **Component**: A component.
        # 
        # This parameter is required.
        self.episode_type = episode_type
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The ID of the video source.
        # 
        # >Notice: 
        # 
        # This parameter is required and applies only when EpisodeType is set to Resource.
        # 
        # 
        # 
        # If you add a video source by calling the [AddCasterVideoResource](https://help.aliyun.com/document_detail/2848020.html) operation, check the value of the ResourceId parameter that is returned.
        self.resource_id = resource_id
        # The start time. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The switch policy. Valid values:
        # 
        # >Notice: 
        # 
        # This parameter applies only when EpisodeType is set to Resource.
        # 
        # 
        # 
        # - **TimeFirst**: Time first.
        # 
        # - **ContentFirst**: Content first.
        # 
        # > For more information about video sources, see [Add a video source](https://help.aliyun.com/document_detail/66094.html).
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

