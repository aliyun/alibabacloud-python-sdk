# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ChangeApplicationInfoRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: str = None,
        app_name: str = None,
        app_type_list: str = None,
        apping_list: str = None,
        item_code: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_id = app_id
        self.app_name = app_name
        self.app_type_list = app_type_list
        self.apping_list = apping_list
        self.item_code = item_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type_list is not None:
            result['AppTypeList'] = self.app_type_list
        if self.apping_list is not None:
            result['AppingList'] = self.apping_list
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTypeList') is not None:
            self.app_type_list = m.get('AppTypeList')
        if m.get('AppingList') is not None:
            self.apping_list = m.get('AppingList')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class ChangeApplicationInfoResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_id = app_id
        self.code = code
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeApplicationInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeApplicationInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ChangeApplicationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChargeFlowRequest(TeaModel):
    def __init__(
        self,
        channel_code: str = None,
        instance_id: str = None,
        item_code: str = None,
        mobile: str = None,
        order_time: str = None,
        out_biz_no: str = None,
        uid: int = None,
    ):
        self.channel_code = channel_code
        self.instance_id = instance_id
        self.item_code = item_code
        self.mobile = mobile
        self.order_time = order_time
        self.out_biz_no = out_biz_no
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.order_time is not None:
            result['OrderTime'] = self.order_time
        if self.out_biz_no is not None:
            result['OutBizNo'] = self.out_biz_no
        if self.uid is not None:
            result['UId'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OrderTime') is not None:
            self.order_time = m.get('OrderTime')
        if m.get('OutBizNo') is not None:
            self.out_biz_no = m.get('OutBizNo')
        if m.get('UId') is not None:
            self.uid = m.get('UId')
        return self


class ChargeFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        customer_flow_order_id: str = None,
        customer_flow_request_id: str = None,
        status: str = None,
    ):
        self.biz_code = biz_code
        self.customer_flow_order_id = customer_flow_order_id
        self.customer_flow_request_id = customer_flow_request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ChargeFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ChargeFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChargeFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChargeFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChargeFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ChargeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationInfoRequestAppingList(TeaModel):
    def __init__(
        self,
        ext_id: int = None,
        flow_ip: List[str] = None,
        flow_url: List[str] = None,
        original_ip_list: List[str] = None,
        original_url_list: List[str] = None,
    ):
        self.ext_id = ext_id
        self.flow_ip = flow_ip
        self.flow_url = flow_url
        self.original_ip_list = original_ip_list
        self.original_url_list = original_url_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id is not None:
            result['ExtId'] = self.ext_id
        if self.flow_ip is not None:
            result['FlowIp'] = self.flow_ip
        if self.flow_url is not None:
            result['FlowUrl'] = self.flow_url
        if self.original_ip_list is not None:
            result['OriginalIpList'] = self.original_ip_list
        if self.original_url_list is not None:
            result['OriginalUrlList'] = self.original_url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtId') is not None:
            self.ext_id = m.get('ExtId')
        if m.get('FlowIp') is not None:
            self.flow_ip = m.get('FlowIp')
        if m.get('FlowUrl') is not None:
            self.flow_url = m.get('FlowUrl')
        if m.get('OriginalIpList') is not None:
            self.original_ip_list = m.get('OriginalIpList')
        if m.get('OriginalUrlList') is not None:
            self.original_url_list = m.get('OriginalUrlList')
        return self


class CreateApplicationInfoRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_name: str = None,
        app_type_list: List[str] = None,
        apping_list: List[CreateApplicationInfoRequestAppingList] = None,
        item_code: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_name = app_name
        self.app_type_list = app_type_list
        self.apping_list = apping_list
        self.item_code = item_code

    def validate(self):
        if self.apping_list:
            for k in self.apping_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type_list is not None:
            result['AppTypeList'] = self.app_type_list
        result['AppingList'] = []
        if self.apping_list is not None:
            for k in self.apping_list:
                result['AppingList'].append(k.to_map() if k else None)
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTypeList') is not None:
            self.app_type_list = m.get('AppTypeList')
        self.apping_list = []
        if m.get('AppingList') is not None:
            for k in m.get('AppingList'):
                temp_model = CreateApplicationInfoRequestAppingList()
                self.apping_list.append(temp_model.from_map(k))
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class CreateApplicationInfoResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_id = app_id
        self.code = code
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateApplicationInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApplicationInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateApplicationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAliyunXgipTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAliyunXgipTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAliyunXgipTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetAliyunXgipTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_code: str = None,
        item_code: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_code = app_code
        self.item_code = item_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeFlowInstanceRequest(TeaModel):
    def __init__(
        self,
        aliuid: int = None,
        app_id: str = None,
        instance_id: str = None,
        item_code: str = None,
    ):
        self.aliuid = aliuid
        self.app_id = app_id
        self.instance_id = instance_id
        self.item_code = item_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class GetFreeFlowInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        end_time: str = None,
        instance_memo: str = None,
        instance_status: str = None,
        open_time: str = None,
        spec_type: str = None,
        start_time: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.end_time = end_time
        self.instance_memo = instance_memo
        self.instance_status = instance_status
        self.open_time = open_time
        self.spec_type = spec_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_memo is not None:
            result['InstanceMemo'] = self.instance_memo
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceMemo') is not None:
            self.instance_memo = m.get('InstanceMemo')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetFreeFlowInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetFreeFlowInstanceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
                temp_model = GetFreeFlowInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFreeFlowInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFreeFlowInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFreeFlowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeFlowProductListRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        instance_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetFreeFlowProductListResponseBodyData(TeaModel):
    def __init__(
        self,
        configured: bool = None,
        flow_product_amount: str = None,
        flow_product_id: str = None,
        flow_product_name: str = None,
        flow_product_period: str = None,
        flow_type: str = None,
        operator: str = None,
        spec_type: str = None,
        spid: str = None,
        unit_price: int = None,
    ):
        self.configured = configured
        self.flow_product_amount = flow_product_amount
        self.flow_product_id = flow_product_id
        self.flow_product_name = flow_product_name
        self.flow_product_period = flow_product_period
        self.flow_type = flow_type
        self.operator = operator
        self.spec_type = spec_type
        self.spid = spid
        self.unit_price = unit_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configured is not None:
            result['Configured'] = self.configured
        if self.flow_product_amount is not None:
            result['FlowProductAmount'] = self.flow_product_amount
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.flow_product_name is not None:
            result['FlowProductName'] = self.flow_product_name
        if self.flow_product_period is not None:
            result['FlowProductPeriod'] = self.flow_product_period
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.spid is not None:
            result['Spid'] = self.spid
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configured') is not None:
            self.configured = m.get('Configured')
        if m.get('FlowProductAmount') is not None:
            self.flow_product_amount = m.get('FlowProductAmount')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('FlowProductName') is not None:
            self.flow_product_name = m.get('FlowProductName')
        if m.get('FlowProductPeriod') is not None:
            self.flow_product_period = m.get('FlowProductPeriod')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('Spid') is not None:
            self.spid = m.get('Spid')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        return self


class GetFreeFlowProductListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetFreeFlowProductListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
                temp_model = GetFreeFlowProductListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFreeFlowProductListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFreeFlowProductListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFreeFlowProductListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeFlowUsageRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        cur_page_num: int = None,
        instance_id: str = None,
        month: str = None,
        num_per_page: int = None,
    ):
        self.ali_uid = ali_uid
        self.cur_page_num = cur_page_num
        self.instance_id = instance_id
        self.month = month
        self.num_per_page = num_per_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        return self


class GetFreeFlowUsageResponseBodyDataCustomerList(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        customer_end_time: str = None,
        customer_flow_order_id: str = None,
        customer_flow_status: str = None,
        customer_open_time: str = None,
        customer_start_time: str = None,
        flow_product_id: str = None,
        flow_product_name: str = None,
        is_lasting: bool = None,
        mobile_number: str = None,
        unit_num: int = None,
        unit_price: int = None,
    ):
        self.channel_id = channel_id
        self.customer_end_time = customer_end_time
        self.customer_flow_order_id = customer_flow_order_id
        self.customer_flow_status = customer_flow_status
        self.customer_open_time = customer_open_time
        self.customer_start_time = customer_start_time
        self.flow_product_id = flow_product_id
        self.flow_product_name = flow_product_name
        self.is_lasting = is_lasting
        self.mobile_number = mobile_number
        self.unit_num = unit_num
        self.unit_price = unit_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.customer_end_time is not None:
            result['CustomerEndTime'] = self.customer_end_time
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_status is not None:
            result['CustomerFlowStatus'] = self.customer_flow_status
        if self.customer_open_time is not None:
            result['CustomerOpenTime'] = self.customer_open_time
        if self.customer_start_time is not None:
            result['CustomerStartTime'] = self.customer_start_time
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.flow_product_name is not None:
            result['FlowProductName'] = self.flow_product_name
        if self.is_lasting is not None:
            result['IsLasting'] = self.is_lasting
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CustomerEndTime') is not None:
            self.customer_end_time = m.get('CustomerEndTime')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowStatus') is not None:
            self.customer_flow_status = m.get('CustomerFlowStatus')
        if m.get('CustomerOpenTime') is not None:
            self.customer_open_time = m.get('CustomerOpenTime')
        if m.get('CustomerStartTime') is not None:
            self.customer_start_time = m.get('CustomerStartTime')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('FlowProductName') is not None:
            self.flow_product_name = m.get('FlowProductName')
        if m.get('IsLasting') is not None:
            self.is_lasting = m.get('IsLasting')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        return self


class GetFreeFlowUsageResponseBodyData(TeaModel):
    def __init__(
        self,
        cur_page_num: int = None,
        customer_list: List[GetFreeFlowUsageResponseBodyDataCustomerList] = None,
        has_next: bool = None,
        has_prev: bool = None,
        instance_id: str = None,
        num_per_page: int = None,
        total_num: int = None,
        total_page_num: int = None,
    ):
        self.cur_page_num = cur_page_num
        self.customer_list = customer_list
        self.has_next = has_next
        self.has_prev = has_prev
        self.instance_id = instance_id
        self.num_per_page = num_per_page
        self.total_num = total_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.customer_list:
            for k in self.customer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        result['CustomerList'] = []
        if self.customer_list is not None:
            for k in self.customer_list:
                result['CustomerList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.has_prev is not None:
            result['HasPrev'] = self.has_prev
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        self.customer_list = []
        if m.get('CustomerList') is not None:
            for k in m.get('CustomerList'):
                temp_model = GetFreeFlowUsageResponseBodyDataCustomerList()
                self.customer_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('HasPrev') is not None:
            self.has_prev = m.get('HasPrev')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class GetFreeFlowUsageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetFreeFlowUsageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFreeFlowUsageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFreeFlowUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFreeFlowUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFreeFlowUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeFlowUsageStatisticRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: str = None,
        app_name: str = None,
        instance_id: str = None,
        month: int = None,
    ):
        self.ali_uid = ali_uid
        self.app_id = app_id
        self.app_name = app_name
        self.instance_id = instance_id
        self.month = month

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        return self


class GetFreeFlowUsageStatisticResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        spec_type: str = None,
        total_money: str = None,
        total_order_number: int = None,
        total_unit_number: int = None,
        yun_out_product: str = None,
    ):
        self.instance_id = instance_id
        self.spec_type = spec_type
        self.total_money = total_money
        self.total_order_number = total_order_number
        self.total_unit_number = total_unit_number
        self.yun_out_product = yun_out_product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.total_money is not None:
            result['TotalMoney'] = self.total_money
        if self.total_order_number is not None:
            result['TotalOrderNumber'] = self.total_order_number
        if self.total_unit_number is not None:
            result['TotalUnitNumber'] = self.total_unit_number
        if self.yun_out_product is not None:
            result['YunOutProduct'] = self.yun_out_product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('TotalMoney') is not None:
            self.total_money = m.get('TotalMoney')
        if m.get('TotalOrderNumber') is not None:
            self.total_order_number = m.get('TotalOrderNumber')
        if m.get('TotalUnitNumber') is not None:
            self.total_unit_number = m.get('TotalUnitNumber')
        if m.get('YunOutProduct') is not None:
            self.yun_out_product = m.get('YunOutProduct')
        return self


class GetFreeFlowUsageStatisticResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetFreeFlowUsageStatisticResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
                temp_model = GetFreeFlowUsageStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFreeFlowUsageStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFreeFlowUsageStatisticResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFreeFlowUsageStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInventoryInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        item_code: str = None,
        mobile: str = None,
        uid: int = None,
    ):
        self.instance_id = instance_id
        self.item_code = item_code
        self.mobile = mobile
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.uid is not None:
            result['UId'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('UId') is not None:
            self.uid = m.get('UId')
        return self


class GetInventoryInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        inventory: int = None,
        residual_inventory: int = None,
        used_stock: int = None,
    ):
        self.inventory = inventory
        self.residual_inventory = residual_inventory
        self.used_stock = used_stock

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory is not None:
            result['Inventory'] = self.inventory
        if self.residual_inventory is not None:
            result['ResidualInventory'] = self.residual_inventory
        if self.used_stock is not None:
            result['UsedStock'] = self.used_stock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Inventory') is not None:
            self.inventory = m.get('Inventory')
        if m.get('ResidualInventory') is not None:
            self.residual_inventory = m.get('ResidualInventory')
        if m.get('UsedStock') is not None:
            self.used_stock = m.get('UsedStock')
        return self


class GetInventoryInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInventoryInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetInventoryInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInventoryInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInventoryInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetInventoryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetItemInstListRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        instance_id: str = None,
        item_code: str = None,
        mobile: str = None,
        page_size: int = None,
        status: str = None,
        uid: int = None,
    ):
        self.current = current
        self.instance_id = instance_id
        self.item_code = item_code
        self.mobile = mobile
        self.page_size = page_size
        self.status = status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.uid is not None:
            result['UId'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UId') is not None:
            self.uid = m.get('UId')
        return self


class GetItemInstListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        instance_id: str = None,
        product_id: str = None,
        product_name: str = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.product_id = product_id
        self.product_name = product_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetItemInstListResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current = current
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetItemInstListResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[GetItemInstListResponseBodyDataList] = None,
        page_info: GetItemInstListResponseBodyDataPageInfo = None,
    ):
        self.list = list
        self.page_info = page_info

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetItemInstListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = GetItemInstListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        return self


class GetItemInstListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetItemInstListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetItemInstListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetItemInstListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetItemInstListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetItemInstListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetItemListRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        biz_code: str = None,
    ):
        self.ali_uid = ali_uid
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        return self


class GetItemListResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_type: str = None,
        item_buy_url: str = None,
        item_code: str = None,
        item_name: str = None,
        name: str = None,
    ):
        self.biz_code = biz_code
        self.biz_type = biz_type
        self.item_buy_url = item_buy_url
        self.item_code = item_code
        self.item_name = item_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.item_buy_url is not None:
            result['ItemBuyUrl'] = self.item_buy_url
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ItemBuyUrl') is not None:
            self.item_buy_url = m.get('ItemBuyUrl')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetItemListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetItemListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
                temp_model = GetItemListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetItemListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetItemListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderFreeFlowProductStatusRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        customer_flow_order_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.customer_flow_order_id = customer_flow_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        return self


class GetOrderFreeFlowProductStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        customer_flow_order_id: str = None,
        customer_flow_request_id: str = None,
        error: str = None,
        status: str = None,
    ):
        self.customer_flow_order_id = customer_flow_order_id
        self.customer_flow_request_id = customer_flow_request_id
        self.error = error
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.error is not None:
            result['Error'] = self.error
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetOrderFreeFlowProductStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetOrderFreeFlowProductStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetOrderFreeFlowProductStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderFreeFlowProductStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrderFreeFlowProductStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetOrderFreeFlowProductStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderItemListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderItemListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrderItemListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetOrderItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQosFlowUsageRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        cur_page_num: int = None,
        end_time: str = None,
        instance_id: str = None,
        month: int = None,
        num_per_page: int = None,
        start_time: str = None,
        type: bool = None,
    ):
        self.ali_uid = ali_uid
        self.cur_page_num = cur_page_num
        self.end_time = end_time
        self.instance_id = instance_id
        self.month = month
        self.num_per_page = num_per_page
        self.start_time = start_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetQosFlowUsageResponseBodyDataCustomerList(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: str = None,
        ds_day: int = None,
        ds_month: int = None,
        end_time: str = None,
        instance_id: str = None,
        item_code: str = None,
        message: str = None,
        name: str = None,
        operator: str = None,
        order_num: int = None,
        product_id: str = None,
        product_name: str = None,
        provice: str = None,
        qos_request_id: str = None,
        remark: str = None,
        spec_type: str = None,
        start_time: str = None,
        status: str = None,
        total_price: int = None,
        totol_time: int = None,
    ):
        self.ali_uid = ali_uid
        self.app_id = app_id
        self.ds_day = ds_day
        self.ds_month = ds_month
        self.end_time = end_time
        self.instance_id = instance_id
        self.item_code = item_code
        self.message = message
        self.name = name
        self.operator = operator
        self.order_num = order_num
        self.product_id = product_id
        self.product_name = product_name
        self.provice = provice
        self.qos_request_id = qos_request_id
        self.remark = remark
        self.spec_type = spec_type
        self.start_time = start_time
        self.status = status
        self.total_price = total_price
        self.totol_time = totol_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ds_day is not None:
            result['DsDay'] = self.ds_day
        if self.ds_month is not None:
            result['DsMonth'] = self.ds_month
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.provice is not None:
            result['Provice'] = self.provice
        if self.qos_request_id is not None:
            result['QosRequestId'] = self.qos_request_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.totol_time is not None:
            result['TotolTime'] = self.totol_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DsDay') is not None:
            self.ds_day = m.get('DsDay')
        if m.get('DsMonth') is not None:
            self.ds_month = m.get('DsMonth')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Provice') is not None:
            self.provice = m.get('Provice')
        if m.get('QosRequestId') is not None:
            self.qos_request_id = m.get('QosRequestId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('TotolTime') is not None:
            self.totol_time = m.get('TotolTime')
        return self


class GetQosFlowUsageResponseBodyData(TeaModel):
    def __init__(
        self,
        cur_page_num: int = None,
        customer_list: List[GetQosFlowUsageResponseBodyDataCustomerList] = None,
        has_next: bool = None,
        has_prev: bool = None,
        instance_id: str = None,
        num_per_page: int = None,
        total_num: int = None,
        total_page_num: int = None,
    ):
        self.cur_page_num = cur_page_num
        self.customer_list = customer_list
        self.has_next = has_next
        self.has_prev = has_prev
        self.instance_id = instance_id
        self.num_per_page = num_per_page
        self.total_num = total_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.customer_list:
            for k in self.customer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        result['CustomerList'] = []
        if self.customer_list is not None:
            for k in self.customer_list:
                result['CustomerList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.has_prev is not None:
            result['HasPrev'] = self.has_prev
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        self.customer_list = []
        if m.get('CustomerList') is not None:
            for k in m.get('CustomerList'):
                temp_model = GetQosFlowUsageResponseBodyDataCustomerList()
                self.customer_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('HasPrev') is not None:
            self.has_prev = m.get('HasPrev')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class GetQosFlowUsageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQosFlowUsageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetQosFlowUsageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQosFlowUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQosFlowUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetQosFlowUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQosUsageStatisticRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        cur_page_num: int = None,
        end_time: str = None,
        instance_id: str = None,
        month: int = None,
        num_per_page: int = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.ali_uid = ali_uid
        self.cur_page_num = cur_page_num
        self.end_time = end_time
        self.instance_id = instance_id
        self.month = month
        self.num_per_page = num_per_page
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetQosUsageStatisticResponseBodyDataGetQosUsageStatisticResList(TeaModel):
    def __init__(
        self,
        bill_count: int = None,
        ds_day: int = None,
        fail_count: int = None,
        instance_id: str = None,
        month: int = None,
        operator: str = None,
        product_name: str = None,
        provice: str = None,
        spec_type: str = None,
        sucess_count: int = None,
        total_count: int = None,
        yun_out_product: str = None,
    ):
        self.bill_count = bill_count
        self.ds_day = ds_day
        self.fail_count = fail_count
        self.instance_id = instance_id
        self.month = month
        self.operator = operator
        self.product_name = product_name
        self.provice = provice
        self.spec_type = spec_type
        self.sucess_count = sucess_count
        self.total_count = total_count
        self.yun_out_product = yun_out_product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_count is not None:
            result['BillCount'] = self.bill_count
        if self.ds_day is not None:
            result['DsDay'] = self.ds_day
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.provice is not None:
            result['Provice'] = self.provice
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.sucess_count is not None:
            result['SucessCount'] = self.sucess_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.yun_out_product is not None:
            result['YunOutProduct'] = self.yun_out_product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillCount') is not None:
            self.bill_count = m.get('BillCount')
        if m.get('DsDay') is not None:
            self.ds_day = m.get('DsDay')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Provice') is not None:
            self.provice = m.get('Provice')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('SucessCount') is not None:
            self.sucess_count = m.get('SucessCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('YunOutProduct') is not None:
            self.yun_out_product = m.get('YunOutProduct')
        return self


class GetQosUsageStatisticResponseBodyData(TeaModel):
    def __init__(
        self,
        cur_page_num: int = None,
        get_qos_usage_statistic_res_list: List[GetQosUsageStatisticResponseBodyDataGetQosUsageStatisticResList] = None,
        num_per_page: int = None,
        total_num: int = None,
    ):
        self.cur_page_num = cur_page_num
        self.get_qos_usage_statistic_res_list = get_qos_usage_statistic_res_list
        self.num_per_page = num_per_page
        self.total_num = total_num

    def validate(self):
        if self.get_qos_usage_statistic_res_list:
            for k in self.get_qos_usage_statistic_res_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        result['GetQosUsageStatisticResList'] = []
        if self.get_qos_usage_statistic_res_list is not None:
            for k in self.get_qos_usage_statistic_res_list:
                result['GetQosUsageStatisticResList'].append(k.to_map() if k else None)
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        self.get_qos_usage_statistic_res_list = []
        if m.get('GetQosUsageStatisticResList') is not None:
            for k in m.get('GetQosUsageStatisticResList'):
                temp_model = GetQosUsageStatisticResponseBodyDataGetQosUsageStatisticResList()
                self.get_qos_usage_statistic_res_list.append(temp_model.from_map(k))
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetQosUsageStatisticResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQosUsageStatisticResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetQosUsageStatisticResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQosUsageStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQosUsageStatisticResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetQosUsageStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUatDataListRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        ds_month: int = None,
        item_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.ds_month = ds_month
        self.item_id = item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.ds_month is not None:
            result['DsMonth'] = self.ds_month
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DsMonth') is not None:
            self.ds_month = m.get('DsMonth')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class GetUatDataListResponseBodyDataDsList(TeaModel):
    def __init__(
        self,
        ds_data: int = None,
        ds_day: int = None,
    ):
        self.ds_data = ds_data
        self.ds_day = ds_day

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ds_data is not None:
            result['DsData'] = self.ds_data
        if self.ds_day is not None:
            result['DsDay'] = self.ds_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsData') is not None:
            self.ds_data = m.get('DsData')
        if m.get('DsDay') is not None:
            self.ds_day = m.get('DsDay')
        return self


class GetUatDataListResponseBodyData(TeaModel):
    def __init__(
        self,
        ds_list: List[GetUatDataListResponseBodyDataDsList] = None,
        spec_type: str = None,
    ):
        self.ds_list = ds_list
        self.spec_type = spec_type

    def validate(self):
        if self.ds_list:
            for k in self.ds_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DsList'] = []
        if self.ds_list is not None:
            for k in self.ds_list:
                result['DsList'].append(k.to_map() if k else None)
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ds_list = []
        if m.get('DsList') is not None:
            for k in m.get('DsList'):
                temp_model = GetUatDataListResponseBodyDataDsList()
                self.ds_list.append(temp_model.from_map(k))
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        return self


class GetUatDataListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetUatDataListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
                temp_model = GetUatDataListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUatDataListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUatDataListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetUatDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUatSpecCtDataRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        ds_month: int = None,
        item_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.ds_month = ds_month
        self.item_id = item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.ds_month is not None:
            result['DsMonth'] = self.ds_month
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DsMonth') is not None:
            self.ds_month = m.get('DsMonth')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class GetUatSpecCtDataResponseBodyData(TeaModel):
    def __init__(
        self,
        month_count: int = None,
        spec_type: str = None,
    ):
        self.month_count = month_count
        self.spec_type = spec_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.month_count is not None:
            result['MonthCount'] = self.month_count
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonthCount') is not None:
            self.month_count = m.get('MonthCount')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        return self


class GetUatSpecCtDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetUatSpecCtDataResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
                temp_model = GetUatSpecCtDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUatSpecCtDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUatSpecCtDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetUatSpecCtDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MockGetOrderFreeFlowProductStatusRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        customer_flow_order_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.customer_flow_order_id = customer_flow_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        return self


class MockGetOrderFreeFlowProductStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        customer_flow_order_id: str = None,
        customer_flow_request_id: str = None,
        error: str = None,
        status: str = None,
    ):
        self.customer_flow_order_id = customer_flow_order_id
        self.customer_flow_request_id = customer_flow_request_id
        self.error = error
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.error is not None:
            result['Error'] = self.error
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class MockGetOrderFreeFlowProductStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: MockGetOrderFreeFlowProductStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = MockGetOrderFreeFlowProductStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MockGetOrderFreeFlowProductStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MockGetOrderFreeFlowProductStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = MockGetOrderFreeFlowProductStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MockOrderFreeFlowProductRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        channel_id: str = None,
        customer_flow_request_id: str = None,
        flow_product_id: str = None,
        instance_id: str = None,
        lasting: str = None,
        mobile_number: str = None,
        notify_url: str = None,
        operator: str = None,
        purchase_order_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.channel_id = channel_id
        self.customer_flow_request_id = customer_flow_request_id
        self.flow_product_id = flow_product_id
        self.instance_id = instance_id
        self.lasting = lasting
        self.mobile_number = mobile_number
        self.notify_url = notify_url
        self.operator = operator
        self.purchase_order_id = purchase_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lasting is not None:
            result['Lasting'] = self.lasting
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.purchase_order_id is not None:
            result['PurchaseOrderId'] = self.purchase_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lasting') is not None:
            self.lasting = m.get('Lasting')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PurchaseOrderId') is not None:
            self.purchase_order_id = m.get('PurchaseOrderId')
        return self


class MockOrderFreeFlowProductResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        customer_flow_order_id: str = None,
        customer_flow_request_id: str = None,
        status: str = None,
    ):
        self.biz_code = biz_code
        self.customer_flow_order_id = customer_flow_order_id
        self.customer_flow_request_id = customer_flow_request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class MockOrderFreeFlowProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: MockOrderFreeFlowProductResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = MockOrderFreeFlowProductResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MockOrderFreeFlowProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MockOrderFreeFlowProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = MockOrderFreeFlowProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApplicationRequestAppingList(TeaModel):
    def __init__(
        self,
        ext_id: int = None,
        flow_ip: List[str] = None,
        flow_url: List[str] = None,
        original_ip_list: List[str] = None,
        original_url_list: List[str] = None,
    ):
        self.ext_id = ext_id
        self.flow_ip = flow_ip
        self.flow_url = flow_url
        self.original_ip_list = original_ip_list
        self.original_url_list = original_url_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id is not None:
            result['ExtId'] = self.ext_id
        if self.flow_ip is not None:
            result['FlowIp'] = self.flow_ip
        if self.flow_url is not None:
            result['FlowUrl'] = self.flow_url
        if self.original_ip_list is not None:
            result['OriginalIpList'] = self.original_ip_list
        if self.original_url_list is not None:
            result['OriginalUrlList'] = self.original_url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtId') is not None:
            self.ext_id = m.get('ExtId')
        if m.get('FlowIp') is not None:
            self.flow_ip = m.get('FlowIp')
        if m.get('FlowUrl') is not None:
            self.flow_url = m.get('FlowUrl')
        if m.get('OriginalIpList') is not None:
            self.original_ip_list = m.get('OriginalIpList')
        if m.get('OriginalUrlList') is not None:
            self.original_url_list = m.get('OriginalUrlList')
        return self


class ModifyApplicationRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_code: str = None,
        app_name: str = None,
        app_type_list: List[str] = None,
        apping_list: List[ModifyApplicationRequestAppingList] = None,
    ):
        self.ali_uid = ali_uid
        self.app_code = app_code
        self.app_name = app_name
        self.app_type_list = app_type_list
        self.apping_list = apping_list

    def validate(self):
        if self.apping_list:
            for k in self.apping_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type_list is not None:
            result['AppTypeList'] = self.app_type_list
        result['AppingList'] = []
        if self.apping_list is not None:
            for k in self.apping_list:
                result['AppingList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTypeList') is not None:
            self.app_type_list = m.get('AppTypeList')
        self.apping_list = []
        if m.get('AppingList') is not None:
            for k in m.get('AppingList'):
                temp_model = ModifyApplicationRequestAppingList()
                self.apping_list.append(temp_model.from_map(k))
        return self


class ModifyApplicationResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_id = app_id
        self.code = code
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OrderFreeFlowProductRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        channel_id: str = None,
        customer_flow_request_id: str = None,
        flow_product_id: str = None,
        instance_id: str = None,
        lasting: str = None,
        mobile_number: str = None,
        notify_url: str = None,
        operator: str = None,
        purchase_order_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.channel_id = channel_id
        self.customer_flow_request_id = customer_flow_request_id
        self.flow_product_id = flow_product_id
        self.instance_id = instance_id
        self.lasting = lasting
        self.mobile_number = mobile_number
        self.notify_url = notify_url
        self.operator = operator
        self.purchase_order_id = purchase_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lasting is not None:
            result['Lasting'] = self.lasting
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.purchase_order_id is not None:
            result['PurchaseOrderId'] = self.purchase_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lasting') is not None:
            self.lasting = m.get('Lasting')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PurchaseOrderId') is not None:
            self.purchase_order_id = m.get('PurchaseOrderId')
        return self


class OrderFreeFlowProductResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        customer_flow_order_id: str = None,
        customer_flow_request_id: str = None,
        status: str = None,
    ):
        self.biz_code = biz_code
        self.customer_flow_order_id = customer_flow_order_id
        self.customer_flow_request_id = customer_flow_request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class OrderFreeFlowProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: OrderFreeFlowProductResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = OrderFreeFlowProductResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OrderFreeFlowProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OrderFreeFlowProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = OrderFreeFlowProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OrderQosProductRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        channel_id: str = None,
        ipv_6: str = None,
        instance_id: str = None,
        ip_type: str = None,
        mobile_number: str = None,
        operator: str = None,
        private_ipv_4: str = None,
        product_id: str = None,
        provice: str = None,
        public_ipv_4: str = None,
        qos_request_id: str = None,
        target_ip_list: List[str] = None,
        token: str = None,
        unit_num: int = None,
    ):
        self.ali_uid = ali_uid
        self.channel_id = channel_id
        self.ipv_6 = ipv_6
        self.instance_id = instance_id
        self.ip_type = ip_type
        self.mobile_number = mobile_number
        self.operator = operator
        self.private_ipv_4 = private_ipv_4
        self.product_id = product_id
        self.provice = provice
        self.public_ipv_4 = public_ipv_4
        self.qos_request_id = qos_request_id
        self.target_ip_list = target_ip_list
        self.token = token
        self.unit_num = unit_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.private_ipv_4 is not None:
            result['PrivateIpv4'] = self.private_ipv_4
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.provice is not None:
            result['Provice'] = self.provice
        if self.public_ipv_4 is not None:
            result['PublicIpv4'] = self.public_ipv_4
        if self.qos_request_id is not None:
            result['QosRequestId'] = self.qos_request_id
        if self.target_ip_list is not None:
            result['TargetIpList'] = self.target_ip_list
        if self.token is not None:
            result['Token'] = self.token
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PrivateIpv4') is not None:
            self.private_ipv_4 = m.get('PrivateIpv4')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Provice') is not None:
            self.provice = m.get('Provice')
        if m.get('PublicIpv4') is not None:
            self.public_ipv_4 = m.get('PublicIpv4')
        if m.get('QosRequestId') is not None:
            self.qos_request_id = m.get('QosRequestId')
        if m.get('TargetIpList') is not None:
            self.target_ip_list = m.get('TargetIpList')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class OrderQosProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OrderQosProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OrderQosProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = OrderQosProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderListRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        instance_id: str = None,
        item_code: str = None,
        mobile: str = None,
        order_time: str = None,
        out_biz_no: str = None,
        page_size: int = None,
        uid: int = None,
    ):
        self.current = current
        self.instance_id = instance_id
        self.item_code = item_code
        self.mobile = mobile
        self.order_time = order_time
        self.out_biz_no = out_biz_no
        self.page_size = page_size
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.order_time is not None:
            result['OrderTime'] = self.order_time
        if self.out_biz_no is not None:
            result['OutBizNo'] = self.out_biz_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.uid is not None:
            result['UId'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OrderTime') is not None:
            self.order_time = m.get('OrderTime')
        if m.get('OutBizNo') is not None:
            self.out_biz_no = m.get('OutBizNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UId') is not None:
            self.uid = m.get('UId')
        return self


class QueryOrderListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        message: str = None,
        mobile: str = None,
        operator: str = None,
        order_id: str = None,
        order_time: str = None,
        out_biz_no: str = None,
        product_id: str = None,
        product_name: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.message = message
        self.mobile = mobile
        self.operator = operator
        self.order_id = order_id
        self.order_time = order_time
        self.out_biz_no = out_biz_no
        self.product_id = product_id
        self.product_name = product_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_time is not None:
            result['OrderTime'] = self.order_time
        if self.out_biz_no is not None:
            result['OutBizNo'] = self.out_biz_no
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderTime') is not None:
            self.order_time = m.get('OrderTime')
        if m.get('OutBizNo') is not None:
            self.out_biz_no = m.get('OutBizNo')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryOrderListResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current = current
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryOrderListResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryOrderListResponseBodyDataList] = None,
        page_info: QueryOrderListResponseBodyDataPageInfo = None,
    ):
        self.list = list
        self.page_info = page_info

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryOrderListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = QueryOrderListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        return self


class QueryOrderListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryOrderListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryOrderListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOrderListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOrderListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryOrderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApplicationInfoRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: str = None,
        app_name: str = None,
        app_type_list: str = None,
        apping_list: str = None,
        item_code: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_id = app_id
        self.app_name = app_name
        self.app_type_list = app_type_list
        self.apping_list = apping_list
        self.item_code = item_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type_list is not None:
            result['AppTypeList'] = self.app_type_list
        if self.apping_list is not None:
            result['AppingList'] = self.apping_list
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTypeList') is not None:
            self.app_type_list = m.get('AppTypeList')
        if m.get('AppingList') is not None:
            self.apping_list = m.get('AppingList')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class SaveApplicationInfoResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.app_id = app_id
        self.code = code
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveApplicationInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveApplicationInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SaveApplicationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkGetInventoryInfoRequest(TeaModel):
    def __init__(
        self,
        channel_code: str = None,
        instance_id: str = None,
        item_code: str = None,
        mobile: str = None,
        out_biz_no: str = None,
        uid: int = None,
    ):
        self.channel_code = channel_code
        self.instance_id = instance_id
        self.item_code = item_code
        self.mobile = mobile
        self.out_biz_no = out_biz_no
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.out_biz_no is not None:
            result['OutBizNo'] = self.out_biz_no
        if self.uid is not None:
            result['UId'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OutBizNo') is not None:
            self.out_biz_no = m.get('OutBizNo')
        if m.get('UId') is not None:
            self.uid = m.get('UId')
        return self


class SdkGetInventoryInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        inventory: int = None,
        residual_inventory: int = None,
        used_stock: int = None,
    ):
        self.inventory = inventory
        self.residual_inventory = residual_inventory
        self.used_stock = used_stock

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory is not None:
            result['Inventory'] = self.inventory
        if self.residual_inventory is not None:
            result['ResidualInventory'] = self.residual_inventory
        if self.used_stock is not None:
            result['UsedStock'] = self.used_stock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Inventory') is not None:
            self.inventory = m.get('Inventory')
        if m.get('ResidualInventory') is not None:
            self.residual_inventory = m.get('ResidualInventory')
        if m.get('UsedStock') is not None:
            self.used_stock = m.get('UsedStock')
        return self


class SdkGetInventoryInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SdkGetInventoryInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SdkGetInventoryInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SdkGetInventoryInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SdkGetInventoryInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SdkGetInventoryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkOrderQosProductRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        channel_id: str = None,
        ct_token: str = None,
        ipv_6: str = None,
        instance_id: str = None,
        ip_type: str = None,
        mobile_number: str = None,
        operator: str = None,
        private_ipv_4: str = None,
        product_id: str = None,
        provice: str = None,
        public_ipv_4: str = None,
        qos_request_id: str = None,
        target_ip_list: List[str] = None,
        token: str = None,
        unit_num: int = None,
    ):
        self.ali_uid = ali_uid
        self.channel_id = channel_id
        self.ct_token = ct_token
        self.ipv_6 = ipv_6
        self.instance_id = instance_id
        self.ip_type = ip_type
        self.mobile_number = mobile_number
        self.operator = operator
        self.private_ipv_4 = private_ipv_4
        self.product_id = product_id
        self.provice = provice
        self.public_ipv_4 = public_ipv_4
        self.qos_request_id = qos_request_id
        self.target_ip_list = target_ip_list
        self.token = token
        self.unit_num = unit_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.ct_token is not None:
            result['CtToken'] = self.ct_token
        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.private_ipv_4 is not None:
            result['PrivateIpv4'] = self.private_ipv_4
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.provice is not None:
            result['Provice'] = self.provice
        if self.public_ipv_4 is not None:
            result['PublicIpv4'] = self.public_ipv_4
        if self.qos_request_id is not None:
            result['QosRequestId'] = self.qos_request_id
        if self.target_ip_list is not None:
            result['TargetIpList'] = self.target_ip_list
        if self.token is not None:
            result['Token'] = self.token
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CtToken') is not None:
            self.ct_token = m.get('CtToken')
        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PrivateIpv4') is not None:
            self.private_ipv_4 = m.get('PrivateIpv4')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Provice') is not None:
            self.provice = m.get('Provice')
        if m.get('PublicIpv4') is not None:
            self.public_ipv_4 = m.get('PublicIpv4')
        if m.get('QosRequestId') is not None:
            self.qos_request_id = m.get('QosRequestId')
        if m.get('TargetIpList') is not None:
            self.target_ip_list = m.get('TargetIpList')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class SdkOrderQosProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SdkOrderQosProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SdkOrderQosProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SdkOrderQosProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkValidateStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        credential_type: str = None,
        credential_value: str = None,
        operator: str = None,
        token: str = None,
    ):
        self.app_id = app_id
        self.credential_type = credential_type
        self.credential_value = credential_value
        self.operator = operator
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.credential_value is not None:
            result['CredentialValue'] = self.credential_value
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('CredentialValue') is not None:
            self.credential_value = m.get('CredentialValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class SdkValidateStatusResponseBodyDataAppExtPopList(TeaModel):
    def __init__(
        self,
        ext_id: int = None,
        flow_ip: List[str] = None,
        flow_url: List[str] = None,
        original_ip_list: List[str] = None,
        original_url_list: List[str] = None,
    ):
        self.ext_id = ext_id
        self.flow_ip = flow_ip
        self.flow_url = flow_url
        self.original_ip_list = original_ip_list
        self.original_url_list = original_url_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id is not None:
            result['ExtId'] = self.ext_id
        if self.flow_ip is not None:
            result['FlowIp'] = self.flow_ip
        if self.flow_url is not None:
            result['FlowUrl'] = self.flow_url
        if self.original_ip_list is not None:
            result['OriginalIpList'] = self.original_ip_list
        if self.original_url_list is not None:
            result['OriginalUrlList'] = self.original_url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtId') is not None:
            self.ext_id = m.get('ExtId')
        if m.get('FlowIp') is not None:
            self.flow_ip = m.get('FlowIp')
        if m.get('FlowUrl') is not None:
            self.flow_url = m.get('FlowUrl')
        if m.get('OriginalIpList') is not None:
            self.original_ip_list = m.get('OriginalIpList')
        if m.get('OriginalUrlList') is not None:
            self.original_url_list = m.get('OriginalUrlList')
        return self


class SdkValidateStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        app_ext_pop_list: List[SdkValidateStatusResponseBodyDataAppExtPopList] = None,
        free_flow: bool = None,
        pseudo_code: str = None,
    ):
        self.app_ext_pop_list = app_ext_pop_list
        self.free_flow = free_flow
        self.pseudo_code = pseudo_code

    def validate(self):
        if self.app_ext_pop_list:
            for k in self.app_ext_pop_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppExtPopList'] = []
        if self.app_ext_pop_list is not None:
            for k in self.app_ext_pop_list:
                result['AppExtPopList'].append(k.to_map() if k else None)
        if self.free_flow is not None:
            result['FreeFlow'] = self.free_flow
        if self.pseudo_code is not None:
            result['PseudoCode'] = self.pseudo_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_ext_pop_list = []
        if m.get('AppExtPopList') is not None:
            for k in m.get('AppExtPopList'):
                temp_model = SdkValidateStatusResponseBodyDataAppExtPopList()
                self.app_ext_pop_list.append(temp_model.from_map(k))
        if m.get('FreeFlow') is not None:
            self.free_flow = m.get('FreeFlow')
        if m.get('PseudoCode') is not None:
            self.pseudo_code = m.get('PseudoCode')
        return self


class SdkValidateStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SdkValidateStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SdkValidateStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SdkValidateStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SdkValidateStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SdkValidateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidControllerAuthorRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        item_code: str = None,
    ):
        self.ali_uid = ali_uid
        self.item_code = item_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class ValidControllerAuthorResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidControllerAuthorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidControllerAuthorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ValidControllerAuthorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidFlowRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        item_code: str = None,
        mobile: str = None,
        uid: int = None,
    ):
        self.instance_id = instance_id
        self.item_code = item_code
        self.mobile = mobile
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.uid is not None:
            result['UId'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('UId') is not None:
            self.uid = m.get('UId')
        return self


class ValidFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
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
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ValidFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateStatusRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: str = None,
        credential_type: str = None,
        credential_value: str = None,
        operator: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_id = app_id
        self.credential_type = credential_type
        self.credential_value = credential_value
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.credential_value is not None:
            result['CredentialValue'] = self.credential_value
        if self.operator is not None:
            result['Operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('CredentialValue') is not None:
            self.credential_value = m.get('CredentialValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        return self


class ValidateStatusResponseBodyDataAppExtPopList(TeaModel):
    def __init__(
        self,
        ext_id: int = None,
        flow_ip: List[str] = None,
        flow_url: List[str] = None,
        original_ip_list: List[str] = None,
        original_url_list: List[str] = None,
    ):
        self.ext_id = ext_id
        self.flow_ip = flow_ip
        self.flow_url = flow_url
        self.original_ip_list = original_ip_list
        self.original_url_list = original_url_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id is not None:
            result['ExtId'] = self.ext_id
        if self.flow_ip is not None:
            result['FlowIp'] = self.flow_ip
        if self.flow_url is not None:
            result['FlowUrl'] = self.flow_url
        if self.original_ip_list is not None:
            result['OriginalIpList'] = self.original_ip_list
        if self.original_url_list is not None:
            result['OriginalUrlList'] = self.original_url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtId') is not None:
            self.ext_id = m.get('ExtId')
        if m.get('FlowIp') is not None:
            self.flow_ip = m.get('FlowIp')
        if m.get('FlowUrl') is not None:
            self.flow_url = m.get('FlowUrl')
        if m.get('OriginalIpList') is not None:
            self.original_ip_list = m.get('OriginalIpList')
        if m.get('OriginalUrlList') is not None:
            self.original_url_list = m.get('OriginalUrlList')
        return self


class ValidateStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        app_ext_pop_list: List[ValidateStatusResponseBodyDataAppExtPopList] = None,
        free_flow: bool = None,
        pseudo_code: str = None,
    ):
        self.app_ext_pop_list = app_ext_pop_list
        self.free_flow = free_flow
        self.pseudo_code = pseudo_code

    def validate(self):
        if self.app_ext_pop_list:
            for k in self.app_ext_pop_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppExtPopList'] = []
        if self.app_ext_pop_list is not None:
            for k in self.app_ext_pop_list:
                result['AppExtPopList'].append(k.to_map() if k else None)
        if self.free_flow is not None:
            result['FreeFlow'] = self.free_flow
        if self.pseudo_code is not None:
            result['PseudoCode'] = self.pseudo_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_ext_pop_list = []
        if m.get('AppExtPopList') is not None:
            for k in m.get('AppExtPopList'):
                temp_model = ValidateStatusResponseBodyDataAppExtPopList()
                self.app_ext_pop_list.append(temp_model.from_map(k))
        if m.get('FreeFlow') is not None:
            self.free_flow = m.get('FreeFlow')
        if m.get('PseudoCode') is not None:
            self.pseudo_code = m.get('PseudoCode')
        return self


class ValidateStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ValidateStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.rt = rt
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
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ValidateStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidateStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ValidateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


