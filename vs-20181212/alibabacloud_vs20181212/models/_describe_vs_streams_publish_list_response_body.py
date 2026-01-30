# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsStreamsPublishListResponseBody(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        publish_info: main_models.DescribeVsStreamsPublishListResponseBodyPublishInfo = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.publish_info = publish_info
        self.request_id = request_id
        self.total_num = total_num
        self.total_page = total_page

    def validate(self):
        if self.publish_info:
            self.publish_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.publish_info is not None:
            result['PublishInfo'] = self.publish_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PublishInfo') is not None:
            temp_model = main_models.DescribeVsStreamsPublishListResponseBodyPublishInfo()
            self.publish_info = temp_model.from_map(m.get('PublishInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeVsStreamsPublishListResponseBodyPublishInfo(DaraModel):
    def __init__(
        self,
        live_stream_publish_info: List[main_models.DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo] = None,
    ):
        self.live_stream_publish_info = live_stream_publish_info

    def validate(self):
        if self.live_stream_publish_info:
            for v1 in self.live_stream_publish_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamPublishInfo'] = []
        if self.live_stream_publish_info is not None:
            for k1 in self.live_stream_publish_info:
                result['LiveStreamPublishInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_publish_info = []
        if m.get('LiveStreamPublishInfo') is not None:
            for k1 in m.get('LiveStreamPublishInfo'):
                temp_model = main_models.DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo()
                self.live_stream_publish_info.append(temp_model.from_map(k1))

        return self

class DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        client_addr: str = None,
        domain_name: str = None,
        edge_node_addr: str = None,
        publish_domain: str = None,
        publish_time: str = None,
        publish_type: str = None,
        publish_url: str = None,
        stop_time: str = None,
        stream_name: str = None,
        stream_url: str = None,
        transcode_id: str = None,
        transcoded: str = None,
    ):
        self.app_name = app_name
        self.client_addr = client_addr
        self.domain_name = domain_name
        self.edge_node_addr = edge_node_addr
        self.publish_domain = publish_domain
        self.publish_time = publish_time
        self.publish_type = publish_type
        self.publish_url = publish_url
        self.stop_time = stop_time
        self.stream_name = stream_name
        self.stream_url = stream_url
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

        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.edge_node_addr is not None:
            result['EdgeNodeAddr'] = self.edge_node_addr

        if self.publish_domain is not None:
            result['PublishDomain'] = self.publish_domain

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        if self.transcode_id is not None:
            result['TranscodeId'] = self.transcode_id

        if self.transcoded is not None:
            result['Transcoded'] = self.transcoded

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EdgeNodeAddr') is not None:
            self.edge_node_addr = m.get('EdgeNodeAddr')

        if m.get('PublishDomain') is not None:
            self.publish_domain = m.get('PublishDomain')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        if m.get('TranscodeId') is not None:
            self.transcode_id = m.get('TranscodeId')

        if m.get('Transcoded') is not None:
            self.transcoded = m.get('Transcoded')

        return self

