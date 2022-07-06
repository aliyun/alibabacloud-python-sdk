# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CreateDeviceRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        city: str = None,
        device_model_number: str = None,
        device_name: str = None,
        device_type: str = None,
        district: str = None,
        extra_map: Dict[str, Any] = None,
        first_scene: str = None,
        floor: str = None,
        location_name: str = None,
        media_id: str = None,
        outer_code: str = None,
        province: str = None,
        second_scene: str = None,
    ):
        self.channel_id = channel_id
        self.city = city
        self.device_model_number = device_model_number
        self.device_name = device_name
        self.device_type = device_type
        self.district = district
        self.extra_map = extra_map
        self.first_scene = first_scene
        self.floor = floor
        self.location_name = location_name
        self.media_id = media_id
        self.outer_code = outer_code
        self.province = province
        self.second_scene = second_scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.city is not None:
            result['City'] = self.city
        if self.device_model_number is not None:
            result['DeviceModelNumber'] = self.device_model_number
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.district is not None:
            result['District'] = self.district
        if self.extra_map is not None:
            result['ExtraMap'] = self.extra_map
        if self.first_scene is not None:
            result['FirstScene'] = self.first_scene
        if self.floor is not None:
            result['Floor'] = self.floor
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.outer_code is not None:
            result['OuterCode'] = self.outer_code
        if self.province is not None:
            result['Province'] = self.province
        if self.second_scene is not None:
            result['SecondScene'] = self.second_scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('DeviceModelNumber') is not None:
            self.device_model_number = m.get('DeviceModelNumber')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('ExtraMap') is not None:
            self.extra_map = m.get('ExtraMap')
        if m.get('FirstScene') is not None:
            self.first_scene = m.get('FirstScene')
        if m.get('Floor') is not None:
            self.floor = m.get('Floor')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OuterCode') is not None:
            self.outer_code = m.get('OuterCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('SecondScene') is not None:
            self.second_scene = m.get('SecondScene')
        return self


class CreateDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        city: str = None,
        device_model_number: str = None,
        device_name: str = None,
        device_type: str = None,
        district: str = None,
        extra_map_shrink: str = None,
        first_scene: str = None,
        floor: str = None,
        location_name: str = None,
        media_id: str = None,
        outer_code: str = None,
        province: str = None,
        second_scene: str = None,
    ):
        self.channel_id = channel_id
        self.city = city
        self.device_model_number = device_model_number
        self.device_name = device_name
        self.device_type = device_type
        self.district = district
        self.extra_map_shrink = extra_map_shrink
        self.first_scene = first_scene
        self.floor = floor
        self.location_name = location_name
        self.media_id = media_id
        self.outer_code = outer_code
        self.province = province
        self.second_scene = second_scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.city is not None:
            result['City'] = self.city
        if self.device_model_number is not None:
            result['DeviceModelNumber'] = self.device_model_number
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.district is not None:
            result['District'] = self.district
        if self.extra_map_shrink is not None:
            result['ExtraMap'] = self.extra_map_shrink
        if self.first_scene is not None:
            result['FirstScene'] = self.first_scene
        if self.floor is not None:
            result['Floor'] = self.floor
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.outer_code is not None:
            result['OuterCode'] = self.outer_code
        if self.province is not None:
            result['Province'] = self.province
        if self.second_scene is not None:
            result['SecondScene'] = self.second_scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('DeviceModelNumber') is not None:
            self.device_model_number = m.get('DeviceModelNumber')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('ExtraMap') is not None:
            self.extra_map_shrink = m.get('ExtraMap')
        if m.get('FirstScene') is not None:
            self.first_scene = m.get('FirstScene')
        if m.get('Floor') is not None:
            self.floor = m.get('Floor')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OuterCode') is not None:
            self.outer_code = m.get('OuterCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('SecondScene') is not None:
            self.second_scene = m.get('SecondScene')
        return self


class CreateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Id of the request
        self.code = code
        self.message = message
        self.model = model
        # Id of the request
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
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDeviceResponseBody = None,
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
            temp_model = CreateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserFinishedAdRequest(TeaModel):
    def __init__(
        self,
        adid: int = None,
        clicklink: str = None,
        id: str = None,
        mediaid: str = None,
        tagid: str = None,
        uid: str = None,
    ):
        # adid
        self.adid = adid
        # clicklink
        self.clicklink = clicklink
        # id
        self.id = id
        # mediaid
        self.mediaid = mediaid
        # tagid
        self.tagid = tagid
        # uid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adid is not None:
            result['Adid'] = self.adid
        if self.clicklink is not None:
            result['Clicklink'] = self.clicklink
        if self.id is not None:
            result['Id'] = self.id
        if self.mediaid is not None:
            result['Mediaid'] = self.mediaid
        if self.tagid is not None:
            result['Tagid'] = self.tagid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adid') is not None:
            self.adid = m.get('Adid')
        if m.get('Clicklink') is not None:
            self.clicklink = m.get('Clicklink')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mediaid') is not None:
            self.mediaid = m.get('Mediaid')
        if m.get('Tagid') is not None:
            self.tagid = m.get('Tagid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetUserFinishedAdResponseBodyHeader(TeaModel):
    def __init__(
        self,
        cost_time: int = None,
        rpc_id: str = None,
        trace_id: str = None,
        version: str = None,
    ):
        # costTime
        self.cost_time = cost_time
        # rpcId
        self.rpc_id = rpc_id
        # traceId
        self.trace_id = trace_id
        # version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetUserFinishedAdResponseBodyResult(TeaModel):
    def __init__(
        self,
        commission: str = None,
        marketing_type: str = None,
        objective: str = None,
        success: bool = None,
    ):
        self.commission = commission
        self.marketing_type = marketing_type
        self.objective = objective
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commission is not None:
            result['Commission'] = self.commission
        if self.marketing_type is not None:
            result['MarketingType'] = self.marketing_type
        if self.objective is not None:
            result['Objective'] = self.objective
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commission') is not None:
            self.commission = m.get('Commission')
        if m.get('MarketingType') is not None:
            self.marketing_type = m.get('MarketingType')
        if m.get('Objective') is not None:
            self.objective = m.get('Objective')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserFinishedAdResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        ext: Dict[str, str] = None,
        header: GetUserFinishedAdResponseBodyHeader = None,
        request_id: str = None,
        result: GetUserFinishedAdResponseBodyResult = None,
        success: bool = None,
    ):
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # ext
        self.ext = ext
        # header
        self.header = header
        self.request_id = request_id
        self.result = result
        # success
        self.success = success

    def validate(self):
        if self.header:
            self.header.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Header') is not None:
            temp_model = GetUserFinishedAdResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetUserFinishedAdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserFinishedAdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserFinishedAdResponseBody = None,
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
            temp_model = GetUserFinishedAdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAdvertisingRequestApp(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        mediaid: str = None,
        sn: str = None,
    ):
        self.ext = ext
        # mediaid
        self.mediaid = mediaid
        # sn
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.mediaid is not None:
            result['Mediaid'] = self.mediaid
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Mediaid') is not None:
            self.mediaid = m.get('Mediaid')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class ListAdvertisingRequestImp(TeaModel):
    def __init__(
        self,
        id: str = None,
        tagid: str = None,
    ):
        # id
        self.id = id
        # tagid
        self.tagid = tagid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tagid is not None:
            result['Tagid'] = self.tagid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Tagid') is not None:
            self.tagid = m.get('Tagid')
        return self


class ListAdvertisingRequestUser(TeaModel):
    def __init__(
        self,
        id: str = None,
        usertype: str = None,
    ):
        # uid
        self.id = id
        # uidtype
        self.usertype = usertype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.usertype is not None:
            result['Usertype'] = self.usertype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Usertype') is not None:
            self.usertype = m.get('Usertype')
        return self


class ListAdvertisingRequest(TeaModel):
    def __init__(
        self,
        app: ListAdvertisingRequestApp = None,
        dealtype: int = None,
        ext: Dict[str, Any] = None,
        id: str = None,
        imp: List[ListAdvertisingRequestImp] = None,
        test: int = None,
        user: ListAdvertisingRequestUser = None,
    ):
        # app
        self.app = app
        self.dealtype = dealtype
        self.ext = ext
        # id
        self.id = id
        # imp
        self.imp = imp
        # test
        self.test = test
        # user
        self.user = user

    def validate(self):
        if self.app:
            self.app.validate()
        if self.imp:
            for k in self.imp:
                if k:
                    k.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.dealtype is not None:
            result['Dealtype'] = self.dealtype
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        result['Imp'] = []
        if self.imp is not None:
            for k in self.imp:
                result['Imp'].append(k.to_map() if k else None)
        if self.test is not None:
            result['Test'] = self.test
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = ListAdvertisingRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('Dealtype') is not None:
            self.dealtype = m.get('Dealtype')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.imp = []
        if m.get('Imp') is not None:
            for k in m.get('Imp'):
                temp_model = ListAdvertisingRequestImp()
                self.imp.append(temp_model.from_map(k))
        if m.get('Test') is not None:
            self.test = m.get('Test')
        if m.get('User') is not None:
            temp_model = ListAdvertisingRequestUser()
            self.user = temp_model.from_map(m['User'])
        return self


class ListAdvertisingShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        dealtype: int = None,
        ext_shrink: str = None,
        id: str = None,
        imp_shrink: str = None,
        test: int = None,
        user_shrink: str = None,
    ):
        # app
        self.app_shrink = app_shrink
        self.dealtype = dealtype
        self.ext_shrink = ext_shrink
        # id
        self.id = id
        # imp
        self.imp_shrink = imp_shrink
        # test
        self.test = test
        # user
        self.user_shrink = user_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.dealtype is not None:
            result['Dealtype'] = self.dealtype
        if self.ext_shrink is not None:
            result['Ext'] = self.ext_shrink
        if self.id is not None:
            result['Id'] = self.id
        if self.imp_shrink is not None:
            result['Imp'] = self.imp_shrink
        if self.test is not None:
            result['Test'] = self.test
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('Dealtype') is not None:
            self.dealtype = m.get('Dealtype')
        if m.get('Ext') is not None:
            self.ext_shrink = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Imp') is not None:
            self.imp_shrink = m.get('Imp')
        if m.get('Test') is not None:
            self.test = m.get('Test')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        return self


class ListAdvertisingResponseBodyHeader(TeaModel):
    def __init__(
        self,
        cost_time: int = None,
        rpc_id: str = None,
        trace_id: str = None,
        version: str = None,
    ):
        # costTime
        self.cost_time = cost_time
        # rpcId
        self.rpc_id = rpc_id
        # traceId
        self.trace_id = trace_id
        # version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAdvertisingResponseBodyResultSeatbidBidAdsIcon(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListAdvertisingResponseBodyResultSeatbidBidAdsImages(TeaModel):
    def __init__(
        self,
        desc: str = None,
        format: str = None,
        url: str = None,
    ):
        self.desc = desc
        self.format = format
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.format is not None:
            result['Format'] = self.format
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListAdvertisingResponseBodyResultSeatbidBidAdsTrackers(TeaModel):
    def __init__(
        self,
        imps: List[str] = None,
    ):
        self.imps = imps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.imps is not None:
            result['Imps'] = self.imps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Imps') is not None:
            self.imps = m.get('Imps')
        return self


class ListAdvertisingResponseBodyResultSeatbidBidAds(TeaModel):
    def __init__(
        self,
        crid: str = None,
        crurl: str = None,
        icon: ListAdvertisingResponseBodyResultSeatbidBidAdsIcon = None,
        id: str = None,
        images: List[ListAdvertisingResponseBodyResultSeatbidBidAdsImages] = None,
        interacttype: int = None,
        labeltype: str = None,
        landingurls: List[str] = None,
        marketingtype: str = None,
        objective: str = None,
        price: str = None,
        seat: str = None,
        style: str = None,
        title: str = None,
        trackers: ListAdvertisingResponseBodyResultSeatbidBidAdsTrackers = None,
        type: str = None,
    ):
        self.crid = crid
        self.crurl = crurl
        self.icon = icon
        self.id = id
        self.images = images
        self.interacttype = interacttype
        self.labeltype = labeltype
        self.landingurls = landingurls
        self.marketingtype = marketingtype
        self.objective = objective
        self.price = price
        self.seat = seat
        self.style = style
        self.title = title
        self.trackers = trackers
        self.type = type

    def validate(self):
        if self.icon:
            self.icon.validate()
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.trackers:
            self.trackers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crid is not None:
            result['Crid'] = self.crid
        if self.crurl is not None:
            result['Crurl'] = self.crurl
        if self.icon is not None:
            result['Icon'] = self.icon.to_map()
        if self.id is not None:
            result['Id'] = self.id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.interacttype is not None:
            result['Interacttype'] = self.interacttype
        if self.labeltype is not None:
            result['Labeltype'] = self.labeltype
        if self.landingurls is not None:
            result['Landingurls'] = self.landingurls
        if self.marketingtype is not None:
            result['Marketingtype'] = self.marketingtype
        if self.objective is not None:
            result['Objective'] = self.objective
        if self.price is not None:
            result['Price'] = self.price
        if self.seat is not None:
            result['Seat'] = self.seat
        if self.style is not None:
            result['Style'] = self.style
        if self.title is not None:
            result['Title'] = self.title
        if self.trackers is not None:
            result['Trackers'] = self.trackers.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crid') is not None:
            self.crid = m.get('Crid')
        if m.get('Crurl') is not None:
            self.crurl = m.get('Crurl')
        if m.get('Icon') is not None:
            temp_model = ListAdvertisingResponseBodyResultSeatbidBidAdsIcon()
            self.icon = temp_model.from_map(m['Icon'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListAdvertisingResponseBodyResultSeatbidBidAdsImages()
                self.images.append(temp_model.from_map(k))
        if m.get('Interacttype') is not None:
            self.interacttype = m.get('Interacttype')
        if m.get('Labeltype') is not None:
            self.labeltype = m.get('Labeltype')
        if m.get('Landingurls') is not None:
            self.landingurls = m.get('Landingurls')
        if m.get('Marketingtype') is not None:
            self.marketingtype = m.get('Marketingtype')
        if m.get('Objective') is not None:
            self.objective = m.get('Objective')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Seat') is not None:
            self.seat = m.get('Seat')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Trackers') is not None:
            temp_model = ListAdvertisingResponseBodyResultSeatbidBidAdsTrackers()
            self.trackers = temp_model.from_map(m['Trackers'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAdvertisingResponseBodyResultSeatbidBid(TeaModel):
    def __init__(
        self,
        ads: List[ListAdvertisingResponseBodyResultSeatbidBidAds] = None,
        impid: str = None,
    ):
        self.ads = ads
        self.impid = impid

    def validate(self):
        if self.ads:
            for k in self.ads:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Ads'] = []
        if self.ads is not None:
            for k in self.ads:
                result['Ads'].append(k.to_map() if k else None)
        if self.impid is not None:
            result['Impid'] = self.impid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ads = []
        if m.get('Ads') is not None:
            for k in m.get('Ads'):
                temp_model = ListAdvertisingResponseBodyResultSeatbidBidAds()
                self.ads.append(temp_model.from_map(k))
        if m.get('Impid') is not None:
            self.impid = m.get('Impid')
        return self


class ListAdvertisingResponseBodyResultSeatbid(TeaModel):
    def __init__(
        self,
        bid: List[ListAdvertisingResponseBodyResultSeatbidBid] = None,
    ):
        self.bid = bid

    def validate(self):
        if self.bid:
            for k in self.bid:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bid'] = []
        if self.bid is not None:
            for k in self.bid:
                result['Bid'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bid = []
        if m.get('Bid') is not None:
            for k in m.get('Bid'):
                temp_model = ListAdvertisingResponseBodyResultSeatbidBid()
                self.bid.append(temp_model.from_map(k))
        return self


class ListAdvertisingResponseBodyResult(TeaModel):
    def __init__(
        self,
        bidid: str = None,
        id: str = None,
        seatbid: List[ListAdvertisingResponseBodyResultSeatbid] = None,
    ):
        self.bidid = bidid
        self.id = id
        self.seatbid = seatbid

    def validate(self):
        if self.seatbid:
            for k in self.seatbid:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bidid is not None:
            result['Bidid'] = self.bidid
        if self.id is not None:
            result['Id'] = self.id
        result['Seatbid'] = []
        if self.seatbid is not None:
            for k in self.seatbid:
                result['Seatbid'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bidid') is not None:
            self.bidid = m.get('Bidid')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.seatbid = []
        if m.get('Seatbid') is not None:
            for k in m.get('Seatbid'):
                temp_model = ListAdvertisingResponseBodyResultSeatbid()
                self.seatbid.append(temp_model.from_map(k))
        return self


class ListAdvertisingResponseBody(TeaModel):
    def __init__(
        self,
        errorcode: str = None,
        errormsg: str = None,
        ext: Dict[str, str] = None,
        header: ListAdvertisingResponseBodyHeader = None,
        request_id: str = None,
        result: ListAdvertisingResponseBodyResult = None,
        success: bool = None,
    ):
        # errorCode
        self.errorcode = errorcode
        # errorMsg
        self.errormsg = errormsg
        # ext
        self.ext = ext
        # header
        self.header = header
        self.request_id = request_id
        self.result = result
        # success
        self.success = success

    def validate(self):
        if self.header:
            self.header.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.errorcode is not None:
            result['Errorcode'] = self.errorcode
        if self.errormsg is not None:
            result['Errormsg'] = self.errormsg
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Errorcode') is not None:
            self.errorcode = m.get('Errorcode')
        if m.get('Errormsg') is not None:
            self.errormsg = m.get('Errormsg')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Header') is not None:
            temp_model = ListAdvertisingResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListAdvertisingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAdvertisingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAdvertisingResponseBody = None,
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
            temp_model = ListAdvertisingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


