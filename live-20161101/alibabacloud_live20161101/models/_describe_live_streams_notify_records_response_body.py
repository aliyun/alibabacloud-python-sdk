# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamsNotifyRecordsResponseBody(DaraModel):
    def __init__(
        self,
        notify_records_info: main_models.DescribeLiveStreamsNotifyRecordsResponseBodyNotifyRecordsInfo = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The stream ingest callback records.
        self.notify_records_info = notify_records_info
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries that meet the specified conditions.
        self.total_num = total_num
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.notify_records_info:
            self.notify_records_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notify_records_info is not None:
            result['NotifyRecordsInfo'] = self.notify_records_info.to_map()

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
        if m.get('NotifyRecordsInfo') is not None:
            temp_model = main_models.DescribeLiveStreamsNotifyRecordsResponseBodyNotifyRecordsInfo()
            self.notify_records_info = temp_model.from_map(m.get('NotifyRecordsInfo'))

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

class DescribeLiveStreamsNotifyRecordsResponseBodyNotifyRecordsInfo(DaraModel):
    def __init__(
        self,
        live_stream_notify_records_info: List[main_models.DescribeLiveStreamsNotifyRecordsResponseBodyNotifyRecordsInfoLiveStreamNotifyRecordsInfo] = None,
    ):
        self.live_stream_notify_records_info = live_stream_notify_records_info

    def validate(self):
        if self.live_stream_notify_records_info:
            for v1 in self.live_stream_notify_records_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamNotifyRecordsInfo'] = []
        if self.live_stream_notify_records_info is not None:
            for k1 in self.live_stream_notify_records_info:
                result['LiveStreamNotifyRecordsInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_notify_records_info = []
        if m.get('LiveStreamNotifyRecordsInfo') is not None:
            for k1 in m.get('LiveStreamNotifyRecordsInfo'):
                temp_model = main_models.DescribeLiveStreamsNotifyRecordsResponseBodyNotifyRecordsInfoLiveStreamNotifyRecordsInfo()
                self.live_stream_notify_records_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamsNotifyRecordsResponseBodyNotifyRecordsInfoLiveStreamNotifyRecordsInfo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
        domain_name: str = None,
        notify_content: str = None,
        notify_header: str = None,
        notify_response: str = None,
        notify_result: str = None,
        notify_time: str = None,
        notify_type: str = None,
        notify_url: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The result of the request. If success is returned, the request is successful. If an error message is returned, the request failed.
        self.description = description
        # The ingest domain.
        self.domain_name = domain_name
        # The callback content.
        self.notify_content = notify_content
        self.notify_header = notify_header
        self.notify_response = notify_response
        # The callback result. Valid values:
        # 
        # *   success
        # *   failed
        self.notify_result = notify_result
        # The time when the callback was invoked. The time is displayed in UTC.
        self.notify_time = notify_time
        # The event. Valid values:
        # 
        # *   publish: The stream ingest starts.
        # *   publish_done: The stream ingest is interrupted.
        self.notify_type = notify_type
        # The callback URL.
        self.notify_url = notify_url
        # The name of the live stream.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.notify_content is not None:
            result['NotifyContent'] = self.notify_content

        if self.notify_header is not None:
            result['NotifyHeader'] = self.notify_header

        if self.notify_response is not None:
            result['NotifyResponse'] = self.notify_response

        if self.notify_result is not None:
            result['NotifyResult'] = self.notify_result

        if self.notify_time is not None:
            result['NotifyTime'] = self.notify_time

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('NotifyContent') is not None:
            self.notify_content = m.get('NotifyContent')

        if m.get('NotifyHeader') is not None:
            self.notify_header = m.get('NotifyHeader')

        if m.get('NotifyResponse') is not None:
            self.notify_response = m.get('NotifyResponse')

        if m.get('NotifyResult') is not None:
            self.notify_result = m.get('NotifyResult')

        if m.get('NotifyTime') is not None:
            self.notify_time = m.get('NotifyTime')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

