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
        # The ID of the production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The ID of the material in ApsaraVideo VOD.
        # 
        # >  Specify either this parameter or the ResourceUrl parameter.
        self.material_id = material_id
        self.owner_id = owner_id
        self.region_id = region_id
        # The resource type. Valid values:
        # 
        # *   LIVE: live stream. You can add a live stream from ApsaraVideo Live or by using a third-party URL.
        # *   VOD: on-demand video. You can add an on-demand video from ApsaraVideo VOD or by using a third-party URL.
        # *   PIC: image. You can add an image from ApsaraVideo VOD or by using a third-party URL.
        # 
        # >  Set this parameter to one of the preceding values, or leave this parameter empty.
        self.resource_type = resource_type
        # The URL of the third-party material.
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

