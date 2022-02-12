# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class ApeInnerCommonApiRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        channel: str = None,
        end_time: str = None,
        lat: str = None,
        lon: str = None,
        page_num: int = None,
        page_size: int = None,
        sp_code: str = None,
        start_time: str = None,
        station: str = None,
    ):
        # appName
        self.app_name = app_name
        # channel
        self.channel = channel
        # endTime
        self.end_time = end_time
        # lat
        self.lat = lat
        # lon
        self.lon = lon
        # pageNum
        self.page_num = page_num
        # pageSize
        self.page_size = page_size
        # spCode
        self.sp_code = sp_code
        # startTime
        self.start_time = start_time
        # station
        self.station = station

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lat is not None:
            result['Lat'] = self.lat
        if self.lon is not None:
            result['Lon'] = self.lon
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sp_code is not None:
            result['SpCode'] = self.sp_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.station is not None:
            result['Station'] = self.station
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpCode') is not None:
            self.sp_code = m.get('SpCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Station') is not None:
            self.station = m.get('Station')
        return self


class ApeInnerCommonApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # rt
        self.rt = rt
        # success
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


class ApeInnerCommonApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApeInnerCommonApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApeInnerCommonApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApeProvinceStationRefRequest(TeaModel):
    def __init__(
        self,
        adcode: int = None,
        app_name: str = None,
        city: str = None,
        cnty: str = None,
        country: str = None,
        offset: int = None,
        page_size: int = None,
        province_code: int = None,
        province_name: str = None,
        station_name: str = None,
    ):
        # adcode
        self.adcode = adcode
        # appName
        self.app_name = app_name
        # city
        self.city = city
        # cnty
        self.cnty = cnty
        # country
        self.country = country
        # offset
        self.offset = offset
        # pageSize
        self.page_size = page_size
        # provinceCode
        self.province_code = province_code
        # provinceName
        self.province_name = province_name
        # stationName
        self.station_name = station_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adcode is not None:
            result['Adcode'] = self.adcode
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.city is not None:
            result['City'] = self.city
        if self.cnty is not None:
            result['Cnty'] = self.cnty
        if self.country is not None:
            result['Country'] = self.country
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.province_code is not None:
            result['ProvinceCode'] = self.province_code
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.station_name is not None:
            result['StationName'] = self.station_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adcode') is not None:
            self.adcode = m.get('Adcode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Cnty') is not None:
            self.cnty = m.get('Cnty')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProvinceCode') is not None:
            self.province_code = m.get('ProvinceCode')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('StationName') is not None:
            self.station_name = m.get('StationName')
        return self


class ApeProvinceStationRefResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # rt
        self.rt = rt
        # success
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


class ApeProvinceStationRefResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApeProvinceStationRefResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApeProvinceStationRefResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HistoricalRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        order_id: str = None,
        page_num: int = None,
        page_size: int = None,
        start_time: str = None,
        station: str = None,
    ):
        # endTime
        self.end_time = end_time
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id
        # pageNum
        self.page_num = page_num
        # pageSize
        self.page_size = page_size
        # startTime
        self.start_time = start_time
        # 全国（入参单一站点）
        self.station = station

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.station is not None:
            result['Station'] = self.station
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Station') is not None:
            self.station = m.get('Station')
        return self


class HistoricalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # rt
        self.rt = rt
        # success
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


class HistoricalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HistoricalResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = HistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StationDayRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        start_forecast: str = None,
        station: str = None,
    ):
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id
        # 气象预测开始时间
        self.start_forecast = start_forecast
        # 全国站点（入参单一站点）
        self.station = station

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.start_forecast is not None:
            result['StartForecast'] = self.start_forecast
        if self.station is not None:
            result['Station'] = self.station
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('StartForecast') is not None:
            self.start_forecast = m.get('StartForecast')
        if m.get('Station') is not None:
            self.station = m.get('Station')
        return self


class StationDayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # rt
        self.rt = rt
        # success
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


class StationDayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StationDayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StationDayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WeatherforecastRequest(TeaModel):
    def __init__(
        self,
        lat: str = None,
        lon: str = None,
        order_id: str = None,
        start_forecast: str = None,
    ):
        # 纬度，范围为（15°N~59.95°N）
        self.lat = lat
        # 经度，范围为（70°E~139.96°E）
        self.lon = lon
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id
        # yyyymmdd080000或yyyymmdd200000
        self.start_forecast = start_forecast

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lat is not None:
            result['Lat'] = self.lat
        if self.lon is not None:
            result['Lon'] = self.lon
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.start_forecast is not None:
            result['StartForecast'] = self.start_forecast
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('StartForecast') is not None:
            self.start_forecast = m.get('StartForecast')
        return self


class WeatherforecastResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # rt
        self.rt = rt
        # success
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


class WeatherforecastResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WeatherforecastResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = WeatherforecastResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WeatherforecastTimeRequest(TeaModel):
    def __init__(
        self,
        cur_hour: str = None,
        lat: str = None,
        lon: str = None,
        order_id: str = None,
    ):
        # 20210809090000
        self.cur_hour = cur_hour
        # 纬度，范围为（15°N~59.95°N
        self.lat = lat
        # 经度，范围为（70°E~139.96°E）
        self.lon = lon
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_hour is not None:
            result['CurHour'] = self.cur_hour
        if self.lat is not None:
            result['Lat'] = self.lat
        if self.lon is not None:
            result['Lon'] = self.lon
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurHour') is not None:
            self.cur_hour = m.get('CurHour')
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class WeatherforecastTimeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # rt
        self.rt = rt
        # success
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


class WeatherforecastTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WeatherforecastTimeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = WeatherforecastTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WeathermonitorRequest(TeaModel):
    def __init__(
        self,
        cur_hour: str = None,
        order_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # 气象实况时间 yyyymmddhh0000 （数据最小时间2021-08-16）（小时）	20210817120000
        self.cur_hour = cur_hour
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id
        # 页码
        self.page_num = page_num
        # 页面条数
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_hour is not None:
            result['CurHour'] = self.cur_hour
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurHour') is not None:
            self.cur_hour = m.get('CurHour')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class WeathermonitorResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        request_id: str = None,
        rt: int = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # rt
        self.rt = rt
        # success
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


class WeathermonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WeathermonitorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = WeathermonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


