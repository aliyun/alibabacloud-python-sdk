# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeHighRiskPieChartResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeHighRiskPieChartResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Status code
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error details
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned object
        self.result_object = result_object
        # Whether the request was successful.
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DescribeHighRiskPieChartResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        high_risk_ipcity: main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCity = None,
        high_risk_ipprovince: main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvince = None,
        high_risk_mobile_city: main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCity = None,
        high_risk_mobile_province: main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvince = None,
    ):
        # High-risk IP city
        self.high_risk_ipcity = high_risk_ipcity
        # High-risk IP归属province
        self.high_risk_ipprovince = high_risk_ipprovince
        # High-risk mobile phone归属city
        self.high_risk_mobile_city = high_risk_mobile_city
        # High-risk mobile phone\\"s province of origin
        self.high_risk_mobile_province = high_risk_mobile_province

    def validate(self):
        if self.high_risk_ipcity:
            self.high_risk_ipcity.validate()
        if self.high_risk_ipprovince:
            self.high_risk_ipprovince.validate()
        if self.high_risk_mobile_city:
            self.high_risk_mobile_city.validate()
        if self.high_risk_mobile_province:
            self.high_risk_mobile_province.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.high_risk_ipcity is not None:
            result['highRiskIPCity'] = self.high_risk_ipcity.to_map()

        if self.high_risk_ipprovince is not None:
            result['highRiskIPProvince'] = self.high_risk_ipprovince.to_map()

        if self.high_risk_mobile_city is not None:
            result['highRiskMobileCity'] = self.high_risk_mobile_city.to_map()

        if self.high_risk_mobile_province is not None:
            result['highRiskMobileProvince'] = self.high_risk_mobile_province.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('highRiskIPCity') is not None:
            temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCity()
            self.high_risk_ipcity = temp_model.from_map(m.get('highRiskIPCity'))

        if m.get('highRiskIPProvince') is not None:
            temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvince()
            self.high_risk_ipprovince = temp_model.from_map(m.get('highRiskIPProvince'))

        if m.get('highRiskMobileCity') is not None:
            temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCity()
            self.high_risk_mobile_city = temp_model.from_map(m.get('highRiskMobileCity'))

        if m.get('highRiskMobileProvince') is not None:
            temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvince()
            self.high_risk_mobile_province = temp_model.from_map(m.get('highRiskMobileProvince'))

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvince(DaraModel):
    def __init__(
        self,
        animation: bool = None,
        grid: main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvinceGrid = None,
        series: List[main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvinceSeries] = None,
    ):
        # Indicator, default true
        self.animation = animation
        # Belongs to grid.
        self.grid = grid
        # Chart data
        self.series = series

    def validate(self):
        if self.grid:
            self.grid.validate()
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.animation is not None:
            result['animation'] = self.animation

        if self.grid is not None:
            result['grid'] = self.grid.to_map()

        result['series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['series'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('animation') is not None:
            self.animation = m.get('animation')

        if m.get('grid') is not None:
            temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvinceGrid()
            self.grid = temp_model.from_map(m.get('grid'))

        self.series = []
        if m.get('series') is not None:
            for k1 in m.get('series'):
                temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvinceSeries()
                self.series.append(temp_model.from_map(k1))

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvinceSeries(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvinceSeriesData] = None,
        name: str = None,
        rose_type: str = None,
    ):
        # High-risk position data.
        self.data = data
        # Display title
        self.name = name
        # Chart identifier, default false
        self.rose_type = rose_type

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.rose_type is not None:
            result['roseType'] = self.rose_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvinceSeriesData()
                self.data.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('roseType') is not None:
            self.rose_type = m.get('roseType')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvinceSeriesData(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # Field name
        self.name = name
        # Data value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileProvinceGrid(DaraModel):
    def __init__(
        self,
        show: bool = None,
    ):
        # Chart flag, default is false
        self.show = show

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show is not None:
            result['show'] = self.show

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('show') is not None:
            self.show = m.get('show')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCity(DaraModel):
    def __init__(
        self,
        animation: bool = None,
        grid: main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCityGrid = None,
        series: List[main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCitySeries] = None,
    ):
        # Chart flag, default is true
        self.animation = animation
        # Belongs to grid.
        self.grid = grid
        # Chart data
        self.series = series

    def validate(self):
        if self.grid:
            self.grid.validate()
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.animation is not None:
            result['animation'] = self.animation

        if self.grid is not None:
            result['grid'] = self.grid.to_map()

        result['series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['series'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('animation') is not None:
            self.animation = m.get('animation')

        if m.get('grid') is not None:
            temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCityGrid()
            self.grid = temp_model.from_map(m.get('grid'))

        self.series = []
        if m.get('series') is not None:
            for k1 in m.get('series'):
                temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCitySeries()
                self.series.append(temp_model.from_map(k1))

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCitySeries(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCitySeriesData] = None,
        name: str = None,
        rose_type: str = None,
    ):
        # Returned data object
        self.data = data
        # Field name
        self.name = name
        # Chart flag, default is false
        self.rose_type = rose_type

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.rose_type is not None:
            result['roseType'] = self.rose_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCitySeriesData()
                self.data.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('roseType') is not None:
            self.rose_type = m.get('roseType')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCitySeriesData(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # Field name
        self.name = name
        # Data value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskMobileCityGrid(DaraModel):
    def __init__(
        self,
        show: bool = None,
    ):
        # Chart flag, default is false
        self.show = show

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show is not None:
            result['show'] = self.show

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('show') is not None:
            self.show = m.get('show')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvince(DaraModel):
    def __init__(
        self,
        animation: bool = None,
        grid: main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvinceGrid = None,
        series: List[main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvinceSeries] = None,
    ):
        # Chart identifier, default is true
        self.animation = animation
        # Belonging grid.
        self.grid = grid
        # Chart data
        self.series = series

    def validate(self):
        if self.grid:
            self.grid.validate()
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.animation is not None:
            result['animation'] = self.animation

        if self.grid is not None:
            result['grid'] = self.grid.to_map()

        result['series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['series'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('animation') is not None:
            self.animation = m.get('animation')

        if m.get('grid') is not None:
            temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvinceGrid()
            self.grid = temp_model.from_map(m.get('grid'))

        self.series = []
        if m.get('series') is not None:
            for k1 in m.get('series'):
                temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvinceSeries()
                self.series.append(temp_model.from_map(k1))

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvinceSeries(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvinceSeriesData] = None,
        name: str = None,
        rose_type: str = None,
    ):
        # Returned data object
        self.data = data
        # Field name
        self.name = name
        # Chart identifier, default is false
        self.rose_type = rose_type

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.rose_type is not None:
            result['roseType'] = self.rose_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvinceSeriesData()
                self.data.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('roseType') is not None:
            self.rose_type = m.get('roseType')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvinceSeriesData(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # Variable name
        self.name = name
        # Data value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPProvinceGrid(DaraModel):
    def __init__(
        self,
        show: bool = None,
    ):
        # Chart identifier, default is false
        self.show = show

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show is not None:
            result['show'] = self.show

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('show') is not None:
            self.show = m.get('show')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCity(DaraModel):
    def __init__(
        self,
        animation: bool = None,
        grid: main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCityGrid = None,
        series: List[main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCitySeries] = None,
    ):
        # Chart flag, default true
        self.animation = animation
        # Belonging grid.
        self.grid = grid
        # Chart data
        self.series = series

    def validate(self):
        if self.grid:
            self.grid.validate()
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.animation is not None:
            result['animation'] = self.animation

        if self.grid is not None:
            result['grid'] = self.grid.to_map()

        result['series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['series'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('animation') is not None:
            self.animation = m.get('animation')

        if m.get('grid') is not None:
            temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCityGrid()
            self.grid = temp_model.from_map(m.get('grid'))

        self.series = []
        if m.get('series') is not None:
            for k1 in m.get('series'):
                temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCitySeries()
                self.series.append(temp_model.from_map(k1))

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCitySeries(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCitySeriesData] = None,
        name: str = None,
        rose_type: str = None,
    ):
        # Returned data object
        self.data = data
        # Field name
        self.name = name
        # Chart identifier, default is false
        self.rose_type = rose_type

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.rose_type is not None:
            result['roseType'] = self.rose_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCitySeriesData()
                self.data.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('roseType') is not None:
            self.rose_type = m.get('roseType')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCitySeriesData(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # Field name
        self.name = name
        # Data value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeHighRiskPieChartResponseBodyResultObjectHighRiskIPCityGrid(DaraModel):
    def __init__(
        self,
        show: bool = None,
    ):
        # Chart flag, default false
        self.show = show

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show is not None:
            result['show'] = self.show

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('show') is not None:
            self.show = m.get('show')

        return self

