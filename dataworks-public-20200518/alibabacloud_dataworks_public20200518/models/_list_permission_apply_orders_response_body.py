# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListPermissionApplyOrdersResponseBody(DaraModel):
    def __init__(
        self,
        apply_orders: main_models.ListPermissionApplyOrdersResponseBodyApplyOrders = None,
        request_id: str = None,
    ):
        # The paginated query results of permission requests.
        self.apply_orders = apply_orders
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.apply_orders:
            self.apply_orders.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_orders is not None:
            result['ApplyOrders'] = self.apply_orders.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyOrders') is not None:
            temp_model = main_models.ListPermissionApplyOrdersResponseBodyApplyOrders()
            self.apply_orders = temp_model.from_map(m.get('ApplyOrders'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPermissionApplyOrdersResponseBodyApplyOrders(DaraModel):
    def __init__(
        self,
        apply_order: List[main_models.ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrder] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of permission requests.
        self.apply_order = apply_order
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of permission requests returned.
        self.total_count = total_count

    def validate(self):
        if self.apply_order:
            for v1 in self.apply_order:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplyOrder'] = []
        if self.apply_order is not None:
            for k1 in self.apply_order:
                result['ApplyOrder'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_order = []
        if m.get('ApplyOrder') is not None:
            for k1 in m.get('ApplyOrder'):
                temp_model = main_models.ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrder()
                self.apply_order.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrder(DaraModel):
    def __init__(
        self,
        apply_base_id: str = None,
        apply_timestamp: int = None,
        approve_content: main_models.ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrderApproveContent = None,
        finish_approval_comment: str = None,
        finish_approval_timestamp: int = None,
        flow_id: str = None,
        flow_status: int = None,
    ):
        # The Alibaba Cloud account ID of the user who submitted the permission request.
        self.apply_base_id = apply_base_id
        # The time when the permission request was submitted, in Unix timestamp format.
        self.apply_timestamp = apply_timestamp
        # The content of the permission request.
        self.approve_content = approve_content
        # The final approval comment.
        self.finish_approval_comment = finish_approval_comment
        # The final approval timestamp. Displayed as a Unix timestamp.
        self.finish_approval_timestamp = finish_approval_timestamp
        # The permission request ID.
        self.flow_id = flow_id
        # The status of the permission request. Valid values:
        # 
        # *   1: Pending approval
        # *   2: Approved and authorization succeeded
        # *   3: Approved but authorization failed
        # *   4: Rejected
        self.flow_status = flow_status

    def validate(self):
        if self.approve_content:
            self.approve_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_base_id is not None:
            result['ApplyBaseId'] = self.apply_base_id

        if self.apply_timestamp is not None:
            result['ApplyTimestamp'] = self.apply_timestamp

        if self.approve_content is not None:
            result['ApproveContent'] = self.approve_content.to_map()

        if self.finish_approval_comment is not None:
            result['FinishApprovalComment'] = self.finish_approval_comment

        if self.finish_approval_timestamp is not None:
            result['FinishApprovalTimestamp'] = self.finish_approval_timestamp

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyBaseId') is not None:
            self.apply_base_id = m.get('ApplyBaseId')

        if m.get('ApplyTimestamp') is not None:
            self.apply_timestamp = m.get('ApplyTimestamp')

        if m.get('ApproveContent') is not None:
            temp_model = main_models.ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrderApproveContent()
            self.approve_content = temp_model.from_map(m.get('ApproveContent'))

        if m.get('FinishApprovalComment') is not None:
            self.finish_approval_comment = m.get('FinishApprovalComment')

        if m.get('FinishApprovalTimestamp') is not None:
            self.finish_approval_timestamp = m.get('FinishApprovalTimestamp')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')

        return self

class ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrderApproveContent(DaraModel):
    def __init__(
        self,
        apply_reason: str = None,
        order_type: int = None,
        project_meta: main_models.ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrderApproveContentProjectMeta = None,
    ):
        # The reason for the permission request, which is used by administrators for evaluation and approval.
        self.apply_reason = apply_reason
        # The type of permission request. Only the value 1 is supported, which indicates an ACL permission request for objects.
        self.order_type = order_type
        # The content of the requested object.
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

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.project_meta is not None:
            result['ProjectMeta'] = self.project_meta.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyReason') is not None:
            self.apply_reason = m.get('ApplyReason')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ProjectMeta') is not None:
            temp_model = main_models.ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrderApproveContentProjectMeta()
            self.project_meta = temp_model.from_map(m.get('ProjectMeta'))

        return self

class ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrderApproveContentProjectMeta(DaraModel):
    def __init__(
        self,
        object_meta_list: List[main_models.ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrderApproveContentProjectMetaObjectMetaList] = None,
        workspace_name: str = None,
    ):
        # The information about the requested object.
        self.object_meta_list = object_meta_list
        # The name of the DataWorks workspace that contains the MaxCompute project for which permissions are requested.
        self.workspace_name = workspace_name

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
        result['ObjectMetaList'] = []
        if self.object_meta_list is not None:
            for k1 in self.object_meta_list:
                result['ObjectMetaList'].append(k1.to_map() if k1 else None)

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_meta_list = []
        if m.get('ObjectMetaList') is not None:
            for k1 in m.get('ObjectMetaList'):
                temp_model = main_models.ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrderApproveContentProjectMetaObjectMetaList()
                self.object_meta_list.append(temp_model.from_map(k1))

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class ListPermissionApplyOrdersResponseBodyApplyOrdersApplyOrderApproveContentProjectMetaObjectMetaList(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        object_name: str = None,
    ):
        # The operation type.
        self.actions = actions
        # The name of the requested table.
        self.object_name = object_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['Actions'] = self.actions

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        return self

