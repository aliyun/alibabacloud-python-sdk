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
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
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
        # This parameter is required.
        self.name = name
        self.owner_list = owner_list
        self.parent_path = parent_path
        # This parameter is required.
        self.path = path
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

