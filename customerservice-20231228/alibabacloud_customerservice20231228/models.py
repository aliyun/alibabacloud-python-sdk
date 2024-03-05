# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class DataValue(TeaModel):
    def __init__(
        self,
        doc_id: int = None,
        name: str = None,
        file_name: str = None,
        url: str = None,
        upload_time: str = None,
        order_id: str = None,
        apply_id: str = None,
    ):
        self.doc_id = doc_id
        self.name = name
        self.file_name = file_name
        self.url = url
        self.upload_time = upload_time
        self.order_id = order_id
        self.apply_id = apply_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.name is not None:
            result['name'] = self.name
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.url is not None:
            result['url'] = self.url
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        return self


class GetDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        file_key: str = None,
        free_order_apply_code: str = None,
        order_id: str = None,
        scene: str = None,
    ):
        self.file_id = file_id
        self.file_key = file_key
        self.free_order_apply_code = free_order_apply_code
        self.order_id = order_id
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_key is not None:
            result['fileKey'] = self.file_key
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileKey') is not None:
            self.file_key = m.get('fileKey')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class GetDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDownloadUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseSupportPlanDetailRequest(TeaModel):
    def __init__(
        self,
        free_order_apply_codes: List[str] = None,
        order_ids: List[int] = None,
    ):
        self.free_order_apply_codes = free_order_apply_codes
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.free_order_apply_codes is not None:
            result['freeOrderApplyCodes'] = self.free_order_apply_codes
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('freeOrderApplyCodes') is not None:
            self.free_order_apply_codes = m.get('freeOrderApplyCodes')
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataDingGroups(TeaModel):
    def __init__(
        self,
        main_ding_department_id: str = None,
        main_ding_group_id: str = None,
        main_ding_group_name: str = None,
        sub_ding_department_id: str = None,
        sub_ding_group_id: str = None,
        sub_ding_group_name: str = None,
    ):
        self.main_ding_department_id = main_ding_department_id
        self.main_ding_group_id = main_ding_group_id
        self.main_ding_group_name = main_ding_group_name
        self.sub_ding_department_id = sub_ding_department_id
        self.sub_ding_group_id = sub_ding_group_id
        self.sub_ding_group_name = sub_ding_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_ding_department_id is not None:
            result['mainDingDepartmentId'] = self.main_ding_department_id
        if self.main_ding_group_id is not None:
            result['mainDingGroupId'] = self.main_ding_group_id
        if self.main_ding_group_name is not None:
            result['mainDingGroupName'] = self.main_ding_group_name
        if self.sub_ding_department_id is not None:
            result['subDingDepartmentId'] = self.sub_ding_department_id
        if self.sub_ding_group_id is not None:
            result['subDingGroupId'] = self.sub_ding_group_id
        if self.sub_ding_group_name is not None:
            result['subDingGroupName'] = self.sub_ding_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mainDingDepartmentId') is not None:
            self.main_ding_department_id = m.get('mainDingDepartmentId')
        if m.get('mainDingGroupId') is not None:
            self.main_ding_group_id = m.get('mainDingGroupId')
        if m.get('mainDingGroupName') is not None:
            self.main_ding_group_name = m.get('mainDingGroupName')
        if m.get('subDingDepartmentId') is not None:
            self.sub_ding_department_id = m.get('subDingDepartmentId')
        if m.get('subDingGroupId') is not None:
            self.sub_ding_group_id = m.get('subDingGroupId')
        if m.get('subDingGroupName') is not None:
            self.sub_ding_group_name = m.get('subDingGroupName')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataDocs(TeaModel):
    def __init__(
        self,
        doc_id: int = None,
        file_name: str = None,
        free_order_apply_code: str = None,
        name: str = None,
        order_id: str = None,
        upload_time: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.file_name = file_name
        self.free_order_apply_code = free_order_apply_code
        self.name = name
        self.order_id = order_id
        self.upload_time = upload_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.name is not None:
            result['name'] = self.name
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesDocNode(TeaModel):
    def __init__(
        self,
        doc_id: int = None,
        doc_name: str = None,
        doc_submit_time: str = None,
        file_name: str = None,
        free_order_apply_code: str = None,
        order_id: str = None,
    ):
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.doc_submit_time = doc_submit_time
        self.file_name = file_name
        self.free_order_apply_code = free_order_apply_code
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_name is not None:
            result['docName'] = self.doc_name
        if self.doc_submit_time is not None:
            result['docSubmitTime'] = self.doc_submit_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')
        if m.get('docSubmitTime') is not None:
            self.doc_submit_time = m.get('docSubmitTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesFinishNode(TeaModel):
    def __init__(
        self,
        finish_time: str = None,
    ):
        self.finish_time = finish_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderAuditNode(TeaModel):
    def __init__(
        self,
        audit_time: str = None,
        status: str = None,
        status_name: str = None,
    ):
        self.audit_time = audit_time
        self.status = status
        self.status_name = status_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_time is not None:
            result['auditTime'] = self.audit_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_name is not None:
            result['statusName'] = self.status_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditTime') is not None:
            self.audit_time = m.get('auditTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusName') is not None:
            self.status_name = m.get('statusName')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderNode(TeaModel):
    def __init__(
        self,
        apply_time: str = None,
        uid: int = None,
    ):
        self.apply_time = apply_time
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesOrderNode(TeaModel):
    def __init__(
        self,
        pay_time: str = None,
        uid: int = None,
    ):
        self.pay_time = pay_time
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesServiceImplementation(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodes(TeaModel):
    def __init__(
        self,
        doc_node: GetEnterpriseSupportPlanDetailResponseBodyDataNodesDocNode = None,
        finish_node: GetEnterpriseSupportPlanDetailResponseBodyDataNodesFinishNode = None,
        free_order_audit_node: GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderAuditNode = None,
        free_order_node: GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderNode = None,
        name: str = None,
        order_date: int = None,
        order_node: GetEnterpriseSupportPlanDetailResponseBodyDataNodesOrderNode = None,
        service_implementation: GetEnterpriseSupportPlanDetailResponseBodyDataNodesServiceImplementation = None,
        status: int = None,
    ):
        self.doc_node = doc_node
        self.finish_node = finish_node
        self.free_order_audit_node = free_order_audit_node
        self.free_order_node = free_order_node
        self.name = name
        self.order_date = order_date
        self.order_node = order_node
        self.service_implementation = service_implementation
        self.status = status

    def validate(self):
        if self.doc_node:
            self.doc_node.validate()
        if self.finish_node:
            self.finish_node.validate()
        if self.free_order_audit_node:
            self.free_order_audit_node.validate()
        if self.free_order_node:
            self.free_order_node.validate()
        if self.order_node:
            self.order_node.validate()
        if self.service_implementation:
            self.service_implementation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_node is not None:
            result['docNode'] = self.doc_node.to_map()
        if self.finish_node is not None:
            result['finishNode'] = self.finish_node.to_map()
        if self.free_order_audit_node is not None:
            result['freeOrderAuditNode'] = self.free_order_audit_node.to_map()
        if self.free_order_node is not None:
            result['freeOrderNode'] = self.free_order_node.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.order_date is not None:
            result['orderDate'] = self.order_date
        if self.order_node is not None:
            result['orderNode'] = self.order_node.to_map()
        if self.service_implementation is not None:
            result['serviceImplementation'] = self.service_implementation.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesDocNode()
            self.doc_node = temp_model.from_map(m['docNode'])
        if m.get('finishNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesFinishNode()
            self.finish_node = temp_model.from_map(m['finishNode'])
        if m.get('freeOrderAuditNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderAuditNode()
            self.free_order_audit_node = temp_model.from_map(m['freeOrderAuditNode'])
        if m.get('freeOrderNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderNode()
            self.free_order_node = temp_model.from_map(m['freeOrderNode'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderDate') is not None:
            self.order_date = m.get('orderDate')
        if m.get('orderNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesOrderNode()
            self.order_node = temp_model.from_map(m['orderNode'])
        if m.get('serviceImplementation') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesServiceImplementation()
            self.service_implementation = temp_model.from_map(m['serviceImplementation'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataServiceItemsOperateList(TeaModel):
    def __init__(
        self,
        name: str = None,
        name_1: str = None,
    ):
        self.name = name
        self.name_1 = name_1

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.name_1 is not None:
            result['name1'] = self.name_1
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('name1') is not None:
            self.name_1 = m.get('name1')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataServiceItems(TeaModel):
    def __init__(
        self,
        content: str = None,
        desc: str = None,
        name: str = None,
        operate_list: List[GetEnterpriseSupportPlanDetailResponseBodyDataServiceItemsOperateList] = None,
    ):
        self.content = content
        self.desc = desc
        self.name = name
        self.operate_list = operate_list

    def validate(self):
        if self.operate_list:
            for k in self.operate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.desc is not None:
            result['desc'] = self.desc
        if self.name is not None:
            result['name'] = self.name
        result['operateList'] = []
        if self.operate_list is not None:
            for k in self.operate_list:
                result['operateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.operate_list = []
        if m.get('operateList') is not None:
            for k in m.get('operateList'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataServiceItemsOperateList()
                self.operate_list.append(temp_model.from_map(k))
        return self


class GetEnterpriseSupportPlanDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        can_apply_free_order: bool = None,
        customer_id: int = None,
        ding_groups: List[GetEnterpriseSupportPlanDetailResponseBodyDataDingGroups] = None,
        docs: List[GetEnterpriseSupportPlanDetailResponseBodyDataDocs] = None,
        end_time: str = None,
        first_pay_time: str = None,
        free_order_apply_code: str = None,
        free_order_apply_id: int = None,
        free_order_apply_time: str = None,
        free_order_approved_time: str = None,
        free_order_expect_start_time: str = None,
        instance_id: str = None,
        nodes: List[GetEnterpriseSupportPlanDetailResponseBodyDataNodes] = None,
        order_ids: List[int] = None,
        service_items: List[GetEnterpriseSupportPlanDetailResponseBodyDataServiceItems] = None,
        service_name: str = None,
        service_status: str = None,
        service_status_name: str = None,
        service_type: str = None,
        sort_time: str = None,
        start_time: str = None,
        task_num: int = None,
    ):
        self.can_apply_free_order = can_apply_free_order
        self.customer_id = customer_id
        self.ding_groups = ding_groups
        self.docs = docs
        self.end_time = end_time
        self.first_pay_time = first_pay_time
        self.free_order_apply_code = free_order_apply_code
        self.free_order_apply_id = free_order_apply_id
        self.free_order_apply_time = free_order_apply_time
        self.free_order_approved_time = free_order_approved_time
        self.free_order_expect_start_time = free_order_expect_start_time
        self.instance_id = instance_id
        self.nodes = nodes
        self.order_ids = order_ids
        self.service_items = service_items
        self.service_name = service_name
        self.service_status = service_status
        self.service_status_name = service_status_name
        self.service_type = service_type
        self.sort_time = sort_time
        self.start_time = start_time
        self.task_num = task_num

    def validate(self):
        if self.ding_groups:
            for k in self.ding_groups:
                if k:
                    k.validate()
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.service_items:
            for k in self.service_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_apply_free_order is not None:
            result['canApplyFreeOrder'] = self.can_apply_free_order
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        result['dingGroups'] = []
        if self.ding_groups is not None:
            for k in self.ding_groups:
                result['dingGroups'].append(k.to_map() if k else None)
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.first_pay_time is not None:
            result['firstPayTime'] = self.first_pay_time
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.free_order_apply_id is not None:
            result['freeOrderApplyId'] = self.free_order_apply_id
        if self.free_order_apply_time is not None:
            result['freeOrderApplyTime'] = self.free_order_apply_time
        if self.free_order_approved_time is not None:
            result['freeOrderApprovedTime'] = self.free_order_approved_time
        if self.free_order_expect_start_time is not None:
            result['freeOrderExpectStartTime'] = self.free_order_expect_start_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        result['serviceItems'] = []
        if self.service_items is not None:
            for k in self.service_items:
                result['serviceItems'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_status_name is not None:
            result['serviceStatusName'] = self.service_status_name
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.sort_time is not None:
            result['sortTime'] = self.sort_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.task_num is not None:
            result['taskNum'] = self.task_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canApplyFreeOrder') is not None:
            self.can_apply_free_order = m.get('canApplyFreeOrder')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        self.ding_groups = []
        if m.get('dingGroups') is not None:
            for k in m.get('dingGroups'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataDingGroups()
                self.ding_groups.append(temp_model.from_map(k))
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataDocs()
                self.docs.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('firstPayTime') is not None:
            self.first_pay_time = m.get('firstPayTime')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('freeOrderApplyId') is not None:
            self.free_order_apply_id = m.get('freeOrderApplyId')
        if m.get('freeOrderApplyTime') is not None:
            self.free_order_apply_time = m.get('freeOrderApplyTime')
        if m.get('freeOrderApprovedTime') is not None:
            self.free_order_approved_time = m.get('freeOrderApprovedTime')
        if m.get('freeOrderExpectStartTime') is not None:
            self.free_order_expect_start_time = m.get('freeOrderExpectStartTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.nodes = []
        if m.get('nodes') is not None:
            for k in m.get('nodes'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        self.service_items = []
        if m.get('serviceItems') is not None:
            for k in m.get('serviceItems'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataServiceItems()
                self.service_items.append(temp_model.from_map(k))
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('serviceStatusName') is not None:
            self.service_status_name = m.get('serviceStatusName')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('sortTime') is not None:
            self.sort_time = m.get('sortTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')
        return self


class GetEnterpriseSupportPlanDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEnterpriseSupportPlanDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnterpriseSupportPlanDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnterpriseSupportPlanDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPreViewUrlRequest(TeaModel):
    def __init__(
        self,
        apply_code: str = None,
        file_id: int = None,
        file_key: str = None,
        order_id: str = None,
        scene: str = None,
    ):
        self.apply_code = apply_code
        self.file_id = file_id
        self.file_key = file_key
        self.order_id = order_id
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_key is not None:
            result['fileKey'] = self.file_key
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileKey') is not None:
            self.file_key = m.get('fileKey')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class GetPreViewUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPreViewUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPreViewUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPreViewUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceDetailRequest(TeaModel):
    def __init__(
        self,
        apply_code: str = None,
    ):
        self.apply_code = apply_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        return self


class GetServiceDetailResponseBodyDataAppointments(TeaModel):
    def __init__(
        self,
        huhang_id: int = None,
        purchase_code: int = None,
        purchase_desc: str = None,
        support_days: int = None,
        travel_days: int = None,
    ):
        self.huhang_id = huhang_id
        self.purchase_code = purchase_code
        self.purchase_desc = purchase_desc
        self.support_days = support_days
        self.travel_days = travel_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.huhang_id is not None:
            result['huhangId'] = self.huhang_id
        if self.purchase_code is not None:
            result['purchaseCode'] = self.purchase_code
        if self.purchase_desc is not None:
            result['purchaseDesc'] = self.purchase_desc
        if self.support_days is not None:
            result['supportDays'] = self.support_days
        if self.travel_days is not None:
            result['travelDays'] = self.travel_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('huhangId') is not None:
            self.huhang_id = m.get('huhangId')
        if m.get('purchaseCode') is not None:
            self.purchase_code = m.get('purchaseCode')
        if m.get('purchaseDesc') is not None:
            self.purchase_desc = m.get('purchaseDesc')
        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')
        if m.get('travelDays') is not None:
            self.travel_days = m.get('travelDays')
        return self


class GetServiceDetailResponseBodyDataPayOrders(TeaModel):
    def __init__(
        self,
        amount: str = None,
        compass_commodity_code: str = None,
        compass_commodity_name: str = None,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        modifier_emp_id: str = None,
        operate: Dict[str, Any] = None,
        order_detail: Any = None,
        order_id: int = None,
        original_price: float = None,
        pay_amount: float = None,
        pay_time: str = None,
        product_name: str = None,
        rene_wal_url: str = None,
        service_content_map: Dict[str, Any] = None,
        status: int = None,
        status_str: str = None,
        support_days: int = None,
        uid: str = None,
        url: str = None,
    ):
        self.amount = amount
        self.compass_commodity_code = compass_commodity_code
        self.compass_commodity_name = compass_commodity_name
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.modifier_emp_id = modifier_emp_id
        self.operate = operate
        self.order_detail = order_detail
        self.order_id = order_id
        self.original_price = original_price
        self.pay_amount = pay_amount
        self.pay_time = pay_time
        self.product_name = product_name
        self.rene_wal_url = rene_wal_url
        self.service_content_map = service_content_map
        self.status = status
        self.status_str = status_str
        self.support_days = support_days
        self.uid = uid
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.compass_commodity_code is not None:
            result['compassCommodityCode'] = self.compass_commodity_code
        if self.compass_commodity_name is not None:
            result['compassCommodityName'] = self.compass_commodity_name
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.operate is not None:
            result['operate'] = self.operate
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.original_price is not None:
            result['originalPrice'] = self.original_price
        if self.pay_amount is not None:
            result['payAmount'] = self.pay_amount
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url
        if self.service_content_map is not None:
            result['serviceContentMap'] = self.service_content_map
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_days is not None:
            result['supportDays'] = self.support_days
        if self.uid is not None:
            result['uid'] = self.uid
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('compassCommodityCode') is not None:
            self.compass_commodity_code = m.get('compassCommodityCode')
        if m.get('compassCommodityName') is not None:
            self.compass_commodity_name = m.get('compassCommodityName')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('operate') is not None:
            self.operate = m.get('operate')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('originalPrice') is not None:
            self.original_price = m.get('originalPrice')
        if m.get('payAmount') is not None:
            self.pay_amount = m.get('payAmount')
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')
        if m.get('serviceContentMap') is not None:
            self.service_content_map = m.get('serviceContentMap')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersApplyFileVOList(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersExtList(TeaModel):
    def __init__(
        self,
        key_code: str = None,
        name: str = None,
        value: Any = None,
        view: str = None,
    ):
        self.key_code = key_code
        self.name = name
        self.value = value
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformanceNodeDTOS(TeaModel):
    def __init__(
        self,
        display: bool = None,
        extend_info: Any = None,
        index: int = None,
        node_name: str = None,
        status: int = None,
    ):
        self.display = display
        self.extend_info = extend_info
        self.index = index
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksApplyFileVOList(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksExtList(TeaModel):
    def __init__(
        self,
        key_code: str = None,
        name: str = None,
        value: Any = None,
        view: str = None,
    ):
        self.key_code = key_code
        self.name = name
        self.value = value
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksPerformanceNodeDTOS(TeaModel):
    def __init__(
        self,
        display: bool = None,
        extend_info: Any = None,
        index: int = None,
        node_name: str = None,
        status: int = None,
    ):
        self.display = display
        self.extend_info = extend_info
        self.index = index
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceMonthReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceSchemes(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksTamEngineers(TeaModel):
    def __init__(
        self,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hr_status: str = None,
        id: int = None,
        last_name: str = None,
        modifier_emp_id: str = None,
        name: str = None,
        nick_name_en: str = None,
        realm_id: int = None,
        workid: str = None,
    ):
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hr_status = hr_status
        self.id = id
        self.last_name = last_name
        self.modifier_emp_id = modifier_emp_id
        self.name = name
        self.nick_name_en = nick_name_en
        self.realm_id = realm_id
        self.workid = workid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacks(TeaModel):
    def __init__(
        self,
        apply_file_volist: List[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksApplyFileVOList] = None,
        appointment_code: str = None,
        appointment_end_time: int = None,
        appointment_id: str = None,
        appointment_pass_time: int = None,
        appointment_time: int = None,
        commodity_desc: str = None,
        creator_emp_id: str = None,
        cycle_service: bool = None,
        ext_list: List[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksExtList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        order_detail: Any = None,
        order_id: int = None,
        performance_node_dtos: List[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksPerformanceNodeDTOS] = None,
        purchase_pack_code: int = None,
        service_apply_id: int = None,
        service_month_reports: List[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceMonthReports] = None,
        service_reports: List[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceReports] = None,
        service_schemes: List[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceSchemes] = None,
        status: int = None,
        status_str: str = None,
        support_time: List[int] = None,
        tam_engineers: List[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksTamEngineers] = None,
    ):
        self.apply_file_volist = apply_file_volist
        self.appointment_code = appointment_code
        self.appointment_end_time = appointment_end_time
        self.appointment_id = appointment_id
        self.appointment_pass_time = appointment_pass_time
        self.appointment_time = appointment_time
        self.commodity_desc = commodity_desc
        self.creator_emp_id = creator_emp_id
        self.cycle_service = cycle_service
        self.ext_list = ext_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.order_detail = order_detail
        self.order_id = order_id
        self.performance_node_dtos = performance_node_dtos
        self.purchase_pack_code = purchase_pack_code
        self.service_apply_id = service_apply_id
        self.service_month_reports = service_month_reports
        self.service_reports = service_reports
        self.service_schemes = service_schemes
        self.status = status
        self.status_str = status_str
        self.support_time = support_time
        self.tam_engineers = tam_engineers

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersServiceMonthReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersServiceReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersServiceSchemes(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersTamEngineers(TeaModel):
    def __init__(
        self,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hr_status: str = None,
        id: int = None,
        last_name: str = None,
        modifier_emp_id: str = None,
        name: str = None,
        nick_name_en: str = None,
        realm_id: int = None,
        workid: str = None,
    ):
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hr_status = hr_status
        self.id = id
        self.last_name = last_name
        self.modifier_emp_id = modifier_emp_id
        self.name = name
        self.nick_name_en = nick_name_en
        self.realm_id = realm_id
        self.workid = workid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrders(TeaModel):
    def __init__(
        self,
        apply_file_volist: List[GetServiceDetailResponseBodyDataPerformanceOrdersApplyFileVOList] = None,
        appointment_code: str = None,
        appointment_end_time: int = None,
        appointment_id: str = None,
        appointment_pass_time: int = None,
        appointment_time: int = None,
        commodity_desc: str = None,
        creator_emp_id: str = None,
        cycle_service: bool = None,
        ext_list: List[GetServiceDetailResponseBodyDataPerformanceOrdersExtList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        order_detail: Any = None,
        order_id: int = None,
        pack_count: int = None,
        pack_details: List[Dict[str, Any]] = None,
        performance_node_dtos: List[GetServiceDetailResponseBodyDataPerformanceOrdersPerformanceNodeDTOS] = None,
        performance_packs: List[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacks] = None,
        purchase_pack_code: int = None,
        service_apply_id: int = None,
        service_month_reports: List[GetServiceDetailResponseBodyDataPerformanceOrdersServiceMonthReports] = None,
        service_reports: List[GetServiceDetailResponseBodyDataPerformanceOrdersServiceReports] = None,
        service_schemes: List[GetServiceDetailResponseBodyDataPerformanceOrdersServiceSchemes] = None,
        status: int = None,
        status_str: str = None,
        support_time: List[int] = None,
        tam_engineers: List[GetServiceDetailResponseBodyDataPerformanceOrdersTamEngineers] = None,
    ):
        self.apply_file_volist = apply_file_volist
        self.appointment_code = appointment_code
        self.appointment_end_time = appointment_end_time
        self.appointment_id = appointment_id
        self.appointment_pass_time = appointment_pass_time
        self.appointment_time = appointment_time
        self.commodity_desc = commodity_desc
        self.creator_emp_id = creator_emp_id
        self.cycle_service = cycle_service
        self.ext_list = ext_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.order_detail = order_detail
        self.order_id = order_id
        self.pack_count = pack_count
        self.pack_details = pack_details
        self.performance_node_dtos = performance_node_dtos
        self.performance_packs = performance_packs
        self.purchase_pack_code = purchase_pack_code
        self.service_apply_id = service_apply_id
        self.service_month_reports = service_month_reports
        self.service_reports = service_reports
        self.service_schemes = service_schemes
        self.status = status
        self.status_str = status_str
        self.support_time = support_time
        self.tam_engineers = tam_engineers

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.performance_packs:
            for k in self.performance_packs:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.pack_count is not None:
            result['packCount'] = self.pack_count
        if self.pack_details is not None:
            result['packDetails'] = self.pack_details
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k in self.performance_packs:
                result['performancePacks'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('packCount') is not None:
            self.pack_count = m.get('packCount')
        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k in m.get('performancePacks'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class GetServiceDetailResponseBodyDataPerformancePacksApplyFileVOList(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksExtList(TeaModel):
    def __init__(
        self,
        key_code: str = None,
        name: str = None,
        value: Any = None,
        view: str = None,
    ):
        self.key_code = key_code
        self.name = name
        self.value = value
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksPerformanceNodeDTOS(TeaModel):
    def __init__(
        self,
        display: bool = None,
        extend_info: Any = None,
        index: int = None,
        node_name: str = None,
        status: int = None,
    ):
        self.display = display
        self.extend_info = extend_info
        self.index = index
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksServiceMonthReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksServiceReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksServiceSchemes(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksTamEngineers(TeaModel):
    def __init__(
        self,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hr_status: str = None,
        id: int = None,
        last_name: str = None,
        modifier_emp_id: str = None,
        name: str = None,
        nick_name_en: str = None,
        realm_id: int = None,
        workid: str = None,
    ):
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hr_status = hr_status
        self.id = id
        self.last_name = last_name
        self.modifier_emp_id = modifier_emp_id
        self.name = name
        self.nick_name_en = nick_name_en
        self.realm_id = realm_id
        self.workid = workid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class GetServiceDetailResponseBodyDataPerformancePacks(TeaModel):
    def __init__(
        self,
        apply_file_volist: List[GetServiceDetailResponseBodyDataPerformancePacksApplyFileVOList] = None,
        appointment_code: str = None,
        appointment_end_time: int = None,
        appointment_id: str = None,
        appointment_pass_time: int = None,
        appointment_time: int = None,
        commodity_desc: str = None,
        creator_emp_id: str = None,
        cycle_service: bool = None,
        ext_list: List[GetServiceDetailResponseBodyDataPerformancePacksExtList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        order_detail: Any = None,
        order_id: int = None,
        performance_node_dtos: List[GetServiceDetailResponseBodyDataPerformancePacksPerformanceNodeDTOS] = None,
        purchase_pack_code: int = None,
        service_apply_id: int = None,
        service_month_reports: List[GetServiceDetailResponseBodyDataPerformancePacksServiceMonthReports] = None,
        service_reports: List[GetServiceDetailResponseBodyDataPerformancePacksServiceReports] = None,
        service_schemes: List[GetServiceDetailResponseBodyDataPerformancePacksServiceSchemes] = None,
        status: int = None,
        status_str: str = None,
        support_time: List[int] = None,
        tam_engineers: List[GetServiceDetailResponseBodyDataPerformancePacksTamEngineers] = None,
    ):
        self.apply_file_volist = apply_file_volist
        self.appointment_code = appointment_code
        self.appointment_end_time = appointment_end_time
        self.appointment_id = appointment_id
        self.appointment_pass_time = appointment_pass_time
        self.appointment_time = appointment_time
        self.commodity_desc = commodity_desc
        self.creator_emp_id = creator_emp_id
        self.cycle_service = cycle_service
        self.ext_list = ext_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.order_detail = order_detail
        self.order_id = order_id
        self.performance_node_dtos = performance_node_dtos
        self.purchase_pack_code = purchase_pack_code
        self.service_apply_id = service_apply_id
        self.service_month_reports = service_month_reports
        self.service_reports = service_reports
        self.service_schemes = service_schemes
        self.status = status
        self.status_str = status_str
        self.support_time = support_time
        self.tam_engineers = tam_engineers

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class GetServiceDetailResponseBodyDataServiceReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        applier_id: str = None,
        apply_code: str = None,
        apply_time: int = None,
        appointments: List[GetServiceDetailResponseBodyDataAppointments] = None,
        buy_url: str = None,
        creator_emp_id: str = None,
        customer_name: str = None,
        cycle_service: bool = None,
        executed_count: int = None,
        finish_count: int = None,
        form_map: Dict[str, Any] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        pack_details: List[Dict[str, Any]] = None,
        pay_orders: List[GetServiceDetailResponseBodyDataPayOrders] = None,
        pay_url: str = None,
        performance_orders: List[GetServiceDetailResponseBodyDataPerformanceOrders] = None,
        performance_packs: List[GetServiceDetailResponseBodyDataPerformancePacks] = None,
        rene_wal_url: str = None,
        service_code: str = None,
        service_name: str = None,
        service_reports: List[GetServiceDetailResponseBodyDataServiceReports] = None,
        service_time_range: List[int] = None,
        status: str = None,
        status_code: int = None,
        status_str: str = None,
        term_of_validity: str = None,
        total_pack: int = None,
        type: str = None,
        use_pack: int = None,
    ):
        self.applier_id = applier_id
        self.apply_code = apply_code
        self.apply_time = apply_time
        self.appointments = appointments
        self.buy_url = buy_url
        self.creator_emp_id = creator_emp_id
        self.customer_name = customer_name
        self.cycle_service = cycle_service
        self.executed_count = executed_count
        self.finish_count = finish_count
        self.form_map = form_map
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.pack_details = pack_details
        self.pay_orders = pay_orders
        self.pay_url = pay_url
        self.performance_orders = performance_orders
        self.performance_packs = performance_packs
        self.rene_wal_url = rene_wal_url
        self.service_code = service_code
        self.service_name = service_name
        self.service_reports = service_reports
        self.service_time_range = service_time_range
        self.status = status
        self.status_code = status_code
        self.status_str = status_str
        self.term_of_validity = term_of_validity
        self.total_pack = total_pack
        self.type = type
        self.use_pack = use_pack

    def validate(self):
        if self.appointments:
            for k in self.appointments:
                if k:
                    k.validate()
        if self.pay_orders:
            for k in self.pay_orders:
                if k:
                    k.validate()
        if self.performance_orders:
            for k in self.performance_orders:
                if k:
                    k.validate()
        if self.performance_packs:
            for k in self.performance_packs:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applier_id is not None:
            result['applierId'] = self.applier_id
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        result['appointments'] = []
        if self.appointments is not None:
            for k in self.appointments:
                result['appointments'].append(k.to_map() if k else None)
        if self.buy_url is not None:
            result['buyUrl'] = self.buy_url
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.customer_name is not None:
            result['customerName'] = self.customer_name
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        if self.executed_count is not None:
            result['executedCount'] = self.executed_count
        if self.finish_count is not None:
            result['finishCount'] = self.finish_count
        if self.form_map is not None:
            result['formMap'] = self.form_map
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.pack_details is not None:
            result['packDetails'] = self.pack_details
        result['payOrders'] = []
        if self.pay_orders is not None:
            for k in self.pay_orders:
                result['payOrders'].append(k.to_map() if k else None)
        if self.pay_url is not None:
            result['payUrl'] = self.pay_url
        result['performanceOrders'] = []
        if self.performance_orders is not None:
            for k in self.performance_orders:
                result['performanceOrders'].append(k.to_map() if k else None)
        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k in self.performance_packs:
                result['performancePacks'].append(k.to_map() if k else None)
        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        if self.service_time_range is not None:
            result['serviceTimeRange'] = self.service_time_range
        if self.status is not None:
            result['status'] = self.status
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.term_of_validity is not None:
            result['termOfValidity'] = self.term_of_validity
        if self.total_pack is not None:
            result['totalPack'] = self.total_pack
        if self.type is not None:
            result['type'] = self.type
        if self.use_pack is not None:
            result['usePack'] = self.use_pack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applierId') is not None:
            self.applier_id = m.get('applierId')
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        self.appointments = []
        if m.get('appointments') is not None:
            for k in m.get('appointments'):
                temp_model = GetServiceDetailResponseBodyDataAppointments()
                self.appointments.append(temp_model.from_map(k))
        if m.get('buyUrl') is not None:
            self.buy_url = m.get('buyUrl')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        if m.get('executedCount') is not None:
            self.executed_count = m.get('executedCount')
        if m.get('finishCount') is not None:
            self.finish_count = m.get('finishCount')
        if m.get('formMap') is not None:
            self.form_map = m.get('formMap')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')
        self.pay_orders = []
        if m.get('payOrders') is not None:
            for k in m.get('payOrders'):
                temp_model = GetServiceDetailResponseBodyDataPayOrders()
                self.pay_orders.append(temp_model.from_map(k))
        if m.get('payUrl') is not None:
            self.pay_url = m.get('payUrl')
        self.performance_orders = []
        if m.get('performanceOrders') is not None:
            for k in m.get('performanceOrders'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrders()
                self.performance_orders.append(temp_model.from_map(k))
        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k in m.get('performancePacks'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k))
        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = GetServiceDetailResponseBodyDataServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        if m.get('serviceTimeRange') is not None:
            self.service_time_range = m.get('serviceTimeRange')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('termOfValidity') is not None:
            self.term_of_validity = m.get('termOfValidity')
        if m.get('totalPack') is not None:
            self.total_pack = m.get('totalPack')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('usePack') is not None:
            self.use_pack = m.get('usePack')
        return self


class GetServiceDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetServiceDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetServiceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetServiceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetYunQiTaskByRecordIdRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['recordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        return self


class GetYunQiTaskByRecordIdResponseBodyData(TeaModel):
    def __init__(
        self,
        chat_id: str = None,
        create_time: int = None,
        creator_name: str = None,
        end_time: int = None,
        evaluation_star: int = None,
        important: str = None,
        main_ding_department_id: str = None,
        main_ding_group_id: str = None,
        main_ding_group_name: str = None,
        product_name: str = None,
        record_id: str = None,
        status: str = None,
        sub_ding_department_id: str = None,
        sub_ding_group_id: str = None,
        sub_ding_group_name: str = None,
        title: str = None,
    ):
        self.chat_id = chat_id
        self.create_time = create_time
        self.creator_name = creator_name
        self.end_time = end_time
        self.evaluation_star = evaluation_star
        self.important = important
        self.main_ding_department_id = main_ding_department_id
        self.main_ding_group_id = main_ding_group_id
        self.main_ding_group_name = main_ding_group_name
        self.product_name = product_name
        self.record_id = record_id
        self.status = status
        self.sub_ding_department_id = sub_ding_department_id
        self.sub_ding_group_id = sub_ding_group_id
        self.sub_ding_group_name = sub_ding_group_name
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.evaluation_star is not None:
            result['evaluationStar'] = self.evaluation_star
        if self.important is not None:
            result['important'] = self.important
        if self.main_ding_department_id is not None:
            result['mainDingDepartmentId'] = self.main_ding_department_id
        if self.main_ding_group_id is not None:
            result['mainDingGroupId'] = self.main_ding_group_id
        if self.main_ding_group_name is not None:
            result['mainDingGroupName'] = self.main_ding_group_name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.status is not None:
            result['status'] = self.status
        if self.sub_ding_department_id is not None:
            result['subDingDepartmentId'] = self.sub_ding_department_id
        if self.sub_ding_group_id is not None:
            result['subDingGroupId'] = self.sub_ding_group_id
        if self.sub_ding_group_name is not None:
            result['subDingGroupName'] = self.sub_ding_group_name
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('evaluationStar') is not None:
            self.evaluation_star = m.get('evaluationStar')
        if m.get('important') is not None:
            self.important = m.get('important')
        if m.get('mainDingDepartmentId') is not None:
            self.main_ding_department_id = m.get('mainDingDepartmentId')
        if m.get('mainDingGroupId') is not None:
            self.main_ding_group_id = m.get('mainDingGroupId')
        if m.get('mainDingGroupName') is not None:
            self.main_ding_group_name = m.get('mainDingGroupName')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subDingDepartmentId') is not None:
            self.sub_ding_department_id = m.get('subDingDepartmentId')
        if m.get('subDingGroupId') is not None:
            self.sub_ding_group_id = m.get('subDingGroupId')
        if m.get('subDingGroupName') is not None:
            self.sub_ding_group_name = m.get('subDingGroupName')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetYunQiTaskByRecordIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetYunQiTaskByRecordIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetYunQiTaskByRecordIdResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetYunQiTaskByRecordIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetYunQiTaskByRecordIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetYunQiTaskByRecordIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDocsGroupByYearRequest(TeaModel):
    def __init__(
        self,
        apply_codes: List[str] = None,
        file_name_keyword: str = None,
        order_ids: List[int] = None,
        product_code: str = None,
        scene: str = None,
    ):
        self.apply_codes = apply_codes
        self.file_name_keyword = file_name_keyword
        self.order_ids = order_ids
        self.product_code = product_code
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_codes is not None:
            result['applyCodes'] = self.apply_codes
        if self.file_name_keyword is not None:
            result['fileNameKeyword'] = self.file_name_keyword
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyCodes') is not None:
            self.apply_codes = m.get('applyCodes')
        if m.get('fileNameKeyword') is not None:
            self.file_name_keyword = m.get('fileNameKeyword')
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class ListDocsGroupByYearResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, List[DataValue]] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v in self.data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['data'][k] = l1
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = {}
        if m.get('data') is not None:
            for k, v in m.get('data').items():
                l1 = []
                for k1 in v:
                    temp_model = DataValue()
                    l1.append(temp_model.from_map(k1))
                self.data['k'] = l1
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListDocsGroupByYearResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDocsGroupByYearResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDocsGroupByYearResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnterpriseSupportPlanRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnterpriseSupportPlanResponseBodyDataDocs(TeaModel):
    def __init__(
        self,
        doc_id: int = None,
        file_name: str = None,
        free_order_apply_code: str = None,
        name: str = None,
        order_id: str = None,
        upload_time: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.file_name = file_name
        self.free_order_apply_code = free_order_apply_code
        self.name = name
        self.order_id = order_id
        self.upload_time = upload_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.name is not None:
            result['name'] = self.name
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesDocNode(TeaModel):
    def __init__(
        self,
        doc_id: int = None,
        doc_name: str = None,
        doc_submit_time: str = None,
        file_name: str = None,
        free_order_apply_code: str = None,
        order_id: str = None,
    ):
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.doc_submit_time = doc_submit_time
        self.file_name = file_name
        self.free_order_apply_code = free_order_apply_code
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_name is not None:
            result['docName'] = self.doc_name
        if self.doc_submit_time is not None:
            result['docSubmitTime'] = self.doc_submit_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')
        if m.get('docSubmitTime') is not None:
            self.doc_submit_time = m.get('docSubmitTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode(TeaModel):
    def __init__(
        self,
        finish_time: str = None,
    ):
        self.finish_time = finish_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode(TeaModel):
    def __init__(
        self,
        audit_time: str = None,
        status: str = None,
        status_name: str = None,
    ):
        self.audit_time = audit_time
        self.status = status
        self.status_name = status_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_time is not None:
            result['auditTime'] = self.audit_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_name is not None:
            result['statusName'] = self.status_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditTime') is not None:
            self.audit_time = m.get('auditTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusName') is not None:
            self.status_name = m.get('statusName')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode(TeaModel):
    def __init__(
        self,
        apply_time: str = None,
        uid: int = None,
    ):
        self.apply_time = apply_time
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode(TeaModel):
    def __init__(
        self,
        pay_time: str = None,
        uid: int = None,
    ):
        self.pay_time = pay_time
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodes(TeaModel):
    def __init__(
        self,
        doc_node: ListEnterpriseSupportPlanResponseBodyDataNodesDocNode = None,
        finish_node: ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode = None,
        free_order_audit_node: ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode = None,
        free_order_node: ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode = None,
        name: str = None,
        order_date: int = None,
        order_node: ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode = None,
        service_implementation: ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation = None,
        status: int = None,
    ):
        self.doc_node = doc_node
        self.finish_node = finish_node
        self.free_order_audit_node = free_order_audit_node
        self.free_order_node = free_order_node
        self.name = name
        self.order_date = order_date
        self.order_node = order_node
        self.service_implementation = service_implementation
        self.status = status

    def validate(self):
        if self.doc_node:
            self.doc_node.validate()
        if self.finish_node:
            self.finish_node.validate()
        if self.free_order_audit_node:
            self.free_order_audit_node.validate()
        if self.free_order_node:
            self.free_order_node.validate()
        if self.order_node:
            self.order_node.validate()
        if self.service_implementation:
            self.service_implementation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_node is not None:
            result['docNode'] = self.doc_node.to_map()
        if self.finish_node is not None:
            result['finishNode'] = self.finish_node.to_map()
        if self.free_order_audit_node is not None:
            result['freeOrderAuditNode'] = self.free_order_audit_node.to_map()
        if self.free_order_node is not None:
            result['freeOrderNode'] = self.free_order_node.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.order_date is not None:
            result['orderDate'] = self.order_date
        if self.order_node is not None:
            result['orderNode'] = self.order_node.to_map()
        if self.service_implementation is not None:
            result['serviceImplementation'] = self.service_implementation.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesDocNode()
            self.doc_node = temp_model.from_map(m['docNode'])
        if m.get('finishNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode()
            self.finish_node = temp_model.from_map(m['finishNode'])
        if m.get('freeOrderAuditNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode()
            self.free_order_audit_node = temp_model.from_map(m['freeOrderAuditNode'])
        if m.get('freeOrderNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode()
            self.free_order_node = temp_model.from_map(m['freeOrderNode'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderDate') is not None:
            self.order_date = m.get('orderDate')
        if m.get('orderNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode()
            self.order_node = temp_model.from_map(m['orderNode'])
        if m.get('serviceImplementation') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation()
            self.service_implementation = temp_model.from_map(m['serviceImplementation'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListEnterpriseSupportPlanResponseBodyDataOperateInfos(TeaModel):
    def __init__(
        self,
        can_click: bool = None,
        text: str = None,
        url: str = None,
    ):
        self.can_click = can_click
        self.text = text
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_click is not None:
            result['canClick'] = self.can_click
        if self.text is not None:
            result['text'] = self.text
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canClick') is not None:
            self.can_click = m.get('canClick')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEnterpriseSupportPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        can_apply_free_order: bool = None,
        customer_id: int = None,
        docs: List[ListEnterpriseSupportPlanResponseBodyDataDocs] = None,
        end_time: str = None,
        first_pay_time: str = None,
        free_order_apply_code: str = None,
        free_order_apply_id: int = None,
        free_order_apply_time: str = None,
        free_order_approved_time: str = None,
        free_order_expect_start_time: str = None,
        instance_id: str = None,
        nodes: List[ListEnterpriseSupportPlanResponseBodyDataNodes] = None,
        operate_infos: List[ListEnterpriseSupportPlanResponseBodyDataOperateInfos] = None,
        order_ids: List[int] = None,
        service_name: str = None,
        service_status: str = None,
        service_status_name: str = None,
        service_type: str = None,
        sort_time: str = None,
        start_time: str = None,
        task_num: int = None,
    ):
        self.can_apply_free_order = can_apply_free_order
        self.customer_id = customer_id
        self.docs = docs
        self.end_time = end_time
        self.first_pay_time = first_pay_time
        self.free_order_apply_code = free_order_apply_code
        self.free_order_apply_id = free_order_apply_id
        self.free_order_apply_time = free_order_apply_time
        self.free_order_approved_time = free_order_approved_time
        self.free_order_expect_start_time = free_order_expect_start_time
        self.instance_id = instance_id
        self.nodes = nodes
        self.operate_infos = operate_infos
        self.order_ids = order_ids
        self.service_name = service_name
        self.service_status = service_status
        self.service_status_name = service_status_name
        self.service_type = service_type
        self.sort_time = sort_time
        self.start_time = start_time
        self.task_num = task_num

    def validate(self):
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.operate_infos:
            for k in self.operate_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_apply_free_order is not None:
            result['canApplyFreeOrder'] = self.can_apply_free_order
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.first_pay_time is not None:
            result['firstPayTime'] = self.first_pay_time
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.free_order_apply_id is not None:
            result['freeOrderApplyId'] = self.free_order_apply_id
        if self.free_order_apply_time is not None:
            result['freeOrderApplyTime'] = self.free_order_apply_time
        if self.free_order_approved_time is not None:
            result['freeOrderApprovedTime'] = self.free_order_approved_time
        if self.free_order_expect_start_time is not None:
            result['freeOrderExpectStartTime'] = self.free_order_expect_start_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        result['operateInfos'] = []
        if self.operate_infos is not None:
            for k in self.operate_infos:
                result['operateInfos'].append(k.to_map() if k else None)
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_status_name is not None:
            result['serviceStatusName'] = self.service_status_name
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.sort_time is not None:
            result['sortTime'] = self.sort_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.task_num is not None:
            result['taskNum'] = self.task_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canApplyFreeOrder') is not None:
            self.can_apply_free_order = m.get('canApplyFreeOrder')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = ListEnterpriseSupportPlanResponseBodyDataDocs()
                self.docs.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('firstPayTime') is not None:
            self.first_pay_time = m.get('firstPayTime')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('freeOrderApplyId') is not None:
            self.free_order_apply_id = m.get('freeOrderApplyId')
        if m.get('freeOrderApplyTime') is not None:
            self.free_order_apply_time = m.get('freeOrderApplyTime')
        if m.get('freeOrderApprovedTime') is not None:
            self.free_order_approved_time = m.get('freeOrderApprovedTime')
        if m.get('freeOrderExpectStartTime') is not None:
            self.free_order_expect_start_time = m.get('freeOrderExpectStartTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.nodes = []
        if m.get('nodes') is not None:
            for k in m.get('nodes'):
                temp_model = ListEnterpriseSupportPlanResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        self.operate_infos = []
        if m.get('operateInfos') is not None:
            for k in m.get('operateInfos'):
                temp_model = ListEnterpriseSupportPlanResponseBodyDataOperateInfos()
                self.operate_infos.append(temp_model.from_map(k))
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('serviceStatusName') is not None:
            self.service_status_name = m.get('serviceStatusName')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('sortTime') is not None:
            self.sort_time = m.get('sortTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')
        return self


class ListEnterpriseSupportPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListEnterpriseSupportPlanResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListEnterpriseSupportPlanResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnterpriseSupportPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnterpriseSupportPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnterpriseSupportPlanSimpleRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataDocs(TeaModel):
    def __init__(
        self,
        doc_id: int = None,
        file_name: str = None,
        free_order_apply_code: str = None,
        name: str = None,
        order_id: str = None,
        upload_time: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.file_name = file_name
        self.free_order_apply_code = free_order_apply_code
        self.name = name
        self.order_id = order_id
        self.upload_time = upload_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.name is not None:
            result['name'] = self.name
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesDocNode(TeaModel):
    def __init__(
        self,
        doc_id: int = None,
        doc_name: str = None,
        doc_submit_time: str = None,
        file_name: str = None,
        free_order_apply_code: str = None,
        order_id: str = None,
    ):
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.doc_submit_time = doc_submit_time
        self.file_name = file_name
        self.free_order_apply_code = free_order_apply_code
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_name is not None:
            result['docName'] = self.doc_name
        if self.doc_submit_time is not None:
            result['docSubmitTime'] = self.doc_submit_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')
        if m.get('docSubmitTime') is not None:
            self.doc_submit_time = m.get('docSubmitTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFinishNode(TeaModel):
    def __init__(
        self,
        finish_time: str = None,
    ):
        self.finish_time = finish_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderAuditNode(TeaModel):
    def __init__(
        self,
        audit_time: str = None,
        status: str = None,
        status_name: str = None,
    ):
        self.audit_time = audit_time
        self.status = status
        self.status_name = status_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_time is not None:
            result['auditTime'] = self.audit_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_name is not None:
            result['statusName'] = self.status_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditTime') is not None:
            self.audit_time = m.get('auditTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusName') is not None:
            self.status_name = m.get('statusName')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderNode(TeaModel):
    def __init__(
        self,
        apply_time: str = None,
        uid: int = None,
    ):
        self.apply_time = apply_time
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesOrderNode(TeaModel):
    def __init__(
        self,
        pay_time: str = None,
        uid: int = None,
    ):
        self.pay_time = pay_time
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesServiceImplementation(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodes(TeaModel):
    def __init__(
        self,
        doc_node: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesDocNode = None,
        finish_node: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFinishNode = None,
        free_order_audit_node: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderAuditNode = None,
        free_order_node: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderNode = None,
        name: str = None,
        order_date: int = None,
        order_node: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesOrderNode = None,
        service_implementation: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesServiceImplementation = None,
        status: int = None,
    ):
        self.doc_node = doc_node
        self.finish_node = finish_node
        self.free_order_audit_node = free_order_audit_node
        self.free_order_node = free_order_node
        self.name = name
        self.order_date = order_date
        self.order_node = order_node
        self.service_implementation = service_implementation
        self.status = status

    def validate(self):
        if self.doc_node:
            self.doc_node.validate()
        if self.finish_node:
            self.finish_node.validate()
        if self.free_order_audit_node:
            self.free_order_audit_node.validate()
        if self.free_order_node:
            self.free_order_node.validate()
        if self.order_node:
            self.order_node.validate()
        if self.service_implementation:
            self.service_implementation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_node is not None:
            result['docNode'] = self.doc_node.to_map()
        if self.finish_node is not None:
            result['finishNode'] = self.finish_node.to_map()
        if self.free_order_audit_node is not None:
            result['freeOrderAuditNode'] = self.free_order_audit_node.to_map()
        if self.free_order_node is not None:
            result['freeOrderNode'] = self.free_order_node.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.order_date is not None:
            result['orderDate'] = self.order_date
        if self.order_node is not None:
            result['orderNode'] = self.order_node.to_map()
        if self.service_implementation is not None:
            result['serviceImplementation'] = self.service_implementation.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesDocNode()
            self.doc_node = temp_model.from_map(m['docNode'])
        if m.get('finishNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFinishNode()
            self.finish_node = temp_model.from_map(m['finishNode'])
        if m.get('freeOrderAuditNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderAuditNode()
            self.free_order_audit_node = temp_model.from_map(m['freeOrderAuditNode'])
        if m.get('freeOrderNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderNode()
            self.free_order_node = temp_model.from_map(m['freeOrderNode'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderDate') is not None:
            self.order_date = m.get('orderDate')
        if m.get('orderNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesOrderNode()
            self.order_node = temp_model.from_map(m['orderNode'])
        if m.get('serviceImplementation') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesServiceImplementation()
            self.service_implementation = temp_model.from_map(m['serviceImplementation'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyData(TeaModel):
    def __init__(
        self,
        can_apply_free_order: bool = None,
        customer_id: int = None,
        docs: List[ListEnterpriseSupportPlanSimpleResponseBodyDataDocs] = None,
        end_time: str = None,
        first_pay_time: str = None,
        free_order_apply_code: str = None,
        free_order_apply_id: int = None,
        free_order_apply_time: str = None,
        free_order_approved_time: str = None,
        free_order_expect_start_time: str = None,
        instance_id: str = None,
        nodes: List[ListEnterpriseSupportPlanSimpleResponseBodyDataNodes] = None,
        order_ids: List[int] = None,
        service_name: str = None,
        service_status: str = None,
        service_status_name: str = None,
        service_type: str = None,
        sort_time: str = None,
        start_time: str = None,
        task_num: int = None,
    ):
        self.can_apply_free_order = can_apply_free_order
        self.customer_id = customer_id
        self.docs = docs
        self.end_time = end_time
        self.first_pay_time = first_pay_time
        self.free_order_apply_code = free_order_apply_code
        self.free_order_apply_id = free_order_apply_id
        self.free_order_apply_time = free_order_apply_time
        self.free_order_approved_time = free_order_approved_time
        self.free_order_expect_start_time = free_order_expect_start_time
        self.instance_id = instance_id
        self.nodes = nodes
        self.order_ids = order_ids
        self.service_name = service_name
        self.service_status = service_status
        self.service_status_name = service_status_name
        self.service_type = service_type
        self.sort_time = sort_time
        self.start_time = start_time
        self.task_num = task_num

    def validate(self):
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_apply_free_order is not None:
            result['canApplyFreeOrder'] = self.can_apply_free_order
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.first_pay_time is not None:
            result['firstPayTime'] = self.first_pay_time
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.free_order_apply_id is not None:
            result['freeOrderApplyId'] = self.free_order_apply_id
        if self.free_order_apply_time is not None:
            result['freeOrderApplyTime'] = self.free_order_apply_time
        if self.free_order_approved_time is not None:
            result['freeOrderApprovedTime'] = self.free_order_approved_time
        if self.free_order_expect_start_time is not None:
            result['freeOrderExpectStartTime'] = self.free_order_expect_start_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_status_name is not None:
            result['serviceStatusName'] = self.service_status_name
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.sort_time is not None:
            result['sortTime'] = self.sort_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.task_num is not None:
            result['taskNum'] = self.task_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canApplyFreeOrder') is not None:
            self.can_apply_free_order = m.get('canApplyFreeOrder')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataDocs()
                self.docs.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('firstPayTime') is not None:
            self.first_pay_time = m.get('firstPayTime')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('freeOrderApplyId') is not None:
            self.free_order_apply_id = m.get('freeOrderApplyId')
        if m.get('freeOrderApplyTime') is not None:
            self.free_order_apply_time = m.get('freeOrderApplyTime')
        if m.get('freeOrderApprovedTime') is not None:
            self.free_order_approved_time = m.get('freeOrderApprovedTime')
        if m.get('freeOrderExpectStartTime') is not None:
            self.free_order_expect_start_time = m.get('freeOrderExpectStartTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.nodes = []
        if m.get('nodes') is not None:
            for k in m.get('nodes'):
                temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('serviceStatusName') is not None:
            self.service_status_name = m.get('serviceStatusName')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('sortTime') is not None:
            self.sort_time = m.get('sortTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')
        return self


class ListEnterpriseSupportPlanSimpleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListEnterpriseSupportPlanSimpleResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListEnterpriseSupportPlanSimpleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnterpriseSupportPlanSimpleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnterpriseSupportPlanSimpleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceApplyRequest(TeaModel):
    def __init__(
        self,
        apply_type: List[str] = None,
        end_date: int = None,
        page_num: int = None,
        page_size: int = None,
        product_code: int = None,
        start_date: int = None,
        status: str = None,
    ):
        self.apply_type = apply_type
        self.end_date = end_date
        self.page_num = page_num
        self.page_size = page_size
        self.product_code = product_code
        self.start_date = start_date
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_type is not None:
            result['applyType'] = self.apply_type
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyType') is not None:
            self.apply_type = m.get('applyType')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListServiceApplyResponseBodyDataListAppointments(TeaModel):
    def __init__(
        self,
        huhang_id: int = None,
        purchase_code: int = None,
        purchase_desc: str = None,
        support_days: int = None,
        travel_days: int = None,
    ):
        self.huhang_id = huhang_id
        self.purchase_code = purchase_code
        self.purchase_desc = purchase_desc
        self.support_days = support_days
        self.travel_days = travel_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.huhang_id is not None:
            result['huhangId'] = self.huhang_id
        if self.purchase_code is not None:
            result['purchaseCode'] = self.purchase_code
        if self.purchase_desc is not None:
            result['purchaseDesc'] = self.purchase_desc
        if self.support_days is not None:
            result['supportDays'] = self.support_days
        if self.travel_days is not None:
            result['travelDays'] = self.travel_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('huhangId') is not None:
            self.huhang_id = m.get('huhangId')
        if m.get('purchaseCode') is not None:
            self.purchase_code = m.get('purchaseCode')
        if m.get('purchaseDesc') is not None:
            self.purchase_desc = m.get('purchaseDesc')
        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')
        if m.get('travelDays') is not None:
            self.travel_days = m.get('travelDays')
        return self


class ListServiceApplyResponseBodyDataListPayOrders(TeaModel):
    def __init__(
        self,
        amount: str = None,
        compass_commodity_code: str = None,
        compass_commodity_name: str = None,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        modifier_emp_id: str = None,
        operate: Dict[str, Any] = None,
        order_detail: Any = None,
        order_id: int = None,
        original_price: float = None,
        pay_amount: float = None,
        pay_time: str = None,
        product_name: str = None,
        rene_wal_url: str = None,
        service_content_map: Dict[str, Any] = None,
        status: int = None,
        status_str: str = None,
        support_days: int = None,
        uid: str = None,
        url: str = None,
    ):
        self.amount = amount
        self.compass_commodity_code = compass_commodity_code
        self.compass_commodity_name = compass_commodity_name
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.modifier_emp_id = modifier_emp_id
        self.operate = operate
        self.order_detail = order_detail
        self.order_id = order_id
        self.original_price = original_price
        self.pay_amount = pay_amount
        self.pay_time = pay_time
        self.product_name = product_name
        self.rene_wal_url = rene_wal_url
        self.service_content_map = service_content_map
        self.status = status
        self.status_str = status_str
        self.support_days = support_days
        self.uid = uid
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.compass_commodity_code is not None:
            result['compassCommodityCode'] = self.compass_commodity_code
        if self.compass_commodity_name is not None:
            result['compassCommodityName'] = self.compass_commodity_name
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.operate is not None:
            result['operate'] = self.operate
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.original_price is not None:
            result['originalPrice'] = self.original_price
        if self.pay_amount is not None:
            result['payAmount'] = self.pay_amount
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url
        if self.service_content_map is not None:
            result['serviceContentMap'] = self.service_content_map
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_days is not None:
            result['supportDays'] = self.support_days
        if self.uid is not None:
            result['uid'] = self.uid
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('compassCommodityCode') is not None:
            self.compass_commodity_code = m.get('compassCommodityCode')
        if m.get('compassCommodityName') is not None:
            self.compass_commodity_name = m.get('compassCommodityName')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('operate') is not None:
            self.operate = m.get('operate')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('originalPrice') is not None:
            self.original_price = m.get('originalPrice')
        if m.get('payAmount') is not None:
            self.pay_amount = m.get('payAmount')
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')
        if m.get('serviceContentMap') is not None:
            self.service_content_map = m.get('serviceContentMap')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersExtList(TeaModel):
    def __init__(
        self,
        key_code: str = None,
        name: str = None,
        value: Any = None,
        view: str = None,
    ):
        self.key_code = key_code
        self.name = name
        self.value = value
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS(TeaModel):
    def __init__(
        self,
        display: bool = None,
        extend_info: Any = None,
        index: int = None,
        node_name: str = None,
        status: int = None,
    ):
        self.display = display
        self.extend_info = extend_info
        self.index = index
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList(TeaModel):
    def __init__(
        self,
        key_code: str = None,
        name: str = None,
        value: Any = None,
        view: str = None,
    ):
        self.key_code = key_code
        self.name = name
        self.value = value
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS(TeaModel):
    def __init__(
        self,
        display: bool = None,
        extend_info: Any = None,
        index: int = None,
        node_name: str = None,
        status: int = None,
    ):
        self.display = display
        self.extend_info = extend_info
        self.index = index
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers(TeaModel):
    def __init__(
        self,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hr_status: str = None,
        id: int = None,
        last_name: str = None,
        modifier_emp_id: str = None,
        name: str = None,
        nick_name_en: str = None,
        realm_id: int = None,
        workid: str = None,
    ):
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hr_status = hr_status
        self.id = id
        self.last_name = last_name
        self.modifier_emp_id = modifier_emp_id
        self.name = name
        self.nick_name_en = nick_name_en
        self.realm_id = realm_id
        self.workid = workid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks(TeaModel):
    def __init__(
        self,
        apply_file_volist: List[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList] = None,
        appointment_code: str = None,
        appointment_end_time: int = None,
        appointment_id: str = None,
        appointment_pass_time: int = None,
        appointment_time: int = None,
        commodity_desc: str = None,
        creator_emp_id: str = None,
        cycle_service: bool = None,
        ext_list: List[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        ntm_commodity_code: str = None,
        order_detail: Any = None,
        order_id: int = None,
        performance_node_dtos: List[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS] = None,
        purchase_pack_code: int = None,
        service_apply_id: int = None,
        service_month_reports: List[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports] = None,
        service_reports: List[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports] = None,
        service_schemes: List[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes] = None,
        status: int = None,
        status_str: str = None,
        support_time: List[int] = None,
        tam_engineers: List[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers] = None,
    ):
        self.apply_file_volist = apply_file_volist
        self.appointment_code = appointment_code
        self.appointment_end_time = appointment_end_time
        self.appointment_id = appointment_id
        self.appointment_pass_time = appointment_pass_time
        self.appointment_time = appointment_time
        self.commodity_desc = commodity_desc
        self.creator_emp_id = creator_emp_id
        self.cycle_service = cycle_service
        self.ext_list = ext_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.ntm_commodity_code = ntm_commodity_code
        self.order_detail = order_detail
        self.order_id = order_id
        self.performance_node_dtos = performance_node_dtos
        self.purchase_pack_code = purchase_pack_code
        self.service_apply_id = service_apply_id
        self.service_month_reports = service_month_reports
        self.service_reports = service_reports
        self.service_schemes = service_schemes
        self.status = status
        self.status_str = status_str
        self.support_time = support_time
        self.tam_engineers = tam_engineers

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.ntm_commodity_code is not None:
            result['ntmCommodityCode'] = self.ntm_commodity_code
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('ntmCommodityCode') is not None:
            self.ntm_commodity_code = m.get('ntmCommodityCode')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers(TeaModel):
    def __init__(
        self,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hr_status: str = None,
        id: int = None,
        last_name: str = None,
        modifier_emp_id: str = None,
        name: str = None,
        nick_name_en: str = None,
        realm_id: int = None,
        workid: str = None,
    ):
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hr_status = hr_status
        self.id = id
        self.last_name = last_name
        self.modifier_emp_id = modifier_emp_id
        self.name = name
        self.nick_name_en = nick_name_en
        self.realm_id = realm_id
        self.workid = workid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrders(TeaModel):
    def __init__(
        self,
        apply_file_volist: List[ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList] = None,
        appointment_code: str = None,
        appointment_end_time: int = None,
        appointment_id: str = None,
        appointment_pass_time: int = None,
        appointment_time: int = None,
        commodity_desc: str = None,
        creator_emp_id: str = None,
        cycle_service: bool = None,
        ext_list: List[ListServiceApplyResponseBodyDataListPerformanceOrdersExtList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        ntm_commodity_code: str = None,
        order_detail: Any = None,
        order_id: int = None,
        pack_count: int = None,
        pack_details: List[Dict[str, Any]] = None,
        performance_node_dtos: List[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS] = None,
        performance_packs: List[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks] = None,
        purchase_pack_code: int = None,
        service_apply_id: int = None,
        service_month_reports: List[ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports] = None,
        service_reports: List[ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports] = None,
        service_schemes: List[ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes] = None,
        status: int = None,
        status_str: str = None,
        support_time: List[int] = None,
        tam_engineers: List[ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers] = None,
    ):
        self.apply_file_volist = apply_file_volist
        self.appointment_code = appointment_code
        self.appointment_end_time = appointment_end_time
        self.appointment_id = appointment_id
        self.appointment_pass_time = appointment_pass_time
        self.appointment_time = appointment_time
        self.commodity_desc = commodity_desc
        self.creator_emp_id = creator_emp_id
        self.cycle_service = cycle_service
        self.ext_list = ext_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.ntm_commodity_code = ntm_commodity_code
        self.order_detail = order_detail
        self.order_id = order_id
        self.pack_count = pack_count
        self.pack_details = pack_details
        self.performance_node_dtos = performance_node_dtos
        self.performance_packs = performance_packs
        self.purchase_pack_code = purchase_pack_code
        self.service_apply_id = service_apply_id
        self.service_month_reports = service_month_reports
        self.service_reports = service_reports
        self.service_schemes = service_schemes
        self.status = status
        self.status_str = status_str
        self.support_time = support_time
        self.tam_engineers = tam_engineers

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.performance_packs:
            for k in self.performance_packs:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.ntm_commodity_code is not None:
            result['ntmCommodityCode'] = self.ntm_commodity_code
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.pack_count is not None:
            result['packCount'] = self.pack_count
        if self.pack_details is not None:
            result['packDetails'] = self.pack_details
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k in self.performance_packs:
                result['performancePacks'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('ntmCommodityCode') is not None:
            self.ntm_commodity_code = m.get('ntmCommodityCode')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('packCount') is not None:
            self.pack_count = m.get('packCount')
        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k in m.get('performancePacks'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksExtList(TeaModel):
    def __init__(
        self,
        key_code: str = None,
        name: str = None,
        value: Any = None,
        view: str = None,
    ):
        self.key_code = key_code
        self.name = name
        self.value = value
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS(TeaModel):
    def __init__(
        self,
        display: bool = None,
        extend_info: Any = None,
        index: int = None,
        node_name: str = None,
        status: int = None,
    ):
        self.display = display
        self.extend_info = extend_info
        self.index = index
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksServiceReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers(TeaModel):
    def __init__(
        self,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hr_status: str = None,
        id: int = None,
        last_name: str = None,
        modifier_emp_id: str = None,
        name: str = None,
        nick_name_en: str = None,
        realm_id: int = None,
        workid: str = None,
    ):
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hr_status = hr_status
        self.id = id
        self.last_name = last_name
        self.modifier_emp_id = modifier_emp_id
        self.name = name
        self.nick_name_en = nick_name_en
        self.realm_id = realm_id
        self.workid = workid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacks(TeaModel):
    def __init__(
        self,
        apply_file_volist: List[ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList] = None,
        appointment_code: str = None,
        appointment_end_time: int = None,
        appointment_id: str = None,
        appointment_pass_time: int = None,
        appointment_time: int = None,
        commodity_desc: str = None,
        creator_emp_id: str = None,
        cycle_service: bool = None,
        ext_list: List[ListServiceApplyResponseBodyDataListPerformancePacksExtList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        ntm_commodity_code: str = None,
        order_detail: Any = None,
        order_id: int = None,
        performance_node_dtos: List[ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS] = None,
        purchase_pack_code: int = None,
        service_apply_id: int = None,
        service_month_reports: List[ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports] = None,
        service_reports: List[ListServiceApplyResponseBodyDataListPerformancePacksServiceReports] = None,
        service_schemes: List[ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes] = None,
        status: int = None,
        status_str: str = None,
        support_time: List[int] = None,
        tam_engineers: List[ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers] = None,
    ):
        self.apply_file_volist = apply_file_volist
        self.appointment_code = appointment_code
        self.appointment_end_time = appointment_end_time
        self.appointment_id = appointment_id
        self.appointment_pass_time = appointment_pass_time
        self.appointment_time = appointment_time
        self.commodity_desc = commodity_desc
        self.creator_emp_id = creator_emp_id
        self.cycle_service = cycle_service
        self.ext_list = ext_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.ntm_commodity_code = ntm_commodity_code
        self.order_detail = order_detail
        self.order_id = order_id
        self.performance_node_dtos = performance_node_dtos
        self.purchase_pack_code = purchase_pack_code
        self.service_apply_id = service_apply_id
        self.service_month_reports = service_month_reports
        self.service_reports = service_reports
        self.service_schemes = service_schemes
        self.status = status
        self.status_str = status_str
        self.support_time = support_time
        self.tam_engineers = tam_engineers

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.ntm_commodity_code is not None:
            result['ntmCommodityCode'] = self.ntm_commodity_code
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('ntmCommodityCode') is not None:
            self.ntm_commodity_code = m.get('ntmCommodityCode')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class ListServiceApplyResponseBodyDataListServiceReports(TeaModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataList(TeaModel):
    def __init__(
        self,
        applier_id: str = None,
        apply_code: str = None,
        apply_component_details: List[List[str]] = None,
        apply_time: int = None,
        appointments: List[ListServiceApplyResponseBodyDataListAppointments] = None,
        buy_url: str = None,
        creator_emp_id: str = None,
        customer_name: str = None,
        cycle_service: bool = None,
        executed_count: int = None,
        finish_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        pack_details: List[Dict[str, Any]] = None,
        pay_orders: List[ListServiceApplyResponseBodyDataListPayOrders] = None,
        pay_url: str = None,
        performance_orders: List[ListServiceApplyResponseBodyDataListPerformanceOrders] = None,
        performance_packs: List[ListServiceApplyResponseBodyDataListPerformancePacks] = None,
        rene_wal_url: str = None,
        service_code: str = None,
        service_name: str = None,
        service_reports: List[ListServiceApplyResponseBodyDataListServiceReports] = None,
        service_time_range: List[int] = None,
        status: str = None,
        status_code: int = None,
        status_str: str = None,
        term_of_validity: str = None,
        total_pack: int = None,
        type: str = None,
        use_pack: int = None,
    ):
        self.applier_id = applier_id
        self.apply_code = apply_code
        self.apply_component_details = apply_component_details
        self.apply_time = apply_time
        self.appointments = appointments
        self.buy_url = buy_url
        self.creator_emp_id = creator_emp_id
        self.customer_name = customer_name
        self.cycle_service = cycle_service
        self.executed_count = executed_count
        self.finish_count = finish_count
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.pack_details = pack_details
        self.pay_orders = pay_orders
        self.pay_url = pay_url
        self.performance_orders = performance_orders
        self.performance_packs = performance_packs
        self.rene_wal_url = rene_wal_url
        self.service_code = service_code
        self.service_name = service_name
        self.service_reports = service_reports
        self.service_time_range = service_time_range
        self.status = status
        self.status_code = status_code
        self.status_str = status_str
        self.term_of_validity = term_of_validity
        self.total_pack = total_pack
        self.type = type
        self.use_pack = use_pack

    def validate(self):
        if self.appointments:
            for k in self.appointments:
                if k:
                    k.validate()
        if self.pay_orders:
            for k in self.pay_orders:
                if k:
                    k.validate()
        if self.performance_orders:
            for k in self.performance_orders:
                if k:
                    k.validate()
        if self.performance_packs:
            for k in self.performance_packs:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applier_id is not None:
            result['applierId'] = self.applier_id
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        if self.apply_component_details is not None:
            result['applyComponentDetails'] = self.apply_component_details
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        result['appointments'] = []
        if self.appointments is not None:
            for k in self.appointments:
                result['appointments'].append(k.to_map() if k else None)
        if self.buy_url is not None:
            result['buyUrl'] = self.buy_url
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.customer_name is not None:
            result['customerName'] = self.customer_name
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        if self.executed_count is not None:
            result['executedCount'] = self.executed_count
        if self.finish_count is not None:
            result['finishCount'] = self.finish_count
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.pack_details is not None:
            result['packDetails'] = self.pack_details
        result['payOrders'] = []
        if self.pay_orders is not None:
            for k in self.pay_orders:
                result['payOrders'].append(k.to_map() if k else None)
        if self.pay_url is not None:
            result['payUrl'] = self.pay_url
        result['performanceOrders'] = []
        if self.performance_orders is not None:
            for k in self.performance_orders:
                result['performanceOrders'].append(k.to_map() if k else None)
        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k in self.performance_packs:
                result['performancePacks'].append(k.to_map() if k else None)
        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        if self.service_time_range is not None:
            result['serviceTimeRange'] = self.service_time_range
        if self.status is not None:
            result['status'] = self.status
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.term_of_validity is not None:
            result['termOfValidity'] = self.term_of_validity
        if self.total_pack is not None:
            result['totalPack'] = self.total_pack
        if self.type is not None:
            result['type'] = self.type
        if self.use_pack is not None:
            result['usePack'] = self.use_pack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applierId') is not None:
            self.applier_id = m.get('applierId')
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        if m.get('applyComponentDetails') is not None:
            self.apply_component_details = m.get('applyComponentDetails')
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        self.appointments = []
        if m.get('appointments') is not None:
            for k in m.get('appointments'):
                temp_model = ListServiceApplyResponseBodyDataListAppointments()
                self.appointments.append(temp_model.from_map(k))
        if m.get('buyUrl') is not None:
            self.buy_url = m.get('buyUrl')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        if m.get('executedCount') is not None:
            self.executed_count = m.get('executedCount')
        if m.get('finishCount') is not None:
            self.finish_count = m.get('finishCount')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')
        self.pay_orders = []
        if m.get('payOrders') is not None:
            for k in m.get('payOrders'):
                temp_model = ListServiceApplyResponseBodyDataListPayOrders()
                self.pay_orders.append(temp_model.from_map(k))
        if m.get('payUrl') is not None:
            self.pay_url = m.get('payUrl')
        self.performance_orders = []
        if m.get('performanceOrders') is not None:
            for k in m.get('performanceOrders'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrders()
                self.performance_orders.append(temp_model.from_map(k))
        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k in m.get('performancePacks'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k))
        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = ListServiceApplyResponseBodyDataListServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        if m.get('serviceTimeRange') is not None:
            self.service_time_range = m.get('serviceTimeRange')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('termOfValidity') is not None:
            self.term_of_validity = m.get('termOfValidity')
        if m.get('totalPack') is not None:
            self.total_pack = m.get('totalPack')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('usePack') is not None:
            self.use_pack = m.get('usePack')
        return self


class ListServiceApplyResponseBodyData(TeaModel):
    def __init__(
        self,
        extend: Any = None,
        list: List[ListServiceApplyResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extend = extend
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend is not None:
            result['extend'] = self.extend
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListServiceApplyResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListServiceApplyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListServiceApplyResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListServiceApplyResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListServiceApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceApplyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListYunQiTaskByUidRequest(TeaModel):
    def __init__(
        self,
        create_time_end: int = None,
        create_time_start: int = None,
        free_order_apply_codes: List[str] = None,
        free_order_apply_ids: List[int] = None,
        order_ids: List[int] = None,
        page_num: int = None,
        page_size: int = None,
        status_list: List[str] = None,
    ):
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.free_order_apply_codes = free_order_apply_codes
        self.free_order_apply_ids = free_order_apply_ids
        self.order_ids = order_ids
        self.page_num = page_num
        self.page_size = page_size
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_end is not None:
            result['createTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['createTimeStart'] = self.create_time_start
        if self.free_order_apply_codes is not None:
            result['freeOrderApplyCodes'] = self.free_order_apply_codes
        if self.free_order_apply_ids is not None:
            result['freeOrderApplyIds'] = self.free_order_apply_ids
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status_list is not None:
            result['statusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTimeEnd') is not None:
            self.create_time_end = m.get('createTimeEnd')
        if m.get('createTimeStart') is not None:
            self.create_time_start = m.get('createTimeStart')
        if m.get('freeOrderApplyCodes') is not None:
            self.free_order_apply_codes = m.get('freeOrderApplyCodes')
        if m.get('freeOrderApplyIds') is not None:
            self.free_order_apply_ids = m.get('freeOrderApplyIds')
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        return self


class ListYunQiTaskByUidResponseBodyDataList(TeaModel):
    def __init__(
        self,
        chat_id: str = None,
        create_time: int = None,
        creator_name: str = None,
        end_time: int = None,
        evaluation_star: int = None,
        important: str = None,
        main_ding_department_id: str = None,
        main_ding_group_id: str = None,
        main_ding_group_name: str = None,
        product_name: str = None,
        record_id: str = None,
        status: str = None,
        sub_ding_department_id: str = None,
        sub_ding_group_id: str = None,
        sub_ding_group_name: str = None,
        title: str = None,
    ):
        self.chat_id = chat_id
        self.create_time = create_time
        self.creator_name = creator_name
        self.end_time = end_time
        self.evaluation_star = evaluation_star
        self.important = important
        self.main_ding_department_id = main_ding_department_id
        self.main_ding_group_id = main_ding_group_id
        self.main_ding_group_name = main_ding_group_name
        self.product_name = product_name
        self.record_id = record_id
        self.status = status
        self.sub_ding_department_id = sub_ding_department_id
        self.sub_ding_group_id = sub_ding_group_id
        self.sub_ding_group_name = sub_ding_group_name
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.evaluation_star is not None:
            result['evaluationStar'] = self.evaluation_star
        if self.important is not None:
            result['important'] = self.important
        if self.main_ding_department_id is not None:
            result['mainDingDepartmentId'] = self.main_ding_department_id
        if self.main_ding_group_id is not None:
            result['mainDingGroupId'] = self.main_ding_group_id
        if self.main_ding_group_name is not None:
            result['mainDingGroupName'] = self.main_ding_group_name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.status is not None:
            result['status'] = self.status
        if self.sub_ding_department_id is not None:
            result['subDingDepartmentId'] = self.sub_ding_department_id
        if self.sub_ding_group_id is not None:
            result['subDingGroupId'] = self.sub_ding_group_id
        if self.sub_ding_group_name is not None:
            result['subDingGroupName'] = self.sub_ding_group_name
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('evaluationStar') is not None:
            self.evaluation_star = m.get('evaluationStar')
        if m.get('important') is not None:
            self.important = m.get('important')
        if m.get('mainDingDepartmentId') is not None:
            self.main_ding_department_id = m.get('mainDingDepartmentId')
        if m.get('mainDingGroupId') is not None:
            self.main_ding_group_id = m.get('mainDingGroupId')
        if m.get('mainDingGroupName') is not None:
            self.main_ding_group_name = m.get('mainDingGroupName')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subDingDepartmentId') is not None:
            self.sub_ding_department_id = m.get('subDingDepartmentId')
        if m.get('subDingGroupId') is not None:
            self.sub_ding_group_id = m.get('subDingGroupId')
        if m.get('subDingGroupName') is not None:
            self.sub_ding_group_name = m.get('subDingGroupName')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListYunQiTaskByUidResponseBodyData(TeaModel):
    def __init__(
        self,
        extend: Any = None,
        list: List[ListYunQiTaskByUidResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extend = extend
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend is not None:
            result['extend'] = self.extend
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListYunQiTaskByUidResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListYunQiTaskByUidResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListYunQiTaskByUidResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListYunQiTaskByUidResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListYunQiTaskByUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListYunQiTaskByUidResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListYunQiTaskByUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkFileReadedRequest(TeaModel):
    def __init__(
        self,
        apply_code: str = None,
        file_id: int = None,
        order_id: str = None,
        scene: str = None,
    ):
        self.apply_code = apply_code
        self.file_id = file_id
        self.order_id = order_id
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class MarkFileReadedResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class MarkFileReadedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MarkFileReadedResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MarkFileReadedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


