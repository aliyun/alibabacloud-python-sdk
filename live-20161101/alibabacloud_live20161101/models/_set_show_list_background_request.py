# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetShowListBackgroundRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        material_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_type: str = None,
        resource_url: str = None,
    ):
        # The production studio ID.
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the CasterId value returned by the CreateCaster operation.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, navigate to **ApsaraVideo Live console** > **Production Studios** > **Cloud Production Studio** to view the production studio name.
        # 
        # > The production studio name in the production studio list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The video-on-demand material ID.
        # 
        # > Specify either this parameter or ResourceUrl.
        self.material_id = material_id
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The material type. Valid values:
        # 
        # - LIVE: live streaming material. Supports live streaming materials and third-party URLs.
        # 
        # - VOD: video-on-demand material. Supports video-on-demand materials and third-party URLs.
        # 
        # - PIC: image material. Supports video-on-demand materials and third-party URLs.
        # 
        # > Specify one of the three values or leave this parameter empty.
        self.resource_type = resource_type
        # The URL of the external material.
        self.resource_url = resource_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.material_id is not None:
            result['MaterialId'] = self.material_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_url is not None:
            result['ResourceUrl'] = self.resource_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceUrl') is not None:
            self.resource_url = m.get('ResourceUrl')

        return self

