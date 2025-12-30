# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitDynamicChartJobRequest(DaraModel):
    def __init__(
        self,
        axis_params: str = None,
        background: str = None,
        chart_config: str = None,
        chart_title: str = None,
        chart_type: str = None,
        data_source: str = None,
        description: str = None,
        input: str = None,
        output_config: str = None,
        subtitle: str = None,
        title: str = None,
        unit: str = None,
        user_data: str = None,
    ):
        # The axis configurations. If XAxisFontInterval is set to 0 or left empty, the system automatically determines an optimal interval.
        self.axis_params = axis_params
        # The chart background.
        self.background = background
        # The chart configurations.
        self.chart_config = chart_config
        # The chart title.
        self.chart_title = chart_title
        # The chart type.
        # 
        # Valid values:
        # 
        # *   Line: line chart
        # *   Histogram: bar chart
        # *   Pie: pie chart
        # 
        # This parameter is required.
        self.chart_type = chart_type
        # The data source.
        self.data_source = data_source
        # The job description.
        self.description = description
        # The input data for the chart.
        # 
        # This parameter is required.
        self.input = input
        # The output configurations.
        # 
        # This parameter is required.
        self.output_config = output_config
        # The subtitle.
        self.subtitle = subtitle
        # The job title.
        self.title = title
        # Unit
        self.unit = unit
        # The custom data in JSON format.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.axis_params is not None:
            result['AxisParams'] = self.axis_params

        if self.background is not None:
            result['Background'] = self.background

        if self.chart_config is not None:
            result['ChartConfig'] = self.chart_config

        if self.chart_title is not None:
            result['ChartTitle'] = self.chart_title

        if self.chart_type is not None:
            result['ChartType'] = self.chart_type

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.description is not None:
            result['Description'] = self.description

        if self.input is not None:
            result['Input'] = self.input

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.subtitle is not None:
            result['Subtitle'] = self.subtitle

        if self.title is not None:
            result['Title'] = self.title

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AxisParams') is not None:
            self.axis_params = m.get('AxisParams')

        if m.get('Background') is not None:
            self.background = m.get('Background')

        if m.get('ChartConfig') is not None:
            self.chart_config = m.get('ChartConfig')

        if m.get('ChartTitle') is not None:
            self.chart_title = m.get('ChartTitle')

        if m.get('ChartType') is not None:
            self.chart_type = m.get('ChartType')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('Subtitle') is not None:
            self.subtitle = m.get('Subtitle')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

