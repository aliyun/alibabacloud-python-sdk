# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyCasterSceneConfigRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        from_scene_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        to_scene_id: str = None,
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
        # The ID of the source scene, which must be a PVW scene.
        # 
        # This parameter is required.
        self.from_scene_id = from_scene_id
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the destination scene, which must be a PGM scene.
        # 
        # This parameter is required.
        self.to_scene_id = to_scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.from_scene_id is not None:
            result['FromSceneId'] = self.from_scene_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.to_scene_id is not None:
            result['ToSceneId'] = self.to_scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('FromSceneId') is not None:
            self.from_scene_id = m.get('FromSceneId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ToSceneId') is not None:
            self.to_scene_id = m.get('ToSceneId')

        return self

