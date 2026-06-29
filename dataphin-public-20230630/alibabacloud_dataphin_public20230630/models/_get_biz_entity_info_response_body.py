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
        # The business entity details.
        self.biz_entity_info = biz_entity_info
        # The error code. A value of OK indicates that the request was successful.
        self.code = code
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        # The business object.
        self.biz_object = biz_object
        # The business process.
        self.biz_process = biz_process
        # The ID of the business unit to which the business process belongs.
        self.biz_unit_id = biz_unit_id
        # The ID of the data domain to which the business process belongs.
        self.data_domain_id = data_domain_id
        # The business entity type. For more information, refer to the create business entity operation.
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
        # The approval flow ID.
        self.approval_id = approval_id
        # The approval status. Valid values:
        # - INIT: Not submitted.
        # - APPROVING: Pending approval.
        # - AGREE: Approved.
        # - REJECT: Rejected.
        # - FAILED: Validation failed.
        # - REVOKE: Withdrawn.
        self.approval_status = approval_status
        # The list of business event activity IDs contained in the business flow activity. This parameter is valid only when the entity is a business flow activity.
        self.biz_event_entity_id_list = biz_event_entity_id_list
        # The description of the business process.
        self.description = description
        # The display name of the business process.
        self.display_name = display_name
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # Indicates whether the business process is depended on by other entities.
        self.has_dependent = has_dependent
        # The business process ID.
        self.id = id
        # The ID of the user who last modified the business object.
        self.last_modifier = last_modifier
        # The name of the user who last modified the business object.
        self.last_modifier_name = last_modifier_name
        # The name of the business process.
        self.name = name
        # The publish status. Valid values: 
        # - SUBMITTED: Not published.
        # - APPROVING: Pending approval.
        # - PUBLISHED: Published.
        # - REJECT: Publish failed.
        self.online_status = online_status
        # The owner of the business object.
        self.owner_name = owner_name
        # The owner of the business object.
        self.owner_user_id = owner_user_id
        # The preceding business flow activities of the business flow activity.
        self.pre_biz_process_id_list = pre_biz_process_id_list
        # The list of associated published business entity IDs.
        self.ref_biz_entity_id_list = ref_biz_entity_id_list
        # The number of associated fact tables.
        self.ref_fact_table_count = ref_fact_table_count
        # The status. Valid values:
        # - DRAFT: Draft or not published.
        # - SUBMITTING: Submitting.
        # - SUBMITTED: Submitted.
        # - DEVELOPING: Developing.
        # - PUBLISHING: Publishing.
        # - PUBLISHED: Published.
        self.status = status
        # The type of the business process. For more information, refer to the create business entity operation.
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
        # The approval flow ID.
        self.approval_id = approval_id
        # The approval status. Valid values:
        # - INIT: Not submitted.
        # - APPROVING: Pending approval.
        # - AGREE: Approved.
        # - REJECT: Rejected.
        # - FAILED: Validation failed.
        # - REVOKE: Withdrawn.
        self.approval_status = approval_status
        # The list of child business objects of the business object.
        self.child_biz_entity_id_list = child_biz_entity_id_list
        # The description of the business object.
        self.description = description
        # The display name of the business object.
        self.display_name = display_name
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The business object ID.
        self.id = id
        # The ID of the user who last modified the business object.
        self.last_modifier = last_modifier
        # The name of the user who last modified the business object.
        self.last_modifier_name = last_modifier_name
        # The code name of the business object.
        self.name = name
        # The publish status. Valid values: 
        # - SUBMITTED: Not published.
        # - APPROVING: Pending approval.
        # - PUBLISHED: Published.
        # - REJECT: Publish failed.
        self.online_status = online_status
        # The owner of the business object.
        self.owner_name = owner_name
        # The owner of the business object.
        self.owner_user_id = owner_user_id
        # The parent entity that the business object inherits from. Only common business objects support inheritance, and the parent entity must be a published business object.
        self.parent_id = parent_id
        # The list of associated published business entity IDs.
        self.ref_biz_entity_id_list = ref_biz_entity_id_list
        # The number of associated logical dimension tables.
        self.ref_dim_table_count = ref_dim_table_count
        # The number of associated aggregate tables.
        self.ref_summary_table_count = ref_summary_table_count
        # The status. Valid values:
        # - DRAFT: Draft or not published.
        # - SUBMITTING: Submitting.
        # - SUBMITTED: Submitted.
        # - DEVELOPING: Developing.
        # - PUBLISHING: Publishing.
        # - PUBLISHED: Published.
        self.status = status
        # The object type of the business object. For more information, refer to the create business entity operation.
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

