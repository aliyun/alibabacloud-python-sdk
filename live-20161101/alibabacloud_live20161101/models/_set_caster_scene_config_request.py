# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetCasterSceneConfigRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        component_id: List[str] = None,
        layout_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        scene_id: str = None,
    ):
        # The production studio ID.
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the CasterId parameter returned by the CreateCaster operation.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, go to **ApsaraVideo Live console** > **Production Studios** > **China Cloud Production Studio** to view the ID.
        # 
        # > The name of the production studio in the production studio list on the China Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The list of component IDs. The components are arranged in bottom-to-top order within the array.
        # 
        # >N indicates the sequence number. For example:<br>ComponentId.1 indicates the first component ID.<br>ComponentId.2 indicates the second component ID.
        self.component_id = component_id
        # The layout ID. If you call the [DescribeCasterLayouts](https://help.aliyun.com/document_detail/2848028.html) operation to query the layout list of a production studio, check the LayoutId parameter returned by the DescribeCasterLayouts operation.
        self.layout_id = layout_id
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The scene ID. The scene must have been started by calling StartCasterScene. Otherwise, the IncorrectSceneStatus error is returned.
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

