# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class AddCasterProgramResponseBody(DaraModel):
    def __init__(
        self,
        episode_ids: main_models.AddCasterProgramResponseBodyEpisodeIds = None,
        request_id: str = None,
    ):
        # The IDs of the episodes. The episode IDs are listed in the same order as specified by the variable N.
        self.episode_ids = episode_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.episode_ids:
            self.episode_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.episode_ids is not None:
            result['EpisodeIds'] = self.episode_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EpisodeIds') is not None:
            temp_model = main_models.AddCasterProgramResponseBodyEpisodeIds()
            self.episode_ids = temp_model.from_map(m.get('EpisodeIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddCasterProgramResponseBodyEpisodeIds(DaraModel):
    def __init__(
        self,
        episode_id: List[main_models.AddCasterProgramResponseBodyEpisodeIdsEpisodeId] = None,
    ):
        self.episode_id = episode_id

    def validate(self):
        if self.episode_id:
            for v1 in self.episode_id:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EpisodeId'] = []
        if self.episode_id is not None:
            for k1 in self.episode_id:
                result['EpisodeId'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.episode_id = []
        if m.get('EpisodeId') is not None:
            for k1 in m.get('EpisodeId'):
                temp_model = main_models.AddCasterProgramResponseBodyEpisodeIdsEpisodeId()
                self.episode_id.append(temp_model.from_map(k1))

        return self

class AddCasterProgramResponseBodyEpisodeIdsEpisodeId(DaraModel):
    def __init__(
        self,
        episode_id: str = None,
    ):
        # The ID of the episode. You can use the ID as a request parameter in the API operation that is used to modify the episode list, query the information about the episode list, delete the episode, or modify the configurations of the episode.
        self.episode_id = episode_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.episode_id is not None:
            result['EpisodeId'] = self.episode_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EpisodeId') is not None:
            self.episode_id = m.get('EpisodeId')

        return self

