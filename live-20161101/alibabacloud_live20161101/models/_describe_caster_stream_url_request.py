# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCasterStreamUrlRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The ID of the production studio.
        # 
        # If you create a production studio through the [CreateCaster](~~69338#doc-api-live-CreateCaster~~) interface, check the value of the CasterId parameter in the response.
        # 
        # If you create a production studio through the ApsaraVideo Live Console, log in to the console, then check the ID of the production studio through the following path:
        # 
        # Production Studios > Production Studio Management
        # 
        # >  The CasterId is reflected in the Name column on the Production Studio Management page.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        self.owner_id = owner_id
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

