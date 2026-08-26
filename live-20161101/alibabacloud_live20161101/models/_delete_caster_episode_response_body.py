# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCasterEpisodeResponseBody(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        episode_id: str = None,
        request_id: str = None,
    ):
        # The production studio ID. You can use this ID as a request parameter to modify the episode.
        self.caster_id = caster_id
        # The episode ID. You can use this ID as a request parameter to modify the episode.
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
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.episode_id is not None:
            result['EpisodeId'] = self.episode_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('EpisodeId') is not None:
            self.episode_id = m.get('EpisodeId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

