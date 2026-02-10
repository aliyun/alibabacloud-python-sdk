# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeChartDataResponseBody(DaraModel):
    def __init__(
        self,
        all_chart_sub_type_list: List[main_models.DescribeChartDataResponseBodyAllChartSubTypeList] = None,
        chart_data_type: str = None,
        chart_sub_type_list: List[str] = None,
        chart_type: str = None,
        coordinate_data: main_models.DescribeChartDataResponseBodyCoordinateData = None,
        multiple_data: List[main_models.DescribeChartDataResponseBodyMultipleData] = None,
        property_array_value: str = None,
        property_value: str = None,
        propery_array_value: str = None,
        request_id: str = None,
        single_data: main_models.DescribeChartDataResponseBodySingleData = None,
    ):
        # The valid values for all subtypes of the chart.
        self.all_chart_sub_type_list = all_chart_sub_type_list
        # The data type of the chart. Valid values:
        # 
        # *   **commonCoordinate**
        # *   **timeCoordinate**
        # *   **multipleValue**
        # *   **singleValue**
        # *   **propertyValue**
        # *   **propertyArrayValue**
        self.chart_data_type = chart_data_type
        # The subtype values in which the chart is selected.
        self.chart_sub_type_list = chart_sub_type_list
        # The type of the chart. Valid values:
        # 
        # *   **timeLine**
        # *   **timeBar**
        # *   **bar**
        # *   **line**
        # *   **pie**
        # *   **gauge**
        # *   **table**
        # *   **text**
        self.chart_type = chart_type
        # The coordinate data.
        self.coordinate_data = coordinate_data
        # The values in the multi-value charts.
        self.multiple_data = multiple_data
        # The attribute value of the array chart.
        self.property_array_value = property_array_value
        # The data of the chart.
        self.property_value = property_value
        # The array data of the chart.
        self.propery_array_value = propery_array_value
        # The request ID.
        self.request_id = request_id
        # The data of the single value chart.
        self.single_data = single_data

    def validate(self):
        if self.all_chart_sub_type_list:
            for v1 in self.all_chart_sub_type_list:
                 if v1:
                    v1.validate()
        if self.coordinate_data:
            self.coordinate_data.validate()
        if self.multiple_data:
            for v1 in self.multiple_data:
                 if v1:
                    v1.validate()
        if self.single_data:
            self.single_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AllChartSubTypeList'] = []
        if self.all_chart_sub_type_list is not None:
            for k1 in self.all_chart_sub_type_list:
                result['AllChartSubTypeList'].append(k1.to_map() if k1 else None)

        if self.chart_data_type is not None:
            result['ChartDataType'] = self.chart_data_type

        if self.chart_sub_type_list is not None:
            result['ChartSubTypeList'] = self.chart_sub_type_list

        if self.chart_type is not None:
            result['ChartType'] = self.chart_type

        if self.coordinate_data is not None:
            result['CoordinateData'] = self.coordinate_data.to_map()

        result['MultipleData'] = []
        if self.multiple_data is not None:
            for k1 in self.multiple_data:
                result['MultipleData'].append(k1.to_map() if k1 else None)

        if self.property_array_value is not None:
            result['PropertyArrayValue'] = self.property_array_value

        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        if self.propery_array_value is not None:
            result['ProperyArrayValue'] = self.propery_array_value

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.single_data is not None:
            result['SingleData'] = self.single_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_chart_sub_type_list = []
        if m.get('AllChartSubTypeList') is not None:
            for k1 in m.get('AllChartSubTypeList'):
                temp_model = main_models.DescribeChartDataResponseBodyAllChartSubTypeList()
                self.all_chart_sub_type_list.append(temp_model.from_map(k1))

        if m.get('ChartDataType') is not None:
            self.chart_data_type = m.get('ChartDataType')

        if m.get('ChartSubTypeList') is not None:
            self.chart_sub_type_list = m.get('ChartSubTypeList')

        if m.get('ChartType') is not None:
            self.chart_type = m.get('ChartType')

        if m.get('CoordinateData') is not None:
            temp_model = main_models.DescribeChartDataResponseBodyCoordinateData()
            self.coordinate_data = temp_model.from_map(m.get('CoordinateData'))

        self.multiple_data = []
        if m.get('MultipleData') is not None:
            for k1 in m.get('MultipleData'):
                temp_model = main_models.DescribeChartDataResponseBodyMultipleData()
                self.multiple_data.append(temp_model.from_map(k1))

        if m.get('PropertyArrayValue') is not None:
            self.property_array_value = m.get('PropertyArrayValue')

        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        if m.get('ProperyArrayValue') is not None:
            self.propery_array_value = m.get('ProperyArrayValue')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SingleData') is not None:
            temp_model = main_models.DescribeChartDataResponseBodySingleData()
            self.single_data = temp_model.from_map(m.get('SingleData'))

        return self

class DescribeChartDataResponseBodySingleData(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: int = None,
    ):
        # The name of the data type.
        self.name = name
        # The type of the data.
        self.type = type
        # The value in the single value chart.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeChartDataResponseBodyMultipleData(DaraModel):
    def __init__(
        self,
        color: str = None,
        name: str = None,
        type: str = None,
        value: int = None,
    ):
        # The font color, which is an RGBA value.
        self.color = color
        # The name of the data type.
        self.name = name
        # The type of the data.
        self.type = type
        # The attribute value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.color is not None:
            result['Color'] = self.color

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeChartDataResponseBodyCoordinateData(DaraModel):
    def __init__(
        self,
        xaxis: List[str] = None,
        yaxis_list: List[main_models.DescribeChartDataResponseBodyCoordinateDataYAxisList] = None,
    ):
        # The x-axis values.
        self.xaxis = xaxis
        # The y-axis values.
        self.yaxis_list = yaxis_list

    def validate(self):
        if self.yaxis_list:
            for v1 in self.yaxis_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.xaxis is not None:
            result['XAxis'] = self.xaxis

        result['YAxisList'] = []
        if self.yaxis_list is not None:
            for k1 in self.yaxis_list:
                result['YAxisList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XAxis') is not None:
            self.xaxis = m.get('XAxis')

        self.yaxis_list = []
        if m.get('YAxisList') is not None:
            for k1 in m.get('YAxisList'):
                temp_model = main_models.DescribeChartDataResponseBodyCoordinateDataYAxisList()
                self.yaxis_list.append(temp_model.from_map(k1))

        return self

class DescribeChartDataResponseBodyCoordinateDataYAxisList(DaraModel):
    def __init__(
        self,
        name: str = None,
        sub_type: str = None,
        type: str = None,
        value: List[str] = None,
    ):
        # The name of the data type.
        self.name = name
        # The subtype data of the chart.
        self.sub_type = sub_type
        # The type of the data.
        self.type = type
        # The values of the y-axis that corresponds to x-axis points.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeChartDataResponseBodyAllChartSubTypeList(DaraModel):
    def __init__(
        self,
        sub_type: str = None,
        sub_type_name: str = None,
    ):
        # The subtype of the chart.
        self.sub_type = sub_type
        # The name of the chart subtype.
        self.sub_type_name = sub_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.sub_type_name is not None:
            result['SubTypeName'] = self.sub_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('SubTypeName') is not None:
            self.sub_type_name = m.get('SubTypeName')

        return self

