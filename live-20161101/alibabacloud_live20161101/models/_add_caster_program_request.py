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
        # The production studio ID.
        # 
        # - If you created the production studio by calling the [CreateCaster operation](https://help.aliyun.com/document_detail/2848009.html), check the CasterId value returned by the CreateCaster operation.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, navigate to **ApsaraVideo Live console** > **Production Studio** > **Cloud Production Studio** to view the production studio name.
        # 
        # > The production studio name in the production studio list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The program list information.
        # 
        # This parameter is required.
        self.episode = episode
        self.owner_id = owner_id
        # The region ID.
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
        # The component list. Elements are arranged from bottom to top in order.
        # >Notice: This parameter is valid and required when Episode.N.EpisodeType is set to **Component**.
        # 
        # 
        #  When the node type is **Resource**, this indicates that the component is bound to the video source and switches synchronously.
        self.component_id = component_id
        # The end time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC). This parameter is required. If not specified, MissingParameter is returned.
        self.end_time = end_time
        # The program name.
        self.episode_name = episode_name
        # The node type. Valid values: 
        #          
        # - **Resource**: video source. If you select Resource, you must also set the request parameters Episode.N.ResourceId and Episode.N.SwitchType.
        # - **Component**: component. If you select Component, you must also set the request parameter Episode.N.ComponentId.N.
        # 
        # 
        # > 
        # > - When Resource is selected and the referenced resource contains a VodUrl (video-on-demand file), EndTime - StartTime cannot exceed the actual playback duration (in seconds) of the VOD file. Otherwise, InvalidParameter.EndTime is returned.
        self.episode_type = episode_type
        # The video source ID.
        # >Notice: This parameter is valid and required when Episode.N.EpisodeType is set to **Resource**.
        #   
        #  This parameter is not applicable when Episode.N.EpisodeType is set to **Component**.
        # 
        # If you added the video source by calling the [AddCasterVideoResource operation](https://help.aliyun.com/document_detail/60250.html), check the ResourceId value returned by the AddCasterVideoResource operation.
        self.resource_id = resource_id
        # The start time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC). This parameter is required. If not specified, MissingParameter is returned.
        self.start_time = start_time
        # The switch policy. Valid values:
        # >Notice: This parameter is valid only when Episode.N.EpisodeType is set to **Resource**.
        # 
        #          
        # - **TimeFirst**: time first. Live video sources can only use the time first policy. 
        # - **ContentFirst**: content first.
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

