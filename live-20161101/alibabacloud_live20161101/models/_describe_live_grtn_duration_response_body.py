# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveGrtnDurationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stream_detail_data: main_models.DescribeLiveGrtnDurationResponseBodyStreamDetailData = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the co-streaming usage data.
        self.stream_detail_data = stream_detail_data

    def validate(self):
        if self.stream_detail_data:
            self.stream_detail_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_detail_data is not None:
            result['StreamDetailData'] = self.stream_detail_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamDetailData') is not None:
            temp_model = main_models.DescribeLiveGrtnDurationResponseBodyStreamDetailData()
            self.stream_detail_data = temp_model.from_map(m.get('StreamDetailData'))

        return self

class DescribeLiveGrtnDurationResponseBodyStreamDetailData(DaraModel):
    def __init__(
        self,
        stream_data: List[main_models.DescribeLiveGrtnDurationResponseBodyStreamDetailDataStreamData] = None,
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
                temp_model = main_models.DescribeLiveGrtnDurationResponseBodyStreamDetailDataStreamData()
                self.stream_data.append(temp_model.from_map(k1))

        return self

class DescribeLiveGrtnDurationResponseBodyStreamDetailDataStreamData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        duration: int = None,
        media_profile: str = None,
        media_type: str = None,
        time_stamp: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The co-streaming duration. Unit: minutes.
        self.duration = duration
        # The media specification. Valid values:
        # 
        # *   0: audio-only. This is a basic specification.
        # *   480P: standard definition (SD). The video resolution is 640 × 480 or lower.
        # *   720P: high definition (HD). The video resolution is 1280 × 720 or lower.
        # *   1080P: full HD. The video resolution is 1920 × 1080 or lower.
        self.media_profile = media_profile
        # The media type. Valid values:
        # 
        # *   audio
        # *   video
        self.media_type = media_type
        # The timestamp of the returned data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.media_profile is not None:
            result['MediaProfile'] = self.media_profile

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('MediaProfile') is not None:
            self.media_profile = m.get('MediaProfile')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

