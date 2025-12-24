# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainStreamTranscodeDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transcode_data_list: main_models.DescribeLiveDomainStreamTranscodeDataResponseBodyTranscodeDataList = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The transcoding usage data returned at each interval.
        self.transcode_data_list = transcode_data_list

    def validate(self):
        if self.transcode_data_list:
            self.transcode_data_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transcode_data_list is not None:
            result['TranscodeDataList'] = self.transcode_data_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TranscodeDataList') is not None:
            temp_model = main_models.DescribeLiveDomainStreamTranscodeDataResponseBodyTranscodeDataList()
            self.transcode_data_list = temp_model.from_map(m.get('TranscodeDataList'))

        return self

class DescribeLiveDomainStreamTranscodeDataResponseBodyTranscodeDataList(DaraModel):
    def __init__(
        self,
        transcode_data: List[main_models.DescribeLiveDomainStreamTranscodeDataResponseBodyTranscodeDataListTranscodeData] = None,
    ):
        self.transcode_data = transcode_data

    def validate(self):
        if self.transcode_data:
            for v1 in self.transcode_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TranscodeData'] = []
        if self.transcode_data is not None:
            for k1 in self.transcode_data:
                result['TranscodeData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.transcode_data = []
        if m.get('TranscodeData') is not None:
            for k1 in m.get('TranscodeData'):
                temp_model = main_models.DescribeLiveDomainStreamTranscodeDataResponseBodyTranscodeDataListTranscodeData()
                self.transcode_data.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainStreamTranscodeDataResponseBodyTranscodeDataListTranscodeData(DaraModel):
    def __init__(
        self,
        domain: str = None,
        duration: int = None,
        fps: str = None,
        region: str = None,
        resolution: str = None,
        tanscode_type: str = None,
        time_stamp: str = None,
    ):
        # The main streaming domain. This parameter is returned only when you add the domain key to the value of the Split parameter.
        self.domain = domain
        # The transcoding length. Unit: minutes.
        self.duration = duration
        # The frame rate of the transcoded stream. This parameter is returned only when you add the fps key to the value of the Split parameter.
        self.fps = fps
        # The region in which the domain name resides. Valid values:
        # 
        # >  This parameter takes effect only when you set Split to region.
        # 
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-qingdao**: China (Qingdao)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **ap-northeast-1**: Japan (Tokyo)
        # *   **ap-southeast-1**: Singapore
        # *   **ap-southeast-5**: Indonesia (Jakarta)
        # *   **eu-central-1**: Germany (Frankfurt)
        self.region = region
        # The resolution of the transcoded stream. This parameter is returned only when you add the resolution key to the value of the Split parameter. Valid values:
        # 
        # *   **2K**
        # *   **4K**
        # *   **LD**: low definition
        # *   **SD**: standard definition
        # *   **HD**: high definition
        # *   **def**: audio
        self.resolution = resolution
        # The transcoding type. Valid values:
        # 
        # >  This parameter takes effect only if the request parameter Split is set to transcode_type.
        # 
        # *   **H264NBHD**: Narrowband HD™ transcoding based on H.264
        # *   **H265NBHD**: Narrowband HD™ transcoding based on H.265
        # *   **AUDIO**: audio transcoding
        self.tanscode_type = tanscode_type
        # The timestamp of the data entry.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.region is not None:
            result['Region'] = self.region

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.tanscode_type is not None:
            result['TanscodeType'] = self.tanscode_type

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('TanscodeType') is not None:
            self.tanscode_type = m.get('TanscodeType')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

