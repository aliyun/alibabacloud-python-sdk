# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateSecurityClassifyCatalogRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateSecurityClassifyCatalogRequestUpdateCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The update instruction.
        # 
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateSecurityClassifyCatalogRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateSecurityClassifyCatalogRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        name: str = None,
        owner_list: List[str] = None,
        parent_path: str = None,
        path: str = None,
        visible_type: str = None,
    ):
        # The name of the classification folder.
        # 
        # This parameter is required.
        self.name = name
        # The list of administrator IDs. This parameter takes effect only when the parent folder is the root folder.
        self.owner_list = owner_list
        # The full path of the parent classification folder. Default value: /.
        self.parent_path = parent_path
        # The original full path of the folder.
        # 
        # This parameter is required.
        self.path = path
        # The visibility scope of the classification folder. This parameter takes effect only when the parent folder is the root folder. Valid values:
        # - PUBLIC: visible to all users.
        # - PRIVATE: visible only to administrators.
        # Default value: PUBLIC.
        self.visible_type = visible_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.owner_list is not None:
            result['OwnerList'] = self.owner_list

        if self.parent_path is not None:
            result['ParentPath'] = self.parent_path

        if self.path is not None:
            result['Path'] = self.path

        if self.visible_type is not None:
            result['VisibleType'] = self.visible_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerList') is not None:
            self.owner_list = m.get('OwnerList')

        if m.get('ParentPath') is not None:
            self.parent_path = m.get('ParentPath')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('VisibleType') is not None:
            self.visible_type = m.get('VisibleType')

        return self

