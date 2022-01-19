# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DailyWeatherQueryRequest(TeaModel):
    def __init__(
        self,
        element: str = None,
        forecast_timestamp: str = None,
        latitude: float = None,
        location: str = None,
        longitude: float = None,
        product: str = None,
    ):
        # 要素
        self.element = element
        # 预报时间
        self.forecast_timestamp = forecast_timestamp
        # 纬度
        self.latitude = latitude
        # 位置
        self.location = location
        # 经度
        self.longitude = longitude
        # 产品代号
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.forecast_timestamp is not None:
            result['forecastTimestamp'] = self.forecast_timestamp
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.location is not None:
            result['location'] = self.location
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('forecastTimestamp') is not None:
            self.forecast_timestamp = m.get('forecastTimestamp')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class DailyWeatherQueryResponseBodyResultDataElements(TeaModel):
    def __init__(
        self,
        element: str = None,
        value: str = None,
    ):
        self.element = element
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DailyWeatherQueryResponseBodyResultData(TeaModel):
    def __init__(
        self,
        elements: List[DailyWeatherQueryResponseBodyResultDataElements] = None,
        forecast_timestamp: str = None,
    ):
        self.elements = elements
        self.forecast_timestamp = forecast_timestamp

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['elements'].append(k.to_map() if k else None)
        if self.forecast_timestamp is not None:
            result['forecastTimestamp'] = self.forecast_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('elements') is not None:
            for k in m.get('elements'):
                temp_model = DailyWeatherQueryResponseBodyResultDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('forecastTimestamp') is not None:
            self.forecast_timestamp = m.get('forecastTimestamp')
        return self


class DailyWeatherQueryResponseBodyResultLocation(TeaModel):
    def __init__(
        self,
        latitude: float = None,
        longitude: float = None,
    ):
        # 纬度
        self.latitude = latitude
        # 经度
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        return self


class DailyWeatherQueryResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[DailyWeatherQueryResponseBodyResultData] = None,
        location: DailyWeatherQueryResponseBodyResultLocation = None,
    ):
        self.data = data
        # 位置
        self.location = location

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.location is not None:
            result['location'] = self.location.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = DailyWeatherQueryResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('location') is not None:
            temp_model = DailyWeatherQueryResponseBodyResultLocation()
            self.location = temp_model.from_map(m['location'])
        return self


class DailyWeatherQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[DailyWeatherQueryResponseBodyResult] = None,
        success: bool = None,
    ):
        # 响应码
        self.code = code
        # 响应信息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 响应结果
        self.result = result
        # 请求是否成功
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DailyWeatherQueryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DailyWeatherQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DailyWeatherQueryResponseBody = None,
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
            temp_model = DailyWeatherQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GridWeatherQueryRequest(TeaModel):
    def __init__(
        self,
        element: str = None,
        forecast_timestamp: str = None,
        latitude: float = None,
        longitude: float = None,
        observation_timestamp: str = None,
        product: str = None,
        report_timestamp: str = None,
    ):
        # 要素
        self.element = element
        # 预报时间
        self.forecast_timestamp = forecast_timestamp
        # 纬度
        self.latitude = latitude
        # 经度
        self.longitude = longitude
        # 观测时间
        self.observation_timestamp = observation_timestamp
        # 产品代号
        self.product = product
        # 起报时间
        self.report_timestamp = report_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.forecast_timestamp is not None:
            result['forecastTimestamp'] = self.forecast_timestamp
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.observation_timestamp is not None:
            result['observationTimestamp'] = self.observation_timestamp
        if self.product is not None:
            result['product'] = self.product
        if self.report_timestamp is not None:
            result['reportTimestamp'] = self.report_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('forecastTimestamp') is not None:
            self.forecast_timestamp = m.get('forecastTimestamp')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('observationTimestamp') is not None:
            self.observation_timestamp = m.get('observationTimestamp')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('reportTimestamp') is not None:
            self.report_timestamp = m.get('reportTimestamp')
        return self


class GridWeatherQueryResponseBodyResultDataElements(TeaModel):
    def __init__(
        self,
        element: str = None,
        value: str = None,
    ):
        self.element = element
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GridWeatherQueryResponseBodyResultData(TeaModel):
    def __init__(
        self,
        elements: List[GridWeatherQueryResponseBodyResultDataElements] = None,
        forecast_timestamp: str = None,
        observation_timestamp: str = None,
    ):
        self.elements = elements
        # 预报时间
        self.forecast_timestamp = forecast_timestamp
        # 观测时间
        self.observation_timestamp = observation_timestamp

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['elements'].append(k.to_map() if k else None)
        if self.forecast_timestamp is not None:
            result['forecastTimestamp'] = self.forecast_timestamp
        if self.observation_timestamp is not None:
            result['observationTimestamp'] = self.observation_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('elements') is not None:
            for k in m.get('elements'):
                temp_model = GridWeatherQueryResponseBodyResultDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('forecastTimestamp') is not None:
            self.forecast_timestamp = m.get('forecastTimestamp')
        if m.get('observationTimestamp') is not None:
            self.observation_timestamp = m.get('observationTimestamp')
        return self


class GridWeatherQueryResponseBodyResultLocation(TeaModel):
    def __init__(
        self,
        latitude: float = None,
        longitude: float = None,
    ):
        # 纬度
        self.latitude = latitude
        # 经度
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        return self


class GridWeatherQueryResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[GridWeatherQueryResponseBodyResultData] = None,
        location: GridWeatherQueryResponseBodyResultLocation = None,
        report_timestamp: str = None,
    ):
        # 该位置的查询结果
        self.data = data
        # 位置
        self.location = location
        # 起报时间
        self.report_timestamp = report_timestamp

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.report_timestamp is not None:
            result['reportTimestamp'] = self.report_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GridWeatherQueryResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('location') is not None:
            temp_model = GridWeatherQueryResponseBodyResultLocation()
            self.location = temp_model.from_map(m['location'])
        if m.get('reportTimestamp') is not None:
            self.report_timestamp = m.get('reportTimestamp')
        return self


class GridWeatherQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[GridWeatherQueryResponseBodyResult] = None,
        success: bool = None,
    ):
        # 响应码
        self.code = code
        # 响应信息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 响应结果
        self.result = result
        # 请求是否成功
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GridWeatherQueryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GridWeatherQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GridWeatherQueryResponseBody = None,
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
            temp_model = GridWeatherQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


