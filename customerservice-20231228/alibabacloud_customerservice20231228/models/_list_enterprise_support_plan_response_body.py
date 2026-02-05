# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_customerservice20231228 import models as main_models
from darabonba.model import DaraModel

class ListEnterpriseSupportPlanResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListEnterpriseSupportPlanResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('data'):
                temp_model = main_models.ListEnterpriseSupportPlanResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListEnterpriseSupportPlanResponseBodyData(DaraModel):
    def __init__(
        self,
        can_apply_free_order: bool = None,
        customer_id: str = None,
        docs: List[main_models.ListEnterpriseSupportPlanResponseBodyDataDocs] = None,
        end_time: str = None,
        first_pay_time: str = None,
        free_order_apply_code: str = None,
        free_order_apply_id: int = None,
        free_order_apply_time: str = None,
        free_order_approved_time: str = None,
        free_order_expect_start_time: str = None,
        gtsp_project_id: int = None,
        instance_id: str = None,
        nodes: List[main_models.ListEnterpriseSupportPlanResponseBodyDataNodes] = None,
        operate_infos: List[main_models.ListEnterpriseSupportPlanResponseBodyDataOperateInfos] = None,
        order_ids: List[int] = None,
        service_name: str = None,
        service_status: str = None,
        service_status_name: str = None,
        service_type: str = None,
        sort_time: str = None,
        start_time: str = None,
        tags: List[main_models.ListEnterpriseSupportPlanResponseBodyDataTags] = None,
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
        self.gtsp_project_id = gtsp_project_id
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
        self.tags = tags
        self.task_num = task_num

    def validate(self):
        if self.docs:
            for v1 in self.docs:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()
        if self.operate_infos:
            for v1 in self.operate_infos:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_apply_free_order is not None:
            result['canApplyFreeOrder'] = self.can_apply_free_order

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        result['docs'] = []
        if self.docs is not None:
            for k1 in self.docs:
                result['docs'].append(k1.to_map() if k1 else None)

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

        if self.gtsp_project_id is not None:
            result['gtspProjectId'] = self.gtsp_project_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        result['nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['nodes'].append(k1.to_map() if k1 else None)

        result['operateInfos'] = []
        if self.operate_infos is not None:
            for k1 in self.operate_infos:
                result['operateInfos'].append(k1.to_map() if k1 else None)

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

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('docs'):
                temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataDocs()
                self.docs.append(temp_model.from_map(k1))

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

        if m.get('gtspProjectId') is not None:
            self.gtsp_project_id = m.get('gtspProjectId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        self.nodes = []
        if m.get('nodes') is not None:
            for k1 in m.get('nodes'):
                temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        self.operate_infos = []
        if m.get('operateInfos') is not None:
            for k1 in m.get('operateInfos'):
                temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataOperateInfos()
                self.operate_infos.append(temp_model.from_map(k1))

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

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')

        return self

class ListEnterpriseSupportPlanResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        extend_infos: List[str] = None,
        show: bool = None,
        tag_code: str = None,
        tag_name: str = None,
    ):
        self.extend_infos = extend_infos
        self.show = show
        self.tag_code = tag_code
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_infos is not None:
            result['extendInfos'] = self.extend_infos

        if self.show is not None:
            result['show'] = self.show

        if self.tag_code is not None:
            result['tagCode'] = self.tag_code

        if self.tag_name is not None:
            result['tagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendInfos') is not None:
            self.extend_infos = m.get('extendInfos')

        if m.get('show') is not None:
            self.show = m.get('show')

        if m.get('tagCode') is not None:
            self.tag_code = m.get('tagCode')

        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')

        return self

class ListEnterpriseSupportPlanResponseBodyDataOperateInfos(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ListEnterpriseSupportPlanResponseBodyDataNodes(DaraModel):
    def __init__(
        self,
        doc_node: main_models.ListEnterpriseSupportPlanResponseBodyDataNodesDocNode = None,
        finish_node: main_models.ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode = None,
        free_order_audit_node: main_models.ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode = None,
        free_order_node: main_models.ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode = None,
        name: str = None,
        order_date: int = None,
        order_node: main_models.ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode = None,
        service_implementation: main_models.ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataNodesDocNode()
            self.doc_node = temp_model.from_map(m.get('docNode'))

        if m.get('finishNode') is not None:
            temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode()
            self.finish_node = temp_model.from_map(m.get('finishNode'))

        if m.get('freeOrderAuditNode') is not None:
            temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode()
            self.free_order_audit_node = temp_model.from_map(m.get('freeOrderAuditNode'))

        if m.get('freeOrderNode') is not None:
            temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode()
            self.free_order_node = temp_model.from_map(m.get('freeOrderNode'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('orderDate') is not None:
            self.order_date = m.get('orderDate')

        if m.get('orderNode') is not None:
            temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode()
            self.order_node = temp_model.from_map(m.get('orderNode'))

        if m.get('serviceImplementation') is not None:
            temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation()
            self.service_implementation = temp_model.from_map(m.get('serviceImplementation'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode(DaraModel):
    def __init__(
        self,
        pay_time: str = None,
        uid: str = None,
    ):
        self.pay_time = pay_time
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode(DaraModel):
    def __init__(
        self,
        apply_time: str = None,
        uid: str = None,
    ):
        self.apply_time = apply_time
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode(DaraModel):
    def __init__(
        self,
        finish_time: str = None,
    ):
        self.finish_time = finish_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        return self

class ListEnterpriseSupportPlanResponseBodyDataNodesDocNode(DaraModel):
    def __init__(
        self,
        attachments: List[Any] = None,
        doc_id: int = None,
        doc_name: str = None,
        doc_submit_time: str = None,
        file_name: str = None,
        free_order_apply_code: str = None,
        order_id: str = None,
    ):
        self.attachments = attachments
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.doc_submit_time = doc_submit_time
        self.file_name = file_name
        self.free_order_apply_code = free_order_apply_code
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachments is not None:
            result['attachments'] = self.attachments

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
        if m.get('attachments') is not None:
            self.attachments = m.get('attachments')

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

class ListEnterpriseSupportPlanResponseBodyDataDocs(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.ListEnterpriseSupportPlanResponseBodyDataDocsAttachments] = None,
        doc_id: int = None,
        evaluated: bool = None,
        evaluation_url: str = None,
        file_name: str = None,
        free_order_apply_code: str = None,
        name: str = None,
        order_id: str = None,
        upload_time: str = None,
        url: str = None,
    ):
        self.attachments = attachments
        self.doc_id = doc_id
        self.evaluated = evaluated
        self.evaluation_url = evaluation_url
        self.file_name = file_name
        self.free_order_apply_code = free_order_apply_code
        self.name = name
        self.order_id = order_id
        self.upload_time = upload_time
        self.url = url

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['attachments'].append(k1.to_map() if k1 else None)

        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.evaluated is not None:
            result['evaluated'] = self.evaluated

        if self.evaluation_url is not None:
            result['evaluationUrl'] = self.evaluation_url

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
        self.attachments = []
        if m.get('attachments') is not None:
            for k1 in m.get('attachments'):
                temp_model = main_models.ListEnterpriseSupportPlanResponseBodyDataDocsAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('evaluated') is not None:
            self.evaluated = m.get('evaluated')

        if m.get('evaluationUrl') is not None:
            self.evaluation_url = m.get('evaluationUrl')

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



class ListEnterpriseSupportPlanResponseBodyDataDocsAttachments(DaraModel):
    def __init__(
        self,
        doc_id: int = None,
        evaluated: bool = None,
        evaluation_url: str = None,
        file_name: str = None,
        free_order_apply_code: str = None,
        name: str = None,
        order_id: str = None,
        upload_time: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.evaluated = evaluated
        self.evaluation_url = evaluation_url
        self.file_name = file_name
        self.free_order_apply_code = free_order_apply_code
        self.name = name
        self.order_id = order_id
        self.upload_time = upload_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.evaluated is not None:
            result['evaluated'] = self.evaluated

        if self.evaluation_url is not None:
            result['evaluationUrl'] = self.evaluation_url

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

        if m.get('evaluated') is not None:
            self.evaluated = m.get('evaluated')

        if m.get('evaluationUrl') is not None:
            self.evaluation_url = m.get('evaluationUrl')

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

