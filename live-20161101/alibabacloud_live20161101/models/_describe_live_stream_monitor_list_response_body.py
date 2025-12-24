# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamMonitorListResponseBody(DaraModel):
    def __init__(
        self,
        live_stream_monitor_list: List[main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The list of monitoring sessions.
        self.live_stream_monitor_list = live_stream_monitor_list
        # The request ID.
        self.request_id = request_id
        # The number of monitoring sessions.
        self.total = total

    def validate(self):
        if self.live_stream_monitor_list:
            for v1 in self.live_stream_monitor_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamMonitorList'] = []
        if self.live_stream_monitor_list is not None:
            for k1 in self.live_stream_monitor_list:
                result['LiveStreamMonitorList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_monitor_list = []
        if m.get('LiveStreamMonitorList') is not None:
            for k1 in m.get('LiveStreamMonitorList'):
                temp_model = main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorList()
                self.live_stream_monitor_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorList(DaraModel):
    def __init__(
        self,
        audio_from: int = None,
        callback_url: str = None,
        ding_talk_web_hook_url: str = None,
        domain: str = None,
        input_list: List[main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListInputList] = None,
        monitor_config: str = None,
        monitor_id: str = None,
        monitor_name: str = None,
        output_template: str = None,
        output_urls: main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListOutputUrls = None,
        region: str = None,
        start_time: str = None,
        status: int = None,
        stop_time: str = None,
    ):
        # The audio source in the layout.
        self.audio_from = audio_from
        # The callback URL that sends monitoring alerts.
        self.callback_url = callback_url
        # The URL of the DingTalk chatbot.
        self.ding_talk_web_hook_url = ding_talk_web_hook_url
        # The domain name.
        self.domain = domain
        # The list of monitored input streams.
        self.input_list = input_list
        # The monitoring alert thresholds. The following fields are included:
        # 
        # *   fpsLowThres: the video frame rate alert threshold. The value is a floating-point number.
        # *   brHighThres: the audio/video bitrate alert threshold. The value is a floating-point number.
        # *   eofDurationThresSec: the interruption duration alert threshold. The value is a floating-point number.
        self.monitor_config = monitor_config
        # The ID of the monitoring session.
        self.monitor_id = monitor_id
        # The name of the monitoring session.
        self.monitor_name = monitor_name
        # The output resolution template. Valid values:
        # 
        # *   **lp_ld**: low definition
        # *   **lp_sd**: standard definition
        # *   **lp_hd**: high definition
        # *   **lp_ud**: ultra-high definition
        self.output_template = output_template
        # The output URLs.
        self.output_urls = output_urls
        # The ID of the region. Valid values:
        # 
        # *   cn-shanghai: China (Shanghai)
        # *   cn-beijing: China (Beijing)
        # *   ap-southeast-1: Singapore
        self.region = region
        # The start time of live monitoring. The time is displayed in UTC.
        self.start_time = start_time
        # The status of the monitoring session. Valid values:
        # 
        # *   1: Monitoring
        # *   0: Unmonitored
        self.status = status
        # The end time of live monitoring. The time is displayed in UTC.
        self.stop_time = stop_time

    def validate(self):
        if self.input_list:
            for v1 in self.input_list:
                 if v1:
                    v1.validate()
        if self.output_urls:
            self.output_urls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_from is not None:
            result['AudioFrom'] = self.audio_from

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.ding_talk_web_hook_url is not None:
            result['DingTalkWebHookUrl'] = self.ding_talk_web_hook_url

        if self.domain is not None:
            result['Domain'] = self.domain

        result['InputList'] = []
        if self.input_list is not None:
            for k1 in self.input_list:
                result['InputList'].append(k1.to_map() if k1 else None)

        if self.monitor_config is not None:
            result['MonitorConfig'] = self.monitor_config

        if self.monitor_id is not None:
            result['MonitorId'] = self.monitor_id

        if self.monitor_name is not None:
            result['MonitorName'] = self.monitor_name

        if self.output_template is not None:
            result['OutputTemplate'] = self.output_template

        if self.output_urls is not None:
            result['OutputUrls'] = self.output_urls.to_map()

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioFrom') is not None:
            self.audio_from = m.get('AudioFrom')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('DingTalkWebHookUrl') is not None:
            self.ding_talk_web_hook_url = m.get('DingTalkWebHookUrl')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        self.input_list = []
        if m.get('InputList') is not None:
            for k1 in m.get('InputList'):
                temp_model = main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListInputList()
                self.input_list.append(temp_model.from_map(k1))

        if m.get('MonitorConfig') is not None:
            self.monitor_config = m.get('MonitorConfig')

        if m.get('MonitorId') is not None:
            self.monitor_id = m.get('MonitorId')

        if m.get('MonitorName') is not None:
            self.monitor_name = m.get('MonitorName')

        if m.get('OutputTemplate') is not None:
            self.output_template = m.get('OutputTemplate')

        if m.get('OutputUrls') is not None:
            temp_model = main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListOutputUrls()
            self.output_urls = temp_model.from_map(m.get('OutputUrls'))

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        return self

class DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListOutputUrls(DaraModel):
    def __init__(
        self,
        flv_url: str = None,
        rtmp_url: str = None,
    ):
        # The output URL in the Flash Video (FLV) format.
        self.flv_url = flv_url
        # The output URL in the Real-Time Messaging Protocol (RTMP) format.
        self.rtmp_url = rtmp_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flv_url is not None:
            result['FlvUrl'] = self.flv_url

        if self.rtmp_url is not None:
            result['RtmpUrl'] = self.rtmp_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlvUrl') is not None:
            self.flv_url = m.get('FlvUrl')

        if m.get('RtmpUrl') is not None:
            self.rtmp_url = m.get('RtmpUrl')

        return self

class DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListInputList(DaraModel):
    def __init__(
        self,
        index: int = None,
        input_url: str = None,
        layout_config: main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListInputListLayoutConfig = None,
        layout_id: int = None,
        play_config: main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListInputListPlayConfig = None,
        stream_name: str = None,
    ):
        # The index.
        self.index = index
        # The URL of the input stream.
        self.input_url = input_url
        # The layout information.
        self.layout_config = layout_config
        # The layout ID, which must start from 1.
        self.layout_id = layout_id
        # The playback configurations.
        self.play_config = play_config
        # The display name of the monitored stream.
        self.stream_name = stream_name

    def validate(self):
        if self.layout_config:
            self.layout_config.validate()
        if self.play_config:
            self.play_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.input_url is not None:
            result['InputUrl'] = self.input_url

        if self.layout_config is not None:
            result['LayoutConfig'] = self.layout_config.to_map()

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.play_config is not None:
            result['PlayConfig'] = self.play_config.to_map()

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('InputUrl') is not None:
            self.input_url = m.get('InputUrl')

        if m.get('LayoutConfig') is not None:
            temp_model = main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListInputListLayoutConfig()
            self.layout_config = temp_model.from_map(m.get('LayoutConfig'))

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('PlayConfig') is not None:
            temp_model = main_models.DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListInputListPlayConfig()
            self.play_config = temp_model.from_map(m.get('PlayConfig'))

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

class DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListInputListPlayConfig(DaraModel):
    def __init__(
        self,
        volume_rate: float = None,
    ):
        # The volume. Valid values: 0 to 1. The value is rounded to two decimal places.
        self.volume_rate = volume_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.volume_rate is not None:
            result['VolumeRate'] = self.volume_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VolumeRate') is not None:
            self.volume_rate = m.get('VolumeRate')

        return self

class DescribeLiveStreamMonitorListResponseBodyLiveStreamMonitorListInputListLayoutConfig(DaraModel):
    def __init__(
        self,
        fill_mode: str = None,
        position_normalized: List[float] = None,
        position_refer: str = None,
        size_normalized: List[float] = None,
    ):
        # The fill type. Set this value to none.
        self.fill_mode = fill_mode
        # The position of the layer, in the format of [unk][x,y][unk]. The values of x and y need to be normalized.
        self.position_normalized = position_normalized
        # The reference position of the element. Valid values:
        # 
        # *   topLeft
        # *   topRight
        # *   bottomLeft
        # *   bottomRight
        self.position_refer = position_refer
        # The size of the layer. Unit: bytes.
        self.size_normalized = size_normalized

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fill_mode is not None:
            result['FillMode'] = self.fill_mode

        if self.position_normalized is not None:
            result['PositionNormalized'] = self.position_normalized

        if self.position_refer is not None:
            result['PositionRefer'] = self.position_refer

        if self.size_normalized is not None:
            result['SizeNormalized'] = self.size_normalized

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FillMode') is not None:
            self.fill_mode = m.get('FillMode')

        if m.get('PositionNormalized') is not None:
            self.position_normalized = m.get('PositionNormalized')

        if m.get('PositionRefer') is not None:
            self.position_refer = m.get('PositionRefer')

        if m.get('SizeNormalized') is not None:
            self.size_normalized = m.get('SizeNormalized')

        return self

