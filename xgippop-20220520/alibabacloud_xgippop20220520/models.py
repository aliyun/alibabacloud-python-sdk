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
        # 阿里UID
        self.ali_uid = ali_uid
        self.app_id = app_id
        # 应用名称
        self.app_name = app_name
        # dynamic|static
        self.app_type_list = app_type_list
        # [
        self.apping_list = apping_list
        # 商品code
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
        # 结果码
        self.code = code
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


class GetFreeFlowStatusRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: str = None,
        flow_product_id: str = None,
        mobile_number: str = None,
        net_type: str = None,
        operator: str = None,
        private_ip: str = None,
        pseudo_code: str = None,
        public_ip: str = None,
        token: str = None,
    ):
        self.ali_uid = ali_uid
        # 应用ID
        self.app_id = app_id
        # 免流产品ID
        self.flow_product_id = flow_product_id
        # C端手机号
        self.mobile_number = mobile_number
        # 网络类型，如3G、4G、5G
        self.net_type = net_type
        # 取值包括cm（中国移动）/ct（中国电信）/cu（中国联通）
        self.operator = operator
        # 手机端私网ip地址
        self.private_ip = private_ip
        # C端手机在运营商侧端伪码，如："75D35971BD"
        self.pseudo_code = pseudo_code
        # 手机端公网ip地址
        self.public_ip = public_ip
        # 通过云通信获取的token
        self.token = token

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
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip
        if self.pseudo_code is not None:
            result['PseudoCode'] = self.pseudo_code
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')
        if m.get('PseudoCode') is not None:
            self.pseudo_code = m.get('PseudoCode')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetFreeFlowStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
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


class GetFreeFlowStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFreeFlowStatusResponseBody = None,
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
            temp_model = GetFreeFlowStatusResponseBody()
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
        # 当前页
        self.cur_page_num = cur_page_num
        # 实例ID
        self.instance_id = instance_id
        # 查询月份
        self.month = month
        # 每页的记录数量
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
        # 购买渠道
        self.channel_id = channel_id
        # C端产品失效时间
        self.customer_end_time = customer_end_time
        self.customer_flow_order_id = customer_flow_order_id
        # C端免流状态，取值包括create/working/expiration
        self.customer_flow_status = customer_flow_status
        # C端产品开通时间
        self.customer_open_time = customer_open_time
        # C端产品生效时间
        self.customer_start_time = customer_start_time
        # 免流产品ID
        self.flow_product_id = flow_product_id
        # 免流产品名
        self.flow_product_name = flow_product_name
        # 是否包月，true或false
        self.is_lasting = is_lasting
        # C端手机号
        self.mobile_number = mobile_number
        # 该流量包的计量单元数
        self.unit_num = unit_num
        # 流量包价格
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
        # 当前页数
        self.cur_page_num = cur_page_num
        # C端用户列表
        self.customer_list = customer_list
        # 是否有下一页
        self.has_next = has_next
        # 是否有上一页
        self.has_prev = has_prev
        # 实例ID
        self.instance_id = instance_id
        # 每页的记录条数
        self.num_per_page = num_per_page
        # 总记录条数
        self.total_num = total_num
        # 总页数
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
        # 该实例对应的包类型
        self.spec_type = spec_type
        self.total_money = total_money
        # 该实例的订单总数
        self.total_order_number = total_order_number
        # 该实例的订单总计量单元数
        self.total_unit_number = total_unit_number
        # 产品规格
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


class GetOrderFreeFlowProductStatusRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        customer_flow_order_id: str = None,
    ):
        self.ali_uid = ali_uid
        # 在订购接口2.1.9中引擎侧生成的id
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
        # C端免流订单ID
        self.customer_flow_order_id = customer_flow_order_id
        self.customer_flow_request_id = customer_flow_request_id
        # status为fail时，描述fail的具体原因
        self.error = error
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
        # 结果码
        self.code = code
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
        biz_code: str = None,
        customer_flow_order_id: str = None,
        customer_flow_request_id: str = None,
        status: str = None,
    ):
        self.biz_code = biz_code
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
        # 阿里UID
        self.ali_uid = ali_uid
        self.app_id = app_id
        # 应用名称
        self.app_name = app_name
        # dynamic|static
        self.app_type_list = app_type_list
        # [
        self.apping_list = apping_list
        # 商品code
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


class ValidateStatusRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: str = None,
        credential_type: str = None,
        credential_value: str = None,
        operator: str = None,
    ):
        # 阿里UID
        self.ali_uid = ali_uid
        # 应用名称
        self.app_id = app_id
        # 凭证类型
        self.credential_type = credential_type
        # mobile=150xxxx4661
        self.credential_value = credential_value
        # 取值包括cm（中国移动）/ct（中国电信）/cu（中国联通）
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


class ValidateStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        app_ext_pop_list: List[ValidateStatusResponseBodyDataAppExtPopList] = None,
        free_flow: bool = None,
        pseudo_code: str = None,
    ):
        self.app_ext_pop_list = app_ext_pop_list
        # 是否处于免流状态，取值范围为true/false
        self.free_flow = free_flow
        # 伪码
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


