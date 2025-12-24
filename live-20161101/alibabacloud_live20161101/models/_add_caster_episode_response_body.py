# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCasterEpisodeResponseBody(DaraModel):
    def __init__(
        self,
        episode_id: str = None,
        request_id: str = None,
    ):
        # The ID of the episode. You can use the ID as a request parameter in the API operation that is used to query the information about the episode list, modify the configurations of the episode, and delete the episode.
        self.episode_id = episode_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.episode_id is not None:
            result['EpisodeId'] = self.episode_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EpisodeId') is not None:
            self.episode_id = m.get('EpisodeId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

