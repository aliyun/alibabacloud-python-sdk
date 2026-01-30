# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsStreamsOnlineListResponseBody(DaraModel):
    def __init__(
        self,
        online_info: main_models.DescribeVsStreamsOnlineListResponseBodyOnlineInfo = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.online_info = online_info
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_num = total_num
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
            temp_model = main_models.DescribeVsStreamsOnlineListResponseBodyOnlineInfo()
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

class DescribeVsStreamsOnlineListResponseBodyOnlineInfo(DaraModel):
    def __init__(
        self,
        live_stream_online_info: List[main_models.DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo] = None,
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
                temp_model = main_models.DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo()
                self.live_stream_online_info.append(temp_model.from_map(k1))

        return self

class DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        publish_domain: str = None,
        publish_time: str = None,
        publish_type: str = None,
        publish_url: str = None,
        stream_name: str = None,
        transcode_id: str = None,
        transcoded: str = None,
    ):
        self.app_name = app_name
        self.domain_name = domain_name
        self.publish_domain = publish_domain
        self.publish_time = publish_time
        self.publish_type = publish_type
        self.publish_url = publish_url
        self.stream_name = stream_name
        self.transcode_id = transcode_id
        self.transcoded = transcoded

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.publish_domain is not None:
            result['PublishDomain'] = self.publish_domain

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.transcode_id is not None:
            result['TranscodeId'] = self.transcode_id

        if self.transcoded is not None:
            result['Transcoded'] = self.transcoded

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PublishDomain') is not None:
            self.publish_domain = m.get('PublishDomain')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TranscodeId') is not None:
            self.transcode_id = m.get('TranscodeId')

        if m.get('Transcoded') is not None:
            self.transcoded = m.get('Transcoded')

        return self

