# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEditingProjectMaterialsRequest(DaraModel):
    def __init__(
        self,
        material_ids: str = None,
        material_type: str = None,
        project_id: str = None,
    ):
        # The material ID. Separate multiple material IDs with commas (,). You can specify up to 10 IDs.
        # 
        # This parameter is required.
        self.material_ids = material_ids
        # The material type. Valid values:
        # 
        # \\- video
        # 
        # \\- image
        # 
        # \\- audio
        # 
        # \\- subtitle
        # 
        # \\- text
        # 
        # This parameter is required.
        self.material_type = material_type
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
        if self.material_ids is not None:
            result['MaterialIds'] = self.material_ids

        if self.material_type is not None:
            result['MaterialType'] = self.material_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialIds') is not None:
            self.material_ids = m.get('MaterialIds')

        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

