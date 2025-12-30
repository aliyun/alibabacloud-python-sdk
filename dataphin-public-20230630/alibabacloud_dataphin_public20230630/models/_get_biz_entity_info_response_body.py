# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBizEntityInfoResponseBody(DaraModel):
    def __init__(
        self,
        biz_entity_info: main_models.GetBizEntityInfoResponseBodyBizEntityInfo = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.biz_entity_info = biz_entity_info
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.biz_entity_info:
            self.biz_entity_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_entity_info is not None:
            result['BizEntityInfo'] = self.biz_entity_info.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizEntityInfo') is not None:
            temp_model = main_models.GetBizEntityInfoResponseBodyBizEntityInfo()
            self.biz_entity_info = temp_model.from_map(m.get('BizEntityInfo'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBizEntityInfoResponseBodyBizEntityInfo(DaraModel):
    def __init__(
        self,
        biz_object: main_models.GetBizEntityInfoResponseBodyBizEntityInfoBizObject = None,
        biz_process: main_models.GetBizEntityInfoResponseBodyBizEntityInfoBizProcess = None,
        biz_unit_id: int = None,
        data_domain_id: int = None,
        type: str = None,
    ):
        self.biz_object = biz_object
        self.biz_process = biz_process
        self.biz_unit_id = biz_unit_id
        self.data_domain_id = data_domain_id
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
            temp_model = main_models.GetBizEntityInfoResponseBodyBizEntityInfoBizObject()
            self.biz_object = temp_model.from_map(m.get('BizObject'))

        if m.get('BizProcess') is not None:
            temp_model = main_models.GetBizEntityInfoResponseBodyBizEntityInfoBizProcess()
            self.biz_process = temp_model.from_map(m.get('BizProcess'))

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('DataDomainId') is not None:
            self.data_domain_id = m.get('DataDomainId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetBizEntityInfoResponseBodyBizEntityInfoBizProcess(DaraModel):
    def __init__(
        self,
        approval_id: str = None,
        approval_status: str = None,
        biz_event_entity_id_list: List[int] = None,
        description: str = None,
        display_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_dependent: bool = None,
        id: int = None,
        last_modifier: str = None,
        last_modifier_name: str = None,
        name: str = None,
        online_status: str = None,
        owner_name: str = None,
        owner_user_id: str = None,
        pre_biz_process_id_list: List[int] = None,
        ref_biz_entity_id_list: List[int] = None,
        ref_fact_table_count: int = None,
        status: str = None,
        type: str = None,
    ):
        self.approval_id = approval_id
        self.approval_status = approval_status
        self.biz_event_entity_id_list = biz_event_entity_id_list
        self.description = description
        self.display_name = display_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.has_dependent = has_dependent
        self.id = id
        self.last_modifier = last_modifier
        self.last_modifier_name = last_modifier_name
        self.name = name
        self.online_status = online_status
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id
        self.pre_biz_process_id_list = pre_biz_process_id_list
        self.ref_biz_entity_id_list = ref_biz_entity_id_list
        self.ref_fact_table_count = ref_fact_table_count
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id

        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.biz_event_entity_id_list is not None:
            result['BizEventEntityIdList'] = self.biz_event_entity_id_list

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.has_dependent is not None:
            result['HasDependent'] = self.has_dependent

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.last_modifier_name is not None:
            result['LastModifierName'] = self.last_modifier_name

        if self.name is not None:
            result['Name'] = self.name

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.pre_biz_process_id_list is not None:
            result['PreBizProcessIdList'] = self.pre_biz_process_id_list

        if self.ref_biz_entity_id_list is not None:
            result['RefBizEntityIdList'] = self.ref_biz_entity_id_list

        if self.ref_fact_table_count is not None:
            result['RefFactTableCount'] = self.ref_fact_table_count

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')

        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('BizEventEntityIdList') is not None:
            self.biz_event_entity_id_list = m.get('BizEventEntityIdList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HasDependent') is not None:
            self.has_dependent = m.get('HasDependent')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LastModifierName') is not None:
            self.last_modifier_name = m.get('LastModifierName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('PreBizProcessIdList') is not None:
            self.pre_biz_process_id_list = m.get('PreBizProcessIdList')

        if m.get('RefBizEntityIdList') is not None:
            self.ref_biz_entity_id_list = m.get('RefBizEntityIdList')

        if m.get('RefFactTableCount') is not None:
            self.ref_fact_table_count = m.get('RefFactTableCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetBizEntityInfoResponseBodyBizEntityInfoBizObject(DaraModel):
    def __init__(
        self,
        approval_id: str = None,
        approval_status: str = None,
        child_biz_entity_id_list: List[int] = None,
        description: str = None,
        display_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        last_modifier: str = None,
        last_modifier_name: str = None,
        name: str = None,
        online_status: str = None,
        owner_name: str = None,
        owner_user_id: str = None,
        parent_id: int = None,
        ref_biz_entity_id_list: List[int] = None,
        ref_dim_table_count: int = None,
        ref_summary_table_count: int = None,
        status: str = None,
        type: str = None,
    ):
        self.approval_id = approval_id
        self.approval_status = approval_status
        self.child_biz_entity_id_list = child_biz_entity_id_list
        self.description = description
        self.display_name = display_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.last_modifier = last_modifier
        self.last_modifier_name = last_modifier_name
        self.name = name
        self.online_status = online_status
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id
        self.parent_id = parent_id
        self.ref_biz_entity_id_list = ref_biz_entity_id_list
        self.ref_dim_table_count = ref_dim_table_count
        self.ref_summary_table_count = ref_summary_table_count
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id

        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.child_biz_entity_id_list is not None:
            result['ChildBizEntityIdList'] = self.child_biz_entity_id_list

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.last_modifier_name is not None:
            result['LastModifierName'] = self.last_modifier_name

        if self.name is not None:
            result['Name'] = self.name

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.ref_biz_entity_id_list is not None:
            result['RefBizEntityIdList'] = self.ref_biz_entity_id_list

        if self.ref_dim_table_count is not None:
            result['RefDimTableCount'] = self.ref_dim_table_count

        if self.ref_summary_table_count is not None:
            result['RefSummaryTableCount'] = self.ref_summary_table_count

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')

        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('ChildBizEntityIdList') is not None:
            self.child_biz_entity_id_list = m.get('ChildBizEntityIdList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LastModifierName') is not None:
            self.last_modifier_name = m.get('LastModifierName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RefBizEntityIdList') is not None:
            self.ref_biz_entity_id_list = m.get('RefBizEntityIdList')

        if m.get('RefDimTableCount') is not None:
            self.ref_dim_table_count = m.get('RefDimTableCount')

        if m.get('RefSummaryTableCount') is not None:
            self.ref_summary_table_count = m.get('RefSummaryTableCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

