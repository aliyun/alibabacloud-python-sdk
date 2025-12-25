# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetAuthorityTemplateItemResponseBody(DaraModel):
    def __init__(
        self,
        authority_template_item_list: main_models.GetAuthorityTemplateItemResponseBodyAuthorityTemplateItemList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        tid: int = None,
    ):
        # The permission templates.
        self.authority_template_item_list = authority_template_item_list
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The ID of the tenant.
        self.tid = tid

    def validate(self):
        if self.authority_template_item_list:
            self.authority_template_item_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authority_template_item_list is not None:
            result['AuthorityTemplateItemList'] = self.authority_template_item_list.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityTemplateItemList') is not None:
            temp_model = main_models.GetAuthorityTemplateItemResponseBodyAuthorityTemplateItemList()
            self.authority_template_item_list = temp_model.from_map(m.get('AuthorityTemplateItemList'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class GetAuthorityTemplateItemResponseBodyAuthorityTemplateItemList(DaraModel):
    def __init__(
        self,
        authority_template_item: List[main_models.GetAuthorityTemplateItemResponseBodyAuthorityTemplateItemListAuthorityTemplateItem] = None,
    ):
        self.authority_template_item = authority_template_item

    def validate(self):
        if self.authority_template_item:
            for v1 in self.authority_template_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorityTemplateItem'] = []
        if self.authority_template_item is not None:
            for k1 in self.authority_template_item:
                result['AuthorityTemplateItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authority_template_item = []
        if m.get('AuthorityTemplateItem') is not None:
            for k1 in m.get('AuthorityTemplateItem'):
                temp_model = main_models.GetAuthorityTemplateItemResponseBodyAuthorityTemplateItemListAuthorityTemplateItem()
                self.authority_template_item.append(temp_model.from_map(k1))

        return self

class GetAuthorityTemplateItemResponseBodyAuthorityTemplateItemListAuthorityTemplateItem(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        db_id: int = None,
        instance_id: int = None,
        item_id: int = None,
        modifier_id: int = None,
        resource_type: str = None,
        table_name: str = None,
        template_id: int = None,
    ):
        # The additional information. For example, permissions to log on to an instance are added to the permission template.
        self.attribute = attribute
        # The ID of the database.
        self.db_id = db_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the resource.
        self.item_id = item_id
        # The ID of the user who modifies the resource.
        self.modifier_id = modifier_id
        # The type of the resource. Valid values:
        # 
        # *   **INSTANCE**: instance
        # *   **LOGIC_DB**: logical database
        # *   **META_DB**: physical database
        # *   **LOGIC_TABLE**: logical table
        # *   **LOGIC_TABLE**: physical table
        self.resource_type = resource_type
        # The name of the table.
        self.table_name = table_name
        # The ID of the permission template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

