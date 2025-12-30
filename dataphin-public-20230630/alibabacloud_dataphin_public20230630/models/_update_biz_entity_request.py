# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateBizEntityRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateBizEntityRequestUpdateCommand = None,
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
            temp_model = main_models.UpdateBizEntityRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateBizEntityRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        biz_object: main_models.UpdateBizEntityRequestUpdateCommandBizObject = None,
        biz_process: main_models.UpdateBizEntityRequestUpdateCommandBizProcess = None,
        biz_unit_id: int = None,
        data_domain_id: int = None,
        id: int = None,
        type: str = None,
    ):
        self.biz_object = biz_object
        self.biz_process = biz_process
        # This parameter is required.
        self.biz_unit_id = biz_unit_id
        # This parameter is required.
        self.data_domain_id = data_domain_id
        # This parameter is required.
        self.id = id
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

        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizObject') is not None:
            temp_model = main_models.UpdateBizEntityRequestUpdateCommandBizObject()
            self.biz_object = temp_model.from_map(m.get('BizObject'))

        if m.get('BizProcess') is not None:
            temp_model = main_models.UpdateBizEntityRequestUpdateCommandBizProcess()
            self.biz_process = temp_model.from_map(m.get('BizProcess'))

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('DataDomainId') is not None:
            self.data_domain_id = m.get('DataDomainId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateBizEntityRequestUpdateCommandBizProcess(DaraModel):
    def __init__(
        self,
        biz_event_entity_id_list: List[int] = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        owner_user_id: str = None,
        pre_biz_process_id_list: List[int] = None,
        ref_biz_entity_id_list: List[int] = None,
    ):
        self.biz_event_entity_id_list = biz_event_entity_id_list
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.owner_user_id = owner_user_id
        self.pre_biz_process_id_list = pre_biz_process_id_list
        self.ref_biz_entity_id_list = ref_biz_entity_id_list

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

        return self

class UpdateBizEntityRequestUpdateCommandBizObject(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        name: str = None,
        owner_user_id: str = None,
        parent_id: int = None,
        ref_biz_entity_id_list: List[int] = None,
    ):
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.owner_user_id = owner_user_id
        self.parent_id = parent_id
        self.ref_biz_entity_id_list = ref_biz_entity_id_list

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

        return self

