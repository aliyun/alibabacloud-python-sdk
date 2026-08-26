# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCasterLayoutsRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        layout_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The ID of the production studio.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value returned in the response.
        # 
        # - If you created the production studio in the LIVE console, find the ID on the **Production Studio** > **Cloud Production Studio** page.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The layout ID.
        # 
        # If you do not provide a value for LayoutId, all layouts of the production studio are returned.
        self.layout_id = layout_id
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

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

