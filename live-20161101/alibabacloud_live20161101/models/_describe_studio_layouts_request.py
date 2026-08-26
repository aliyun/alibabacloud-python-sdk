# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStudioLayoutsRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        layout_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The production studio ID.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the CasterId parameter value returned by the CreateCaster operation.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, go to **ApsaraVideo Live console** > **Production Studio** > **Cloud Production Studio** to view the ID.
        # 
        # > 
        # > - The production studio name in the production studio list on the Cloud Production Studio page is the production studio ID.
        # > - Only virtual studio production studios (NormType=4) are supported. If you pass in a production studio ID of another type, InvalidCaster.NotFound is returned. Call DescribeCasters and filter by NormType=4 to obtain the virtual studio production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The layout ID.
        # Separate multiple layout IDs with commas (,). If this parameter is not specified, all layouts under the production studio are returned.
        # 
        # If you added virtual studio layout settings by calling the [AddStudioLayout](https://help.aliyun.com/document_detail/2848062.html) operation, check the LayoutId parameter value returned by the AddStudioLayout operation.
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

