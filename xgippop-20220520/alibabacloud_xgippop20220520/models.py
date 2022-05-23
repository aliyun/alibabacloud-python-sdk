# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


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
        # cdn ip
        self.flow_ip = flow_ip
        # cdn 域名信息
        self.flow_url = flow_url
        # 业务方ip集合
        self.original_ip_list = original_ip_list
        # 业务方域名集合
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
        # 阿里UID
        self.ali_uid = ali_uid
        # 应用名称
        self.app_name = app_name
        # dynamic（动态业务）/static（静态业务
        self.app_type_list = app_type_list
        self.apping_list = apping_list
        # 商品code
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
        # 应用id
        self.app_id = app_id
        # 结果码
        self.code = code
        # 结果描述
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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


class GetApplicationRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_code: str = None,
    ):
        # 阿里UID
        self.ali_uid = ali_uid
        # 应用ID
        self.app_code = app_code

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        return self


class GetApplicationResponseBodyDataAppingList(TeaModel):
    def __init__(
        self,
        ext_id: int = None,
        flow_ip: List[str] = None,
        flow_url: List[str] = None,
        original_ip_list: List[str] = None,
        original_url_list: List[str] = None,
    ):
        self.ext_id = ext_id
        # cdn ip
        self.flow_ip = flow_ip
        # cdn 域名信息
        self.flow_url = flow_url
        # 业务方ip集合
        self.original_ip_list = original_ip_list
        # 业务方域名集合
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


class GetApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
        app_type_list: str = None,
        apping_list: List[GetApplicationResponseBodyDataAppingList] = None,
        end_time: str = None,
        item_code: str = None,
        open_time: str = None,
        start_time: str = None,
    ):
        # 用户编号
        self.ali_uid = ali_uid
        # 应用编号
        self.app_id = app_id
        # 应用名称
        self.app_name = app_name
        self.app_status = app_status
        # //dynamic（动态业务）/static（静态业务）  // 前端传递，参数3
        self.app_type_list = app_type_list
        self.apping_list = apping_list
        self.end_time = end_time
        # Database Column Remarks:
        self.item_code = item_code
        # 开通时间
        self.open_time = open_time
        self.start_time = start_time

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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type_list is not None:
            result['AppTypeList'] = self.app_type_list
        result['AppingList'] = []
        if self.apping_list is not None:
            for k in self.apping_list:
                result['AppingList'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppTypeList') is not None:
            self.app_type_list = m.get('AppTypeList')
        self.apping_list = []
        if m.get('AppingList') is not None:
            for k in m.get('AppingList'):
                temp_model = GetApplicationResponseBodyDataAppingList()
                self.apping_list.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetApplicationResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        # 结果码
        self.code = code
        # 结果
        self.data = data
        # 结果描述
        self.message = message
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id
        # 服务端处理耗时，ms
        self.rt = rt
        # 是否成功
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
                temp_model = GetApplicationResponseBodyData()
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
        ali_uid: int = None,
        app_id: str = None,
        instance_id: str = None,
        item_code: str = None,
    ):
        self.ali_uid = ali_uid
        # 应用ID
        self.app_id = app_id
        # 实例ID
        self.instance_id = instance_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
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
        # APP编号
        self.app_code = app_code
        # APP名称
        self.app_name = app_name
        # 产品失效时间
        self.end_time = end_time
        # 实例名称
        self.instance_memo = instance_memo
        # 实例状态
        self.instance_status = instance_status
        # 产品开通时间
        self.open_time = open_time
        # 规格类型
        self.spec_type = spec_type
        # 产品生效时间
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
        # 结果码
        self.code = code
        # 结果
        self.data = data
        # 结果描述
        self.message = message
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id
        # 服务端处理耗时，ms
        self.rt = rt
        # 是否成功
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
        # 用户编号
        self.ali_uid = ali_uid
        # 实例ID
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
        # 产品当前状态，true为已配置，false为未配置
        self.configured = configured
        # 产品包含的流量大小
        self.flow_product_amount = flow_product_amount
        # 免流产品ID
        self.flow_product_id = flow_product_id
        # 流量包名称
        self.flow_product_name = flow_product_name
        # 产品周期
        self.flow_product_period = flow_product_period
        # 取值包括free（定向流量）/normal（通用流量）
        self.flow_type = flow_type
        # 取值包括cm（中国移动）/ct（中国电信）/cu（中国联通）
        self.operator = operator
        # 注意这里返回的全量套餐里，只能包含SpecType与该InstanceId的SpecType相同的规格
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
        # 结果码
        self.code = code
        # 结果
        self.data = data
        # 结果描述
        self.message = message
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id
        # 服务端处理耗时，ms
        self.rt = rt
        # 是否成功
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
        # cdn ip
        self.flow_ip = flow_ip
        # cdn 域名信息
        self.flow_url = flow_url
        # 业务方ip集合
        self.original_ip_list = original_ip_list
        # 业务方域名集合
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
        # AliUid
        self.ali_uid = ali_uid
        # AppId
        self.app_code = app_code
        # 应用名称
        self.app_name = app_name
        # dynamic（动态业务）/static（静态业务
        self.app_type_list = app_type_list
        # 扩展属性 源域名和源ip信息保存
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
        # 应用id
        self.app_id = app_id
        # 结果码
        self.code = code
        # 结果描述
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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
        # 渠道ID
        self.channel_id = channel_id
        # 客户侧生成的QoS请求ID，需要保证请求幂等性，确保不同请求间该参数值唯一
        self.customer_flow_request_id = customer_flow_request_id
        # 免流产品ID
        self.flow_product_id = flow_product_id
        # 实例ID
        self.instance_id = instance_id
        # 是否包月，true为包月，false为不包月
        self.lasting = lasting
        # C端手机号
        self.mobile_number = mobile_number
        # 客户提供的回调通知接口url
        self.notify_url = notify_url
        # 取值包括cm（中国移动）/ct（中国电信）/cu（中国联通）
        self.operator = operator
        # 支付订单ID
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
        customer_flow_order_id: str = None,
        customer_flow_request_id: str = None,
        status: str = None,
    ):
        # C端免流订单ID
        self.customer_flow_order_id = customer_flow_order_id
        self.customer_flow_request_id = customer_flow_request_id
        # 执行中ordering、成功success、失败fail
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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # 结果码
        self.code = code
        # 结果
        self.data = data
        # 结果描述
        self.message = message
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id
        # 服务端处理耗时，ms
        self.rt = rt
        # 是否成功
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


