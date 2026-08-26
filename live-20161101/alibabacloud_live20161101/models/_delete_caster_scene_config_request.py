# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCasterSceneConfigRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        scene_id: str = None,
        type: str = None,
    ):
        # The production studio ID.
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the CasterId parameter value returned by the CreateCaster operation.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, go to **ApsaraVideo Live console** > **Production Studios** > **China Cloud-based China Production Studio** to view the ID.
        # 
        # > The name of the production studio in the production studio list on the China Cloud-based Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The scene ID.
        # 
        # This parameter is required.
        self.scene_id = scene_id
        # The scene configuration type. Valid values:
        # 
        # - **Component**: component configuration.
        # - **Layout**: layout configuration.
        # - **All**: component and layout configuration.
        # 
        # This parameter is required.
        self.type = type

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

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

