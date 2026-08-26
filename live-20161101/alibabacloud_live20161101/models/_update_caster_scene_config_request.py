# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateCasterSceneConfigRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        component_id: List[str] = None,
        layout_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        scene_id: str = None,
    ):
        # The ID of the production studio.
        # 
        # - If you create a production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value from the response.
        # 
        # - If you create a production studio in the ApsaraVideo Live console, find the ID on the **Cloud Production Studio** page. Navigate to this page by choosing **Production Studio** > **Cloud Production Studio** in the ApsaraVideo Live console.
        # 
        # > The name of the production studio in the list is its ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # A list of component IDs. The components in the array are layered from bottom to top.
        # 
        # > N indicates the sequence number. For example, ComponentId.1 is the ID of the first component and ComponentId.2 is the ID of the second component.
        self.component_id = component_id
        # The ID of the layout. If you query the layout list for the production studio by calling the [DescribeCasterLayouts](https://help.aliyun.com/document_detail/2848028.html) operation, use the LayoutId value from the response.
        # 
        # This parameter is required.
        self.layout_id = layout_id
        self.owner_id = owner_id
        # The ID of the region.
        self.region_id = region_id
        # The ID of the scene.
        # 
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

