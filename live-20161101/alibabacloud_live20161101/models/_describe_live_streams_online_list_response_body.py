# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamsOnlineListResponseBody(DaraModel):
    def __init__(
        self,
        online_info: main_models.DescribeLiveStreamsOnlineListResponseBodyOnlineInfo = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The information about the live streams that are being ingested.
        self.online_info = online_info
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of streams that meet the specified conditions.
        self.total_num = total_num
        # The total number of pages returned.
        self.total_page = total_page

    def validate(self):
        if self.online_info:
            self.online_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.online_info is not None:
            result['OnlineInfo'] = self.online_info.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineInfo') is not None:
            temp_model = main_models.DescribeLiveStreamsOnlineListResponseBodyOnlineInfo()
            self.online_info = temp_model.from_map(m.get('OnlineInfo'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeLiveStreamsOnlineListResponseBodyOnlineInfo(DaraModel):
    def __init__(
        self,
        live_stream_online_info: List[main_models.DescribeLiveStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo] = None,
    ):
        self.live_stream_online_info = live_stream_online_info

    def validate(self):
        if self.live_stream_online_info:
            for v1 in self.live_stream_online_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamOnlineInfo'] = []
        if self.live_stream_online_info is not None:
            for k1 in self.live_stream_online_info:
                result['LiveStreamOnlineInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_online_info = []
        if m.get('LiveStreamOnlineInfo') is not None:
            for k1 in m.get('LiveStreamOnlineInfo'):
                temp_model = main_models.DescribeLiveStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo()
                self.live_stream_online_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        audio_codec_id: int = None,
        audio_data_rate: int = None,
        client_ip: str = None,
        domain_name: str = None,
        frame_rate: int = None,
        height: int = None,
        publish_domain: str = None,
        publish_time: str = None,
        publish_type: str = None,
        publish_url: str = None,
        server_ip: str = None,
        stream_name: str = None,
        transcoded: str = None,
        video_codec_id: int = None,
        video_data_rate: int = None,
        width: int = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The ID of the audio codec.
        self.audio_codec_id = audio_codec_id
        # The audio bitrate of the live stream. Unit: Kbit/s.
        # 
        # >  This parameter can be returned after you submit a ticket for whitelist configuration. For more information about how to submit a ticket, see Contact us.
        self.audio_data_rate = audio_data_rate
        # The IP address of the client for stream ingest.
        self.client_ip = client_ip
        # The main streaming domain.
        self.domain_name = domain_name
        # The frame rate. Unit: FPS.
        self.frame_rate = frame_rate
        # The height of the video resolution. Unit: pixels.
        self.height = height
        # The ingest domain. If live center ingest was used, the streaming domain is returned.
        self.publish_domain = publish_domain
        # The start time of stream ingest. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.publish_time = publish_time
        # The ingest type. Valid values:
        # 
        # *   **edge**: edge ingest.
        # *   **center**: live center ingest.
        self.publish_type = publish_type
        # The complete URL that was used to ingest the stream.
        self.publish_url = publish_url
        # The IP address of the ingest node.
        self.server_ip = server_ip
        # The name of the live stream.
        self.stream_name = stream_name
        # Indicates whether the stream was transcoded. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.transcoded = transcoded
        # The ID of the video codec.
        self.video_codec_id = video_codec_id
        # The video bitrate of the live stream. Unit: Kbit/s.
        # 
        # >  This parameter can be returned after you submit a ticket for whitelist configuration. For more information about how to submit a ticket, see Contact us.
        self.video_data_rate = video_data_rate
        # The width of the video resolution. Unit: pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.audio_codec_id is not None:
            result['AudioCodecId'] = self.audio_codec_id

        if self.audio_data_rate is not None:
            result['AudioDataRate'] = self.audio_data_rate

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        if self.height is not None:
            result['Height'] = self.height

        if self.publish_domain is not None:
            result['PublishDomain'] = self.publish_domain

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.transcoded is not None:
            result['Transcoded'] = self.transcoded

        if self.video_codec_id is not None:
            result['VideoCodecId'] = self.video_codec_id

        if self.video_data_rate is not None:
            result['VideoDataRate'] = self.video_data_rate

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AudioCodecId') is not None:
            self.audio_codec_id = m.get('AudioCodecId')

        if m.get('AudioDataRate') is not None:
            self.audio_data_rate = m.get('AudioDataRate')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('PublishDomain') is not None:
            self.publish_domain = m.get('PublishDomain')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Transcoded') is not None:
            self.transcoded = m.get('Transcoded')

        if m.get('VideoCodecId') is not None:
            self.video_codec_id = m.get('VideoCodecId')

        if m.get('VideoDataRate') is not None:
            self.video_data_rate = m.get('VideoDataRate')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

