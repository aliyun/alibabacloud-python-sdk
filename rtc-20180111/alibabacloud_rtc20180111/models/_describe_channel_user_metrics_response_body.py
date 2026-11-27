# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeChannelUserMetricsResponseBody(DaraModel):
    def __init__(
        self,
        metric_datas: List[main_models.DescribeChannelUserMetricsResponseBodyMetricDatas] = None,
        overall_data: main_models.DescribeChannelUserMetricsResponseBodyOverallData = None,
        request_id: str = None,
    ):
        # The metric data list.
        self.metric_datas = metric_datas
        # The overview data.
        self.overall_data = overall_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.metric_datas:
            for v1 in self.metric_datas:
                 if v1:
                    v1.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetricDatas'] = []
        if self.metric_datas is not None:
            for k1 in self.metric_datas:
                result['MetricDatas'].append(k1.to_map() if k1 else None)

        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_datas = []
        if m.get('MetricDatas') is not None:
            for k1 in m.get('MetricDatas'):
                temp_model = main_models.DescribeChannelUserMetricsResponseBodyMetricDatas()
                self.metric_datas.append(temp_model.from_map(k1))

        if m.get('OverallData') is not None:
            temp_model = main_models.DescribeChannelUserMetricsResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m.get('OverallData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeChannelUserMetricsResponseBodyOverallData(DaraModel):
    def __init__(
        self,
        total_bad_exp_num: int = None,
        total_join_fail_num: int = None,
        total_pub_user_num: int = None,
        total_sub_user_num: int = None,
        total_user_num: int = None,
    ):
        # The total number of users with abnormal communication experience.
        self.total_bad_exp_num = total_bad_exp_num
        # The total number of users who failed to join the channel.
        self.total_join_fail_num = total_join_fail_num
        # The total number of publishing users.
        self.total_pub_user_num = total_pub_user_num
        # The total number of subscribing users.
        self.total_sub_user_num = total_sub_user_num
        # The total number of users.
        self.total_user_num = total_user_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_bad_exp_num is not None:
            result['TotalBadExpNum'] = self.total_bad_exp_num

        if self.total_join_fail_num is not None:
            result['TotalJoinFailNum'] = self.total_join_fail_num

        if self.total_pub_user_num is not None:
            result['TotalPubUserNum'] = self.total_pub_user_num

        if self.total_sub_user_num is not None:
            result['TotalSubUserNum'] = self.total_sub_user_num

        if self.total_user_num is not None:
            result['TotalUserNum'] = self.total_user_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalBadExpNum') is not None:
            self.total_bad_exp_num = m.get('TotalBadExpNum')

        if m.get('TotalJoinFailNum') is not None:
            self.total_join_fail_num = m.get('TotalJoinFailNum')

        if m.get('TotalPubUserNum') is not None:
            self.total_pub_user_num = m.get('TotalPubUserNum')

        if m.get('TotalSubUserNum') is not None:
            self.total_sub_user_num = m.get('TotalSubUserNum')

        if m.get('TotalUserNum') is not None:
            self.total_user_num = m.get('TotalUserNum')

        return self

class DescribeChannelUserMetricsResponseBodyMetricDatas(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeChannelUserMetricsResponseBodyMetricDatasNodes] = None,
        type: str = None,
    ):
        # The list of coordinate points in the metric trends chart.
        self.nodes = nodes
        # The metric type. Valid values:
        # - **ALL_NUM**: the number of users per unit of time.
        # - **PUB_NUM**: the number of publishing users per unit of time.
        # - **SUB_NUM**: the number of subscribing users per unit of time.
        # - **JOIN_FAIL_NUM**: the number of users who failed to join the channel per unit of time.
        # - **BAD_EXP_NUM**: the number of users with abnormal communication experience per unit of time.
        self.type = type

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeChannelUserMetricsResponseBodyMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeChannelUserMetricsResponseBodyMetricDatasNodes(DaraModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        # The extended properties.
        self.ext = ext
        # The x-axis coordinate in the metric trends chart.
        self.x = x
        # The y-axis coordinate in the metric trends chart.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

