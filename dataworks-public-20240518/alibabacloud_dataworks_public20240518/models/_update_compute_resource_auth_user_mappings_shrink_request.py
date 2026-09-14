# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateComputeResourceAuthUserMappingsShrinkRequest(DaraModel):
    def __init__(
        self,
        compute_resource_id: int = None,
        project_id: int = None,
        remove_user_ids_shrink: str = None,
        upserts_shrink: str = None,
    ):
        # The compute resource ID.
        # 
        # This parameter is required.
        self.compute_resource_id = compute_resource_id
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The list of user mappings to remove.
        self.remove_user_ids_shrink = remove_user_ids_shrink
        # The list of objects to update.
        self.upserts_shrink = upserts_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource_id is not None:
            result['ComputeResourceId'] = self.compute_resource_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.remove_user_ids_shrink is not None:
            result['RemoveUserIds'] = self.remove_user_ids_shrink

        if self.upserts_shrink is not None:
            result['Upserts'] = self.upserts_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResourceId') is not None:
            self.compute_resource_id = m.get('ComputeResourceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RemoveUserIds') is not None:
            self.remove_user_ids_shrink = m.get('RemoveUserIds')

        if m.get('Upserts') is not None:
            self.upserts_shrink = m.get('Upserts')

        return self

