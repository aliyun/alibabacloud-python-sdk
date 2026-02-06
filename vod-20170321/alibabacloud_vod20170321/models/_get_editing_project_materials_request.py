# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEditingProjectMaterialsRequest(DaraModel):
    def __init__(
        self,
        material_type: str = None,
        owner_account: str = None,
        owner_id: str = None,
        project_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        type: str = None,
    ):
        # The type of the material. Valid values:
        # 
        # *   **video**
        # *   **audio**
        # *   **image**
        self.material_type = material_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the online editing project. You can use one of the following methods to obtain the ID of the online editing project:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Production Center** > **Video Editing** to obtain the ID of the specified online editing project.
        # *   Call the **AddEditingProject** operation. The value of the response parameter ProjectId is the ID of the specified online editing project.
        # 
        # This parameter is required.
        self.project_id = project_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the material. Valid values:
        # 
        # *   **video**
        # *   **audio**
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

