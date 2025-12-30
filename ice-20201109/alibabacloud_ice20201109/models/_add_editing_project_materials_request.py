# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddEditingProjectMaterialsRequest(DaraModel):
    def __init__(
        self,
        material_maps: str = None,
        project_id: str = None,
    ):
        # The material ID. Separate multiple material IDs with commas (,). Each type supports up to 10 material IDs. The following material types are supported:
        # 
        # *   video
        # *   audio
        # *   image
        # *   liveStream
        # *   editingProject
        # 
        # This parameter is required.
        self.material_maps = material_maps
        # The ID of the online editing project.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.material_maps is not None:
            result['MaterialMaps'] = self.material_maps

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialMaps') is not None:
            self.material_maps = m.get('MaterialMaps')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

