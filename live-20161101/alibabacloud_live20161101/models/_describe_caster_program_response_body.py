# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCasterProgramResponseBody(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        episodes: main_models.DescribeCasterProgramResponseBodyEpisodes = None,
        program_effect: int = None,
        program_name: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The ID of the production studio.
        self.caster_id = caster_id
        # The list of the episodes.
        self.episodes = episodes
        # Indicates whether carousel playback is enabled.
        # 
        # *   **0**: Carousel playback is disabled.
        # *   **1**: Carousel playback is enabled.
        self.program_effect = program_effect
        # The name of the episode list.
        self.program_name = program_name
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.episodes:
            self.episodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.episodes is not None:
            result['Episodes'] = self.episodes.to_map()

        if self.program_effect is not None:
            result['ProgramEffect'] = self.program_effect

        if self.program_name is not None:
            result['ProgramName'] = self.program_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('Episodes') is not None:
            temp_model = main_models.DescribeCasterProgramResponseBodyEpisodes()
            self.episodes = temp_model.from_map(m.get('Episodes'))

        if m.get('ProgramEffect') is not None:
            self.program_effect = m.get('ProgramEffect')

        if m.get('ProgramName') is not None:
            self.program_name = m.get('ProgramName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeCasterProgramResponseBodyEpisodes(DaraModel):
    def __init__(
        self,
        episode: List[main_models.DescribeCasterProgramResponseBodyEpisodesEpisode] = None,
    ):
        self.episode = episode

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
        result['Episode'] = []
        if self.episode is not None:
            for k1 in self.episode:
                result['Episode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.episode = []
        if m.get('Episode') is not None:
            for k1 in m.get('Episode'):
                temp_model = main_models.DescribeCasterProgramResponseBodyEpisodesEpisode()
                self.episode.append(temp_model.from_map(k1))

        return self

class DescribeCasterProgramResponseBodyEpisodesEpisode(DaraModel):
    def __init__(
        self,
        component_ids: main_models.DescribeCasterProgramResponseBodyEpisodesEpisodeComponentIds = None,
        end_time: str = None,
        episode_id: str = None,
        episode_name: str = None,
        episode_type: str = None,
        resource_id: str = None,
        start_time: str = None,
        status: int = None,
        switch_type: str = None,
    ):
        # The components.
        self.component_ids = component_ids
        # The end of the time range during which data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The ID of the episode.
        self.episode_id = episode_id
        # The name of the episode.
        self.episode_name = episode_name
        # The type of the episode. Valid values:
        # 
        # *   **Resource**: a video resource
        # *   **Component**: a component
        self.episode_type = episode_type
        # The ID of the video resource.
        self.resource_id = resource_id
        # The beginning of the time range during which data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time
        # The status of the episode.
        self.status = status
        # The policy for switching episodes. Valid values:
        # 
        # *   **TimeFirst**: The episode starts when the previous episode ends and ends when the next episode starts. If no next episode exists, the episode keeps repeating until a new episode is added or the production studio stops. This value is required for live video resources.
        # *   **ContentFirst**: The episode starts and ends as scheduled.
        self.switch_type = switch_type

    def validate(self):
        if self.component_ids:
            self.component_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_ids is not None:
            result['ComponentIds'] = self.component_ids.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.episode_id is not None:
            result['EpisodeId'] = self.episode_id

        if self.episode_name is not None:
            result['EpisodeName'] = self.episode_name

        if self.episode_type is not None:
            result['EpisodeType'] = self.episode_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentIds') is not None:
            temp_model = main_models.DescribeCasterProgramResponseBodyEpisodesEpisodeComponentIds()
            self.component_ids = temp_model.from_map(m.get('ComponentIds'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EpisodeId') is not None:
            self.episode_id = m.get('EpisodeId')

        if m.get('EpisodeName') is not None:
            self.episode_name = m.get('EpisodeName')

        if m.get('EpisodeType') is not None:
            self.episode_type = m.get('EpisodeType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')

        return self

class DescribeCasterProgramResponseBodyEpisodesEpisodeComponentIds(DaraModel):
    def __init__(
        self,
        component_id: List[str] = None,
    ):
        self.component_id = component_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        return self

