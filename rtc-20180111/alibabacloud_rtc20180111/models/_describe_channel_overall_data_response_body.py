# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeChannelOverallDataResponseBody(DaraModel):
    def __init__(
        self,
        call_info: main_models.DescribeChannelOverallDataResponseBodyCallInfo = None,
        metric_datas: List[main_models.DescribeChannelOverallDataResponseBodyMetricDatas] = None,
        overall_data: main_models.DescribeChannelOverallDataResponseBodyOverallData = None,
        request_id: str = None,
    ):
        self.call_info = call_info
        self.metric_datas = metric_datas
        self.overall_data = overall_data
        self.request_id = request_id

    def validate(self):
        if self.call_info:
            self.call_info.validate()
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
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()

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
        if m.get('CallInfo') is not None:
            temp_model = main_models.DescribeChannelOverallDataResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m.get('CallInfo'))

        self.metric_datas = []
        if m.get('MetricDatas') is not None:
            for k1 in m.get('MetricDatas'):
                temp_model = main_models.DescribeChannelOverallDataResponseBodyMetricDatas()
                self.metric_datas.append(temp_model.from_map(k1))

        if m.get('OverallData') is not None:
            temp_model = main_models.DescribeChannelOverallDataResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m.get('OverallData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeChannelOverallDataResponseBodyOverallData(DaraModel):
    def __init__(
        self,
        conn_avg_time: float = None,
        five_sec_join_rate: float = None,
        total_audio_stuck_rate: float = None,
        total_video_stuck_rate: float = None,
        total_video_vague_rate: float = None,
    ):
        self.conn_avg_time = conn_avg_time
        self.five_sec_join_rate = five_sec_join_rate
        self.total_audio_stuck_rate = total_audio_stuck_rate
        self.total_video_stuck_rate = total_video_stuck_rate
        self.total_video_vague_rate = total_video_vague_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_avg_time is not None:
            result['ConnAvgTime'] = self.conn_avg_time

        if self.five_sec_join_rate is not None:
            result['FiveSecJoinRate'] = self.five_sec_join_rate

        if self.total_audio_stuck_rate is not None:
            result['TotalAudioStuckRate'] = self.total_audio_stuck_rate

        if self.total_video_stuck_rate is not None:
            result['TotalVideoStuckRate'] = self.total_video_stuck_rate

        if self.total_video_vague_rate is not None:
            result['TotalVideoVagueRate'] = self.total_video_vague_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAvgTime') is not None:
            self.conn_avg_time = m.get('ConnAvgTime')

        if m.get('FiveSecJoinRate') is not None:
            self.five_sec_join_rate = m.get('FiveSecJoinRate')

        if m.get('TotalAudioStuckRate') is not None:
            self.total_audio_stuck_rate = m.get('TotalAudioStuckRate')

        if m.get('TotalVideoStuckRate') is not None:
            self.total_video_stuck_rate = m.get('TotalVideoStuckRate')

        if m.get('TotalVideoVagueRate') is not None:
            self.total_video_vague_rate = m.get('TotalVideoVagueRate')

        return self

class DescribeChannelOverallDataResponseBodyMetricDatas(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeChannelOverallDataResponseBodyMetricDatasNodes] = None,
        type: str = None,
    ):
        self.nodes = nodes
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
                temp_model = main_models.DescribeChannelOverallDataResponseBodyMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeChannelOverallDataResponseBodyMetricDatasNodes(DaraModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
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

class DescribeChannelOverallDataResponseBodyCallInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
    ):
        self.app_id = app_id
        self.call_status = call_status
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.call_status is not None:
            result['CallStatus'] = self.call_status

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts

        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts

        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')

        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

