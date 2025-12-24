# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainOnlineUserNumResponseBody(DaraModel):
    def __init__(
        self,
        online_user_info: main_models.DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfo = None,
        request_id: str = None,
        stream_count: int = None,
        user_count: int = None,
    ):
        # The information about the streams.
        self.online_user_info = online_user_info
        # The request ID.
        self.request_id = request_id
        # The number of streams.
        self.stream_count = stream_count
        # The total number of online users at the specified point in time for all the live streams under the main streaming domain.
        self.user_count = user_count

    def validate(self):
        if self.online_user_info:
            self.online_user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.online_user_info is not None:
            result['OnlineUserInfo'] = self.online_user_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineUserInfo') is not None:
            temp_model = main_models.DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfo()
            self.online_user_info = temp_model.from_map(m.get('OnlineUserInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

class DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfo(DaraModel):
    def __init__(
        self,
        live_stream_online_user_num_info: List[main_models.DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo] = None,
    ):
        self.live_stream_online_user_num_info = live_stream_online_user_num_info

    def validate(self):
        if self.live_stream_online_user_num_info:
            for v1 in self.live_stream_online_user_num_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamOnlineUserNumInfo'] = []
        if self.live_stream_online_user_num_info is not None:
            for k1 in self.live_stream_online_user_num_info:
                result['LiveStreamOnlineUserNumInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_online_user_num_info = []
        if m.get('LiveStreamOnlineUserNumInfo') is not None:
            for k1 in m.get('LiveStreamOnlineUserNumInfo'):
                temp_model = main_models.DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo()
                self.live_stream_online_user_num_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo(DaraModel):
    def __init__(
        self,
        infos: main_models.DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos = None,
        stream_name: str = None,
    ):
        # The statistics on the stream.
        self.infos = infos
        # The name of the stream.
        self.stream_name = stream_name

    def validate(self):
        if self.infos:
            self.infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.infos is not None:
            result['Infos'] = self.infos.to_map()

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Infos') is not None:
            temp_model = main_models.DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos()
            self.infos = temp_model.from_map(m.get('Infos'))

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

class DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos(DaraModel):
    def __init__(
        self,
        info: List[main_models.DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo] = None,
    ):
        self.info = info

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['Info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info = []
        if m.get('Info') is not None:
            for k1 in m.get('Info'):
                temp_model = main_models.DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo()
                self.info.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo(DaraModel):
    def __init__(
        self,
        transcode_template: str = None,
        user_number: int = None,
    ):
        # The transcoding template. A value of origin indicates that the stream is a source stream.
        self.transcode_template = transcode_template
        # The number of online users for the stream, which can be a source stream or transcoded stream.
        self.user_number = user_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.transcode_template is not None:
            result['TranscodeTemplate'] = self.transcode_template

        if self.user_number is not None:
            result['UserNumber'] = self.user_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TranscodeTemplate') is not None:
            self.transcode_template = m.get('TranscodeTemplate')

        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')

        return self

