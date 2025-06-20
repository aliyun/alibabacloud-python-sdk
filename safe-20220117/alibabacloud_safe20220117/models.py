# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelBlockRequest(TeaModel):
    def __init__(
        self,
        block_id: int = None,
        cancel_block_desc: str = None,
        create_emp_id: str = None,
    ):
        self.block_id = block_id
        self.cancel_block_desc = cancel_block_desc
        self.create_emp_id = create_emp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_id is not None:
            result['BlockId'] = self.block_id
        if self.cancel_block_desc is not None:
            result['CancelBLockDesc'] = self.cancel_block_desc
        if self.create_emp_id is not None:
            result['CreateEmpId'] = self.create_emp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')
        if m.get('CancelBLockDesc') is not None:
            self.cancel_block_desc = m.get('CancelBLockDesc')
        if m.get('CreateEmpId') is not None:
            self.create_emp_id = m.get('CreateEmpId')
        return self


class CancelBlockResponseBodyData(TeaModel):
    def __init__(
        self,
        approve_instance_id: str = None,
        success: bool = None,
    ):
        self.approve_instance_id = approve_instance_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_instance_id is not None:
            result['ApproveInstanceId'] = self.approve_instance_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveInstanceId') is not None:
            self.approve_instance_id = m.get('ApproveInstanceId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelBlockResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CancelBlockResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CancelBlockResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelBlockResponseBody = None,
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
            temp_model = CancelBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeCancelRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class ChangeCancelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeCancelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeCancelResponseBody = None,
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
            temp_model = ChangeCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeCheckRequestApproveFlowParamApproveNodesApproverDTO(TeaModel):
    def __init__(
        self,
        approve_desc: str = None,
        approve_time: str = None,
        approver_id: str = None,
        approver_name: str = None,
        opinion: int = None,
    ):
        self.approve_desc = approve_desc
        self.approve_time = approve_time
        self.approver_id = approver_id
        self.approver_name = approver_name
        self.opinion = opinion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_desc is not None:
            result['ApproveDesc'] = self.approve_desc
        if self.approve_time is not None:
            result['ApproveTime'] = self.approve_time
        if self.approver_id is not None:
            result['ApproverId'] = self.approver_id
        if self.approver_name is not None:
            result['ApproverName'] = self.approver_name
        if self.opinion is not None:
            result['Opinion'] = self.opinion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveDesc') is not None:
            self.approve_desc = m.get('ApproveDesc')
        if m.get('ApproveTime') is not None:
            self.approve_time = m.get('ApproveTime')
        if m.get('ApproverId') is not None:
            self.approver_id = m.get('ApproverId')
        if m.get('ApproverName') is not None:
            self.approver_name = m.get('ApproverName')
        if m.get('Opinion') is not None:
            self.opinion = m.get('Opinion')
        return self


class ChangeCheckRequestApproveFlowParamApproveNodes(TeaModel):
    def __init__(
        self,
        approver_dto: List[ChangeCheckRequestApproveFlowParamApproveNodesApproverDTO] = None,
        node_status: int = None,
        process_name: str = None,
        process_node_order: int = None,
        strategy: int = None,
    ):
        self.approver_dto = approver_dto
        self.node_status = node_status
        self.process_name = process_name
        self.process_node_order = process_node_order
        self.strategy = strategy

    def validate(self):
        if self.approver_dto:
            for k in self.approver_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproverDTO'] = []
        if self.approver_dto is not None:
            for k in self.approver_dto:
                result['ApproverDTO'].append(k.to_map() if k else None)
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.process_name is not None:
            result['ProcessName'] = self.process_name
        if self.process_node_order is not None:
            result['ProcessNodeOrder'] = self.process_node_order
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approver_dto = []
        if m.get('ApproverDTO') is not None:
            for k in m.get('ApproverDTO'):
                temp_model = ChangeCheckRequestApproveFlowParamApproveNodesApproverDTO()
                self.approver_dto.append(temp_model.from_map(k))
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')
        if m.get('ProcessNodeOrder') is not None:
            self.process_node_order = m.get('ProcessNodeOrder')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        return self


class ChangeCheckRequestApproveFlowParam(TeaModel):
    def __init__(
        self,
        approve_nodes: List[ChangeCheckRequestApproveFlowParamApproveNodes] = None,
        auth_key: str = None,
        auth_sign: str = None,
        bg_vid: str = None,
        flow_status: int = None,
        timestamp: int = None,
    ):
        self.approve_nodes = approve_nodes
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.bg_vid = bg_vid
        self.flow_status = flow_status
        self.timestamp = timestamp

    def validate(self):
        if self.approve_nodes:
            for k in self.approve_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproveNodes'] = []
        if self.approve_nodes is not None:
            for k in self.approve_nodes:
                result['ApproveNodes'].append(k.to_map() if k else None)
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approve_nodes = []
        if m.get('ApproveNodes') is not None:
            for k in m.get('ApproveNodes'):
                temp_model = ChangeCheckRequestApproveFlowParamApproveNodes()
                self.approve_nodes.append(temp_model.from_map(k))
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ChangeCheckRequestBgCustomTemplateExtraDTO(TeaModel):
    def __init__(
        self,
        bg_custom_template: str = None,
        bg_custom_template_id: int = None,
        bg_custom_template_info: str = None,
        bg_custom_template_title: str = None,
        bg_vid: str = None,
        extra_info: str = None,
    ):
        self.bg_custom_template = bg_custom_template
        self.bg_custom_template_id = bg_custom_template_id
        self.bg_custom_template_info = bg_custom_template_info
        self.bg_custom_template_title = bg_custom_template_title
        self.bg_vid = bg_vid
        self.extra_info = extra_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_custom_template is not None:
            result['BgCustomTemplate'] = self.bg_custom_template
        if self.bg_custom_template_id is not None:
            result['BgCustomTemplateId'] = self.bg_custom_template_id
        if self.bg_custom_template_info is not None:
            result['BgCustomTemplateInfo'] = self.bg_custom_template_info
        if self.bg_custom_template_title is not None:
            result['BgCustomTemplateTitle'] = self.bg_custom_template_title
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgCustomTemplate') is not None:
            self.bg_custom_template = m.get('BgCustomTemplate')
        if m.get('BgCustomTemplateId') is not None:
            self.bg_custom_template_id = m.get('BgCustomTemplateId')
        if m.get('BgCustomTemplateInfo') is not None:
            self.bg_custom_template_info = m.get('BgCustomTemplateInfo')
        if m.get('BgCustomTemplateTitle') is not None:
            self.bg_custom_template_title = m.get('BgCustomTemplateTitle')
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        return self


class ChangeCheckRequestBlockInfosHitInfos(TeaModel):
    def __init__(
        self,
        hit_info: str = None,
        hit_object: str = None,
        scope: str = None,
    ):
        self.hit_info = hit_info
        self.hit_object = hit_object
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_info is not None:
            result['HitInfo'] = self.hit_info
        if self.hit_object is not None:
            result['HitObject'] = self.hit_object
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitInfo') is not None:
            self.hit_info = m.get('HitInfo')
        if m.get('HitObject') is not None:
            self.hit_object = m.get('HitObject')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class ChangeCheckRequestBlockInfos(TeaModel):
    def __init__(
        self,
        hit_infos: List[ChangeCheckRequestBlockInfosHitInfos] = None,
        id: int = None,
    ):
        self.hit_infos = hit_infos
        self.id = id

    def validate(self):
        if self.hit_infos:
            for k in self.hit_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitInfos'] = []
        if self.hit_infos is not None:
            for k in self.hit_infos:
                result['HitInfos'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_infos = []
        if m.get('HitInfos') is not None:
            for k in m.get('HitInfos'):
                temp_model = ChangeCheckRequestBlockInfosHitInfos()
                self.hit_infos.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ChangeCheckRequestCallBackInfo(TeaModel):
    def __init__(
        self,
        api: str = None,
        api_version: str = None,
        end_point: str = None,
        extra_info: str = None,
        pop_product: str = None,
        region_id: str = None,
        type: str = None,
        url: str = None,
    ):
        self.api = api
        self.api_version = api_version
        self.end_point = end_point
        self.extra_info = extra_info
        self.pop_product = pop_product
        self.region_id = region_id
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.pop_product is not None:
            result['PopProduct'] = self.pop_product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('PopProduct') is not None:
            self.pop_product = m.get('PopProduct')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ChangeCheckRequestChangeTimes(TeaModel):
    def __init__(
        self,
        change_end_time: int = None,
        change_start_time: int = None,
    ):
        self.change_end_time = change_end_time
        self.change_start_time = change_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        return self


class ChangeCheckRequestDamagedChangeNoticesSensitiveCustomersCustomerInfo(TeaModel):
    def __init__(
        self,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        uid: str = None,
    ):
        self.extra_info = extra_info
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ChangeCheckRequestDamagedChangeNoticesSensitiveCustomers(TeaModel):
    def __init__(
        self,
        customer_info: List[ChangeCheckRequestDamagedChangeNoticesSensitiveCustomersCustomerInfo] = None,
        product_code: str = None,
    ):
        self.customer_info = customer_info
        self.product_code = product_code

    def validate(self):
        if self.customer_info:
            for k in self.customer_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomerInfo'] = []
        if self.customer_info is not None:
            for k in self.customer_info:
                result['CustomerInfo'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_info = []
        if m.get('CustomerInfo') is not None:
            for k in m.get('CustomerInfo'):
                temp_model = ChangeCheckRequestDamagedChangeNoticesSensitiveCustomersCustomerInfo()
                self.customer_info.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ChangeCheckRequestDamagedChangeNotices(TeaModel):
    def __init__(
        self,
        bg_cancel_notice_content: str = None,
        bg_cancel_notice_event_id: str = None,
        channel: List[str] = None,
        content: str = None,
        event_id: str = None,
        sensitive_customers: List[ChangeCheckRequestDamagedChangeNoticesSensitiveCustomers] = None,
        type: str = None,
    ):
        self.bg_cancel_notice_content = bg_cancel_notice_content
        self.bg_cancel_notice_event_id = bg_cancel_notice_event_id
        self.channel = channel
        self.content = content
        self.event_id = event_id
        self.sensitive_customers = sensitive_customers
        self.type = type

    def validate(self):
        if self.sensitive_customers:
            for k in self.sensitive_customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_cancel_notice_content is not None:
            result['BgCancelNoticeContent'] = self.bg_cancel_notice_content
        if self.bg_cancel_notice_event_id is not None:
            result['BgCancelNoticeEventId'] = self.bg_cancel_notice_event_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.content is not None:
            result['Content'] = self.content
        if self.event_id is not None:
            result['EventId'] = self.event_id
        result['SensitiveCustomers'] = []
        if self.sensitive_customers is not None:
            for k in self.sensitive_customers:
                result['SensitiveCustomers'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgCancelNoticeContent') is not None:
            self.bg_cancel_notice_content = m.get('BgCancelNoticeContent')
        if m.get('BgCancelNoticeEventId') is not None:
            self.bg_cancel_notice_event_id = m.get('BgCancelNoticeEventId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        self.sensitive_customers = []
        if m.get('SensitiveCustomers') is not None:
            for k in m.get('SensitiveCustomers'):
                temp_model = ChangeCheckRequestDamagedChangeNoticesSensitiveCustomers()
                self.sensitive_customers.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ChangeCheckRequestInfluenceInfoNoticeInfos(TeaModel):
    def __init__(
        self,
        channel: List[str] = None,
        content: str = None,
        event_id: str = None,
    ):
        self.channel = channel
        self.content = content
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.content is not None:
            result['Content'] = self.content
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class ChangeCheckRequestInfluenceInfoSensitiveCustomersCustomerInfo(TeaModel):
    def __init__(
        self,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        uid: str = None,
    ):
        self.extra_info = extra_info
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ChangeCheckRequestInfluenceInfoSensitiveCustomers(TeaModel):
    def __init__(
        self,
        customer_info: List[ChangeCheckRequestInfluenceInfoSensitiveCustomersCustomerInfo] = None,
        product_code: str = None,
    ):
        self.customer_info = customer_info
        self.product_code = product_code

    def validate(self):
        if self.customer_info:
            for k in self.customer_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomerInfo'] = []
        if self.customer_info is not None:
            for k in self.customer_info:
                result['CustomerInfo'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_info = []
        if m.get('CustomerInfo') is not None:
            for k in m.get('CustomerInfo'):
                temp_model = ChangeCheckRequestInfluenceInfoSensitiveCustomersCustomerInfo()
                self.customer_info.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ChangeCheckRequestInfluenceInfo(TeaModel):
    def __init__(
        self,
        notice_infos: List[ChangeCheckRequestInfluenceInfoNoticeInfos] = None,
        sensitive_customers: List[ChangeCheckRequestInfluenceInfoSensitiveCustomers] = None,
    ):
        self.notice_infos = notice_infos
        self.sensitive_customers = sensitive_customers

    def validate(self):
        if self.notice_infos:
            for k in self.notice_infos:
                if k:
                    k.validate()
        if self.sensitive_customers:
            for k in self.sensitive_customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NoticeInfos'] = []
        if self.notice_infos is not None:
            for k in self.notice_infos:
                result['NoticeInfos'].append(k.to_map() if k else None)
        result['SensitiveCustomers'] = []
        if self.sensitive_customers is not None:
            for k in self.sensitive_customers:
                result['SensitiveCustomers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notice_infos = []
        if m.get('NoticeInfos') is not None:
            for k in m.get('NoticeInfos'):
                temp_model = ChangeCheckRequestInfluenceInfoNoticeInfos()
                self.notice_infos.append(temp_model.from_map(k))
        self.sensitive_customers = []
        if m.get('SensitiveCustomers') is not None:
            for k in m.get('SensitiveCustomers'):
                temp_model = ChangeCheckRequestInfluenceInfoSensitiveCustomers()
                self.sensitive_customers.append(temp_model.from_map(k))
        return self


class ChangeCheckRequestInstance(TeaModel):
    def __init__(
        self,
        attribution_app: List[str] = None,
        influence_app: List[str] = None,
        instance: List[str] = None,
        nc: List[str] = None,
        uids: List[str] = None,
    ):
        self.attribution_app = attribution_app
        self.influence_app = influence_app
        self.instance = instance
        self.nc = nc
        self.uids = uids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribution_app is not None:
            result['AttributionApp'] = self.attribution_app
        if self.influence_app is not None:
            result['InfluenceApp'] = self.influence_app
        if self.instance is not None:
            result['Instance'] = self.instance
        if self.nc is not None:
            result['Nc'] = self.nc
        if self.uids is not None:
            result['Uids'] = self.uids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributionApp') is not None:
            self.attribution_app = m.get('AttributionApp')
        if m.get('InfluenceApp') is not None:
            self.influence_app = m.get('InfluenceApp')
        if m.get('Instance') is not None:
            self.instance = m.get('Instance')
        if m.get('Nc') is not None:
            self.nc = m.get('Nc')
        if m.get('Uids') is not None:
            self.uids = m.get('Uids')
        return self


class ChangeCheckRequestProduct(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ChangeCheckRequestReleasePackageInfos(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        release_package: List[str] = None,
    ):
        self.product_code = product_code
        self.release_package = release_package

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.release_package is not None:
            result['ReleasePackage'] = self.release_package
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReleasePackage') is not None:
            self.release_package = m.get('ReleasePackage')
        return self


class ChangeCheckRequest(TeaModel):
    def __init__(
        self,
        affect_customer: str = None,
        approve_flow_param: ChangeCheckRequestApproveFlowParam = None,
        auth_key: str = None,
        auth_sign: str = None,
        bg_custom_template_extra_dto: ChangeCheckRequestBgCustomTemplateExtraDTO = None,
        bg_vid: str = None,
        block_infos: List[ChangeCheckRequestBlockInfos] = None,
        call_back_info: ChangeCheckRequestCallBackInfo = None,
        change_data_type: str = None,
        change_desc: str = None,
        change_end_time: int = None,
        change_env: str = None,
        change_items: str = None,
        change_object: str = None,
        change_opt_sub_type: str = None,
        change_opt_type: str = None,
        change_reason: str = None,
        change_rmarks: str = None,
        change_schemes: str = None,
        change_start_time: int = None,
        change_sub_type_desc: str = None,
        change_system: str = None,
        change_times: List[ChangeCheckRequestChangeTimes] = None,
        change_title: str = None,
        change_validation: str = None,
        creator_emp_id: str = None,
        damaged_change_notices: List[ChangeCheckRequestDamagedChangeNotices] = None,
        executor_emp_id: str = None,
        extra_info: str = None,
        follower: List[str] = None,
        gray_status: str = None,
        harm_change_notice_enum: str = None,
        incidence: str = None,
        influence_info: ChangeCheckRequestInfluenceInfo = None,
        instance: ChangeCheckRequestInstance = None,
        need_modify_doc: str = None,
        product: List[ChangeCheckRequestProduct] = None,
        release_package_infos: List[ChangeCheckRequestReleasePackageInfos] = None,
        req_timestamp: int = None,
        reuse_source_order_id: str = None,
        risk_level: str = None,
        rollback: str = None,
        source_name: str = None,
        source_order_id: str = None,
        source_url: str = None,
        white_type: int = None,
    ):
        self.affect_customer = affect_customer
        self.approve_flow_param = approve_flow_param
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.bg_custom_template_extra_dto = bg_custom_template_extra_dto
        self.bg_vid = bg_vid
        self.block_infos = block_infos
        self.call_back_info = call_back_info
        self.change_data_type = change_data_type
        self.change_desc = change_desc
        self.change_end_time = change_end_time
        self.change_env = change_env
        self.change_items = change_items
        self.change_object = change_object
        self.change_opt_sub_type = change_opt_sub_type
        self.change_opt_type = change_opt_type
        self.change_reason = change_reason
        self.change_rmarks = change_rmarks
        self.change_schemes = change_schemes
        self.change_start_time = change_start_time
        self.change_sub_type_desc = change_sub_type_desc
        self.change_system = change_system
        self.change_times = change_times
        self.change_title = change_title
        self.change_validation = change_validation
        self.creator_emp_id = creator_emp_id
        self.damaged_change_notices = damaged_change_notices
        self.executor_emp_id = executor_emp_id
        self.extra_info = extra_info
        self.follower = follower
        self.gray_status = gray_status
        self.harm_change_notice_enum = harm_change_notice_enum
        self.incidence = incidence
        self.influence_info = influence_info
        self.instance = instance
        self.need_modify_doc = need_modify_doc
        self.product = product
        self.release_package_infos = release_package_infos
        self.req_timestamp = req_timestamp
        self.reuse_source_order_id = reuse_source_order_id
        self.risk_level = risk_level
        self.rollback = rollback
        self.source_name = source_name
        self.source_order_id = source_order_id
        self.source_url = source_url
        self.white_type = white_type

    def validate(self):
        if self.approve_flow_param:
            self.approve_flow_param.validate()
        if self.bg_custom_template_extra_dto:
            self.bg_custom_template_extra_dto.validate()
        if self.block_infos:
            for k in self.block_infos:
                if k:
                    k.validate()
        if self.call_back_info:
            self.call_back_info.validate()
        if self.change_times:
            for k in self.change_times:
                if k:
                    k.validate()
        if self.damaged_change_notices:
            for k in self.damaged_change_notices:
                if k:
                    k.validate()
        if self.influence_info:
            self.influence_info.validate()
        if self.instance:
            self.instance.validate()
        if self.product:
            for k in self.product:
                if k:
                    k.validate()
        if self.release_package_infos:
            for k in self.release_package_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_customer is not None:
            result['AffectCustomer'] = self.affect_customer
        if self.approve_flow_param is not None:
            result['ApproveFlowParam'] = self.approve_flow_param.to_map()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.bg_custom_template_extra_dto is not None:
            result['BgCustomTemplateExtraDTO'] = self.bg_custom_template_extra_dto.to_map()
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        result['BlockInfos'] = []
        if self.block_infos is not None:
            for k in self.block_infos:
                result['BlockInfos'].append(k.to_map() if k else None)
        if self.call_back_info is not None:
            result['CallBackInfo'] = self.call_back_info.to_map()
        if self.change_data_type is not None:
            result['ChangeDataType'] = self.change_data_type
        if self.change_desc is not None:
            result['ChangeDesc'] = self.change_desc
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_env is not None:
            result['ChangeEnv'] = self.change_env
        if self.change_items is not None:
            result['ChangeItems'] = self.change_items
        if self.change_object is not None:
            result['ChangeObject'] = self.change_object
        if self.change_opt_sub_type is not None:
            result['ChangeOptSubType'] = self.change_opt_sub_type
        if self.change_opt_type is not None:
            result['ChangeOptType'] = self.change_opt_type
        if self.change_reason is not None:
            result['ChangeReason'] = self.change_reason
        if self.change_rmarks is not None:
            result['ChangeRmarks'] = self.change_rmarks
        if self.change_schemes is not None:
            result['ChangeSchemes'] = self.change_schemes
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_sub_type_desc is not None:
            result['ChangeSubTypeDesc'] = self.change_sub_type_desc
        if self.change_system is not None:
            result['ChangeSystem'] = self.change_system
        result['ChangeTimes'] = []
        if self.change_times is not None:
            for k in self.change_times:
                result['ChangeTimes'].append(k.to_map() if k else None)
        if self.change_title is not None:
            result['ChangeTitle'] = self.change_title
        if self.change_validation is not None:
            result['ChangeValidation'] = self.change_validation
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        result['DamagedChangeNotices'] = []
        if self.damaged_change_notices is not None:
            for k in self.damaged_change_notices:
                result['DamagedChangeNotices'].append(k.to_map() if k else None)
        if self.executor_emp_id is not None:
            result['ExecutorEmpId'] = self.executor_emp_id
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.follower is not None:
            result['Follower'] = self.follower
        if self.gray_status is not None:
            result['GrayStatus'] = self.gray_status
        if self.harm_change_notice_enum is not None:
            result['HarmChangeNoticeEnum'] = self.harm_change_notice_enum
        if self.incidence is not None:
            result['Incidence'] = self.incidence
        if self.influence_info is not None:
            result['InfluenceInfo'] = self.influence_info.to_map()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.need_modify_doc is not None:
            result['NeedModifyDoc'] = self.need_modify_doc
        result['Product'] = []
        if self.product is not None:
            for k in self.product:
                result['Product'].append(k.to_map() if k else None)
        result['ReleasePackageInfos'] = []
        if self.release_package_infos is not None:
            for k in self.release_package_infos:
                result['ReleasePackageInfos'].append(k.to_map() if k else None)
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.reuse_source_order_id is not None:
            result['ReuseSourceOrderId'] = self.reuse_source_order_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rollback is not None:
            result['Rollback'] = self.rollback
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectCustomer') is not None:
            self.affect_customer = m.get('AffectCustomer')
        if m.get('ApproveFlowParam') is not None:
            temp_model = ChangeCheckRequestApproveFlowParam()
            self.approve_flow_param = temp_model.from_map(m['ApproveFlowParam'])
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('BgCustomTemplateExtraDTO') is not None:
            temp_model = ChangeCheckRequestBgCustomTemplateExtraDTO()
            self.bg_custom_template_extra_dto = temp_model.from_map(m['BgCustomTemplateExtraDTO'])
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        self.block_infos = []
        if m.get('BlockInfos') is not None:
            for k in m.get('BlockInfos'):
                temp_model = ChangeCheckRequestBlockInfos()
                self.block_infos.append(temp_model.from_map(k))
        if m.get('CallBackInfo') is not None:
            temp_model = ChangeCheckRequestCallBackInfo()
            self.call_back_info = temp_model.from_map(m['CallBackInfo'])
        if m.get('ChangeDataType') is not None:
            self.change_data_type = m.get('ChangeDataType')
        if m.get('ChangeDesc') is not None:
            self.change_desc = m.get('ChangeDesc')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeEnv') is not None:
            self.change_env = m.get('ChangeEnv')
        if m.get('ChangeItems') is not None:
            self.change_items = m.get('ChangeItems')
        if m.get('ChangeObject') is not None:
            self.change_object = m.get('ChangeObject')
        if m.get('ChangeOptSubType') is not None:
            self.change_opt_sub_type = m.get('ChangeOptSubType')
        if m.get('ChangeOptType') is not None:
            self.change_opt_type = m.get('ChangeOptType')
        if m.get('ChangeReason') is not None:
            self.change_reason = m.get('ChangeReason')
        if m.get('ChangeRmarks') is not None:
            self.change_rmarks = m.get('ChangeRmarks')
        if m.get('ChangeSchemes') is not None:
            self.change_schemes = m.get('ChangeSchemes')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeSubTypeDesc') is not None:
            self.change_sub_type_desc = m.get('ChangeSubTypeDesc')
        if m.get('ChangeSystem') is not None:
            self.change_system = m.get('ChangeSystem')
        self.change_times = []
        if m.get('ChangeTimes') is not None:
            for k in m.get('ChangeTimes'):
                temp_model = ChangeCheckRequestChangeTimes()
                self.change_times.append(temp_model.from_map(k))
        if m.get('ChangeTitle') is not None:
            self.change_title = m.get('ChangeTitle')
        if m.get('ChangeValidation') is not None:
            self.change_validation = m.get('ChangeValidation')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        self.damaged_change_notices = []
        if m.get('DamagedChangeNotices') is not None:
            for k in m.get('DamagedChangeNotices'):
                temp_model = ChangeCheckRequestDamagedChangeNotices()
                self.damaged_change_notices.append(temp_model.from_map(k))
        if m.get('ExecutorEmpId') is not None:
            self.executor_emp_id = m.get('ExecutorEmpId')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Follower') is not None:
            self.follower = m.get('Follower')
        if m.get('GrayStatus') is not None:
            self.gray_status = m.get('GrayStatus')
        if m.get('HarmChangeNoticeEnum') is not None:
            self.harm_change_notice_enum = m.get('HarmChangeNoticeEnum')
        if m.get('Incidence') is not None:
            self.incidence = m.get('Incidence')
        if m.get('InfluenceInfo') is not None:
            temp_model = ChangeCheckRequestInfluenceInfo()
            self.influence_info = temp_model.from_map(m['InfluenceInfo'])
        if m.get('Instance') is not None:
            temp_model = ChangeCheckRequestInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('NeedModifyDoc') is not None:
            self.need_modify_doc = m.get('NeedModifyDoc')
        self.product = []
        if m.get('Product') is not None:
            for k in m.get('Product'):
                temp_model = ChangeCheckRequestProduct()
                self.product.append(temp_model.from_map(k))
        self.release_package_infos = []
        if m.get('ReleasePackageInfos') is not None:
            for k in m.get('ReleasePackageInfos'):
                temp_model = ChangeCheckRequestReleasePackageInfos()
                self.release_package_infos.append(temp_model.from_map(k))
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('ReuseSourceOrderId') is not None:
            self.reuse_source_order_id = m.get('ReuseSourceOrderId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class ChangeCheckShrinkRequestApproveFlowParamApproveNodesApproverDTO(TeaModel):
    def __init__(
        self,
        approve_desc: str = None,
        approve_time: str = None,
        approver_id: str = None,
        approver_name: str = None,
        opinion: int = None,
    ):
        self.approve_desc = approve_desc
        self.approve_time = approve_time
        self.approver_id = approver_id
        self.approver_name = approver_name
        self.opinion = opinion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_desc is not None:
            result['ApproveDesc'] = self.approve_desc
        if self.approve_time is not None:
            result['ApproveTime'] = self.approve_time
        if self.approver_id is not None:
            result['ApproverId'] = self.approver_id
        if self.approver_name is not None:
            result['ApproverName'] = self.approver_name
        if self.opinion is not None:
            result['Opinion'] = self.opinion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveDesc') is not None:
            self.approve_desc = m.get('ApproveDesc')
        if m.get('ApproveTime') is not None:
            self.approve_time = m.get('ApproveTime')
        if m.get('ApproverId') is not None:
            self.approver_id = m.get('ApproverId')
        if m.get('ApproverName') is not None:
            self.approver_name = m.get('ApproverName')
        if m.get('Opinion') is not None:
            self.opinion = m.get('Opinion')
        return self


class ChangeCheckShrinkRequestApproveFlowParamApproveNodes(TeaModel):
    def __init__(
        self,
        approver_dto: List[ChangeCheckShrinkRequestApproveFlowParamApproveNodesApproverDTO] = None,
        node_status: int = None,
        process_name: str = None,
        process_node_order: int = None,
        strategy: int = None,
    ):
        self.approver_dto = approver_dto
        self.node_status = node_status
        self.process_name = process_name
        self.process_node_order = process_node_order
        self.strategy = strategy

    def validate(self):
        if self.approver_dto:
            for k in self.approver_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproverDTO'] = []
        if self.approver_dto is not None:
            for k in self.approver_dto:
                result['ApproverDTO'].append(k.to_map() if k else None)
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.process_name is not None:
            result['ProcessName'] = self.process_name
        if self.process_node_order is not None:
            result['ProcessNodeOrder'] = self.process_node_order
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approver_dto = []
        if m.get('ApproverDTO') is not None:
            for k in m.get('ApproverDTO'):
                temp_model = ChangeCheckShrinkRequestApproveFlowParamApproveNodesApproverDTO()
                self.approver_dto.append(temp_model.from_map(k))
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')
        if m.get('ProcessNodeOrder') is not None:
            self.process_node_order = m.get('ProcessNodeOrder')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        return self


class ChangeCheckShrinkRequestApproveFlowParam(TeaModel):
    def __init__(
        self,
        approve_nodes: List[ChangeCheckShrinkRequestApproveFlowParamApproveNodes] = None,
        auth_key: str = None,
        auth_sign: str = None,
        bg_vid: str = None,
        flow_status: int = None,
        timestamp: int = None,
    ):
        self.approve_nodes = approve_nodes
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.bg_vid = bg_vid
        self.flow_status = flow_status
        self.timestamp = timestamp

    def validate(self):
        if self.approve_nodes:
            for k in self.approve_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproveNodes'] = []
        if self.approve_nodes is not None:
            for k in self.approve_nodes:
                result['ApproveNodes'].append(k.to_map() if k else None)
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approve_nodes = []
        if m.get('ApproveNodes') is not None:
            for k in m.get('ApproveNodes'):
                temp_model = ChangeCheckShrinkRequestApproveFlowParamApproveNodes()
                self.approve_nodes.append(temp_model.from_map(k))
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ChangeCheckShrinkRequestBgCustomTemplateExtraDTO(TeaModel):
    def __init__(
        self,
        bg_custom_template: str = None,
        bg_custom_template_id: int = None,
        bg_custom_template_info: str = None,
        bg_custom_template_title: str = None,
        bg_vid: str = None,
        extra_info: str = None,
    ):
        self.bg_custom_template = bg_custom_template
        self.bg_custom_template_id = bg_custom_template_id
        self.bg_custom_template_info = bg_custom_template_info
        self.bg_custom_template_title = bg_custom_template_title
        self.bg_vid = bg_vid
        self.extra_info = extra_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_custom_template is not None:
            result['BgCustomTemplate'] = self.bg_custom_template
        if self.bg_custom_template_id is not None:
            result['BgCustomTemplateId'] = self.bg_custom_template_id
        if self.bg_custom_template_info is not None:
            result['BgCustomTemplateInfo'] = self.bg_custom_template_info
        if self.bg_custom_template_title is not None:
            result['BgCustomTemplateTitle'] = self.bg_custom_template_title
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgCustomTemplate') is not None:
            self.bg_custom_template = m.get('BgCustomTemplate')
        if m.get('BgCustomTemplateId') is not None:
            self.bg_custom_template_id = m.get('BgCustomTemplateId')
        if m.get('BgCustomTemplateInfo') is not None:
            self.bg_custom_template_info = m.get('BgCustomTemplateInfo')
        if m.get('BgCustomTemplateTitle') is not None:
            self.bg_custom_template_title = m.get('BgCustomTemplateTitle')
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        return self


class ChangeCheckShrinkRequestBlockInfosHitInfos(TeaModel):
    def __init__(
        self,
        hit_info: str = None,
        hit_object: str = None,
        scope: str = None,
    ):
        self.hit_info = hit_info
        self.hit_object = hit_object
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_info is not None:
            result['HitInfo'] = self.hit_info
        if self.hit_object is not None:
            result['HitObject'] = self.hit_object
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitInfo') is not None:
            self.hit_info = m.get('HitInfo')
        if m.get('HitObject') is not None:
            self.hit_object = m.get('HitObject')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class ChangeCheckShrinkRequestBlockInfos(TeaModel):
    def __init__(
        self,
        hit_infos: List[ChangeCheckShrinkRequestBlockInfosHitInfos] = None,
        id: int = None,
    ):
        self.hit_infos = hit_infos
        self.id = id

    def validate(self):
        if self.hit_infos:
            for k in self.hit_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitInfos'] = []
        if self.hit_infos is not None:
            for k in self.hit_infos:
                result['HitInfos'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_infos = []
        if m.get('HitInfos') is not None:
            for k in m.get('HitInfos'):
                temp_model = ChangeCheckShrinkRequestBlockInfosHitInfos()
                self.hit_infos.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ChangeCheckShrinkRequestCallBackInfo(TeaModel):
    def __init__(
        self,
        api: str = None,
        api_version: str = None,
        end_point: str = None,
        extra_info: str = None,
        pop_product: str = None,
        region_id: str = None,
        type: str = None,
        url: str = None,
    ):
        self.api = api
        self.api_version = api_version
        self.end_point = end_point
        self.extra_info = extra_info
        self.pop_product = pop_product
        self.region_id = region_id
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.pop_product is not None:
            result['PopProduct'] = self.pop_product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('PopProduct') is not None:
            self.pop_product = m.get('PopProduct')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ChangeCheckShrinkRequestChangeTimes(TeaModel):
    def __init__(
        self,
        change_end_time: int = None,
        change_start_time: int = None,
    ):
        self.change_end_time = change_end_time
        self.change_start_time = change_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        return self


class ChangeCheckShrinkRequestInfluenceInfoNoticeInfos(TeaModel):
    def __init__(
        self,
        channel: List[str] = None,
        content: str = None,
        event_id: str = None,
    ):
        self.channel = channel
        self.content = content
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.content is not None:
            result['Content'] = self.content
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class ChangeCheckShrinkRequestInfluenceInfoSensitiveCustomersCustomerInfo(TeaModel):
    def __init__(
        self,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        uid: str = None,
    ):
        self.extra_info = extra_info
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ChangeCheckShrinkRequestInfluenceInfoSensitiveCustomers(TeaModel):
    def __init__(
        self,
        customer_info: List[ChangeCheckShrinkRequestInfluenceInfoSensitiveCustomersCustomerInfo] = None,
        product_code: str = None,
    ):
        self.customer_info = customer_info
        self.product_code = product_code

    def validate(self):
        if self.customer_info:
            for k in self.customer_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomerInfo'] = []
        if self.customer_info is not None:
            for k in self.customer_info:
                result['CustomerInfo'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_info = []
        if m.get('CustomerInfo') is not None:
            for k in m.get('CustomerInfo'):
                temp_model = ChangeCheckShrinkRequestInfluenceInfoSensitiveCustomersCustomerInfo()
                self.customer_info.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ChangeCheckShrinkRequestInfluenceInfo(TeaModel):
    def __init__(
        self,
        notice_infos: List[ChangeCheckShrinkRequestInfluenceInfoNoticeInfos] = None,
        sensitive_customers: List[ChangeCheckShrinkRequestInfluenceInfoSensitiveCustomers] = None,
    ):
        self.notice_infos = notice_infos
        self.sensitive_customers = sensitive_customers

    def validate(self):
        if self.notice_infos:
            for k in self.notice_infos:
                if k:
                    k.validate()
        if self.sensitive_customers:
            for k in self.sensitive_customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NoticeInfos'] = []
        if self.notice_infos is not None:
            for k in self.notice_infos:
                result['NoticeInfos'].append(k.to_map() if k else None)
        result['SensitiveCustomers'] = []
        if self.sensitive_customers is not None:
            for k in self.sensitive_customers:
                result['SensitiveCustomers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notice_infos = []
        if m.get('NoticeInfos') is not None:
            for k in m.get('NoticeInfos'):
                temp_model = ChangeCheckShrinkRequestInfluenceInfoNoticeInfos()
                self.notice_infos.append(temp_model.from_map(k))
        self.sensitive_customers = []
        if m.get('SensitiveCustomers') is not None:
            for k in m.get('SensitiveCustomers'):
                temp_model = ChangeCheckShrinkRequestInfluenceInfoSensitiveCustomers()
                self.sensitive_customers.append(temp_model.from_map(k))
        return self


class ChangeCheckShrinkRequestInstance(TeaModel):
    def __init__(
        self,
        attribution_app: List[str] = None,
        influence_app: List[str] = None,
        instance: List[str] = None,
        nc: List[str] = None,
        uids: List[str] = None,
    ):
        self.attribution_app = attribution_app
        self.influence_app = influence_app
        self.instance = instance
        self.nc = nc
        self.uids = uids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribution_app is not None:
            result['AttributionApp'] = self.attribution_app
        if self.influence_app is not None:
            result['InfluenceApp'] = self.influence_app
        if self.instance is not None:
            result['Instance'] = self.instance
        if self.nc is not None:
            result['Nc'] = self.nc
        if self.uids is not None:
            result['Uids'] = self.uids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributionApp') is not None:
            self.attribution_app = m.get('AttributionApp')
        if m.get('InfluenceApp') is not None:
            self.influence_app = m.get('InfluenceApp')
        if m.get('Instance') is not None:
            self.instance = m.get('Instance')
        if m.get('Nc') is not None:
            self.nc = m.get('Nc')
        if m.get('Uids') is not None:
            self.uids = m.get('Uids')
        return self


class ChangeCheckShrinkRequestProduct(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ChangeCheckShrinkRequestReleasePackageInfos(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        release_package: List[str] = None,
    ):
        self.product_code = product_code
        self.release_package = release_package

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.release_package is not None:
            result['ReleasePackage'] = self.release_package
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReleasePackage') is not None:
            self.release_package = m.get('ReleasePackage')
        return self


class ChangeCheckShrinkRequest(TeaModel):
    def __init__(
        self,
        affect_customer: str = None,
        approve_flow_param: ChangeCheckShrinkRequestApproveFlowParam = None,
        auth_key: str = None,
        auth_sign: str = None,
        bg_custom_template_extra_dto: ChangeCheckShrinkRequestBgCustomTemplateExtraDTO = None,
        bg_vid: str = None,
        block_infos: List[ChangeCheckShrinkRequestBlockInfos] = None,
        call_back_info: ChangeCheckShrinkRequestCallBackInfo = None,
        change_data_type: str = None,
        change_desc: str = None,
        change_end_time: int = None,
        change_env: str = None,
        change_items: str = None,
        change_object: str = None,
        change_opt_sub_type: str = None,
        change_opt_type: str = None,
        change_reason: str = None,
        change_rmarks: str = None,
        change_schemes: str = None,
        change_start_time: int = None,
        change_sub_type_desc: str = None,
        change_system: str = None,
        change_times: List[ChangeCheckShrinkRequestChangeTimes] = None,
        change_title: str = None,
        change_validation: str = None,
        creator_emp_id: str = None,
        damaged_change_notices_shrink: str = None,
        executor_emp_id: str = None,
        extra_info: str = None,
        follower: List[str] = None,
        gray_status: str = None,
        harm_change_notice_enum: str = None,
        incidence: str = None,
        influence_info: ChangeCheckShrinkRequestInfluenceInfo = None,
        instance: ChangeCheckShrinkRequestInstance = None,
        need_modify_doc: str = None,
        product: List[ChangeCheckShrinkRequestProduct] = None,
        release_package_infos: List[ChangeCheckShrinkRequestReleasePackageInfos] = None,
        req_timestamp: int = None,
        reuse_source_order_id: str = None,
        risk_level: str = None,
        rollback: str = None,
        source_name: str = None,
        source_order_id: str = None,
        source_url: str = None,
        white_type: int = None,
    ):
        self.affect_customer = affect_customer
        self.approve_flow_param = approve_flow_param
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.bg_custom_template_extra_dto = bg_custom_template_extra_dto
        self.bg_vid = bg_vid
        self.block_infos = block_infos
        self.call_back_info = call_back_info
        self.change_data_type = change_data_type
        self.change_desc = change_desc
        self.change_end_time = change_end_time
        self.change_env = change_env
        self.change_items = change_items
        self.change_object = change_object
        self.change_opt_sub_type = change_opt_sub_type
        self.change_opt_type = change_opt_type
        self.change_reason = change_reason
        self.change_rmarks = change_rmarks
        self.change_schemes = change_schemes
        self.change_start_time = change_start_time
        self.change_sub_type_desc = change_sub_type_desc
        self.change_system = change_system
        self.change_times = change_times
        self.change_title = change_title
        self.change_validation = change_validation
        self.creator_emp_id = creator_emp_id
        self.damaged_change_notices_shrink = damaged_change_notices_shrink
        self.executor_emp_id = executor_emp_id
        self.extra_info = extra_info
        self.follower = follower
        self.gray_status = gray_status
        self.harm_change_notice_enum = harm_change_notice_enum
        self.incidence = incidence
        self.influence_info = influence_info
        self.instance = instance
        self.need_modify_doc = need_modify_doc
        self.product = product
        self.release_package_infos = release_package_infos
        self.req_timestamp = req_timestamp
        self.reuse_source_order_id = reuse_source_order_id
        self.risk_level = risk_level
        self.rollback = rollback
        self.source_name = source_name
        self.source_order_id = source_order_id
        self.source_url = source_url
        self.white_type = white_type

    def validate(self):
        if self.approve_flow_param:
            self.approve_flow_param.validate()
        if self.bg_custom_template_extra_dto:
            self.bg_custom_template_extra_dto.validate()
        if self.block_infos:
            for k in self.block_infos:
                if k:
                    k.validate()
        if self.call_back_info:
            self.call_back_info.validate()
        if self.change_times:
            for k in self.change_times:
                if k:
                    k.validate()
        if self.influence_info:
            self.influence_info.validate()
        if self.instance:
            self.instance.validate()
        if self.product:
            for k in self.product:
                if k:
                    k.validate()
        if self.release_package_infos:
            for k in self.release_package_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_customer is not None:
            result['AffectCustomer'] = self.affect_customer
        if self.approve_flow_param is not None:
            result['ApproveFlowParam'] = self.approve_flow_param.to_map()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.bg_custom_template_extra_dto is not None:
            result['BgCustomTemplateExtraDTO'] = self.bg_custom_template_extra_dto.to_map()
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        result['BlockInfos'] = []
        if self.block_infos is not None:
            for k in self.block_infos:
                result['BlockInfos'].append(k.to_map() if k else None)
        if self.call_back_info is not None:
            result['CallBackInfo'] = self.call_back_info.to_map()
        if self.change_data_type is not None:
            result['ChangeDataType'] = self.change_data_type
        if self.change_desc is not None:
            result['ChangeDesc'] = self.change_desc
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_env is not None:
            result['ChangeEnv'] = self.change_env
        if self.change_items is not None:
            result['ChangeItems'] = self.change_items
        if self.change_object is not None:
            result['ChangeObject'] = self.change_object
        if self.change_opt_sub_type is not None:
            result['ChangeOptSubType'] = self.change_opt_sub_type
        if self.change_opt_type is not None:
            result['ChangeOptType'] = self.change_opt_type
        if self.change_reason is not None:
            result['ChangeReason'] = self.change_reason
        if self.change_rmarks is not None:
            result['ChangeRmarks'] = self.change_rmarks
        if self.change_schemes is not None:
            result['ChangeSchemes'] = self.change_schemes
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_sub_type_desc is not None:
            result['ChangeSubTypeDesc'] = self.change_sub_type_desc
        if self.change_system is not None:
            result['ChangeSystem'] = self.change_system
        result['ChangeTimes'] = []
        if self.change_times is not None:
            for k in self.change_times:
                result['ChangeTimes'].append(k.to_map() if k else None)
        if self.change_title is not None:
            result['ChangeTitle'] = self.change_title
        if self.change_validation is not None:
            result['ChangeValidation'] = self.change_validation
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        if self.damaged_change_notices_shrink is not None:
            result['DamagedChangeNotices'] = self.damaged_change_notices_shrink
        if self.executor_emp_id is not None:
            result['ExecutorEmpId'] = self.executor_emp_id
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.follower is not None:
            result['Follower'] = self.follower
        if self.gray_status is not None:
            result['GrayStatus'] = self.gray_status
        if self.harm_change_notice_enum is not None:
            result['HarmChangeNoticeEnum'] = self.harm_change_notice_enum
        if self.incidence is not None:
            result['Incidence'] = self.incidence
        if self.influence_info is not None:
            result['InfluenceInfo'] = self.influence_info.to_map()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.need_modify_doc is not None:
            result['NeedModifyDoc'] = self.need_modify_doc
        result['Product'] = []
        if self.product is not None:
            for k in self.product:
                result['Product'].append(k.to_map() if k else None)
        result['ReleasePackageInfos'] = []
        if self.release_package_infos is not None:
            for k in self.release_package_infos:
                result['ReleasePackageInfos'].append(k.to_map() if k else None)
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.reuse_source_order_id is not None:
            result['ReuseSourceOrderId'] = self.reuse_source_order_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rollback is not None:
            result['Rollback'] = self.rollback
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectCustomer') is not None:
            self.affect_customer = m.get('AffectCustomer')
        if m.get('ApproveFlowParam') is not None:
            temp_model = ChangeCheckShrinkRequestApproveFlowParam()
            self.approve_flow_param = temp_model.from_map(m['ApproveFlowParam'])
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('BgCustomTemplateExtraDTO') is not None:
            temp_model = ChangeCheckShrinkRequestBgCustomTemplateExtraDTO()
            self.bg_custom_template_extra_dto = temp_model.from_map(m['BgCustomTemplateExtraDTO'])
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        self.block_infos = []
        if m.get('BlockInfos') is not None:
            for k in m.get('BlockInfos'):
                temp_model = ChangeCheckShrinkRequestBlockInfos()
                self.block_infos.append(temp_model.from_map(k))
        if m.get('CallBackInfo') is not None:
            temp_model = ChangeCheckShrinkRequestCallBackInfo()
            self.call_back_info = temp_model.from_map(m['CallBackInfo'])
        if m.get('ChangeDataType') is not None:
            self.change_data_type = m.get('ChangeDataType')
        if m.get('ChangeDesc') is not None:
            self.change_desc = m.get('ChangeDesc')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeEnv') is not None:
            self.change_env = m.get('ChangeEnv')
        if m.get('ChangeItems') is not None:
            self.change_items = m.get('ChangeItems')
        if m.get('ChangeObject') is not None:
            self.change_object = m.get('ChangeObject')
        if m.get('ChangeOptSubType') is not None:
            self.change_opt_sub_type = m.get('ChangeOptSubType')
        if m.get('ChangeOptType') is not None:
            self.change_opt_type = m.get('ChangeOptType')
        if m.get('ChangeReason') is not None:
            self.change_reason = m.get('ChangeReason')
        if m.get('ChangeRmarks') is not None:
            self.change_rmarks = m.get('ChangeRmarks')
        if m.get('ChangeSchemes') is not None:
            self.change_schemes = m.get('ChangeSchemes')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeSubTypeDesc') is not None:
            self.change_sub_type_desc = m.get('ChangeSubTypeDesc')
        if m.get('ChangeSystem') is not None:
            self.change_system = m.get('ChangeSystem')
        self.change_times = []
        if m.get('ChangeTimes') is not None:
            for k in m.get('ChangeTimes'):
                temp_model = ChangeCheckShrinkRequestChangeTimes()
                self.change_times.append(temp_model.from_map(k))
        if m.get('ChangeTitle') is not None:
            self.change_title = m.get('ChangeTitle')
        if m.get('ChangeValidation') is not None:
            self.change_validation = m.get('ChangeValidation')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        if m.get('DamagedChangeNotices') is not None:
            self.damaged_change_notices_shrink = m.get('DamagedChangeNotices')
        if m.get('ExecutorEmpId') is not None:
            self.executor_emp_id = m.get('ExecutorEmpId')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Follower') is not None:
            self.follower = m.get('Follower')
        if m.get('GrayStatus') is not None:
            self.gray_status = m.get('GrayStatus')
        if m.get('HarmChangeNoticeEnum') is not None:
            self.harm_change_notice_enum = m.get('HarmChangeNoticeEnum')
        if m.get('Incidence') is not None:
            self.incidence = m.get('Incidence')
        if m.get('InfluenceInfo') is not None:
            temp_model = ChangeCheckShrinkRequestInfluenceInfo()
            self.influence_info = temp_model.from_map(m['InfluenceInfo'])
        if m.get('Instance') is not None:
            temp_model = ChangeCheckShrinkRequestInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('NeedModifyDoc') is not None:
            self.need_modify_doc = m.get('NeedModifyDoc')
        self.product = []
        if m.get('Product') is not None:
            for k in m.get('Product'):
                temp_model = ChangeCheckShrinkRequestProduct()
                self.product.append(temp_model.from_map(k))
        self.release_package_infos = []
        if m.get('ReleasePackageInfos') is not None:
            for k in m.get('ReleasePackageInfos'):
                temp_model = ChangeCheckShrinkRequestReleasePackageInfos()
                self.release_package_infos.append(temp_model.from_map(k))
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('ReuseSourceOrderId') is not None:
            self.reuse_source_order_id = m.get('ReuseSourceOrderId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class ChangeCheckResponseBodyDataRuleDetailUrlList(TeaModel):
    def __init__(
        self,
        scene_enum: str = None,
        title: str = None,
        url: str = None,
    ):
        self.scene_enum = scene_enum
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_enum is not None:
            result['SceneEnum'] = self.scene_enum
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneEnum') is not None:
            self.scene_enum = m.get('SceneEnum')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ChangeCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        approve_result_url: str = None,
        bg_check_status: str = None,
        bg_vid: str = None,
        change_status: str = None,
        check_result_url: str = None,
        check_status: str = None,
        checkhold_reason: List[str] = None,
        rule_detail_url_list: List[ChangeCheckResponseBodyDataRuleDetailUrlList] = None,
        source_order_id: str = None,
    ):
        self.approve_result_url = approve_result_url
        self.bg_check_status = bg_check_status
        self.bg_vid = bg_vid
        self.change_status = change_status
        self.check_result_url = check_result_url
        self.check_status = check_status
        self.checkhold_reason = checkhold_reason
        self.rule_detail_url_list = rule_detail_url_list
        self.source_order_id = source_order_id

    def validate(self):
        if self.rule_detail_url_list:
            for k in self.rule_detail_url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_result_url is not None:
            result['ApproveResultUrl'] = self.approve_result_url
        if self.bg_check_status is not None:
            result['BgCheckStatus'] = self.bg_check_status
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        if self.change_status is not None:
            result['ChangeStatus'] = self.change_status
        if self.check_result_url is not None:
            result['CheckResultUrl'] = self.check_result_url
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.checkhold_reason is not None:
            result['CheckholdReason'] = self.checkhold_reason
        result['RuleDetailUrlList'] = []
        if self.rule_detail_url_list is not None:
            for k in self.rule_detail_url_list:
                result['RuleDetailUrlList'].append(k.to_map() if k else None)
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveResultUrl') is not None:
            self.approve_result_url = m.get('ApproveResultUrl')
        if m.get('BgCheckStatus') is not None:
            self.bg_check_status = m.get('BgCheckStatus')
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        if m.get('ChangeStatus') is not None:
            self.change_status = m.get('ChangeStatus')
        if m.get('CheckResultUrl') is not None:
            self.check_result_url = m.get('CheckResultUrl')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckholdReason') is not None:
            self.checkhold_reason = m.get('CheckholdReason')
        self.rule_detail_url_list = []
        if m.get('RuleDetailUrlList') is not None:
            for k in m.get('RuleDetailUrlList'):
                temp_model = ChangeCheckResponseBodyDataRuleDetailUrlList()
                self.rule_detail_url_list.append(temp_model.from_map(k))
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class ChangeCheckResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ChangeCheckResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChangeCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeCheckResponseBody = None,
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
            temp_model = ChangeCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeEndRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        change_end_time: int = None,
        change_result: str = None,
        cur_batch_no: int = None,
        executor_emp_id: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
        total_batch_no: int = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.change_end_time = change_end_time
        self.change_result = change_result
        self.cur_batch_no = cur_batch_no
        self.executor_emp_id = executor_emp_id
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id
        self.total_batch_no = total_batch_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_result is not None:
            result['ChangeResult'] = self.change_result
        if self.cur_batch_no is not None:
            result['CurBatchNo'] = self.cur_batch_no
        if self.executor_emp_id is not None:
            result['ExecutorEmpId'] = self.executor_emp_id
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.total_batch_no is not None:
            result['TotalBatchNo'] = self.total_batch_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeResult') is not None:
            self.change_result = m.get('ChangeResult')
        if m.get('CurBatchNo') is not None:
            self.cur_batch_no = m.get('CurBatchNo')
        if m.get('ExecutorEmpId') is not None:
            self.executor_emp_id = m.get('ExecutorEmpId')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('TotalBatchNo') is not None:
            self.total_batch_no = m.get('TotalBatchNo')
        return self


class ChangeEndResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeEndResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeEndResponseBody = None,
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
            temp_model = ChangeEndResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeStartRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        change_end_time: int = None,
        change_object: str = None,
        change_opt_type: str = None,
        change_start_time: int = None,
        change_title: str = None,
        creator_emp_id: str = None,
        cur_batch_no: int = None,
        executor_emp_id: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
        total_batch_no: int = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.change_end_time = change_end_time
        self.change_object = change_object
        self.change_opt_type = change_opt_type
        self.change_start_time = change_start_time
        self.change_title = change_title
        self.creator_emp_id = creator_emp_id
        self.cur_batch_no = cur_batch_no
        self.executor_emp_id = executor_emp_id
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id
        self.total_batch_no = total_batch_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_object is not None:
            result['ChangeObject'] = self.change_object
        if self.change_opt_type is not None:
            result['ChangeOptType'] = self.change_opt_type
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_title is not None:
            result['ChangeTitle'] = self.change_title
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        if self.cur_batch_no is not None:
            result['CurBatchNo'] = self.cur_batch_no
        if self.executor_emp_id is not None:
            result['ExecutorEmpId'] = self.executor_emp_id
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.total_batch_no is not None:
            result['TotalBatchNo'] = self.total_batch_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeObject') is not None:
            self.change_object = m.get('ChangeObject')
        if m.get('ChangeOptType') is not None:
            self.change_opt_type = m.get('ChangeOptType')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeTitle') is not None:
            self.change_title = m.get('ChangeTitle')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        if m.get('CurBatchNo') is not None:
            self.cur_batch_no = m.get('CurBatchNo')
        if m.get('ExecutorEmpId') is not None:
            self.executor_emp_id = m.get('ExecutorEmpId')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('TotalBatchNo') is not None:
            self.total_batch_no = m.get('TotalBatchNo')
        return self


class ChangeStartResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeStartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeStartResponseBody = None,
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
            temp_model = ChangeStartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBlockRequestApproveStrategyNodes(TeaModel):
    def __init__(
        self,
        approve_rule_type: int = None,
        approve_type: int = None,
        id: int = None,
        name: str = None,
        node_code: str = None,
        priority_order: int = None,
        role_code: int = None,
        role_value: List[str] = None,
        template_id: int = None,
    ):
        self.approve_rule_type = approve_rule_type
        self.approve_type = approve_type
        self.id = id
        self.name = name
        self.node_code = node_code
        self.priority_order = priority_order
        self.role_code = role_code
        self.role_value = role_value
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_rule_type is not None:
            result['ApproveRuleType'] = self.approve_rule_type
        if self.approve_type is not None:
            result['ApproveType'] = self.approve_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.node_code is not None:
            result['NodeCode'] = self.node_code
        if self.priority_order is not None:
            result['PriorityOrder'] = self.priority_order
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        if self.role_value is not None:
            result['RoleValue'] = self.role_value
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveRuleType') is not None:
            self.approve_rule_type = m.get('ApproveRuleType')
        if m.get('ApproveType') is not None:
            self.approve_type = m.get('ApproveType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeCode') is not None:
            self.node_code = m.get('NodeCode')
        if m.get('PriorityOrder') is not None:
            self.priority_order = m.get('PriorityOrder')
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        if m.get('RoleValue') is not None:
            self.role_value = m.get('RoleValue')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateBlockRequestNoticeEnclosureInfos(TeaModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        self.name = name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CreateBlockRequestScopesBlockScopeApp(TeaModel):
    def __init__(
        self,
        app_name: List[str] = None,
        type: int = None,
    ):
        self.app_name = app_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateBlockRequestScopesBlockScopeBgSystem(TeaModel):
    def __init__(
        self,
        relate_codes: List[str] = None,
        self_code_name: str = None,
    ):
        self.relate_codes = relate_codes
        self.self_code_name = self_code_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relate_codes is not None:
            result['RelateCodes'] = self.relate_codes
        if self.self_code_name is not None:
            result['SelfCodeName'] = self.self_code_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelateCodes') is not None:
            self.relate_codes = m.get('RelateCodes')
        if m.get('SelfCodeName') is not None:
            self.self_code_name = m.get('SelfCodeName')
        return self


class CreateBlockRequestScopesBlockScopeClusterRelations(TeaModel):
    def __init__(
        self,
        app_codes: List[str] = None,
        label_codes: List[str] = None,
        relate_codes: List[str] = None,
        self_code: str = None,
    ):
        self.app_codes = app_codes
        self.label_codes = label_codes
        self.relate_codes = relate_codes
        self.self_code = self_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_codes is not None:
            result['AppCodes'] = self.app_codes
        if self.label_codes is not None:
            result['LabelCodes'] = self.label_codes
        if self.relate_codes is not None:
            result['RelateCodes'] = self.relate_codes
        if self.self_code is not None:
            result['SelfCode'] = self.self_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCodes') is not None:
            self.app_codes = m.get('AppCodes')
        if m.get('LabelCodes') is not None:
            self.label_codes = m.get('LabelCodes')
        if m.get('RelateCodes') is not None:
            self.relate_codes = m.get('RelateCodes')
        if m.get('SelfCode') is not None:
            self.self_code = m.get('SelfCode')
        return self


class CreateBlockRequestScopesBlockScopeCluster(TeaModel):
    def __init__(
        self,
        code_names: List[str] = None,
        relations: List[CreateBlockRequestScopesBlockScopeClusterRelations] = None,
    ):
        self.code_names = code_names
        self.relations = relations

    def validate(self):
        if self.relations:
            for k in self.relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_names is not None:
            result['CodeNames'] = self.code_names
        result['Relations'] = []
        if self.relations is not None:
            for k in self.relations:
                result['Relations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeNames') is not None:
            self.code_names = m.get('CodeNames')
        self.relations = []
        if m.get('Relations') is not None:
            for k in m.get('Relations'):
                temp_model = CreateBlockRequestScopesBlockScopeClusterRelations()
                self.relations.append(temp_model.from_map(k))
        return self


class CreateBlockRequestScopesBlockScopeCustomerRelations(TeaModel):
    def __init__(
        self,
        app_codes: List[str] = None,
        label_codes: List[str] = None,
        relate_codes: List[str] = None,
        self_code: str = None,
    ):
        self.app_codes = app_codes
        self.label_codes = label_codes
        self.relate_codes = relate_codes
        self.self_code = self_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_codes is not None:
            result['AppCodes'] = self.app_codes
        if self.label_codes is not None:
            result['LabelCodes'] = self.label_codes
        if self.relate_codes is not None:
            result['RelateCodes'] = self.relate_codes
        if self.self_code is not None:
            result['SelfCode'] = self.self_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCodes') is not None:
            self.app_codes = m.get('AppCodes')
        if m.get('LabelCodes') is not None:
            self.label_codes = m.get('LabelCodes')
        if m.get('RelateCodes') is not None:
            self.relate_codes = m.get('RelateCodes')
        if m.get('SelfCode') is not None:
            self.self_code = m.get('SelfCode')
        return self


class CreateBlockRequestScopesBlockScopeCustomer(TeaModel):
    def __init__(
        self,
        code_names: List[str] = None,
        relations: List[CreateBlockRequestScopesBlockScopeCustomerRelations] = None,
        uid: str = None,
        view_codes: List[int] = None,
    ):
        self.code_names = code_names
        self.relations = relations
        self.uid = uid
        self.view_codes = view_codes

    def validate(self):
        if self.relations:
            for k in self.relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_names is not None:
            result['CodeNames'] = self.code_names
        result['Relations'] = []
        if self.relations is not None:
            for k in self.relations:
                result['Relations'].append(k.to_map() if k else None)
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.view_codes is not None:
            result['ViewCodes'] = self.view_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeNames') is not None:
            self.code_names = m.get('CodeNames')
        self.relations = []
        if m.get('Relations') is not None:
            for k in m.get('Relations'):
                temp_model = CreateBlockRequestScopesBlockScopeCustomerRelations()
                self.relations.append(temp_model.from_map(k))
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('ViewCodes') is not None:
            self.view_codes = m.get('ViewCodes')
        return self


class CreateBlockRequestScopesBlockScopeProductRelations(TeaModel):
    def __init__(
        self,
        app_codes: List[str] = None,
        label_codes: List[str] = None,
        relate_codes: List[str] = None,
        self_code: str = None,
    ):
        self.app_codes = app_codes
        self.label_codes = label_codes
        self.relate_codes = relate_codes
        self.self_code = self_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_codes is not None:
            result['AppCodes'] = self.app_codes
        if self.label_codes is not None:
            result['LabelCodes'] = self.label_codes
        if self.relate_codes is not None:
            result['RelateCodes'] = self.relate_codes
        if self.self_code is not None:
            result['SelfCode'] = self.self_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCodes') is not None:
            self.app_codes = m.get('AppCodes')
        if m.get('LabelCodes') is not None:
            self.label_codes = m.get('LabelCodes')
        if m.get('RelateCodes') is not None:
            self.relate_codes = m.get('RelateCodes')
        if m.get('SelfCode') is not None:
            self.self_code = m.get('SelfCode')
        return self


class CreateBlockRequestScopesBlockScopeProduct(TeaModel):
    def __init__(
        self,
        code_names: List[str] = None,
        key: str = None,
        relations: List[CreateBlockRequestScopesBlockScopeProductRelations] = None,
        view_code: List[str] = None,
    ):
        self.code_names = code_names
        self.key = key
        self.relations = relations
        self.view_code = view_code

    def validate(self):
        if self.relations:
            for k in self.relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_names is not None:
            result['CodeNames'] = self.code_names
        if self.key is not None:
            result['Key'] = self.key
        result['Relations'] = []
        if self.relations is not None:
            for k in self.relations:
                result['Relations'].append(k.to_map() if k else None)
        if self.view_code is not None:
            result['ViewCode'] = self.view_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeNames') is not None:
            self.code_names = m.get('CodeNames')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.relations = []
        if m.get('Relations') is not None:
            for k in m.get('Relations'):
                temp_model = CreateBlockRequestScopesBlockScopeProductRelations()
                self.relations.append(temp_model.from_map(k))
        if m.get('ViewCode') is not None:
            self.view_code = m.get('ViewCode')
        return self


class CreateBlockRequestScopesBlockScope(TeaModel):
    def __init__(
        self,
        app: CreateBlockRequestScopesBlockScopeApp = None,
        bg_system: List[CreateBlockRequestScopesBlockScopeBgSystem] = None,
        cluster: CreateBlockRequestScopesBlockScopeCluster = None,
        customer: List[CreateBlockRequestScopesBlockScopeCustomer] = None,
        dept: List[str] = None,
        express: str = None,
        infrastructure: List[str] = None,
        product: List[CreateBlockRequestScopesBlockScopeProduct] = None,
    ):
        self.app = app
        self.bg_system = bg_system
        self.cluster = cluster
        self.customer = customer
        self.dept = dept
        self.express = express
        self.infrastructure = infrastructure
        self.product = product

    def validate(self):
        if self.app:
            self.app.validate()
        if self.bg_system:
            for k in self.bg_system:
                if k:
                    k.validate()
        if self.cluster:
            self.cluster.validate()
        if self.customer:
            for k in self.customer:
                if k:
                    k.validate()
        if self.product:
            for k in self.product:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        result['BgSystem'] = []
        if self.bg_system is not None:
            for k in self.bg_system:
                result['BgSystem'].append(k.to_map() if k else None)
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        result['Customer'] = []
        if self.customer is not None:
            for k in self.customer:
                result['Customer'].append(k.to_map() if k else None)
        if self.dept is not None:
            result['Dept'] = self.dept
        if self.express is not None:
            result['Express'] = self.express
        if self.infrastructure is not None:
            result['Infrastructure'] = self.infrastructure
        result['Product'] = []
        if self.product is not None:
            for k in self.product:
                result['Product'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = CreateBlockRequestScopesBlockScopeApp()
            self.app = temp_model.from_map(m['App'])
        self.bg_system = []
        if m.get('BgSystem') is not None:
            for k in m.get('BgSystem'):
                temp_model = CreateBlockRequestScopesBlockScopeBgSystem()
                self.bg_system.append(temp_model.from_map(k))
        if m.get('Cluster') is not None:
            temp_model = CreateBlockRequestScopesBlockScopeCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        self.customer = []
        if m.get('Customer') is not None:
            for k in m.get('Customer'):
                temp_model = CreateBlockRequestScopesBlockScopeCustomer()
                self.customer.append(temp_model.from_map(k))
        if m.get('Dept') is not None:
            self.dept = m.get('Dept')
        if m.get('Express') is not None:
            self.express = m.get('Express')
        if m.get('Infrastructure') is not None:
            self.infrastructure = m.get('Infrastructure')
        self.product = []
        if m.get('Product') is not None:
            for k in m.get('Product'):
                temp_model = CreateBlockRequestScopesBlockScopeProduct()
                self.product.append(temp_model.from_map(k))
        return self


class CreateBlockRequestScopes(TeaModel):
    def __init__(
        self,
        block_harm: List[int] = None,
        block_scope: CreateBlockRequestScopesBlockScope = None,
        effect_time: List[int] = None,
        scope_rule: str = None,
        change_object_regex: str = None,
        risk_levels: List[int] = None,
    ):
        self.block_harm = block_harm
        self.block_scope = block_scope
        self.effect_time = effect_time
        self.scope_rule = scope_rule
        self.change_object_regex = change_object_regex
        self.risk_levels = risk_levels

    def validate(self):
        if self.block_scope:
            self.block_scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_harm is not None:
            result['BlockHarm'] = self.block_harm
        if self.block_scope is not None:
            result['BlockScope'] = self.block_scope.to_map()
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.scope_rule is not None:
            result['ScopeRule'] = self.scope_rule
        if self.change_object_regex is not None:
            result['changeObjectRegex'] = self.change_object_regex
        if self.risk_levels is not None:
            result['riskLevels'] = self.risk_levels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHarm') is not None:
            self.block_harm = m.get('BlockHarm')
        if m.get('BlockScope') is not None:
            temp_model = CreateBlockRequestScopesBlockScope()
            self.block_scope = temp_model.from_map(m['BlockScope'])
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('ScopeRule') is not None:
            self.scope_rule = m.get('ScopeRule')
        if m.get('changeObjectRegex') is not None:
            self.change_object_regex = m.get('changeObjectRegex')
        if m.get('riskLevels') is not None:
            self.risk_levels = m.get('riskLevels')
        return self


class CreateBlockRequest(TeaModel):
    def __init__(
        self,
        approve_strategy_nodes: List[CreateBlockRequestApproveStrategyNodes] = None,
        block_id: int = None,
        director: str = None,
        is_need_approve: int = None,
        is_recall: int = None,
        is_template: int = None,
        label_name: str = None,
        notice_desc: str = None,
        notice_enclosure_infos: List[CreateBlockRequestNoticeEnclosureInfos] = None,
        notice_request_link: str = None,
        notice_type: int = None,
        reason: str = None,
        scene: int = None,
        scopes: List[CreateBlockRequestScopes] = None,
        status: int = None,
        title: str = None,
        type: str = None,
        version_id: int = None,
        creator_emp_id: str = None,
    ):
        self.approve_strategy_nodes = approve_strategy_nodes
        self.block_id = block_id
        self.director = director
        self.is_need_approve = is_need_approve
        self.is_recall = is_recall
        self.is_template = is_template
        self.label_name = label_name
        self.notice_desc = notice_desc
        self.notice_enclosure_infos = notice_enclosure_infos
        self.notice_request_link = notice_request_link
        self.notice_type = notice_type
        self.reason = reason
        self.scene = scene
        self.scopes = scopes
        self.status = status
        self.title = title
        self.type = type
        self.version_id = version_id
        self.creator_emp_id = creator_emp_id

    def validate(self):
        if self.approve_strategy_nodes:
            for k in self.approve_strategy_nodes:
                if k:
                    k.validate()
        if self.notice_enclosure_infos:
            for k in self.notice_enclosure_infos:
                if k:
                    k.validate()
        if self.scopes:
            for k in self.scopes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproveStrategyNodes'] = []
        if self.approve_strategy_nodes is not None:
            for k in self.approve_strategy_nodes:
                result['ApproveStrategyNodes'].append(k.to_map() if k else None)
        if self.block_id is not None:
            result['BlockId'] = self.block_id
        if self.director is not None:
            result['Director'] = self.director
        if self.is_need_approve is not None:
            result['IsNeedApprove'] = self.is_need_approve
        if self.is_recall is not None:
            result['IsRecall'] = self.is_recall
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.notice_desc is not None:
            result['NoticeDesc'] = self.notice_desc
        result['NoticeEnclosureInfos'] = []
        if self.notice_enclosure_infos is not None:
            for k in self.notice_enclosure_infos:
                result['NoticeEnclosureInfos'].append(k.to_map() if k else None)
        if self.notice_request_link is not None:
            result['NoticeRequestLink'] = self.notice_request_link
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.scene is not None:
            result['Scene'] = self.scene
        result['Scopes'] = []
        if self.scopes is not None:
            for k in self.scopes:
                result['Scopes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approve_strategy_nodes = []
        if m.get('ApproveStrategyNodes') is not None:
            for k in m.get('ApproveStrategyNodes'):
                temp_model = CreateBlockRequestApproveStrategyNodes()
                self.approve_strategy_nodes.append(temp_model.from_map(k))
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')
        if m.get('Director') is not None:
            self.director = m.get('Director')
        if m.get('IsNeedApprove') is not None:
            self.is_need_approve = m.get('IsNeedApprove')
        if m.get('IsRecall') is not None:
            self.is_recall = m.get('IsRecall')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('NoticeDesc') is not None:
            self.notice_desc = m.get('NoticeDesc')
        self.notice_enclosure_infos = []
        if m.get('NoticeEnclosureInfos') is not None:
            for k in m.get('NoticeEnclosureInfos'):
                temp_model = CreateBlockRequestNoticeEnclosureInfos()
                self.notice_enclosure_infos.append(temp_model.from_map(k))
        if m.get('NoticeRequestLink') is not None:
            self.notice_request_link = m.get('NoticeRequestLink')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        self.scopes = []
        if m.get('Scopes') is not None:
            for k in m.get('Scopes'):
                temp_model = CreateBlockRequestScopes()
                self.scopes.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        return self


class CreateBlockResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBlockResponseBody = None,
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
            temp_model = CreateBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMaYiBlockRequestBlockTimes(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
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
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateMaYiBlockRequestScopeGroupBlockScopeParams(TeaModel):
    def __init__(
        self,
        az: str = None,
        idc: str = None,
        region: str = None,
    ):
        self.az = az
        self.idc = idc
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az is not None:
            result['Az'] = self.az
        if self.idc is not None:
            result['Idc'] = self.idc
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Az') is not None:
            self.az = m.get('Az')
        if m.get('Idc') is not None:
            self.idc = m.get('Idc')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateMaYiBlockRequestScope(TeaModel):
    def __init__(
        self,
        group_block_scope_params: List[CreateMaYiBlockRequestScopeGroupBlockScopeParams] = None,
    ):
        self.group_block_scope_params = group_block_scope_params

    def validate(self):
        if self.group_block_scope_params:
            for k in self.group_block_scope_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupBlockScopeParams'] = []
        if self.group_block_scope_params is not None:
            for k in self.group_block_scope_params:
                result['GroupBlockScopeParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_block_scope_params = []
        if m.get('GroupBlockScopeParams') is not None:
            for k in m.get('GroupBlockScopeParams'):
                temp_model = CreateMaYiBlockRequestScopeGroupBlockScopeParams()
                self.group_block_scope_params.append(temp_model.from_map(k))
        return self


class CreateMaYiBlockRequest(TeaModel):
    def __init__(
        self,
        block_id: str = None,
        block_times: List[CreateMaYiBlockRequestBlockTimes] = None,
        block_type: str = None,
        creator_emp_id: str = None,
        director: List[str] = None,
        fault_version: str = None,
        information: List[str] = None,
        reason: str = None,
        scope: CreateMaYiBlockRequestScope = None,
        title: str = None,
        type: str = None,
    ):
        self.block_id = block_id
        # This parameter is required.
        self.block_times = block_times
        # This parameter is required.
        self.block_type = block_type
        # This parameter is required.
        self.creator_emp_id = creator_emp_id
        # This parameter is required.
        self.director = director
        self.fault_version = fault_version
        self.information = information
        # This parameter is required.
        self.reason = reason
        self.scope = scope
        # This parameter is required.
        self.title = title
        self.type = type

    def validate(self):
        if self.block_times:
            for k in self.block_times:
                if k:
                    k.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_id is not None:
            result['BlockId'] = self.block_id
        result['BlockTimes'] = []
        if self.block_times is not None:
            for k in self.block_times:
                result['BlockTimes'].append(k.to_map() if k else None)
        if self.block_type is not None:
            result['BlockType'] = self.block_type
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        if self.director is not None:
            result['Director'] = self.director
        if self.fault_version is not None:
            result['FaultVersion'] = self.fault_version
        if self.information is not None:
            result['Information'] = self.information
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.scope is not None:
            result['Scope'] = self.scope.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')
        self.block_times = []
        if m.get('BlockTimes') is not None:
            for k in m.get('BlockTimes'):
                temp_model = CreateMaYiBlockRequestBlockTimes()
                self.block_times.append(temp_model.from_map(k))
        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        if m.get('Director') is not None:
            self.director = m.get('Director')
        if m.get('FaultVersion') is not None:
            self.fault_version = m.get('FaultVersion')
        if m.get('Information') is not None:
            self.information = m.get('Information')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Scope') is not None:
            temp_model = CreateMaYiBlockRequestScope()
            self.scope = temp_model.from_map(m['Scope'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateMaYiBlockShrinkRequestBlockTimes(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
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
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateMaYiBlockShrinkRequest(TeaModel):
    def __init__(
        self,
        block_id: str = None,
        block_times: List[CreateMaYiBlockShrinkRequestBlockTimes] = None,
        block_type: str = None,
        creator_emp_id: str = None,
        director: List[str] = None,
        fault_version: str = None,
        information: List[str] = None,
        reason: str = None,
        scope_shrink: str = None,
        title: str = None,
        type: str = None,
    ):
        self.block_id = block_id
        # This parameter is required.
        self.block_times = block_times
        # This parameter is required.
        self.block_type = block_type
        # This parameter is required.
        self.creator_emp_id = creator_emp_id
        # This parameter is required.
        self.director = director
        self.fault_version = fault_version
        self.information = information
        # This parameter is required.
        self.reason = reason
        self.scope_shrink = scope_shrink
        # This parameter is required.
        self.title = title
        self.type = type

    def validate(self):
        if self.block_times:
            for k in self.block_times:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_id is not None:
            result['BlockId'] = self.block_id
        result['BlockTimes'] = []
        if self.block_times is not None:
            for k in self.block_times:
                result['BlockTimes'].append(k.to_map() if k else None)
        if self.block_type is not None:
            result['BlockType'] = self.block_type
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        if self.director is not None:
            result['Director'] = self.director
        if self.fault_version is not None:
            result['FaultVersion'] = self.fault_version
        if self.information is not None:
            result['Information'] = self.information
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.scope_shrink is not None:
            result['Scope'] = self.scope_shrink
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')
        self.block_times = []
        if m.get('BlockTimes') is not None:
            for k in m.get('BlockTimes'):
                temp_model = CreateMaYiBlockShrinkRequestBlockTimes()
                self.block_times.append(temp_model.from_map(k))
        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        if m.get('Director') is not None:
            self.director = m.get('Director')
        if m.get('FaultVersion') is not None:
            self.fault_version = m.get('FaultVersion')
        if m.get('Information') is not None:
            self.information = m.get('Information')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Scope') is not None:
            self.scope_shrink = m.get('Scope')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateMaYiBlockResponseBodyData(TeaModel):
    def __init__(
        self,
        block_id: int = None,
        block_url: str = None,
    ):
        self.block_id = block_id
        self.block_url = block_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_id is not None:
            result['BlockId'] = self.block_id
        if self.block_url is not None:
            result['BlockUrl'] = self.block_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')
        if m.get('BlockUrl') is not None:
            self.block_url = m.get('BlockUrl')
        return self


class CreateMaYiBlockResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateMaYiBlockResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateMaYiBlockResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMaYiBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMaYiBlockResponseBody = None,
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
            temp_model = CreateMaYiBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOperatorRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        bg_object: str = None,
        bg_system: str = None,
        code: str = None,
        cur_emp_id: str = None,
        name: str = None,
        no_check: bool = None,
        no_risk: bool = None,
        req_timestamp: int = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.bg_object = bg_object
        self.bg_system = bg_system
        self.code = code
        self.cur_emp_id = cur_emp_id
        self.name = name
        self.no_check = no_check
        self.no_risk = no_risk
        self.req_timestamp = req_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.bg_object is not None:
            result['BgObject'] = self.bg_object
        if self.bg_system is not None:
            result['BgSystem'] = self.bg_system
        if self.code is not None:
            result['Code'] = self.code
        if self.cur_emp_id is not None:
            result['CurEmpId'] = self.cur_emp_id
        if self.name is not None:
            result['Name'] = self.name
        if self.no_check is not None:
            result['NoCheck'] = self.no_check
        if self.no_risk is not None:
            result['NoRisk'] = self.no_risk
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('BgObject') is not None:
            self.bg_object = m.get('BgObject')
        if m.get('BgSystem') is not None:
            self.bg_system = m.get('BgSystem')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurEmpId') is not None:
            self.cur_emp_id = m.get('CurEmpId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NoCheck') is not None:
            self.no_check = m.get('NoCheck')
        if m.get('NoRisk') is not None:
            self.no_risk = m.get('NoRisk')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        return self


class CreateOperatorResponseBodyData(TeaModel):
    def __init__(
        self,
        approve_strategy_id: int = None,
        rule_id: int = None,
    ):
        self.approve_strategy_id = approve_strategy_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_strategy_id is not None:
            result['ApproveStrategyId'] = self.approve_strategy_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveStrategyId') is not None:
            self.approve_strategy_id = m.get('ApproveStrategyId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateOperatorResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateOperatorResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateOperatorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateOperatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOperatorResponseBody = None,
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
            temp_model = CreateOperatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        need_validate: bool = None,
        query_type: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.need_validate = need_validate
        self.query_type = query_type
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.need_validate is not None:
            result['NeedValidate'] = self.need_validate
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('NeedValidate') is not None:
            self.need_validate = m.get('NeedValidate')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class QueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryResponseBody = None,
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
            temp_model = QueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryApproveFlowRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
        stage: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id
        self.stage = stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.stage is not None:
            result['Stage'] = self.stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        return self


class QueryApproveFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryApproveFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryApproveFlowResponseBody = None,
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
            temp_model = QueryApproveFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBlockEventRequestRegionReqs(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        regions: List[str] = None,
    ):
        self.product_code = product_code
        self.regions = regions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.regions is not None:
            result['Regions'] = self.regions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        return self


class QueryBlockEventRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        bg_system_name: str = None,
        block_harm: str = None,
        category: str = None,
        dept_no: str = None,
        end_time: int = None,
        limit: int = None,
        need_rule: bool = None,
        page: int = None,
        product_codes: List[str] = None,
        region_reqs: List[QueryBlockEventRequestRegionReqs] = None,
        req_timestamp: int = None,
        scope: List[str] = None,
        start_time: int = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.bg_system_name = bg_system_name
        self.block_harm = block_harm
        self.category = category
        self.dept_no = dept_no
        self.end_time = end_time
        self.limit = limit
        self.need_rule = need_rule
        self.page = page
        self.product_codes = product_codes
        self.region_reqs = region_reqs
        self.req_timestamp = req_timestamp
        self.scope = scope
        self.start_time = start_time

    def validate(self):
        if self.region_reqs:
            for k in self.region_reqs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.bg_system_name is not None:
            result['BgSystemName'] = self.bg_system_name
        if self.block_harm is not None:
            result['BlockHarm'] = self.block_harm
        if self.category is not None:
            result['Category'] = self.category
        if self.dept_no is not None:
            result['DeptNo'] = self.dept_no
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.need_rule is not None:
            result['NeedRule'] = self.need_rule
        if self.page is not None:
            result['Page'] = self.page
        if self.product_codes is not None:
            result['ProductCodes'] = self.product_codes
        result['RegionReqs'] = []
        if self.region_reqs is not None:
            for k in self.region_reqs:
                result['RegionReqs'].append(k.to_map() if k else None)
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('BgSystemName') is not None:
            self.bg_system_name = m.get('BgSystemName')
        if m.get('BlockHarm') is not None:
            self.block_harm = m.get('BlockHarm')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeptNo') is not None:
            self.dept_no = m.get('DeptNo')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NeedRule') is not None:
            self.need_rule = m.get('NeedRule')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('ProductCodes') is not None:
            self.product_codes = m.get('ProductCodes')
        self.region_reqs = []
        if m.get('RegionReqs') is not None:
            for k in m.get('RegionReqs'):
                temp_model = QueryBlockEventRequestRegionReqs()
                self.region_reqs.append(temp_model.from_map(k))
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryBlockEventResponseBodyDataDataInfoEventTimesRule(TeaModel):
    def __init__(
        self,
        level_1: str = None,
        level_2: str = None,
        level_3: str = None,
        level_4: str = None,
        level_5: str = None,
        type: str = None,
    ):
        self.level_1 = level_1
        self.level_2 = level_2
        self.level_3 = level_3
        self.level_4 = level_4
        self.level_5 = level_5
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level_1 is not None:
            result['Level1'] = self.level_1
        if self.level_2 is not None:
            result['Level2'] = self.level_2
        if self.level_3 is not None:
            result['Level3'] = self.level_3
        if self.level_4 is not None:
            result['Level4'] = self.level_4
        if self.level_5 is not None:
            result['Level5'] = self.level_5
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level1') is not None:
            self.level_1 = m.get('Level1')
        if m.get('Level2') is not None:
            self.level_2 = m.get('Level2')
        if m.get('Level3') is not None:
            self.level_3 = m.get('Level3')
        if m.get('Level4') is not None:
            self.level_4 = m.get('Level4')
        if m.get('Level5') is not None:
            self.level_5 = m.get('Level5')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryBlockEventResponseBodyDataDataInfoEventTimes(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        express: str = None,
        rule: List[QueryBlockEventResponseBodyDataDataInfoEventTimesRule] = None,
        start_time: int = None,
        rule_id: int = None,
    ):
        self.end_time = end_time
        self.express = express
        self.rule = rule
        self.start_time = start_time
        self.rule_id = rule_id

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.express is not None:
            result['Express'] = self.express
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Express') is not None:
            self.express = m.get('Express')
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = QueryBlockEventResponseBodyDataDataInfoEventTimesRule()
                self.rule.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class QueryBlockEventResponseBodyDataDataInfoLevelType(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: int = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryBlockEventResponseBodyDataDataInfo(TeaModel):
    def __init__(
        self,
        emp_id: str = None,
        end_time: int = None,
        event_times: List[QueryBlockEventResponseBodyDataDataInfoEventTimes] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        reason: str = None,
        start_time: int = None,
        title: str = None,
        url: str = None,
        level_type: QueryBlockEventResponseBodyDataDataInfoLevelType = None,
        version_id: int = None,
    ):
        self.emp_id = emp_id
        self.end_time = end_time
        self.event_times = event_times
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.reason = reason
        self.start_time = start_time
        self.title = title
        self.url = url
        self.level_type = level_type
        self.version_id = version_id

    def validate(self):
        if self.event_times:
            for k in self.event_times:
                if k:
                    k.validate()
        if self.level_type:
            self.level_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emp_id is not None:
            result['EmpId'] = self.emp_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['EventTimes'] = []
        if self.event_times is not None:
            for k in self.event_times:
                result['EventTimes'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.level_type is not None:
            result['levelType'] = self.level_type.to_map()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmpId') is not None:
            self.emp_id = m.get('EmpId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.event_times = []
        if m.get('EventTimes') is not None:
            for k in m.get('EventTimes'):
                temp_model = QueryBlockEventResponseBodyDataDataInfoEventTimes()
                self.event_times.append(temp_model.from_map(k))
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('levelType') is not None:
            temp_model = QueryBlockEventResponseBodyDataDataInfoLevelType()
            self.level_type = temp_model.from_map(m['levelType'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class QueryBlockEventResponseBodyDataPagination(TeaModel):
    def __init__(
        self,
        limit: int = None,
        page: int = None,
    ):
        self.limit = limit
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryBlockEventResponseBodyData(TeaModel):
    def __init__(
        self,
        data_info: List[QueryBlockEventResponseBodyDataDataInfo] = None,
        extra_info: Dict[str, str] = None,
        pagination: QueryBlockEventResponseBodyDataPagination = None,
        total: int = None,
    ):
        self.data_info = data_info
        self.extra_info = extra_info
        self.pagination = pagination
        self.total = total

    def validate(self):
        if self.data_info:
            for k in self.data_info:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataInfo'] = []
        if self.data_info is not None:
            for k in self.data_info:
                result['DataInfo'].append(k.to_map() if k else None)
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_info = []
        if m.get('DataInfo') is not None:
            for k in m.get('DataInfo'):
                temp_model = QueryBlockEventResponseBodyDataDataInfo()
                self.data_info.append(temp_model.from_map(k))
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Pagination') is not None:
            temp_model = QueryBlockEventResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryBlockEventResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryBlockEventResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryBlockEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBlockEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBlockEventResponseBody = None,
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
            temp_model = QueryBlockEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChangeInfoRequestLevelTreeTreeData(TeaModel):
    def __init__(
        self,
        data: List[Any] = None,
        data_sub_type: str = None,
        value: List[str] = None,
    ):
        self.data = data
        self.data_sub_type = data_sub_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.data_sub_type is not None:
            result['DataSubType'] = self.data_sub_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataSubType') is not None:
            self.data_sub_type = m.get('DataSubType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryChangeInfoRequestLevelTree(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        tree_data: List[QueryChangeInfoRequestLevelTreeTreeData] = None,
    ):
        self.data_type = data_type
        self.tree_data = tree_data

    def validate(self):
        if self.tree_data:
            for k in self.tree_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        result['TreeData'] = []
        if self.tree_data is not None:
            for k in self.tree_data:
                result['TreeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        self.tree_data = []
        if m.get('TreeData') is not None:
            for k in m.get('TreeData'):
                temp_model = QueryChangeInfoRequestLevelTreeTreeData()
                self.tree_data.append(temp_model.from_map(k))
        return self


class QueryChangeInfoRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        az: List[str] = None,
        bg_vid: str = None,
        bu_id: str = None,
        change_system: str = None,
        end_time: int = None,
        keyword: str = None,
        level_tree: QueryChangeInfoRequestLevelTree = None,
        limit: int = None,
        page: int = None,
        product: List[str] = None,
        region: List[str] = None,
        req_timestamp: int = None,
        source: str = None,
        source_order_id: str = None,
        start_time: int = None,
        type: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.az = az
        self.bg_vid = bg_vid
        self.bu_id = bu_id
        self.change_system = change_system
        self.end_time = end_time
        self.keyword = keyword
        self.level_tree = level_tree
        self.limit = limit
        self.page = page
        self.product = product
        self.region = region
        self.req_timestamp = req_timestamp
        self.source = source
        self.source_order_id = source_order_id
        self.start_time = start_time
        self.type = type

    def validate(self):
        if self.level_tree:
            self.level_tree.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.az is not None:
            result['Az'] = self.az
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.change_system is not None:
            result['ChangeSystem'] = self.change_system
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.level_tree is not None:
            result['LevelTree'] = self.level_tree.to_map()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.page is not None:
            result['Page'] = self.page
        if self.product is not None:
            result['Product'] = self.product
        if self.region is not None:
            result['Region'] = self.region
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source is not None:
            result['Source'] = self.source
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('Az') is not None:
            self.az = m.get('Az')
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('ChangeSystem') is not None:
            self.change_system = m.get('ChangeSystem')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('LevelTree') is not None:
            temp_model = QueryChangeInfoRequestLevelTree()
            self.level_tree = temp_model.from_map(m['LevelTree'])
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryChangeInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryChangeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryChangeInfoResponseBody = None,
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
            temp_model = QueryChangeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCheckInfoRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class QueryCheckInfoResponseBodyDataCheckDetailListBlockRuleScopeNodeList(TeaModel):
    def __init__(
        self,
        leaf_level: str = None,
        level_1: str = None,
        level_2: str = None,
        level_3: str = None,
        level_4: str = None,
        level_5: str = None,
        path: str = None,
        rule_id: int = None,
        type: str = None,
    ):
        self.leaf_level = leaf_level
        self.level_1 = level_1
        self.level_2 = level_2
        self.level_3 = level_3
        self.level_4 = level_4
        self.level_5 = level_5
        self.path = path
        self.rule_id = rule_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.leaf_level is not None:
            result['LeafLevel'] = self.leaf_level
        if self.level_1 is not None:
            result['Level1'] = self.level_1
        if self.level_2 is not None:
            result['Level2'] = self.level_2
        if self.level_3 is not None:
            result['Level3'] = self.level_3
        if self.level_4 is not None:
            result['Level4'] = self.level_4
        if self.level_5 is not None:
            result['Level5'] = self.level_5
        if self.path is not None:
            result['Path'] = self.path
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LeafLevel') is not None:
            self.leaf_level = m.get('LeafLevel')
        if m.get('Level1') is not None:
            self.level_1 = m.get('Level1')
        if m.get('Level2') is not None:
            self.level_2 = m.get('Level2')
        if m.get('Level3') is not None:
            self.level_3 = m.get('Level3')
        if m.get('Level4') is not None:
            self.level_4 = m.get('Level4')
        if m.get('Level5') is not None:
            self.level_5 = m.get('Level5')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryCheckInfoResponseBodyDataCheckDetailListBlockRule(TeaModel):
    def __init__(
        self,
        block_harm: str = None,
        block_id: int = None,
        express: str = None,
        scope_end_time: int = None,
        scope_node_list: List[QueryCheckInfoResponseBodyDataCheckDetailListBlockRuleScopeNodeList] = None,
        scope_rule_id: int = None,
        scope_start_time: int = None,
    ):
        self.block_harm = block_harm
        self.block_id = block_id
        self.express = express
        self.scope_end_time = scope_end_time
        self.scope_node_list = scope_node_list
        self.scope_rule_id = scope_rule_id
        self.scope_start_time = scope_start_time

    def validate(self):
        if self.scope_node_list:
            for k in self.scope_node_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_harm is not None:
            result['BlockHarm'] = self.block_harm
        if self.block_id is not None:
            result['BlockId'] = self.block_id
        if self.express is not None:
            result['Express'] = self.express
        if self.scope_end_time is not None:
            result['ScopeEndTime'] = self.scope_end_time
        result['ScopeNodeList'] = []
        if self.scope_node_list is not None:
            for k in self.scope_node_list:
                result['ScopeNodeList'].append(k.to_map() if k else None)
        if self.scope_rule_id is not None:
            result['ScopeRuleId'] = self.scope_rule_id
        if self.scope_start_time is not None:
            result['ScopeStartTime'] = self.scope_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHarm') is not None:
            self.block_harm = m.get('BlockHarm')
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')
        if m.get('Express') is not None:
            self.express = m.get('Express')
        if m.get('ScopeEndTime') is not None:
            self.scope_end_time = m.get('ScopeEndTime')
        self.scope_node_list = []
        if m.get('ScopeNodeList') is not None:
            for k in m.get('ScopeNodeList'):
                temp_model = QueryCheckInfoResponseBodyDataCheckDetailListBlockRuleScopeNodeList()
                self.scope_node_list.append(temp_model.from_map(k))
        if m.get('ScopeRuleId') is not None:
            self.scope_rule_id = m.get('ScopeRuleId')
        if m.get('ScopeStartTime') is not None:
            self.scope_start_time = m.get('ScopeStartTime')
        return self


class QueryCheckInfoResponseBodyDataCheckDetailList(TeaModel):
    def __init__(
        self,
        block_rule: List[QueryCheckInfoResponseBodyDataCheckDetailListBlockRule] = None,
        checkhold_reason: str = None,
        desc: str = None,
        pic_info: str = None,
        risk_explain: str = None,
        title: str = None,
        url: str = None,
    ):
        self.block_rule = block_rule
        self.checkhold_reason = checkhold_reason
        self.desc = desc
        self.pic_info = pic_info
        self.risk_explain = risk_explain
        self.title = title
        self.url = url

    def validate(self):
        if self.block_rule:
            for k in self.block_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockRule'] = []
        if self.block_rule is not None:
            for k in self.block_rule:
                result['BlockRule'].append(k.to_map() if k else None)
        if self.checkhold_reason is not None:
            result['CheckholdReason'] = self.checkhold_reason
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info
        if self.risk_explain is not None:
            result['RiskExplain'] = self.risk_explain
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_rule = []
        if m.get('BlockRule') is not None:
            for k in m.get('BlockRule'):
                temp_model = QueryCheckInfoResponseBodyDataCheckDetailListBlockRule()
                self.block_rule.append(temp_model.from_map(k))
        if m.get('CheckholdReason') is not None:
            self.checkhold_reason = m.get('CheckholdReason')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('PicInfo') is not None:
            self.pic_info = m.get('PicInfo')
        if m.get('RiskExplain') is not None:
            self.risk_explain = m.get('RiskExplain')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryCheckInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        check_detail_list: List[QueryCheckInfoResponseBodyDataCheckDetailList] = None,
        check_result_url: str = None,
    ):
        self.check_detail_list = check_detail_list
        self.check_result_url = check_result_url

    def validate(self):
        if self.check_detail_list:
            for k in self.check_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckDetailList'] = []
        if self.check_detail_list is not None:
            for k in self.check_detail_list:
                result['CheckDetailList'].append(k.to_map() if k else None)
        if self.check_result_url is not None:
            result['CheckResultUrl'] = self.check_result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_detail_list = []
        if m.get('CheckDetailList') is not None:
            for k in m.get('CheckDetailList'):
                temp_model = QueryCheckInfoResponseBodyDataCheckDetailList()
                self.check_detail_list.append(temp_model.from_map(k))
        if m.get('CheckResultUrl') is not None:
            self.check_result_url = m.get('CheckResultUrl')
        return self


class QueryCheckInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryCheckInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryCheckInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCheckInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCheckInfoResponseBody = None,
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
            temp_model = QueryCheckInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustomerRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        product: List[str] = None,
        req_timestamp: int = None,
        type: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.product = product
        self.req_timestamp = req_timestamp
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.product is not None:
            result['Product'] = self.product
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryCustomerResponseBodyData(TeaModel):
    def __init__(
        self,
        product: str = None,
        type: str = None,
        uid: str = None,
    ):
        self.product = product
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryCustomerResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[QueryCustomerResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryCustomerResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCustomerResponseBody = None,
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
            temp_model = QueryCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExecuteInfoRequestLevelTreeTreeData(TeaModel):
    def __init__(
        self,
        data: List[Any] = None,
        data_sub_type: str = None,
        value: List[str] = None,
    ):
        self.data = data
        self.data_sub_type = data_sub_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.data_sub_type is not None:
            result['DataSubType'] = self.data_sub_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataSubType') is not None:
            self.data_sub_type = m.get('DataSubType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryExecuteInfoRequestLevelTree(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        tree_data: List[QueryExecuteInfoRequestLevelTreeTreeData] = None,
    ):
        self.data_type = data_type
        self.tree_data = tree_data

    def validate(self):
        if self.tree_data:
            for k in self.tree_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        result['TreeData'] = []
        if self.tree_data is not None:
            for k in self.tree_data:
                result['TreeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        self.tree_data = []
        if m.get('TreeData') is not None:
            for k in m.get('TreeData'):
                temp_model = QueryExecuteInfoRequestLevelTreeTreeData()
                self.tree_data.append(temp_model.from_map(k))
        return self


class QueryExecuteInfoRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        az: List[str] = None,
        bg_vid: str = None,
        bu_id: str = None,
        end_time: int = None,
        ex_vid: str = None,
        keyword: str = None,
        level_tree: QueryExecuteInfoRequestLevelTree = None,
        limit: int = None,
        page: int = None,
        product: List[str] = None,
        region: List[str] = None,
        req_timestamp: int = None,
        source: str = None,
        source_order_id: str = None,
        start_time: int = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.az = az
        self.bg_vid = bg_vid
        self.bu_id = bu_id
        self.end_time = end_time
        self.ex_vid = ex_vid
        self.keyword = keyword
        self.level_tree = level_tree
        self.limit = limit
        self.page = page
        self.product = product
        self.region = region
        self.req_timestamp = req_timestamp
        self.source = source
        self.source_order_id = source_order_id
        self.start_time = start_time

    def validate(self):
        if self.level_tree:
            self.level_tree.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.az is not None:
            result['Az'] = self.az
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ex_vid is not None:
            result['ExVid'] = self.ex_vid
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.level_tree is not None:
            result['LevelTree'] = self.level_tree.to_map()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.page is not None:
            result['Page'] = self.page
        if self.product is not None:
            result['Product'] = self.product
        if self.region is not None:
            result['Region'] = self.region
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source is not None:
            result['Source'] = self.source
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('Az') is not None:
            self.az = m.get('Az')
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExVid') is not None:
            self.ex_vid = m.get('ExVid')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('LevelTree') is not None:
            temp_model = QueryExecuteInfoRequestLevelTree()
            self.level_tree = temp_model.from_map(m['LevelTree'])
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryExecuteInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryExecuteInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryExecuteInfoResponseBody = None,
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
            temp_model = QueryExecuteInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInnerProductInfoRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        limit: int = None,
        page: int = None,
        product_code: str = None,
        req_timestamp: int = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.limit = limit
        self.page = page
        self.product_code = product_code
        self.req_timestamp = req_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.page is not None:
            result['Page'] = self.page
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        return self


class QueryInnerProductInfoResponseBodyDataDataInfo(TeaModel):
    def __init__(
        self,
        inner_product_code: str = None,
        inner_product_name: str = None,
        product_code: str = None,
        product_name: str = None,
    ):
        self.inner_product_code = inner_product_code
        self.inner_product_name = inner_product_name
        self.product_code = product_code
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inner_product_code is not None:
            result['InnerProductCode'] = self.inner_product_code
        if self.inner_product_name is not None:
            result['InnerProductName'] = self.inner_product_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InnerProductCode') is not None:
            self.inner_product_code = m.get('InnerProductCode')
        if m.get('InnerProductName') is not None:
            self.inner_product_name = m.get('InnerProductName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class QueryInnerProductInfoResponseBodyDataPagination(TeaModel):
    def __init__(
        self,
        limit: int = None,
        page: int = None,
    ):
        self.limit = limit
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryInnerProductInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        data_info: List[QueryInnerProductInfoResponseBodyDataDataInfo] = None,
        pagination: QueryInnerProductInfoResponseBodyDataPagination = None,
        total: int = None,
    ):
        self.data_info = data_info
        self.pagination = pagination
        self.total = total

    def validate(self):
        if self.data_info:
            for k in self.data_info:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataInfo'] = []
        if self.data_info is not None:
            for k in self.data_info:
                result['DataInfo'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_info = []
        if m.get('DataInfo') is not None:
            for k in m.get('DataInfo'):
                temp_model = QueryInnerProductInfoResponseBodyDataDataInfo()
                self.data_info.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = QueryInnerProductInfoResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryInnerProductInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryInnerProductInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryInnerProductInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryInnerProductInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryInnerProductInfoResponseBody = None,
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
            temp_model = QueryInnerProductInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRegionAzRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        limit: int = None,
        page: int = None,
        product: str = None,
        req_timestamp: int = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.limit = limit
        self.page = page
        self.product = product
        self.req_timestamp = req_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.page is not None:
            result['Page'] = self.page
        if self.product is not None:
            result['Product'] = self.product
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        return self


class QueryRegionAzResponseBodyDataDataInfo(TeaModel):
    def __init__(
        self,
        az_list: List[str] = None,
        region_code: str = None,
        region_name: str = None,
    ):
        self.az_list = az_list
        self.region_code = region_code
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az_list is not None:
            result['AzList'] = self.az_list
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzList') is not None:
            self.az_list = m.get('AzList')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class QueryRegionAzResponseBodyDataPagination(TeaModel):
    def __init__(
        self,
        limit: int = None,
        page: int = None,
    ):
        self.limit = limit
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryRegionAzResponseBodyData(TeaModel):
    def __init__(
        self,
        data_info: List[QueryRegionAzResponseBodyDataDataInfo] = None,
        pagination: QueryRegionAzResponseBodyDataPagination = None,
        total: int = None,
    ):
        self.data_info = data_info
        self.pagination = pagination
        self.total = total

    def validate(self):
        if self.data_info:
            for k in self.data_info:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataInfo'] = []
        if self.data_info is not None:
            for k in self.data_info:
                result['DataInfo'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_info = []
        if m.get('DataInfo') is not None:
            for k in m.get('DataInfo'):
                temp_model = QueryRegionAzResponseBodyDataDataInfo()
                self.data_info.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = QueryRegionAzResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryRegionAzResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryRegionAzResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryRegionAzResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRegionAzResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRegionAzResponseBody = None,
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
            temp_model = QueryRegionAzResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SafeChangeCancelRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        bg_vid: str = None,
        operate_emp_no: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.bg_vid = bg_vid
        self.operate_emp_no = operate_emp_no
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        if self.operate_emp_no is not None:
            result['OperateEmpNo'] = self.operate_emp_no
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        if m.get('OperateEmpNo') is not None:
            self.operate_emp_no = m.get('OperateEmpNo')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class SafeChangeCancelResponseBodyData(TeaModel):
    def __init__(
        self,
        source_order_id: str = None,
    ):
        self.source_order_id = source_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class SafeChangeCancelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SafeChangeCancelResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SafeChangeCancelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SafeChangeCancelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SafeChangeCancelResponseBody = None,
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
            temp_model = SafeChangeCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SafeChangeCheckRequestApproveFlowParamApproveNodesApproverDTO(TeaModel):
    def __init__(
        self,
        approve_desc: str = None,
        approve_time: int = None,
        approver_id: str = None,
        approver_name: str = None,
        opinion: int = None,
    ):
        self.approve_desc = approve_desc
        self.approve_time = approve_time
        self.approver_id = approver_id
        self.approver_name = approver_name
        self.opinion = opinion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_desc is not None:
            result['ApproveDesc'] = self.approve_desc
        if self.approve_time is not None:
            result['ApproveTime'] = self.approve_time
        if self.approver_id is not None:
            result['ApproverId'] = self.approver_id
        if self.approver_name is not None:
            result['ApproverName'] = self.approver_name
        if self.opinion is not None:
            result['Opinion'] = self.opinion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveDesc') is not None:
            self.approve_desc = m.get('ApproveDesc')
        if m.get('ApproveTime') is not None:
            self.approve_time = m.get('ApproveTime')
        if m.get('ApproverId') is not None:
            self.approver_id = m.get('ApproverId')
        if m.get('ApproverName') is not None:
            self.approver_name = m.get('ApproverName')
        if m.get('Opinion') is not None:
            self.opinion = m.get('Opinion')
        return self


class SafeChangeCheckRequestApproveFlowParamApproveNodes(TeaModel):
    def __init__(
        self,
        approver_dto: List[SafeChangeCheckRequestApproveFlowParamApproveNodesApproverDTO] = None,
        node_status: int = None,
        process_name: str = None,
        process_node_order: int = None,
        strategy: int = None,
    ):
        self.approver_dto = approver_dto
        self.node_status = node_status
        self.process_name = process_name
        self.process_node_order = process_node_order
        self.strategy = strategy

    def validate(self):
        if self.approver_dto:
            for k in self.approver_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproverDTO'] = []
        if self.approver_dto is not None:
            for k in self.approver_dto:
                result['ApproverDTO'].append(k.to_map() if k else None)
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.process_name is not None:
            result['ProcessName'] = self.process_name
        if self.process_node_order is not None:
            result['ProcessNodeOrder'] = self.process_node_order
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approver_dto = []
        if m.get('ApproverDTO') is not None:
            for k in m.get('ApproverDTO'):
                temp_model = SafeChangeCheckRequestApproveFlowParamApproveNodesApproverDTO()
                self.approver_dto.append(temp_model.from_map(k))
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')
        if m.get('ProcessNodeOrder') is not None:
            self.process_node_order = m.get('ProcessNodeOrder')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        return self


class SafeChangeCheckRequestApproveFlowParam(TeaModel):
    def __init__(
        self,
        approve_nodes: List[SafeChangeCheckRequestApproveFlowParamApproveNodes] = None,
        flow_status: int = None,
    ):
        self.approve_nodes = approve_nodes
        self.flow_status = flow_status

    def validate(self):
        if self.approve_nodes:
            for k in self.approve_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproveNodes'] = []
        if self.approve_nodes is not None:
            for k in self.approve_nodes:
                result['ApproveNodes'].append(k.to_map() if k else None)
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approve_nodes = []
        if m.get('ApproveNodes') is not None:
            for k in m.get('ApproveNodes'):
                temp_model = SafeChangeCheckRequestApproveFlowParamApproveNodes()
                self.approve_nodes.append(temp_model.from_map(k))
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        return self


class SafeChangeCheckRequestBgCustomTemplateExtraDTO(TeaModel):
    def __init__(
        self,
        bg_custom_template_info: str = None,
    ):
        self.bg_custom_template_info = bg_custom_template_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_custom_template_info is not None:
            result['BgCustomTemplateInfo'] = self.bg_custom_template_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgCustomTemplateInfo') is not None:
            self.bg_custom_template_info = m.get('BgCustomTemplateInfo')
        return self


class SafeChangeCheckRequestBlockInfosHitInfos(TeaModel):
    def __init__(
        self,
        hit_info: str = None,
        hit_object: str = None,
        scope: str = None,
    ):
        self.hit_info = hit_info
        self.hit_object = hit_object
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_info is not None:
            result['HitInfo'] = self.hit_info
        if self.hit_object is not None:
            result['HitObject'] = self.hit_object
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitInfo') is not None:
            self.hit_info = m.get('HitInfo')
        if m.get('HitObject') is not None:
            self.hit_object = m.get('HitObject')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class SafeChangeCheckRequestBlockInfos(TeaModel):
    def __init__(
        self,
        hit_infos: List[SafeChangeCheckRequestBlockInfosHitInfos] = None,
        id: int = None,
    ):
        self.hit_infos = hit_infos
        self.id = id

    def validate(self):
        if self.hit_infos:
            for k in self.hit_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitInfos'] = []
        if self.hit_infos is not None:
            for k in self.hit_infos:
                result['HitInfos'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_infos = []
        if m.get('HitInfos') is not None:
            for k in m.get('HitInfos'):
                temp_model = SafeChangeCheckRequestBlockInfosHitInfos()
                self.hit_infos.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SafeChangeCheckRequestCallBackInfo(TeaModel):
    def __init__(
        self,
        api: str = None,
        api_version: str = None,
        end_point: str = None,
        pop_product: str = None,
        region_id: str = None,
        type: str = None,
        url: str = None,
    ):
        self.api = api
        self.api_version = api_version
        self.end_point = end_point
        self.pop_product = pop_product
        self.region_id = region_id
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.pop_product is not None:
            result['PopProduct'] = self.pop_product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('PopProduct') is not None:
            self.pop_product = m.get('PopProduct')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SafeChangeCheckRequestChangeTimes(TeaModel):
    def __init__(
        self,
        change_end_time: int = None,
        change_start_time: int = None,
    ):
        self.change_end_time = change_end_time
        self.change_start_time = change_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        return self


class SafeChangeCheckRequestDamagedChangeNoticesSensitiveCustomersCustomerInfo(TeaModel):
    def __init__(
        self,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        uid: str = None,
    ):
        self.extra_info = extra_info
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SafeChangeCheckRequestDamagedChangeNoticesSensitiveCustomers(TeaModel):
    def __init__(
        self,
        customer_info: List[SafeChangeCheckRequestDamagedChangeNoticesSensitiveCustomersCustomerInfo] = None,
        product_code: str = None,
    ):
        self.customer_info = customer_info
        self.product_code = product_code

    def validate(self):
        if self.customer_info:
            for k in self.customer_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomerInfo'] = []
        if self.customer_info is not None:
            for k in self.customer_info:
                result['CustomerInfo'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_info = []
        if m.get('CustomerInfo') is not None:
            for k in m.get('CustomerInfo'):
                temp_model = SafeChangeCheckRequestDamagedChangeNoticesSensitiveCustomersCustomerInfo()
                self.customer_info.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class SafeChangeCheckRequestDamagedChangeNotices(TeaModel):
    def __init__(
        self,
        bg_cancel_notice_content: str = None,
        bg_cancel_notice_event_id: str = None,
        channel: List[str] = None,
        content: str = None,
        event_id: str = None,
        sensitive_customers: List[SafeChangeCheckRequestDamagedChangeNoticesSensitiveCustomers] = None,
        type: str = None,
    ):
        self.bg_cancel_notice_content = bg_cancel_notice_content
        self.bg_cancel_notice_event_id = bg_cancel_notice_event_id
        self.channel = channel
        self.content = content
        self.event_id = event_id
        self.sensitive_customers = sensitive_customers
        self.type = type

    def validate(self):
        if self.sensitive_customers:
            for k in self.sensitive_customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_cancel_notice_content is not None:
            result['BgCancelNoticeContent'] = self.bg_cancel_notice_content
        if self.bg_cancel_notice_event_id is not None:
            result['BgCancelNoticeEventId'] = self.bg_cancel_notice_event_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.content is not None:
            result['Content'] = self.content
        if self.event_id is not None:
            result['EventId'] = self.event_id
        result['SensitiveCustomers'] = []
        if self.sensitive_customers is not None:
            for k in self.sensitive_customers:
                result['SensitiveCustomers'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgCancelNoticeContent') is not None:
            self.bg_cancel_notice_content = m.get('BgCancelNoticeContent')
        if m.get('BgCancelNoticeEventId') is not None:
            self.bg_cancel_notice_event_id = m.get('BgCancelNoticeEventId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        self.sensitive_customers = []
        if m.get('SensitiveCustomers') is not None:
            for k in m.get('SensitiveCustomers'):
                temp_model = SafeChangeCheckRequestDamagedChangeNoticesSensitiveCustomers()
                self.sensitive_customers.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SafeChangeCheckRequestHarmNoticeCombineParam(TeaModel):
    def __init__(
        self,
        combine: bool = None,
        combine_mark: str = None,
        combine_rule: str = None,
    ):
        self.combine = combine
        self.combine_mark = combine_mark
        self.combine_rule = combine_rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.combine is not None:
            result['Combine'] = self.combine
        if self.combine_mark is not None:
            result['CombineMark'] = self.combine_mark
        if self.combine_rule is not None:
            result['CombineRule'] = self.combine_rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Combine') is not None:
            self.combine = m.get('Combine')
        if m.get('CombineMark') is not None:
            self.combine_mark = m.get('CombineMark')
        if m.get('CombineRule') is not None:
            self.combine_rule = m.get('CombineRule')
        return self


class SafeChangeCheckRequestInfluenceInfoNoticeInfos(TeaModel):
    def __init__(
        self,
        channel: List[str] = None,
        content: str = None,
        event_id: str = None,
    ):
        self.channel = channel
        self.content = content
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.content is not None:
            result['Content'] = self.content
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class SafeChangeCheckRequestInfluenceInfoSensitiveCustomersCustomerInfo(TeaModel):
    def __init__(
        self,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        uid: str = None,
    ):
        self.extra_info = extra_info
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SafeChangeCheckRequestInfluenceInfoSensitiveCustomers(TeaModel):
    def __init__(
        self,
        customer_info: List[SafeChangeCheckRequestInfluenceInfoSensitiveCustomersCustomerInfo] = None,
        product_code: str = None,
    ):
        self.customer_info = customer_info
        self.product_code = product_code

    def validate(self):
        if self.customer_info:
            for k in self.customer_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomerInfo'] = []
        if self.customer_info is not None:
            for k in self.customer_info:
                result['CustomerInfo'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_info = []
        if m.get('CustomerInfo') is not None:
            for k in m.get('CustomerInfo'):
                temp_model = SafeChangeCheckRequestInfluenceInfoSensitiveCustomersCustomerInfo()
                self.customer_info.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class SafeChangeCheckRequestInfluenceInfo(TeaModel):
    def __init__(
        self,
        notice_infos: List[SafeChangeCheckRequestInfluenceInfoNoticeInfos] = None,
        sensitive_customers: List[SafeChangeCheckRequestInfluenceInfoSensitiveCustomers] = None,
    ):
        self.notice_infos = notice_infos
        self.sensitive_customers = sensitive_customers

    def validate(self):
        if self.notice_infos:
            for k in self.notice_infos:
                if k:
                    k.validate()
        if self.sensitive_customers:
            for k in self.sensitive_customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NoticeInfos'] = []
        if self.notice_infos is not None:
            for k in self.notice_infos:
                result['NoticeInfos'].append(k.to_map() if k else None)
        result['SensitiveCustomers'] = []
        if self.sensitive_customers is not None:
            for k in self.sensitive_customers:
                result['SensitiveCustomers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notice_infos = []
        if m.get('NoticeInfos') is not None:
            for k in m.get('NoticeInfos'):
                temp_model = SafeChangeCheckRequestInfluenceInfoNoticeInfos()
                self.notice_infos.append(temp_model.from_map(k))
        self.sensitive_customers = []
        if m.get('SensitiveCustomers') is not None:
            for k in m.get('SensitiveCustomers'):
                temp_model = SafeChangeCheckRequestInfluenceInfoSensitiveCustomers()
                self.sensitive_customers.append(temp_model.from_map(k))
        return self


class SafeChangeCheckRequestInstance(TeaModel):
    def __init__(
        self,
        nc: List[str] = None,
        uids: List[str] = None,
        attribution_app: List[str] = None,
        influence_app: List[str] = None,
        instance: List[str] = None,
    ):
        self.nc = nc
        self.uids = uids
        self.attribution_app = attribution_app
        self.influence_app = influence_app
        self.instance = instance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nc is not None:
            result['Nc'] = self.nc
        if self.uids is not None:
            result['Uids'] = self.uids
        if self.attribution_app is not None:
            result['attributionApp'] = self.attribution_app
        if self.influence_app is not None:
            result['influenceApp'] = self.influence_app
        if self.instance is not None:
            result['instance'] = self.instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nc') is not None:
            self.nc = m.get('Nc')
        if m.get('Uids') is not None:
            self.uids = m.get('Uids')
        if m.get('attributionApp') is not None:
            self.attribution_app = m.get('attributionApp')
        if m.get('influenceApp') is not None:
            self.influence_app = m.get('influenceApp')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        return self


class SafeChangeCheckRequestProduct(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SafeChangeCheckRequestReleasePackageInfos(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        release_package: List[str] = None,
    ):
        self.product_code = product_code
        self.release_package = release_package

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.release_package is not None:
            result['ReleasePackage'] = self.release_package
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReleasePackage') is not None:
            self.release_package = m.get('ReleasePackage')
        return self


class SafeChangeCheckRequest(TeaModel):
    def __init__(
        self,
        affect_customer: str = None,
        approve_flow_param: SafeChangeCheckRequestApproveFlowParam = None,
        auth_key: str = None,
        auth_sign: str = None,
        bg_custom_template_extra_dto: SafeChangeCheckRequestBgCustomTemplateExtraDTO = None,
        block_infos: List[SafeChangeCheckRequestBlockInfos] = None,
        call_back_info: SafeChangeCheckRequestCallBackInfo = None,
        change_data_type: str = None,
        change_desc: str = None,
        change_end_time: int = None,
        change_env: str = None,
        change_items: str = None,
        change_object: str = None,
        change_opt_sub_type: str = None,
        change_opt_type: str = None,
        change_reason: str = None,
        change_rmarks: str = None,
        change_schemes: str = None,
        change_start_time: int = None,
        change_sub_type_desc: str = None,
        change_system: str = None,
        change_times: List[SafeChangeCheckRequestChangeTimes] = None,
        change_title: str = None,
        change_validation: str = None,
        checker: List[str] = None,
        creator_emp_id: str = None,
        damaged_change_notices: List[SafeChangeCheckRequestDamagedChangeNotices] = None,
        executor_emp_id: str = None,
        extra_info: str = None,
        follower: List[str] = None,
        gray_status: str = None,
        harm_change_notice_enum: str = None,
        harm_notice_combine_param: SafeChangeCheckRequestHarmNoticeCombineParam = None,
        incidence: str = None,
        influence_info: SafeChangeCheckRequestInfluenceInfo = None,
        instance: SafeChangeCheckRequestInstance = None,
        need_modify_doc: str = None,
        operate_emp_no: str = None,
        product: List[SafeChangeCheckRequestProduct] = None,
        release_package_infos: List[SafeChangeCheckRequestReleasePackageInfos] = None,
        req_timestamp: int = None,
        reuse_source_order_id: str = None,
        risk_level: str = None,
        rollback: str = None,
        source_name: str = None,
        source_order_id: str = None,
        source_url: str = None,
        white_type: int = None,
    ):
        self.affect_customer = affect_customer
        self.approve_flow_param = approve_flow_param
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.bg_custom_template_extra_dto = bg_custom_template_extra_dto
        self.block_infos = block_infos
        self.call_back_info = call_back_info
        self.change_data_type = change_data_type
        self.change_desc = change_desc
        self.change_end_time = change_end_time
        self.change_env = change_env
        self.change_items = change_items
        self.change_object = change_object
        self.change_opt_sub_type = change_opt_sub_type
        self.change_opt_type = change_opt_type
        self.change_reason = change_reason
        self.change_rmarks = change_rmarks
        self.change_schemes = change_schemes
        self.change_start_time = change_start_time
        self.change_sub_type_desc = change_sub_type_desc
        self.change_system = change_system
        self.change_times = change_times
        self.change_title = change_title
        self.change_validation = change_validation
        self.checker = checker
        self.creator_emp_id = creator_emp_id
        self.damaged_change_notices = damaged_change_notices
        self.executor_emp_id = executor_emp_id
        self.extra_info = extra_info
        self.follower = follower
        self.gray_status = gray_status
        self.harm_change_notice_enum = harm_change_notice_enum
        self.harm_notice_combine_param = harm_notice_combine_param
        self.incidence = incidence
        self.influence_info = influence_info
        self.instance = instance
        self.need_modify_doc = need_modify_doc
        self.operate_emp_no = operate_emp_no
        self.product = product
        self.release_package_infos = release_package_infos
        self.req_timestamp = req_timestamp
        self.reuse_source_order_id = reuse_source_order_id
        self.risk_level = risk_level
        self.rollback = rollback
        self.source_name = source_name
        self.source_order_id = source_order_id
        self.source_url = source_url
        self.white_type = white_type

    def validate(self):
        if self.approve_flow_param:
            self.approve_flow_param.validate()
        if self.bg_custom_template_extra_dto:
            self.bg_custom_template_extra_dto.validate()
        if self.block_infos:
            for k in self.block_infos:
                if k:
                    k.validate()
        if self.call_back_info:
            self.call_back_info.validate()
        if self.change_times:
            for k in self.change_times:
                if k:
                    k.validate()
        if self.damaged_change_notices:
            for k in self.damaged_change_notices:
                if k:
                    k.validate()
        if self.harm_notice_combine_param:
            self.harm_notice_combine_param.validate()
        if self.influence_info:
            self.influence_info.validate()
        if self.instance:
            self.instance.validate()
        if self.product:
            for k in self.product:
                if k:
                    k.validate()
        if self.release_package_infos:
            for k in self.release_package_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_customer is not None:
            result['AffectCustomer'] = self.affect_customer
        if self.approve_flow_param is not None:
            result['ApproveFlowParam'] = self.approve_flow_param.to_map()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.bg_custom_template_extra_dto is not None:
            result['BgCustomTemplateExtraDTO'] = self.bg_custom_template_extra_dto.to_map()
        result['BlockInfos'] = []
        if self.block_infos is not None:
            for k in self.block_infos:
                result['BlockInfos'].append(k.to_map() if k else None)
        if self.call_back_info is not None:
            result['CallBackInfo'] = self.call_back_info.to_map()
        if self.change_data_type is not None:
            result['ChangeDataType'] = self.change_data_type
        if self.change_desc is not None:
            result['ChangeDesc'] = self.change_desc
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_env is not None:
            result['ChangeEnv'] = self.change_env
        if self.change_items is not None:
            result['ChangeItems'] = self.change_items
        if self.change_object is not None:
            result['ChangeObject'] = self.change_object
        if self.change_opt_sub_type is not None:
            result['ChangeOptSubType'] = self.change_opt_sub_type
        if self.change_opt_type is not None:
            result['ChangeOptType'] = self.change_opt_type
        if self.change_reason is not None:
            result['ChangeReason'] = self.change_reason
        if self.change_rmarks is not None:
            result['ChangeRmarks'] = self.change_rmarks
        if self.change_schemes is not None:
            result['ChangeSchemes'] = self.change_schemes
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_sub_type_desc is not None:
            result['ChangeSubTypeDesc'] = self.change_sub_type_desc
        if self.change_system is not None:
            result['ChangeSystem'] = self.change_system
        result['ChangeTimes'] = []
        if self.change_times is not None:
            for k in self.change_times:
                result['ChangeTimes'].append(k.to_map() if k else None)
        if self.change_title is not None:
            result['ChangeTitle'] = self.change_title
        if self.change_validation is not None:
            result['ChangeValidation'] = self.change_validation
        if self.checker is not None:
            result['Checker'] = self.checker
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        result['DamagedChangeNotices'] = []
        if self.damaged_change_notices is not None:
            for k in self.damaged_change_notices:
                result['DamagedChangeNotices'].append(k.to_map() if k else None)
        if self.executor_emp_id is not None:
            result['ExecutorEmpId'] = self.executor_emp_id
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.follower is not None:
            result['Follower'] = self.follower
        if self.gray_status is not None:
            result['GrayStatus'] = self.gray_status
        if self.harm_change_notice_enum is not None:
            result['HarmChangeNoticeEnum'] = self.harm_change_notice_enum
        if self.harm_notice_combine_param is not None:
            result['HarmNoticeCombineParam'] = self.harm_notice_combine_param.to_map()
        if self.incidence is not None:
            result['Incidence'] = self.incidence
        if self.influence_info is not None:
            result['InfluenceInfo'] = self.influence_info.to_map()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.need_modify_doc is not None:
            result['NeedModifyDoc'] = self.need_modify_doc
        if self.operate_emp_no is not None:
            result['OperateEmpNo'] = self.operate_emp_no
        result['Product'] = []
        if self.product is not None:
            for k in self.product:
                result['Product'].append(k.to_map() if k else None)
        result['ReleasePackageInfos'] = []
        if self.release_package_infos is not None:
            for k in self.release_package_infos:
                result['ReleasePackageInfos'].append(k.to_map() if k else None)
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.reuse_source_order_id is not None:
            result['ReuseSourceOrderId'] = self.reuse_source_order_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rollback is not None:
            result['Rollback'] = self.rollback
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.white_type is not None:
            result['whiteType'] = self.white_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectCustomer') is not None:
            self.affect_customer = m.get('AffectCustomer')
        if m.get('ApproveFlowParam') is not None:
            temp_model = SafeChangeCheckRequestApproveFlowParam()
            self.approve_flow_param = temp_model.from_map(m['ApproveFlowParam'])
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('BgCustomTemplateExtraDTO') is not None:
            temp_model = SafeChangeCheckRequestBgCustomTemplateExtraDTO()
            self.bg_custom_template_extra_dto = temp_model.from_map(m['BgCustomTemplateExtraDTO'])
        self.block_infos = []
        if m.get('BlockInfos') is not None:
            for k in m.get('BlockInfos'):
                temp_model = SafeChangeCheckRequestBlockInfos()
                self.block_infos.append(temp_model.from_map(k))
        if m.get('CallBackInfo') is not None:
            temp_model = SafeChangeCheckRequestCallBackInfo()
            self.call_back_info = temp_model.from_map(m['CallBackInfo'])
        if m.get('ChangeDataType') is not None:
            self.change_data_type = m.get('ChangeDataType')
        if m.get('ChangeDesc') is not None:
            self.change_desc = m.get('ChangeDesc')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeEnv') is not None:
            self.change_env = m.get('ChangeEnv')
        if m.get('ChangeItems') is not None:
            self.change_items = m.get('ChangeItems')
        if m.get('ChangeObject') is not None:
            self.change_object = m.get('ChangeObject')
        if m.get('ChangeOptSubType') is not None:
            self.change_opt_sub_type = m.get('ChangeOptSubType')
        if m.get('ChangeOptType') is not None:
            self.change_opt_type = m.get('ChangeOptType')
        if m.get('ChangeReason') is not None:
            self.change_reason = m.get('ChangeReason')
        if m.get('ChangeRmarks') is not None:
            self.change_rmarks = m.get('ChangeRmarks')
        if m.get('ChangeSchemes') is not None:
            self.change_schemes = m.get('ChangeSchemes')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeSubTypeDesc') is not None:
            self.change_sub_type_desc = m.get('ChangeSubTypeDesc')
        if m.get('ChangeSystem') is not None:
            self.change_system = m.get('ChangeSystem')
        self.change_times = []
        if m.get('ChangeTimes') is not None:
            for k in m.get('ChangeTimes'):
                temp_model = SafeChangeCheckRequestChangeTimes()
                self.change_times.append(temp_model.from_map(k))
        if m.get('ChangeTitle') is not None:
            self.change_title = m.get('ChangeTitle')
        if m.get('ChangeValidation') is not None:
            self.change_validation = m.get('ChangeValidation')
        if m.get('Checker') is not None:
            self.checker = m.get('Checker')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        self.damaged_change_notices = []
        if m.get('DamagedChangeNotices') is not None:
            for k in m.get('DamagedChangeNotices'):
                temp_model = SafeChangeCheckRequestDamagedChangeNotices()
                self.damaged_change_notices.append(temp_model.from_map(k))
        if m.get('ExecutorEmpId') is not None:
            self.executor_emp_id = m.get('ExecutorEmpId')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Follower') is not None:
            self.follower = m.get('Follower')
        if m.get('GrayStatus') is not None:
            self.gray_status = m.get('GrayStatus')
        if m.get('HarmChangeNoticeEnum') is not None:
            self.harm_change_notice_enum = m.get('HarmChangeNoticeEnum')
        if m.get('HarmNoticeCombineParam') is not None:
            temp_model = SafeChangeCheckRequestHarmNoticeCombineParam()
            self.harm_notice_combine_param = temp_model.from_map(m['HarmNoticeCombineParam'])
        if m.get('Incidence') is not None:
            self.incidence = m.get('Incidence')
        if m.get('InfluenceInfo') is not None:
            temp_model = SafeChangeCheckRequestInfluenceInfo()
            self.influence_info = temp_model.from_map(m['InfluenceInfo'])
        if m.get('Instance') is not None:
            temp_model = SafeChangeCheckRequestInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('NeedModifyDoc') is not None:
            self.need_modify_doc = m.get('NeedModifyDoc')
        if m.get('OperateEmpNo') is not None:
            self.operate_emp_no = m.get('OperateEmpNo')
        self.product = []
        if m.get('Product') is not None:
            for k in m.get('Product'):
                temp_model = SafeChangeCheckRequestProduct()
                self.product.append(temp_model.from_map(k))
        self.release_package_infos = []
        if m.get('ReleasePackageInfos') is not None:
            for k in m.get('ReleasePackageInfos'):
                temp_model = SafeChangeCheckRequestReleasePackageInfos()
                self.release_package_infos.append(temp_model.from_map(k))
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('ReuseSourceOrderId') is not None:
            self.reuse_source_order_id = m.get('ReuseSourceOrderId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('whiteType') is not None:
            self.white_type = m.get('whiteType')
        return self


class SafeChangeCheckShrinkRequestApproveFlowParamApproveNodesApproverDTO(TeaModel):
    def __init__(
        self,
        approve_desc: str = None,
        approve_time: int = None,
        approver_id: str = None,
        approver_name: str = None,
        opinion: int = None,
    ):
        self.approve_desc = approve_desc
        self.approve_time = approve_time
        self.approver_id = approver_id
        self.approver_name = approver_name
        self.opinion = opinion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_desc is not None:
            result['ApproveDesc'] = self.approve_desc
        if self.approve_time is not None:
            result['ApproveTime'] = self.approve_time
        if self.approver_id is not None:
            result['ApproverId'] = self.approver_id
        if self.approver_name is not None:
            result['ApproverName'] = self.approver_name
        if self.opinion is not None:
            result['Opinion'] = self.opinion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveDesc') is not None:
            self.approve_desc = m.get('ApproveDesc')
        if m.get('ApproveTime') is not None:
            self.approve_time = m.get('ApproveTime')
        if m.get('ApproverId') is not None:
            self.approver_id = m.get('ApproverId')
        if m.get('ApproverName') is not None:
            self.approver_name = m.get('ApproverName')
        if m.get('Opinion') is not None:
            self.opinion = m.get('Opinion')
        return self


class SafeChangeCheckShrinkRequestApproveFlowParamApproveNodes(TeaModel):
    def __init__(
        self,
        approver_dto: List[SafeChangeCheckShrinkRequestApproveFlowParamApproveNodesApproverDTO] = None,
        node_status: int = None,
        process_name: str = None,
        process_node_order: int = None,
        strategy: int = None,
    ):
        self.approver_dto = approver_dto
        self.node_status = node_status
        self.process_name = process_name
        self.process_node_order = process_node_order
        self.strategy = strategy

    def validate(self):
        if self.approver_dto:
            for k in self.approver_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproverDTO'] = []
        if self.approver_dto is not None:
            for k in self.approver_dto:
                result['ApproverDTO'].append(k.to_map() if k else None)
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.process_name is not None:
            result['ProcessName'] = self.process_name
        if self.process_node_order is not None:
            result['ProcessNodeOrder'] = self.process_node_order
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approver_dto = []
        if m.get('ApproverDTO') is not None:
            for k in m.get('ApproverDTO'):
                temp_model = SafeChangeCheckShrinkRequestApproveFlowParamApproveNodesApproverDTO()
                self.approver_dto.append(temp_model.from_map(k))
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')
        if m.get('ProcessNodeOrder') is not None:
            self.process_node_order = m.get('ProcessNodeOrder')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        return self


class SafeChangeCheckShrinkRequestApproveFlowParam(TeaModel):
    def __init__(
        self,
        approve_nodes: List[SafeChangeCheckShrinkRequestApproveFlowParamApproveNodes] = None,
        flow_status: int = None,
    ):
        self.approve_nodes = approve_nodes
        self.flow_status = flow_status

    def validate(self):
        if self.approve_nodes:
            for k in self.approve_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproveNodes'] = []
        if self.approve_nodes is not None:
            for k in self.approve_nodes:
                result['ApproveNodes'].append(k.to_map() if k else None)
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approve_nodes = []
        if m.get('ApproveNodes') is not None:
            for k in m.get('ApproveNodes'):
                temp_model = SafeChangeCheckShrinkRequestApproveFlowParamApproveNodes()
                self.approve_nodes.append(temp_model.from_map(k))
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        return self


class SafeChangeCheckShrinkRequestBgCustomTemplateExtraDTO(TeaModel):
    def __init__(
        self,
        bg_custom_template_info: str = None,
    ):
        self.bg_custom_template_info = bg_custom_template_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_custom_template_info is not None:
            result['BgCustomTemplateInfo'] = self.bg_custom_template_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgCustomTemplateInfo') is not None:
            self.bg_custom_template_info = m.get('BgCustomTemplateInfo')
        return self


class SafeChangeCheckShrinkRequestBlockInfosHitInfos(TeaModel):
    def __init__(
        self,
        hit_info: str = None,
        hit_object: str = None,
        scope: str = None,
    ):
        self.hit_info = hit_info
        self.hit_object = hit_object
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_info is not None:
            result['HitInfo'] = self.hit_info
        if self.hit_object is not None:
            result['HitObject'] = self.hit_object
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitInfo') is not None:
            self.hit_info = m.get('HitInfo')
        if m.get('HitObject') is not None:
            self.hit_object = m.get('HitObject')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class SafeChangeCheckShrinkRequestBlockInfos(TeaModel):
    def __init__(
        self,
        hit_infos: List[SafeChangeCheckShrinkRequestBlockInfosHitInfos] = None,
        id: int = None,
    ):
        self.hit_infos = hit_infos
        self.id = id

    def validate(self):
        if self.hit_infos:
            for k in self.hit_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitInfos'] = []
        if self.hit_infos is not None:
            for k in self.hit_infos:
                result['HitInfos'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_infos = []
        if m.get('HitInfos') is not None:
            for k in m.get('HitInfos'):
                temp_model = SafeChangeCheckShrinkRequestBlockInfosHitInfos()
                self.hit_infos.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SafeChangeCheckShrinkRequestCallBackInfo(TeaModel):
    def __init__(
        self,
        api: str = None,
        api_version: str = None,
        end_point: str = None,
        pop_product: str = None,
        region_id: str = None,
        type: str = None,
        url: str = None,
    ):
        self.api = api
        self.api_version = api_version
        self.end_point = end_point
        self.pop_product = pop_product
        self.region_id = region_id
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.pop_product is not None:
            result['PopProduct'] = self.pop_product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('PopProduct') is not None:
            self.pop_product = m.get('PopProduct')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SafeChangeCheckShrinkRequestChangeTimes(TeaModel):
    def __init__(
        self,
        change_end_time: int = None,
        change_start_time: int = None,
    ):
        self.change_end_time = change_end_time
        self.change_start_time = change_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        return self


class SafeChangeCheckShrinkRequestDamagedChangeNoticesSensitiveCustomersCustomerInfo(TeaModel):
    def __init__(
        self,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        uid: str = None,
    ):
        self.extra_info = extra_info
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SafeChangeCheckShrinkRequestDamagedChangeNoticesSensitiveCustomers(TeaModel):
    def __init__(
        self,
        customer_info: List[SafeChangeCheckShrinkRequestDamagedChangeNoticesSensitiveCustomersCustomerInfo] = None,
        product_code: str = None,
    ):
        self.customer_info = customer_info
        self.product_code = product_code

    def validate(self):
        if self.customer_info:
            for k in self.customer_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomerInfo'] = []
        if self.customer_info is not None:
            for k in self.customer_info:
                result['CustomerInfo'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_info = []
        if m.get('CustomerInfo') is not None:
            for k in m.get('CustomerInfo'):
                temp_model = SafeChangeCheckShrinkRequestDamagedChangeNoticesSensitiveCustomersCustomerInfo()
                self.customer_info.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class SafeChangeCheckShrinkRequestDamagedChangeNotices(TeaModel):
    def __init__(
        self,
        bg_cancel_notice_content: str = None,
        bg_cancel_notice_event_id: str = None,
        channel: List[str] = None,
        content: str = None,
        event_id: str = None,
        sensitive_customers: List[SafeChangeCheckShrinkRequestDamagedChangeNoticesSensitiveCustomers] = None,
        type: str = None,
    ):
        self.bg_cancel_notice_content = bg_cancel_notice_content
        self.bg_cancel_notice_event_id = bg_cancel_notice_event_id
        self.channel = channel
        self.content = content
        self.event_id = event_id
        self.sensitive_customers = sensitive_customers
        self.type = type

    def validate(self):
        if self.sensitive_customers:
            for k in self.sensitive_customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_cancel_notice_content is not None:
            result['BgCancelNoticeContent'] = self.bg_cancel_notice_content
        if self.bg_cancel_notice_event_id is not None:
            result['BgCancelNoticeEventId'] = self.bg_cancel_notice_event_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.content is not None:
            result['Content'] = self.content
        if self.event_id is not None:
            result['EventId'] = self.event_id
        result['SensitiveCustomers'] = []
        if self.sensitive_customers is not None:
            for k in self.sensitive_customers:
                result['SensitiveCustomers'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgCancelNoticeContent') is not None:
            self.bg_cancel_notice_content = m.get('BgCancelNoticeContent')
        if m.get('BgCancelNoticeEventId') is not None:
            self.bg_cancel_notice_event_id = m.get('BgCancelNoticeEventId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        self.sensitive_customers = []
        if m.get('SensitiveCustomers') is not None:
            for k in m.get('SensitiveCustomers'):
                temp_model = SafeChangeCheckShrinkRequestDamagedChangeNoticesSensitiveCustomers()
                self.sensitive_customers.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SafeChangeCheckShrinkRequestInfluenceInfoNoticeInfos(TeaModel):
    def __init__(
        self,
        channel: List[str] = None,
        content: str = None,
        event_id: str = None,
    ):
        self.channel = channel
        self.content = content
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.content is not None:
            result['Content'] = self.content
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class SafeChangeCheckShrinkRequestInfluenceInfoSensitiveCustomersCustomerInfo(TeaModel):
    def __init__(
        self,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        uid: str = None,
    ):
        self.extra_info = extra_info
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SafeChangeCheckShrinkRequestInfluenceInfoSensitiveCustomers(TeaModel):
    def __init__(
        self,
        customer_info: List[SafeChangeCheckShrinkRequestInfluenceInfoSensitiveCustomersCustomerInfo] = None,
        product_code: str = None,
    ):
        self.customer_info = customer_info
        self.product_code = product_code

    def validate(self):
        if self.customer_info:
            for k in self.customer_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomerInfo'] = []
        if self.customer_info is not None:
            for k in self.customer_info:
                result['CustomerInfo'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_info = []
        if m.get('CustomerInfo') is not None:
            for k in m.get('CustomerInfo'):
                temp_model = SafeChangeCheckShrinkRequestInfluenceInfoSensitiveCustomersCustomerInfo()
                self.customer_info.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class SafeChangeCheckShrinkRequestInfluenceInfo(TeaModel):
    def __init__(
        self,
        notice_infos: List[SafeChangeCheckShrinkRequestInfluenceInfoNoticeInfos] = None,
        sensitive_customers: List[SafeChangeCheckShrinkRequestInfluenceInfoSensitiveCustomers] = None,
    ):
        self.notice_infos = notice_infos
        self.sensitive_customers = sensitive_customers

    def validate(self):
        if self.notice_infos:
            for k in self.notice_infos:
                if k:
                    k.validate()
        if self.sensitive_customers:
            for k in self.sensitive_customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NoticeInfos'] = []
        if self.notice_infos is not None:
            for k in self.notice_infos:
                result['NoticeInfos'].append(k.to_map() if k else None)
        result['SensitiveCustomers'] = []
        if self.sensitive_customers is not None:
            for k in self.sensitive_customers:
                result['SensitiveCustomers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notice_infos = []
        if m.get('NoticeInfos') is not None:
            for k in m.get('NoticeInfos'):
                temp_model = SafeChangeCheckShrinkRequestInfluenceInfoNoticeInfos()
                self.notice_infos.append(temp_model.from_map(k))
        self.sensitive_customers = []
        if m.get('SensitiveCustomers') is not None:
            for k in m.get('SensitiveCustomers'):
                temp_model = SafeChangeCheckShrinkRequestInfluenceInfoSensitiveCustomers()
                self.sensitive_customers.append(temp_model.from_map(k))
        return self


class SafeChangeCheckShrinkRequestInstance(TeaModel):
    def __init__(
        self,
        nc: List[str] = None,
        uids: List[str] = None,
        attribution_app: List[str] = None,
        influence_app: List[str] = None,
        instance: List[str] = None,
    ):
        self.nc = nc
        self.uids = uids
        self.attribution_app = attribution_app
        self.influence_app = influence_app
        self.instance = instance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nc is not None:
            result['Nc'] = self.nc
        if self.uids is not None:
            result['Uids'] = self.uids
        if self.attribution_app is not None:
            result['attributionApp'] = self.attribution_app
        if self.influence_app is not None:
            result['influenceApp'] = self.influence_app
        if self.instance is not None:
            result['instance'] = self.instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nc') is not None:
            self.nc = m.get('Nc')
        if m.get('Uids') is not None:
            self.uids = m.get('Uids')
        if m.get('attributionApp') is not None:
            self.attribution_app = m.get('attributionApp')
        if m.get('influenceApp') is not None:
            self.influence_app = m.get('influenceApp')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        return self


class SafeChangeCheckShrinkRequestProduct(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SafeChangeCheckShrinkRequestReleasePackageInfos(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        release_package: List[str] = None,
    ):
        self.product_code = product_code
        self.release_package = release_package

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.release_package is not None:
            result['ReleasePackage'] = self.release_package
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReleasePackage') is not None:
            self.release_package = m.get('ReleasePackage')
        return self


class SafeChangeCheckShrinkRequest(TeaModel):
    def __init__(
        self,
        affect_customer: str = None,
        approve_flow_param: SafeChangeCheckShrinkRequestApproveFlowParam = None,
        auth_key: str = None,
        auth_sign: str = None,
        bg_custom_template_extra_dto: SafeChangeCheckShrinkRequestBgCustomTemplateExtraDTO = None,
        block_infos: List[SafeChangeCheckShrinkRequestBlockInfos] = None,
        call_back_info: SafeChangeCheckShrinkRequestCallBackInfo = None,
        change_data_type: str = None,
        change_desc: str = None,
        change_end_time: int = None,
        change_env: str = None,
        change_items: str = None,
        change_object: str = None,
        change_opt_sub_type: str = None,
        change_opt_type: str = None,
        change_reason: str = None,
        change_rmarks: str = None,
        change_schemes: str = None,
        change_start_time: int = None,
        change_sub_type_desc: str = None,
        change_system: str = None,
        change_times: List[SafeChangeCheckShrinkRequestChangeTimes] = None,
        change_title: str = None,
        change_validation: str = None,
        checker: List[str] = None,
        creator_emp_id: str = None,
        damaged_change_notices: List[SafeChangeCheckShrinkRequestDamagedChangeNotices] = None,
        executor_emp_id: str = None,
        extra_info: str = None,
        follower: List[str] = None,
        gray_status: str = None,
        harm_change_notice_enum: str = None,
        harm_notice_combine_param_shrink: str = None,
        incidence: str = None,
        influence_info: SafeChangeCheckShrinkRequestInfluenceInfo = None,
        instance: SafeChangeCheckShrinkRequestInstance = None,
        need_modify_doc: str = None,
        operate_emp_no: str = None,
        product: List[SafeChangeCheckShrinkRequestProduct] = None,
        release_package_infos: List[SafeChangeCheckShrinkRequestReleasePackageInfos] = None,
        req_timestamp: int = None,
        reuse_source_order_id: str = None,
        risk_level: str = None,
        rollback: str = None,
        source_name: str = None,
        source_order_id: str = None,
        source_url: str = None,
        white_type: int = None,
    ):
        self.affect_customer = affect_customer
        self.approve_flow_param = approve_flow_param
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.bg_custom_template_extra_dto = bg_custom_template_extra_dto
        self.block_infos = block_infos
        self.call_back_info = call_back_info
        self.change_data_type = change_data_type
        self.change_desc = change_desc
        self.change_end_time = change_end_time
        self.change_env = change_env
        self.change_items = change_items
        self.change_object = change_object
        self.change_opt_sub_type = change_opt_sub_type
        self.change_opt_type = change_opt_type
        self.change_reason = change_reason
        self.change_rmarks = change_rmarks
        self.change_schemes = change_schemes
        self.change_start_time = change_start_time
        self.change_sub_type_desc = change_sub_type_desc
        self.change_system = change_system
        self.change_times = change_times
        self.change_title = change_title
        self.change_validation = change_validation
        self.checker = checker
        self.creator_emp_id = creator_emp_id
        self.damaged_change_notices = damaged_change_notices
        self.executor_emp_id = executor_emp_id
        self.extra_info = extra_info
        self.follower = follower
        self.gray_status = gray_status
        self.harm_change_notice_enum = harm_change_notice_enum
        self.harm_notice_combine_param_shrink = harm_notice_combine_param_shrink
        self.incidence = incidence
        self.influence_info = influence_info
        self.instance = instance
        self.need_modify_doc = need_modify_doc
        self.operate_emp_no = operate_emp_no
        self.product = product
        self.release_package_infos = release_package_infos
        self.req_timestamp = req_timestamp
        self.reuse_source_order_id = reuse_source_order_id
        self.risk_level = risk_level
        self.rollback = rollback
        self.source_name = source_name
        self.source_order_id = source_order_id
        self.source_url = source_url
        self.white_type = white_type

    def validate(self):
        if self.approve_flow_param:
            self.approve_flow_param.validate()
        if self.bg_custom_template_extra_dto:
            self.bg_custom_template_extra_dto.validate()
        if self.block_infos:
            for k in self.block_infos:
                if k:
                    k.validate()
        if self.call_back_info:
            self.call_back_info.validate()
        if self.change_times:
            for k in self.change_times:
                if k:
                    k.validate()
        if self.damaged_change_notices:
            for k in self.damaged_change_notices:
                if k:
                    k.validate()
        if self.influence_info:
            self.influence_info.validate()
        if self.instance:
            self.instance.validate()
        if self.product:
            for k in self.product:
                if k:
                    k.validate()
        if self.release_package_infos:
            for k in self.release_package_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_customer is not None:
            result['AffectCustomer'] = self.affect_customer
        if self.approve_flow_param is not None:
            result['ApproveFlowParam'] = self.approve_flow_param.to_map()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.bg_custom_template_extra_dto is not None:
            result['BgCustomTemplateExtraDTO'] = self.bg_custom_template_extra_dto.to_map()
        result['BlockInfos'] = []
        if self.block_infos is not None:
            for k in self.block_infos:
                result['BlockInfos'].append(k.to_map() if k else None)
        if self.call_back_info is not None:
            result['CallBackInfo'] = self.call_back_info.to_map()
        if self.change_data_type is not None:
            result['ChangeDataType'] = self.change_data_type
        if self.change_desc is not None:
            result['ChangeDesc'] = self.change_desc
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_env is not None:
            result['ChangeEnv'] = self.change_env
        if self.change_items is not None:
            result['ChangeItems'] = self.change_items
        if self.change_object is not None:
            result['ChangeObject'] = self.change_object
        if self.change_opt_sub_type is not None:
            result['ChangeOptSubType'] = self.change_opt_sub_type
        if self.change_opt_type is not None:
            result['ChangeOptType'] = self.change_opt_type
        if self.change_reason is not None:
            result['ChangeReason'] = self.change_reason
        if self.change_rmarks is not None:
            result['ChangeRmarks'] = self.change_rmarks
        if self.change_schemes is not None:
            result['ChangeSchemes'] = self.change_schemes
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_sub_type_desc is not None:
            result['ChangeSubTypeDesc'] = self.change_sub_type_desc
        if self.change_system is not None:
            result['ChangeSystem'] = self.change_system
        result['ChangeTimes'] = []
        if self.change_times is not None:
            for k in self.change_times:
                result['ChangeTimes'].append(k.to_map() if k else None)
        if self.change_title is not None:
            result['ChangeTitle'] = self.change_title
        if self.change_validation is not None:
            result['ChangeValidation'] = self.change_validation
        if self.checker is not None:
            result['Checker'] = self.checker
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        result['DamagedChangeNotices'] = []
        if self.damaged_change_notices is not None:
            for k in self.damaged_change_notices:
                result['DamagedChangeNotices'].append(k.to_map() if k else None)
        if self.executor_emp_id is not None:
            result['ExecutorEmpId'] = self.executor_emp_id
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.follower is not None:
            result['Follower'] = self.follower
        if self.gray_status is not None:
            result['GrayStatus'] = self.gray_status
        if self.harm_change_notice_enum is not None:
            result['HarmChangeNoticeEnum'] = self.harm_change_notice_enum
        if self.harm_notice_combine_param_shrink is not None:
            result['HarmNoticeCombineParam'] = self.harm_notice_combine_param_shrink
        if self.incidence is not None:
            result['Incidence'] = self.incidence
        if self.influence_info is not None:
            result['InfluenceInfo'] = self.influence_info.to_map()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.need_modify_doc is not None:
            result['NeedModifyDoc'] = self.need_modify_doc
        if self.operate_emp_no is not None:
            result['OperateEmpNo'] = self.operate_emp_no
        result['Product'] = []
        if self.product is not None:
            for k in self.product:
                result['Product'].append(k.to_map() if k else None)
        result['ReleasePackageInfos'] = []
        if self.release_package_infos is not None:
            for k in self.release_package_infos:
                result['ReleasePackageInfos'].append(k.to_map() if k else None)
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.reuse_source_order_id is not None:
            result['ReuseSourceOrderId'] = self.reuse_source_order_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rollback is not None:
            result['Rollback'] = self.rollback
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.white_type is not None:
            result['whiteType'] = self.white_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectCustomer') is not None:
            self.affect_customer = m.get('AffectCustomer')
        if m.get('ApproveFlowParam') is not None:
            temp_model = SafeChangeCheckShrinkRequestApproveFlowParam()
            self.approve_flow_param = temp_model.from_map(m['ApproveFlowParam'])
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('BgCustomTemplateExtraDTO') is not None:
            temp_model = SafeChangeCheckShrinkRequestBgCustomTemplateExtraDTO()
            self.bg_custom_template_extra_dto = temp_model.from_map(m['BgCustomTemplateExtraDTO'])
        self.block_infos = []
        if m.get('BlockInfos') is not None:
            for k in m.get('BlockInfos'):
                temp_model = SafeChangeCheckShrinkRequestBlockInfos()
                self.block_infos.append(temp_model.from_map(k))
        if m.get('CallBackInfo') is not None:
            temp_model = SafeChangeCheckShrinkRequestCallBackInfo()
            self.call_back_info = temp_model.from_map(m['CallBackInfo'])
        if m.get('ChangeDataType') is not None:
            self.change_data_type = m.get('ChangeDataType')
        if m.get('ChangeDesc') is not None:
            self.change_desc = m.get('ChangeDesc')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeEnv') is not None:
            self.change_env = m.get('ChangeEnv')
        if m.get('ChangeItems') is not None:
            self.change_items = m.get('ChangeItems')
        if m.get('ChangeObject') is not None:
            self.change_object = m.get('ChangeObject')
        if m.get('ChangeOptSubType') is not None:
            self.change_opt_sub_type = m.get('ChangeOptSubType')
        if m.get('ChangeOptType') is not None:
            self.change_opt_type = m.get('ChangeOptType')
        if m.get('ChangeReason') is not None:
            self.change_reason = m.get('ChangeReason')
        if m.get('ChangeRmarks') is not None:
            self.change_rmarks = m.get('ChangeRmarks')
        if m.get('ChangeSchemes') is not None:
            self.change_schemes = m.get('ChangeSchemes')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeSubTypeDesc') is not None:
            self.change_sub_type_desc = m.get('ChangeSubTypeDesc')
        if m.get('ChangeSystem') is not None:
            self.change_system = m.get('ChangeSystem')
        self.change_times = []
        if m.get('ChangeTimes') is not None:
            for k in m.get('ChangeTimes'):
                temp_model = SafeChangeCheckShrinkRequestChangeTimes()
                self.change_times.append(temp_model.from_map(k))
        if m.get('ChangeTitle') is not None:
            self.change_title = m.get('ChangeTitle')
        if m.get('ChangeValidation') is not None:
            self.change_validation = m.get('ChangeValidation')
        if m.get('Checker') is not None:
            self.checker = m.get('Checker')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        self.damaged_change_notices = []
        if m.get('DamagedChangeNotices') is not None:
            for k in m.get('DamagedChangeNotices'):
                temp_model = SafeChangeCheckShrinkRequestDamagedChangeNotices()
                self.damaged_change_notices.append(temp_model.from_map(k))
        if m.get('ExecutorEmpId') is not None:
            self.executor_emp_id = m.get('ExecutorEmpId')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Follower') is not None:
            self.follower = m.get('Follower')
        if m.get('GrayStatus') is not None:
            self.gray_status = m.get('GrayStatus')
        if m.get('HarmChangeNoticeEnum') is not None:
            self.harm_change_notice_enum = m.get('HarmChangeNoticeEnum')
        if m.get('HarmNoticeCombineParam') is not None:
            self.harm_notice_combine_param_shrink = m.get('HarmNoticeCombineParam')
        if m.get('Incidence') is not None:
            self.incidence = m.get('Incidence')
        if m.get('InfluenceInfo') is not None:
            temp_model = SafeChangeCheckShrinkRequestInfluenceInfo()
            self.influence_info = temp_model.from_map(m['InfluenceInfo'])
        if m.get('Instance') is not None:
            temp_model = SafeChangeCheckShrinkRequestInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('NeedModifyDoc') is not None:
            self.need_modify_doc = m.get('NeedModifyDoc')
        if m.get('OperateEmpNo') is not None:
            self.operate_emp_no = m.get('OperateEmpNo')
        self.product = []
        if m.get('Product') is not None:
            for k in m.get('Product'):
                temp_model = SafeChangeCheckShrinkRequestProduct()
                self.product.append(temp_model.from_map(k))
        self.release_package_infos = []
        if m.get('ReleasePackageInfos') is not None:
            for k in m.get('ReleasePackageInfos'):
                temp_model = SafeChangeCheckShrinkRequestReleasePackageInfos()
                self.release_package_infos.append(temp_model.from_map(k))
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('ReuseSourceOrderId') is not None:
            self.reuse_source_order_id = m.get('ReuseSourceOrderId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('whiteType') is not None:
            self.white_type = m.get('whiteType')
        return self


class SafeChangeCheckResponseBodyDataRuleDetailUrlList(TeaModel):
    def __init__(
        self,
        scene_enum: str = None,
        title: str = None,
        url: str = None,
    ):
        self.scene_enum = scene_enum
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_enum is not None:
            result['SceneEnum'] = self.scene_enum
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneEnum') is not None:
            self.scene_enum = m.get('SceneEnum')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SafeChangeCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        approve_result_url: str = None,
        bg_check_status: str = None,
        bg_vid: str = None,
        check_result_url: str = None,
        check_status: str = None,
        checkhold_reason: List[str] = None,
        rule_detail_url_list: List[SafeChangeCheckResponseBodyDataRuleDetailUrlList] = None,
        source_order_id: str = None,
    ):
        self.approve_result_url = approve_result_url
        self.bg_check_status = bg_check_status
        self.bg_vid = bg_vid
        self.check_result_url = check_result_url
        self.check_status = check_status
        self.checkhold_reason = checkhold_reason
        self.rule_detail_url_list = rule_detail_url_list
        self.source_order_id = source_order_id

    def validate(self):
        if self.rule_detail_url_list:
            for k in self.rule_detail_url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_result_url is not None:
            result['ApproveResultUrl'] = self.approve_result_url
        if self.bg_check_status is not None:
            result['BgCheckStatus'] = self.bg_check_status
        if self.bg_vid is not None:
            result['BgVid'] = self.bg_vid
        if self.check_result_url is not None:
            result['CheckResultUrl'] = self.check_result_url
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.checkhold_reason is not None:
            result['CheckholdReason'] = self.checkhold_reason
        result['RuleDetailUrlList'] = []
        if self.rule_detail_url_list is not None:
            for k in self.rule_detail_url_list:
                result['RuleDetailUrlList'].append(k.to_map() if k else None)
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveResultUrl') is not None:
            self.approve_result_url = m.get('ApproveResultUrl')
        if m.get('BgCheckStatus') is not None:
            self.bg_check_status = m.get('BgCheckStatus')
        if m.get('BgVid') is not None:
            self.bg_vid = m.get('BgVid')
        if m.get('CheckResultUrl') is not None:
            self.check_result_url = m.get('CheckResultUrl')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckholdReason') is not None:
            self.checkhold_reason = m.get('CheckholdReason')
        self.rule_detail_url_list = []
        if m.get('RuleDetailUrlList') is not None:
            for k in m.get('RuleDetailUrlList'):
                temp_model = SafeChangeCheckResponseBodyDataRuleDetailUrlList()
                self.rule_detail_url_list.append(temp_model.from_map(k))
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class SafeChangeCheckResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SafeChangeCheckResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SafeChangeCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SafeChangeCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SafeChangeCheckResponseBody = None,
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
            temp_model = SafeChangeCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SafeChangeEndRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        change_end_time: int = None,
        change_result: str = None,
        cur_batch_no: int = None,
        executor_emp_id: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
        total_batch_no: int = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.change_end_time = change_end_time
        self.change_result = change_result
        self.cur_batch_no = cur_batch_no
        self.executor_emp_id = executor_emp_id
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id
        self.total_batch_no = total_batch_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_result is not None:
            result['ChangeResult'] = self.change_result
        if self.cur_batch_no is not None:
            result['CurBatchNo'] = self.cur_batch_no
        if self.executor_emp_id is not None:
            result['ExecutorEmpId'] = self.executor_emp_id
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.total_batch_no is not None:
            result['TotalBatchNo'] = self.total_batch_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeResult') is not None:
            self.change_result = m.get('ChangeResult')
        if m.get('CurBatchNo') is not None:
            self.cur_batch_no = m.get('CurBatchNo')
        if m.get('ExecutorEmpId') is not None:
            self.executor_emp_id = m.get('ExecutorEmpId')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('TotalBatchNo') is not None:
            self.total_batch_no = m.get('TotalBatchNo')
        return self


class SafeChangeEndResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SafeChangeEndResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SafeChangeEndResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SafeChangeEndResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SafeChangeEndResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SafeChangeEndResponseBody = None,
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
            temp_model = SafeChangeEndResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SafeChangeQueryRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        need_validate: bool = None,
        query_type: str = None,
        req_timestamp: int = None,
        return_type: bool = None,
        source_order_id: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.need_validate = need_validate
        self.query_type = query_type
        self.req_timestamp = req_timestamp
        self.return_type = return_type
        self.source_order_id = source_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.need_validate is not None:
            result['NeedValidate'] = self.need_validate
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.return_type is not None:
            result['ReturnType'] = self.return_type
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('NeedValidate') is not None:
            self.need_validate = m.get('NeedValidate')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class SafeChangeQueryResponseBodyDataChangeTimes(TeaModel):
    def __init__(
        self,
        change_end_time: int = None,
        change_start_time: int = None,
    ):
        self.change_end_time = change_end_time
        self.change_start_time = change_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        return self


class SafeChangeQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        approve_result_url: str = None,
        approve_status: str = None,
        change_cancel: str = None,
        change_end_time: int = None,
        change_object: str = None,
        change_opt_type: str = None,
        change_result: str = None,
        change_start_time: int = None,
        change_status: str = None,
        change_system: str = None,
        change_times: List[SafeChangeQueryResponseBodyDataChangeTimes] = None,
        change_title: str = None,
        check_result_url: str = None,
        check_status: str = None,
        checkhold_reason: List[str] = None,
        executor_emp_id: str = None,
        executor_emp_name: str = None,
        source_order_id: str = None,
    ):
        self.approve_result_url = approve_result_url
        self.approve_status = approve_status
        self.change_cancel = change_cancel
        self.change_end_time = change_end_time
        self.change_object = change_object
        self.change_opt_type = change_opt_type
        self.change_result = change_result
        self.change_start_time = change_start_time
        self.change_status = change_status
        self.change_system = change_system
        self.change_times = change_times
        self.change_title = change_title
        self.check_result_url = check_result_url
        self.check_status = check_status
        self.checkhold_reason = checkhold_reason
        self.executor_emp_id = executor_emp_id
        self.executor_emp_name = executor_emp_name
        self.source_order_id = source_order_id

    def validate(self):
        if self.change_times:
            for k in self.change_times:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_result_url is not None:
            result['ApproveResultUrl'] = self.approve_result_url
        if self.approve_status is not None:
            result['ApproveStatus'] = self.approve_status
        if self.change_cancel is not None:
            result['ChangeCancel'] = self.change_cancel
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_object is not None:
            result['ChangeObject'] = self.change_object
        if self.change_opt_type is not None:
            result['ChangeOptType'] = self.change_opt_type
        if self.change_result is not None:
            result['ChangeResult'] = self.change_result
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_status is not None:
            result['ChangeStatus'] = self.change_status
        if self.change_system is not None:
            result['ChangeSystem'] = self.change_system
        result['ChangeTimes'] = []
        if self.change_times is not None:
            for k in self.change_times:
                result['ChangeTimes'].append(k.to_map() if k else None)
        if self.change_title is not None:
            result['ChangeTitle'] = self.change_title
        if self.check_result_url is not None:
            result['CheckResultUrl'] = self.check_result_url
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.checkhold_reason is not None:
            result['CheckholdReason'] = self.checkhold_reason
        if self.executor_emp_id is not None:
            result['ExecutorEmpId'] = self.executor_emp_id
        if self.executor_emp_name is not None:
            result['ExecutorEmpName'] = self.executor_emp_name
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveResultUrl') is not None:
            self.approve_result_url = m.get('ApproveResultUrl')
        if m.get('ApproveStatus') is not None:
            self.approve_status = m.get('ApproveStatus')
        if m.get('ChangeCancel') is not None:
            self.change_cancel = m.get('ChangeCancel')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeObject') is not None:
            self.change_object = m.get('ChangeObject')
        if m.get('ChangeOptType') is not None:
            self.change_opt_type = m.get('ChangeOptType')
        if m.get('ChangeResult') is not None:
            self.change_result = m.get('ChangeResult')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeStatus') is not None:
            self.change_status = m.get('ChangeStatus')
        if m.get('ChangeSystem') is not None:
            self.change_system = m.get('ChangeSystem')
        self.change_times = []
        if m.get('ChangeTimes') is not None:
            for k in m.get('ChangeTimes'):
                temp_model = SafeChangeQueryResponseBodyDataChangeTimes()
                self.change_times.append(temp_model.from_map(k))
        if m.get('ChangeTitle') is not None:
            self.change_title = m.get('ChangeTitle')
        if m.get('CheckResultUrl') is not None:
            self.check_result_url = m.get('CheckResultUrl')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckholdReason') is not None:
            self.checkhold_reason = m.get('CheckholdReason')
        if m.get('ExecutorEmpId') is not None:
            self.executor_emp_id = m.get('ExecutorEmpId')
        if m.get('ExecutorEmpName') is not None:
            self.executor_emp_name = m.get('ExecutorEmpName')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class SafeChangeQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SafeChangeQueryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SafeChangeQueryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SafeChangeQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SafeChangeQueryResponseBody = None,
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
            temp_model = SafeChangeQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SafeChangeQueryApproveFlowRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
        stage: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id
        self.stage = stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.stage is not None:
            result['Stage'] = self.stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        return self


class SafeChangeQueryApproveFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        approve_strategy: str = None,
        approver: str = None,
        node_name: str = None,
        node_status: str = None,
    ):
        self.approve_strategy = approve_strategy
        self.approver = approver
        self.node_name = node_name
        self.node_status = node_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_strategy is not None:
            result['ApproveStrategy'] = self.approve_strategy
        if self.approver is not None:
            result['Approver'] = self.approver
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveStrategy') is not None:
            self.approve_strategy = m.get('ApproveStrategy')
        if m.get('Approver') is not None:
            self.approver = m.get('Approver')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        return self


class SafeChangeQueryApproveFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[SafeChangeQueryApproveFlowResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SafeChangeQueryApproveFlowResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SafeChangeQueryApproveFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SafeChangeQueryApproveFlowResponseBody = None,
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
            temp_model = SafeChangeQueryApproveFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SafeChangeStartRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        change_end_time: int = None,
        change_object: str = None,
        change_opt_type: str = None,
        change_start_time: int = None,
        change_title: str = None,
        creator_emp_id: str = None,
        cur_batch_no: int = None,
        executor_emp_id: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
        total_batch_no: int = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.change_end_time = change_end_time
        self.change_object = change_object
        self.change_opt_type = change_opt_type
        self.change_start_time = change_start_time
        self.change_title = change_title
        self.creator_emp_id = creator_emp_id
        self.cur_batch_no = cur_batch_no
        self.executor_emp_id = executor_emp_id
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id
        self.total_batch_no = total_batch_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time
        if self.change_object is not None:
            result['ChangeObject'] = self.change_object
        if self.change_opt_type is not None:
            result['ChangeOptType'] = self.change_opt_type
        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time
        if self.change_title is not None:
            result['ChangeTitle'] = self.change_title
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        if self.cur_batch_no is not None:
            result['CurBatchNo'] = self.cur_batch_no
        if self.executor_emp_id is not None:
            result['ExecutorEmpId'] = self.executor_emp_id
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        if self.total_batch_no is not None:
            result['TotalBatchNo'] = self.total_batch_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')
        if m.get('ChangeObject') is not None:
            self.change_object = m.get('ChangeObject')
        if m.get('ChangeOptType') is not None:
            self.change_opt_type = m.get('ChangeOptType')
        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')
        if m.get('ChangeTitle') is not None:
            self.change_title = m.get('ChangeTitle')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        if m.get('CurBatchNo') is not None:
            self.cur_batch_no = m.get('CurBatchNo')
        if m.get('ExecutorEmpId') is not None:
            self.executor_emp_id = m.get('ExecutorEmpId')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        if m.get('TotalBatchNo') is not None:
            self.total_batch_no = m.get('TotalBatchNo')
        return self


class SafeChangeStartResponseBodyData(TeaModel):
    def __init__(
        self,
        approve_result_url: str = None,
        check_result_url: str = None,
        status: str = None,
        sub_satus: str = None,
    ):
        self.approve_result_url = approve_result_url
        self.check_result_url = check_result_url
        self.status = status
        self.sub_satus = sub_satus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_result_url is not None:
            result['ApproveResultUrl'] = self.approve_result_url
        if self.check_result_url is not None:
            result['CheckResultUrl'] = self.check_result_url
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_satus is not None:
            result['SubSatus'] = self.sub_satus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveResultUrl') is not None:
            self.approve_result_url = m.get('ApproveResultUrl')
        if m.get('CheckResultUrl') is not None:
            self.check_result_url = m.get('CheckResultUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubSatus') is not None:
            self.sub_satus = m.get('SubSatus')
        return self


class SafeChangeStartResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SafeChangeStartResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SafeChangeStartResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SafeChangeStartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SafeChangeStartResponseBody = None,
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
            temp_model = SafeChangeStartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SafeChangeStartApproveRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        creator_emp_id: str = None,
        extra_info: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.creator_emp_id = creator_emp_id
        self.extra_info = extra_info
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class SafeChangeStartApproveResponseBodyData(TeaModel):
    def __init__(
        self,
        approve_status: str = None,
    ):
        self.approve_status = approve_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_status is not None:
            result['ApproveStatus'] = self.approve_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveStatus') is not None:
            self.approve_status = m.get('ApproveStatus')
        return self


class SafeChangeStartApproveResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SafeChangeStartApproveResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SafeChangeStartApproveResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SafeChangeStartApproveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SafeChangeStartApproveResponseBody = None,
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
            temp_model = SafeChangeStartApproveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SafeScopeDataRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        category: str = None,
        code_list: str = None,
        factor: str = None,
        group_by: str = None,
        id_list: str = None,
        item: str = None,
        limit: int = None,
        need_total_count: bool = None,
        order_by: str = None,
        order_direction: str = None,
        page: int = None,
        parent_code: str = None,
        parent_id: int = None,
        product_code: str = None,
        product_id: int = None,
        region_name_en: str = None,
        req_timestamp: int = None,
        search_value: str = None,
        type: int = None,
        uid: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.category = category
        self.code_list = code_list
        self.factor = factor
        self.group_by = group_by
        self.id_list = id_list
        self.item = item
        self.limit = limit
        self.need_total_count = need_total_count
        self.order_by = order_by
        self.order_direction = order_direction
        self.page = page
        self.parent_code = parent_code
        self.parent_id = parent_id
        self.product_code = product_code
        self.product_id = product_id
        self.region_name_en = region_name_en
        self.req_timestamp = req_timestamp
        self.search_value = search_value
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.category is not None:
            result['Category'] = self.category
        if self.code_list is not None:
            result['CodeList'] = self.code_list
        if self.factor is not None:
            result['Factor'] = self.factor
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.id_list is not None:
            result['IdList'] = self.id_list
        if self.item is not None:
            result['Item'] = self.item
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.need_total_count is not None:
            result['NeedTotalCount'] = self.need_total_count
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction
        if self.page is not None:
            result['Page'] = self.page
        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_name_en is not None:
            result['RegionNameEn'] = self.region_name_en
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CodeList') is not None:
            self.code_list = m.get('CodeList')
        if m.get('Factor') is not None:
            self.factor = m.get('Factor')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NeedTotalCount') is not None:
            self.need_total_count = m.get('NeedTotalCount')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionNameEn') is not None:
            self.region_name_en = m.get('RegionNameEn')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SafeScopeDataResponseBodyDataPagination(TeaModel):
    def __init__(
        self,
        limit: int = None,
        page: int = None,
    ):
        self.limit = limit
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class SafeScopeDataResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[Any] = None,
        extra_info: Dict[str, str] = None,
        pagination: SafeScopeDataResponseBodyDataPagination = None,
        total: int = None,
    ):
        self.data = data
        self.extra_info = extra_info
        self.pagination = pagination
        self.total = total

    def validate(self):
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Pagination') is not None:
            temp_model = SafeScopeDataResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SafeScopeDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SafeScopeDataResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SafeScopeDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SafeScopeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SafeScopeDataResponseBody = None,
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
            temp_model = SafeScopeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartApproveRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        creator_emp_id: str = None,
        extra_info: str = None,
        req_timestamp: int = None,
        source_order_id: str = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.creator_emp_id = creator_emp_id
        self.extra_info = extra_info
        self.req_timestamp = req_timestamp
        self.source_order_id = source_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.creator_emp_id is not None:
            result['CreatorEmpId'] = self.creator_emp_id
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        if self.source_order_id is not None:
            result['SourceOrderId'] = self.source_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('CreatorEmpId') is not None:
            self.creator_emp_id = m.get('CreatorEmpId')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        if m.get('SourceOrderId') is not None:
            self.source_order_id = m.get('SourceOrderId')
        return self


class StartApproveResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartApproveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartApproveResponseBody = None,
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
            temp_model = StartApproveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncProductRequestSyncProductListInnerProductList(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SyncProductRequestSyncProductList(TeaModel):
    def __init__(
        self,
        code: str = None,
        inner_product_list: List[SyncProductRequestSyncProductListInnerProductList] = None,
        name: str = None,
    ):
        self.code = code
        self.inner_product_list = inner_product_list
        self.name = name

    def validate(self):
        if self.inner_product_list:
            for k in self.inner_product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['InnerProductList'] = []
        if self.inner_product_list is not None:
            for k in self.inner_product_list:
                result['InnerProductList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.inner_product_list = []
        if m.get('InnerProductList') is not None:
            for k in m.get('InnerProductList'):
                temp_model = SyncProductRequestSyncProductListInnerProductList()
                self.inner_product_list.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SyncProductRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_sign: str = None,
        req_timestamp: int = None,
        sync_product_list: List[SyncProductRequestSyncProductList] = None,
    ):
        self.auth_key = auth_key
        self.auth_sign = auth_sign
        self.req_timestamp = req_timestamp
        self.sync_product_list = sync_product_list

    def validate(self):
        if self.sync_product_list:
            for k in self.sync_product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_sign is not None:
            result['AuthSign'] = self.auth_sign
        if self.req_timestamp is not None:
            result['ReqTimestamp'] = self.req_timestamp
        result['SyncProductList'] = []
        if self.sync_product_list is not None:
            for k in self.sync_product_list:
                result['SyncProductList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSign') is not None:
            self.auth_sign = m.get('AuthSign')
        if m.get('ReqTimestamp') is not None:
            self.req_timestamp = m.get('ReqTimestamp')
        self.sync_product_list = []
        if m.get('SyncProductList') is not None:
            for k in m.get('SyncProductList'):
                temp_model = SyncProductRequestSyncProductList()
                self.sync_product_list.append(temp_model.from_map(k))
        return self


class SyncProductResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncProductResponseBody = None,
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
            temp_model = SyncProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


