# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddEditingProjectMaterialsRequest(DaraModel):
    def __init__(
        self,
        material_ids: str = None,
        material_type: str = None,
        owner_account: str = None,
        owner_id: str = None,
        project_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
    ):
        # Separate multiple material IDs with commas (,). You can specify up to 10 IDs.
        # 
        # >  If you specify multiple materials, make sure that the materials are of the same type as specified in MaterialType.
        # 
        # This parameter is required.
        self.material_ids = material_ids
        # The type of the material. Valid values:
        # 
        # *   **video**
        # *   **audio**
        # *   **image**
        # 
        # This parameter is required.
        self.material_type = material_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the online editing project.
        # 
        # This parameter is required.
        self.project_id = project_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

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

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialIds') is not None:
            self.material_ids = m.get('MaterialIds')

        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

