# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateAssetAttributesRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        update_command: main_models.UpdateAssetAttributesRequestUpdateCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id
        # The update command.
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

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateAssetAttributesRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateAssetAttributesRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        asset_attribute_update_list: List[main_models.UpdateAssetAttributesRequestUpdateCommandAssetAttributeUpdateList] = None,
    ):
        # The list of asset property updates. A maximum of 50 entries can be specified in a single request.
        # 
        # This parameter is required.
        self.asset_attribute_update_list = asset_attribute_update_list

    def validate(self):
        if self.asset_attribute_update_list:
            for v1 in self.asset_attribute_update_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetAttributeUpdateList'] = []
        if self.asset_attribute_update_list is not None:
            for k1 in self.asset_attribute_update_list:
                result['AssetAttributeUpdateList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_attribute_update_list = []
        if m.get('AssetAttributeUpdateList') is not None:
            for k1 in m.get('AssetAttributeUpdateList'):
                temp_model = main_models.UpdateAssetAttributesRequestUpdateCommandAssetAttributeUpdateList()
                self.asset_attribute_update_list.append(temp_model.from_map(k1))

        return self

class UpdateAssetAttributesRequestUpdateCommandAssetAttributeUpdateList(DaraModel):
    def __init__(
        self,
        attribute_list: List[main_models.UpdateAssetAttributesRequestUpdateCommandAssetAttributeUpdateListAttributeList] = None,
        guid: str = None,
    ):
        # The list of properties to update.
        # 
        # This parameter is required.
        self.attribute_list = attribute_list
        # The globally unique identifier (GUID) of the asset. You can obtain this value by calling operations such as ListCatalogAssets and GetTableColumnByTableGuids.
        # 
        # This parameter is required.
        self.guid = guid

    def validate(self):
        if self.attribute_list:
            for v1 in self.attribute_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeList'] = []
        if self.attribute_list is not None:
            for k1 in self.attribute_list:
                result['AttributeList'].append(k1.to_map() if k1 else None)

        if self.guid is not None:
            result['Guid'] = self.guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_list = []
        if m.get('AttributeList') is not None:
            for k1 in m.get('AttributeList'):
                temp_model = main_models.UpdateAssetAttributesRequestUpdateCommandAssetAttributeUpdateListAttributeList()
                self.attribute_list.append(temp_model.from_map(k1))

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        return self

class UpdateAssetAttributesRequestUpdateCommandAssetAttributeUpdateListAttributeList(DaraModel):
    def __init__(
        self,
        attribute_code: str = None,
        values: List[str] = None,
    ):
        # The property code. This value must match the AttributeCode returned by the GetAssetTypeAttributeCodes operation.
        # 
        # This parameter is required.
        self.attribute_code = attribute_code
        # The list of property values. For a single-value property, pass one element. For a multi-value property, pass multiple elements. Pass an empty array [] to clear the property value.
        # 
        # This parameter is required.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_code is not None:
            result['AttributeCode'] = self.attribute_code

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeCode') is not None:
            self.attribute_code = m.get('AttributeCode')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

