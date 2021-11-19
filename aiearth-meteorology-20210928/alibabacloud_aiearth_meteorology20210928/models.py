# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class GridQueryRequest(TeaModel):
    def __init__(
        self,
        element: str = None,
        forecast_timestamp: str = None,
        latitude: float = None,
        longitude: float = None,
        page_no: int = None,
        page_size: int = None,
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
        # 分页编号
        self.page_no = page_no
        # 分页大小
        self.page_size = page_size
        # 产品
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
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
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
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('reportTimestamp') is not None:
            self.report_timestamp = m.get('reportTimestamp')
        return self


class GridQueryResponseBodyModuleList(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        element: str = None,
        element_unit: str = None,
        forecast_timestamp: str = None,
        latitude: float = None,
        longitude: float = None,
        report_timestamp: str = None,
        value: float = None,
    ):
        # 数据类型
        self.data_type = data_type
        # 要素
        self.element = element
        # 要素单位
        self.element_unit = element_unit
        # 预报时间
        self.forecast_timestamp = forecast_timestamp
        # 查询点纬度
        self.latitude = latitude
        # 查询点经度
        self.longitude = longitude
        # 起报时间
        self.report_timestamp = report_timestamp
        # 当前网格值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.element is not None:
            result['element'] = self.element
        if self.element_unit is not None:
            result['elementUnit'] = self.element_unit
        if self.forecast_timestamp is not None:
            result['forecastTimestamp'] = self.forecast_timestamp
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.report_timestamp is not None:
            result['reportTimestamp'] = self.report_timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('elementUnit') is not None:
            self.element_unit = m.get('elementUnit')
        if m.get('forecastTimestamp') is not None:
            self.forecast_timestamp = m.get('forecastTimestamp')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('reportTimestamp') is not None:
            self.report_timestamp = m.get('reportTimestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GridQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        list: List[GridQueryResponseBodyModuleList] = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # 分页结果列表
        self.list = list
        # 分页编号
        self.page_no = page_no
        # 分页大小
        self.page_size = page_size

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
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GridQueryResponseBodyModuleList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GridQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: GridQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 响应码
        self.code = code
        # 响应信息
        self.message = message
        # 响应结果
        self.module = module
        # Id of the request
        self.request_id = request_id
        # 请求是否成功
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('module') is not None:
            temp_model = GridQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GridQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GridQueryResponseBody = None,
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
            temp_model = GridQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


