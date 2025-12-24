# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveAIStudioRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        studio_id: str = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the template. You can obtain the ID from the response to the CreateLiveAIStudio operation.
        # 
        # This parameter is required.
        self.studio_id = studio_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.studio_id is not None:
            result['StudioId'] = self.studio_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StudioId') is not None:
            self.studio_id = m.get('StudioId')

        return self

