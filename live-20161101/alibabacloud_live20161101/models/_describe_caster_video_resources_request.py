# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCasterVideoResourcesRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The ID of the production studio.
        # 
        # - If you create the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the value of CasterId that is returned.
        # 
        # - If you create the production studio in the LIVE console, go to the Cloud Production Studio page to view the ID. To go to the page, choose **LIVE Console** > **Production Studio** > **Cloud Production Studio**.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        self.owner_id = owner_id
        # The ID of the region.
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

