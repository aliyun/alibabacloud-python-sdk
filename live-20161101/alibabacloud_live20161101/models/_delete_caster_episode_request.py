# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCasterEpisodeRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        episode_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The production studio ID.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value from the response.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, go to the **Production Studio** > **Cloud Production Studio** page to view the ID.
        # 
        # > The production studio name on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The episode ID. If you added the episode by calling the [AddCasterEpisode](https://help.aliyun.com/document_detail/2848068.html) operation, use the EpisodeId value from the response.
        # 
        # This parameter is required.
        self.episode_id = episode_id
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id

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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('EpisodeId') is not None:
            self.episode_id = m.get('EpisodeId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

