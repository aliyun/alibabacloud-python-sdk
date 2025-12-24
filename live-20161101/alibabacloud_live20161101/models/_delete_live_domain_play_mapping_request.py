# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveDomainPlayMappingRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        play_domain: str = None,
        pull_domain: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        # The sub-streaming domain.
        # 
        # This parameter is required.
        self.play_domain = play_domain
        # The main streaming domain.
        # 
        # This parameter is required.
        self.pull_domain = pull_domain
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain

        if self.pull_domain is not None:
            result['PullDomain'] = self.pull_domain

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')

        if m.get('PullDomain') is not None:
            self.pull_domain = m.get('PullDomain')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

