# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamTranscodeMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        next_page_token: str = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        stream_detail_data: main_models.DescribeLiveStreamTranscodeMetricDataResponseBodyStreamDetailData = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # A pagination token. When you call this operation, up to 5,000 rows of data can be returned per query. If the number of rows exceeds 5,000, the response includes a pagination token that is used in the next request to retrieve a new page of results.
        # 
        # When you specify the token in the next query, data continues to be obtained from the end of the previous query.
        self.next_page_token = next_page_token
        # The number of rows returned.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range during which data was queried. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The data array returned.
        self.stream_detail_data = stream_detail_data

    def validate(self):
        if self.stream_detail_data:
            self.stream_detail_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_detail_data is not None:
            result['StreamDetailData'] = self.stream_detail_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamDetailData') is not None:
            temp_model = main_models.DescribeLiveStreamTranscodeMetricDataResponseBodyStreamDetailData()
            self.stream_detail_data = temp_model.from_map(m.get('StreamDetailData'))

        return self

class DescribeLiveStreamTranscodeMetricDataResponseBodyStreamDetailData(DaraModel):
    def __init__(
        self,
        stream_data: List[main_models.DescribeLiveStreamTranscodeMetricDataResponseBodyStreamDetailDataStreamData] = None,
    ):
        self.stream_data = stream_data

    def validate(self):
        if self.stream_data:
            for v1 in self.stream_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamData'] = []
        if self.stream_data is not None:
            for k1 in self.stream_data:
                result['StreamData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_data = []
        if m.get('StreamData') is not None:
            for k1 in m.get('StreamData'):
                temp_model = main_models.DescribeLiveStreamTranscodeMetricDataResponseBodyStreamDetailDataStreamData()
                self.stream_data.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamTranscodeMetricDataResponseBodyStreamDetailDataStreamData(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        duration: int = None,
        fps: str = None,
        region: str = None,
        resolution: str = None,
        stream_name: str = None,
        time_stamp: str = None,
        transcode_type: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The duration. Unit: seconds.
        self.duration = duration
        # The frame rate.
        # 
        # Valid values:
        # 
        # *   <!-- -->
        # 
        #     <!-- -->
        # 
        #     normal
        # 
        #     <!-- -->
        # 
        # *   <!-- -->
        # 
        #     <!-- -->
        # 
        #     high
        # 
        #     <!-- -->
        # 
        # *   <!-- -->
        # 
        #     <!-- -->
        # 
        #     def
        # 
        #     <!-- -->
        self.fps = fps
        # The region.
        self.region = region
        # The resolution. Valid values:
        # 
        # *   2K: 2K resolution
        # *   4K: 4K resolution
        # *   LD: low definition
        # *   SD: standard definition
        # *   HD: high definition
        # *   def: audio
        self.resolution = resolution
        # The name of the stream.
        self.stream_name = stream_name
        # The timestamp of the returned data.
        self.time_stamp = time_stamp
        # The transcoding type. Valid values:
        # 
        # *   H264STD: standard transcoding based on H.264
        # *   H264NBHD: Narrowband HD™ transcoding based on H.264
        # *   H265STD: standard transcoding based on H.265
        # *   AUDIO: audio transcoding
        self.transcode_type = transcode_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.region is not None:
            result['Region'] = self.region

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.transcode_type is not None:
            result['TranscodeType'] = self.transcode_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TranscodeType') is not None:
            self.transcode_type = m.get('TranscodeType')

        return self

