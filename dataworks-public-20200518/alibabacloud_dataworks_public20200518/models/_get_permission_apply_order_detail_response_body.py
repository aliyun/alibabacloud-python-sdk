# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetPermissionApplyOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        apply_order_detail: main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetail = None,
        request_id: str = None,
    ):
        # Details of the permission request order.
        self.apply_order_detail = apply_order_detail
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.apply_order_detail:
            self.apply_order_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_order_detail is not None:
            result['ApplyOrderDetail'] = self.apply_order_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyOrderDetail') is not None:
            temp_model = main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetail()
            self.apply_order_detail = temp_model.from_map(m.get('ApplyOrderDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPermissionApplyOrderDetailResponseBodyApplyOrderDetail(DaraModel):
    def __init__(
        self,
        apply_base_id: str = None,
        apply_timestamp: int = None,
        approve_account_list: List[main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveAccountList] = None,
        approve_content: main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContent = None,
        finish_aapproval_timestamp: int = None,
        finish_approval_comment: str = None,
        flow_id: str = None,
        flow_status: int = None,
        grantee_object_list: List[main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailGranteeObjectList] = None,
    ):
        # The ID of the Alibaba Cloud account that was used to submit the permission request order.
        self.apply_base_id = apply_base_id
        # The time when the permission request order was submitted. The value is a UNIX timestamp.
        self.apply_timestamp = apply_timestamp
        # The list of Alibaba Cloud accounts that are used to process the permission request order.
        self.approve_account_list = approve_account_list
        # The content of the permission request.
        self.approve_content = approve_content
        self.finish_aapproval_timestamp = finish_aapproval_timestamp
        self.finish_approval_comment = finish_approval_comment
        # The ID of the permission request order.
        self.flow_id = flow_id
        # The status of the permission request order. Valid values:
        # 
        # *   1: to be processed
        # *   2: approved and authorized
        # *   3: approved but authorization failed
        # *   4: rejected
        self.flow_status = flow_status
        # The information about the account that is used to request permissions.
        self.grantee_object_list = grantee_object_list

    def validate(self):
        if self.approve_account_list:
            for v1 in self.approve_account_list:
                 if v1:
                    v1.validate()
        if self.approve_content:
            self.approve_content.validate()
        if self.grantee_object_list:
            for v1 in self.grantee_object_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_base_id is not None:
            result['ApplyBaseId'] = self.apply_base_id

        if self.apply_timestamp is not None:
            result['ApplyTimestamp'] = self.apply_timestamp

        result['ApproveAccountList'] = []
        if self.approve_account_list is not None:
            for k1 in self.approve_account_list:
                result['ApproveAccountList'].append(k1.to_map() if k1 else None)

        if self.approve_content is not None:
            result['ApproveContent'] = self.approve_content.to_map()

        if self.finish_aapproval_timestamp is not None:
            result['FinishAapprovalTimestamp'] = self.finish_aapproval_timestamp

        if self.finish_approval_comment is not None:
            result['FinishApprovalComment'] = self.finish_approval_comment

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status

        result['GranteeObjectList'] = []
        if self.grantee_object_list is not None:
            for k1 in self.grantee_object_list:
                result['GranteeObjectList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyBaseId') is not None:
            self.apply_base_id = m.get('ApplyBaseId')

        if m.get('ApplyTimestamp') is not None:
            self.apply_timestamp = m.get('ApplyTimestamp')

        self.approve_account_list = []
        if m.get('ApproveAccountList') is not None:
            for k1 in m.get('ApproveAccountList'):
                temp_model = main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveAccountList()
                self.approve_account_list.append(temp_model.from_map(k1))

        if m.get('ApproveContent') is not None:
            temp_model = main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContent()
            self.approve_content = temp_model.from_map(m.get('ApproveContent'))

        if m.get('FinishAapprovalTimestamp') is not None:
            self.finish_aapproval_timestamp = m.get('FinishAapprovalTimestamp')

        if m.get('FinishApprovalComment') is not None:
            self.finish_approval_comment = m.get('FinishApprovalComment')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')

        self.grantee_object_list = []
        if m.get('GranteeObjectList') is not None:
            for k1 in m.get('GranteeObjectList'):
                temp_model = main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailGranteeObjectList()
                self.grantee_object_list.append(temp_model.from_map(k1))

        return self

class GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailGranteeObjectList(DaraModel):
    def __init__(
        self,
        grantee_id: str = None,
        grantee_name: str = None,
        grantee_type: int = None,
        grantee_type_sub: int = None,
    ):
        # The ID of the account that is used to request permissions.
        self.grantee_id = grantee_id
        # The name of the account that is used to request permissions. The name is in the same format as that of the account used to access the MaxCompute project.
        # 
        # *   If the account is an Alibaba Cloud account, the value is in the ALIYUN$+Account name format.
        # *   If the account is a RAM user, the value is in the RAM$+Account name format.
        self.grantee_name = grantee_name
        # The type of the subject that requests permissions. The value is fixed as 1, which indicates users.
        self.grantee_type = grantee_type
        # The subtype of the subject that requests permissions. Valid values:
        # 
        # *   101: production account
        # *   103: individual account
        # *   105: account that requests permissions for others
        self.grantee_type_sub = grantee_type_sub

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grantee_id is not None:
            result['GranteeId'] = self.grantee_id

        if self.grantee_name is not None:
            result['GranteeName'] = self.grantee_name

        if self.grantee_type is not None:
            result['GranteeType'] = self.grantee_type

        if self.grantee_type_sub is not None:
            result['GranteeTypeSub'] = self.grantee_type_sub

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GranteeId') is not None:
            self.grantee_id = m.get('GranteeId')

        if m.get('GranteeName') is not None:
            self.grantee_name = m.get('GranteeName')

        if m.get('GranteeType') is not None:
            self.grantee_type = m.get('GranteeType')

        if m.get('GranteeTypeSub') is not None:
            self.grantee_type_sub = m.get('GranteeTypeSub')

        return self

class GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContent(DaraModel):
    def __init__(
        self,
        apply_reason: str = None,
        deadline: int = None,
        order_type: int = None,
        project_meta: main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContentProjectMeta = None,
    ):
        # The reason of the permission request. The administrator processes the request based on the reason.
        self.apply_reason = apply_reason
        # The expiration time of the permissions that you request. The value is a UNIX timestamp. If LabelSecurity is disabled for the MaxCompute project in which you want to request permissions on the fields of a table, or the security level of the fields is 0 or is lower than or equal to the security level of the Alibaba Cloud account for which you want to request permissions, you can request only permanent permissions.
        self.deadline = deadline
        # The type of the permission request order. The parameter value is 1 and cannot be changed. This value indicates ACL-based authorization.
        self.order_type = order_type
        # The information about the project and workspace that are associated with the object on which you request permissions.
        self.project_meta = project_meta

    def validate(self):
        if self.project_meta:
            self.project_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_reason is not None:
            result['ApplyReason'] = self.apply_reason

        if self.deadline is not None:
            result['Deadline'] = self.deadline

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.project_meta is not None:
            result['ProjectMeta'] = self.project_meta.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyReason') is not None:
            self.apply_reason = m.get('ApplyReason')

        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ProjectMeta') is not None:
            temp_model = main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContentProjectMeta()
            self.project_meta = temp_model.from_map(m.get('ProjectMeta'))

        return self

class GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContentProjectMeta(DaraModel):
    def __init__(
        self,
        max_compute_project_name: str = None,
        object_meta_list: List[main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContentProjectMetaObjectMetaList] = None,
        workspace_id: int = None,
    ):
        # The MaxCompute project to which the object on which you request permissions belongs.
        self.max_compute_project_name = max_compute_project_name
        # The details about the object on which you request permissions.
        self.object_meta_list = object_meta_list
        # The ID of the DataWorks workspace that is associated with the object on which you request permissions.
        self.workspace_id = workspace_id

    def validate(self):
        if self.object_meta_list:
            for v1 in self.object_meta_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_compute_project_name is not None:
            result['MaxComputeProjectName'] = self.max_compute_project_name

        result['ObjectMetaList'] = []
        if self.object_meta_list is not None:
            for k1 in self.object_meta_list:
                result['ObjectMetaList'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxComputeProjectName') is not None:
            self.max_compute_project_name = m.get('MaxComputeProjectName')

        self.object_meta_list = []
        if m.get('ObjectMetaList') is not None:
            for k1 in m.get('ObjectMetaList'):
                temp_model = main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContentProjectMetaObjectMetaList()
                self.object_meta_list.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContentProjectMetaObjectMetaList(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        column_meta_list: List[main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContentProjectMetaObjectMetaListColumnMetaList] = None,
        object_name: str = None,
    ):
        self.actions = actions
        # The information about the column fields in the object on which you request permissions.
        self.column_meta_list = column_meta_list
        # The name of the table on which you request permissions.
        self.object_name = object_name

    def validate(self):
        if self.column_meta_list:
            for v1 in self.column_meta_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['Actions'] = self.actions

        result['ColumnMetaList'] = []
        if self.column_meta_list is not None:
            for k1 in self.column_meta_list:
                result['ColumnMetaList'].append(k1.to_map() if k1 else None)

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')

        self.column_meta_list = []
        if m.get('ColumnMetaList') is not None:
            for k1 in m.get('ColumnMetaList'):
                temp_model = main_models.GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContentProjectMetaObjectMetaListColumnMetaList()
                self.column_meta_list.append(temp_model.from_map(k1))

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        return self

class GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveContentProjectMetaObjectMetaListColumnMetaList(DaraModel):
    def __init__(
        self,
        column_actions: List[str] = None,
        column_comment: str = None,
        column_name: str = None,
        security_level: str = None,
    ):
        self.column_actions = column_actions
        # The description of the column on which you request permissions.
        self.column_comment = column_comment
        # The name of the column on which you request permissions.
        self.column_name = column_name
        # The security level of the column on which you request permissions. Valid values: 0 to 9.
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_actions is not None:
            result['ColumnActions'] = self.column_actions

        if self.column_comment is not None:
            result['ColumnComment'] = self.column_comment

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnActions') is not None:
            self.column_actions = m.get('ColumnActions')

        if m.get('ColumnComment') is not None:
            self.column_comment = m.get('ColumnComment')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        return self

class GetPermissionApplyOrderDetailResponseBodyApplyOrderDetailApproveAccountList(DaraModel):
    def __init__(
        self,
        base_id: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used to process the permission request order.
        self.base_id = base_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_id is not None:
            result['BaseId'] = self.base_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseId') is not None:
            self.base_id = m.get('BaseId')

        return self

