# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateBizEntityRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateBizEntityRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # The create request.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateBizEntityRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateBizEntityRequestCreateCommand(DaraModel):
    def __init__(
        self,
        biz_object: main_models.CreateBizEntityRequestCreateCommandBizObject = None,
        biz_process: main_models.CreateBizEntityRequestCreateCommandBizProcess = None,
        biz_unit_id: int = None,
        data_domain_id: int = None,
        type: str = None,
    ):
        # The business object.
        self.biz_object = biz_object
        # The business activity.
        self.biz_process = biz_process
        # The ID of the business unit to which the business activity belongs.
        # 
        # This parameter is required.
        self.biz_unit_id = biz_unit_id
        # The ID of the data domain to which the business activity belongs.
        # 
        # This parameter is required.
        self.data_domain_id = data_domain_id
        # The business type. Valid values: 
        # - BIZ_OBJECT: business object.
        # - BIZ_PROCESS: business activity.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.biz_object:
            self.biz_object.validate()
        if self.biz_process:
            self.biz_process.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_object is not None:
            result['BizObject'] = self.biz_object.to_map()

        if self.biz_process is not None:
            result['BizProcess'] = self.biz_process.to_map()

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.data_domain_id is not None:
            result['DataDomainId'] = self.data_domain_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizObject') is not None:
            temp_model = main_models.CreateBizEntityRequestCreateCommandBizObject()
            self.biz_object = temp_model.from_map(m.get('BizObject'))

        if m.get('BizProcess') is not None:
            temp_model = main_models.CreateBizEntityRequestCreateCommandBizProcess()
            self.biz_process = temp_model.from_map(m.get('BizProcess'))

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('DataDomainId') is not None:
            self.data_domain_id = m.get('DataDomainId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateBizEntityRequestCreateCommandBizProcess(DaraModel):
    def __init__(
        self,
        biz_event_entity_id_list: List[int] = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        owner_user_id: str = None,
        pre_biz_process_id_list: List[int] = None,
        ref_biz_entity_id_list: List[int] = None,
        type: str = None,
    ):
        # The list of business event activity IDs included in the business process activity. This parameter takes effect only when the current activity is a business process activity.
        self.biz_event_entity_id_list = biz_event_entity_id_list
        # The description of the business activity. The description can be up to 128 characters in length.
        self.description = description
        # The display name of the business activity. The name can be up to 64 characters in length and can contain only Chinese characters, letters, digits, underscores, and hyphens.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The code name of the business activity. The name can be up to 64 characters in length and can contain only letters, digits, and underscores. For ADB_PG engines, the code name can be up to 40 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The user ID of the business activity owner.
        self.owner_user_id = owner_user_id
        # The list of preceding business process activity IDs for the business process activity.
        self.pre_biz_process_id_list = pre_biz_process_id_list
        # The list of associated online business entity IDs.
        self.ref_biz_entity_id_list = ref_biz_entity_id_list
        # The type of the business activity. Valid values:
        # - BIZ_EVENT: business event.
        # - BIZ_SNAPSHOT: business snapshot.
        # - BIZ_PROCESS: business process.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_event_entity_id_list is not None:
            result['BizEventEntityIdList'] = self.biz_event_entity_id_list

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.pre_biz_process_id_list is not None:
            result['PreBizProcessIdList'] = self.pre_biz_process_id_list

        if self.ref_biz_entity_id_list is not None:
            result['RefBizEntityIdList'] = self.ref_biz_entity_id_list

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizEventEntityIdList') is not None:
            self.biz_event_entity_id_list = m.get('BizEventEntityIdList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('PreBizProcessIdList') is not None:
            self.pre_biz_process_id_list = m.get('PreBizProcessIdList')

        if m.get('RefBizEntityIdList') is not None:
            self.ref_biz_entity_id_list = m.get('RefBizEntityIdList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateBizEntityRequestCreateCommandBizObject(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        name: str = None,
        owner_user_id: str = None,
        parent_id: int = None,
        ref_biz_entity_id_list: List[int] = None,
        type: str = None,
    ):
        # The description of the business object. The description can be up to 128 characters in length.
        self.description = description
        # The display name of the business object. The name can be up to 64 characters in length and can contain only Chinese characters, letters, digits, underscores, and hyphens.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The code name of the business object. The name can be up to 64 characters in length and can contain only letters, digits, and underscores. For ADB_PG engines, the code name can be up to 40 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The user ID of the business object owner.
        self.owner_user_id = owner_user_id
        # The parent entity from which the business object inherits. Only common business objects support inheritance, and the parent entity must be an online business object.
        self.parent_id = parent_id
        # The list of associated online business entity IDs.
        self.ref_biz_entity_id_list = ref_biz_entity_id_list
        # The object type of the business object. Valid values:
        # - NORMAL: common object.
        # - ENUM: enumeration object.
        # - VIRTUAL: virtual object.
        # - HIERARCHY: hierarchy object.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.ref_biz_entity_id_list is not None:
            result['RefBizEntityIdList'] = self.ref_biz_entity_id_list

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RefBizEntityIdList') is not None:
            self.ref_biz_entity_id_list = m.get('RefBizEntityIdList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

