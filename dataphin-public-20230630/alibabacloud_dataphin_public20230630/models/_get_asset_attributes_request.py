# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetAssetAttributesRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        query_command: main_models.GetAssetAttributesRequestQueryCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id
        # The query instruction.
        # 
        # This parameter is required.
        self.query_command = query_command

    def validate(self):
        if self.query_command:
            self.query_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.query_command is not None:
            result['QueryCommand'] = self.query_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('QueryCommand') is not None:
            temp_model = main_models.GetAssetAttributesRequestQueryCommand()
            self.query_command = temp_model.from_map(m.get('QueryCommand'))

        return self

class GetAssetAttributesRequestQueryCommand(DaraModel):
    def __init__(
        self,
        attribute_code_list: List[str] = None,
        guid_list: List[str] = None,
    ):
        # The list of property codes to return. If this parameter is not specified, all custom properties of the asset are returned.
        self.attribute_code_list = attribute_code_list
        # The list of asset GUIDs. A maximum of 50 GUIDs are supported.
        # 
        # This parameter is required.
        self.guid_list = guid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_code_list is not None:
            result['AttributeCodeList'] = self.attribute_code_list

        if self.guid_list is not None:
            result['GuidList'] = self.guid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeCodeList') is not None:
            self.attribute_code_list = m.get('AttributeCodeList')

        if m.get('GuidList') is not None:
            self.guid_list = m.get('GuidList')

        return self

