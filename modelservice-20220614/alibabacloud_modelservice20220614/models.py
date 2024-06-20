# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetMonthAmountRequest(TeaModel):
    def __init__(
        self,
        scene_type: str = None,
    ):
        # This parameter is required.
        self.scene_type = scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class GetMonthAmountResponseBody(TeaModel):
    def __init__(
        self,
        background_amount: int = None,
        postpay_amount: int = None,
        prepay_amount: int = None,
        request_id: str = None,
        total_amount: int = None,
    ):
        self.background_amount = background_amount
        self.postpay_amount = postpay_amount
        self.prepay_amount = prepay_amount
        self.request_id = request_id
        self.total_amount = total_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_amount is not None:
            result['BackgroundAmount'] = self.background_amount
        if self.postpay_amount is not None:
            result['PostpayAmount'] = self.postpay_amount
        if self.prepay_amount is not None:
            result['PrepayAmount'] = self.prepay_amount
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundAmount') is not None:
            self.background_amount = m.get('BackgroundAmount')
        if m.get('PostpayAmount') is not None:
            self.postpay_amount = m.get('PostpayAmount')
        if m.get('PrepayAmount') is not None:
            self.prepay_amount = m.get('PrepayAmount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        return self


class GetMonthAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMonthAmountResponseBody = None,
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
            temp_model = GetMonthAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        scene_type: str = None,
    ):
        self.scene_type = scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        host: str = None,
        message: str = None,
        request_id: str = None,
        token: str = None,
    ):
        self.app_id = app_id
        self.code = code
        self.host = host
        self.message = message
        self.request_id = request_id
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
        if self.code is not None:
            result['Code'] = self.code
        if self.host is not None:
            result['Host'] = self.host
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDayAmountRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        scene_type: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.scene_type = scene_type
        # This parameter is required.
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
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDayAmountResponseBodyDayAmounts(TeaModel):
    def __init__(
        self,
        amount: int = None,
        date: str = None,
    ):
        self.amount = amount
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class ListDayAmountResponseBody(TeaModel):
    def __init__(
        self,
        day_amounts: List[ListDayAmountResponseBodyDayAmounts] = None,
        request_id: str = None,
    ):
        self.day_amounts = day_amounts
        self.request_id = request_id

    def validate(self):
        if self.day_amounts:
            for k in self.day_amounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DayAmounts'] = []
        if self.day_amounts is not None:
            for k in self.day_amounts:
                result['DayAmounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.day_amounts = []
        if m.get('DayAmounts') is not None:
            for k in m.get('DayAmounts'):
                temp_model = ListDayAmountResponseBodyDayAmounts()
                self.day_amounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDayAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDayAmountResponseBody = None,
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
            temp_model = ListDayAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRechargeBillsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        scene_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.scene_type = scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class ListRechargeBillsResponseBodyInstanseInfos(TeaModel):
    def __init__(
        self,
        curr_times: int = None,
        gmt_end_time: str = None,
        init_times: int = None,
        instance_id: str = None,
        source: str = None,
    ):
        self.curr_times = curr_times
        self.gmt_end_time = gmt_end_time
        self.init_times = init_times
        self.instance_id = instance_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_times is not None:
            result['CurrTimes'] = self.curr_times
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.init_times is not None:
            result['InitTimes'] = self.init_times
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrTimes') is not None:
            self.curr_times = m.get('CurrTimes')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('InitTimes') is not None:
            self.init_times = m.get('InitTimes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListRechargeBillsResponseBody(TeaModel):
    def __init__(
        self,
        instanse_infos: List[ListRechargeBillsResponseBodyInstanseInfos] = None,
        request_id: str = None,
        residue_amount: int = None,
        total_count: int = None,
    ):
        self.instanse_infos = instanse_infos
        self.request_id = request_id
        self.residue_amount = residue_amount
        self.total_count = total_count

    def validate(self):
        if self.instanse_infos:
            for k in self.instanse_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanseInfos'] = []
        if self.instanse_infos is not None:
            for k in self.instanse_infos:
                result['InstanseInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.residue_amount is not None:
            result['ResidueAmount'] = self.residue_amount
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instanse_infos = []
        if m.get('InstanseInfos') is not None:
            for k in m.get('InstanseInfos'):
                temp_model = ListRechargeBillsResponseBodyInstanseInfos()
                self.instanse_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResidueAmount') is not None:
            self.residue_amount = m.get('ResidueAmount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRechargeBillsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRechargeBillsResponseBody = None,
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
            temp_model = ListRechargeBillsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


