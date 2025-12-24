# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMixStreamListRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        mix_stream_id: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The main streaming domain.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.end_time = end_time
        # The ID of the stream mixing task. If the task was created by calling the [CreateMixStream](https://help.aliyun.com/document_detail/2848087.html) operation, check the value of the response parameter MixStreamId to obtain the ID.
        self.mix_stream_id = mix_stream_id
        self.owner_id = owner_id
        # The number of the page to return. Valid values: an integer that is greater than **0** and does not exceed the maximum value of the INTEGER data type. Default value: **1**.
        self.page_no = page_no
        # The number of entries to return on each page. Default value: **1000**.
        self.page_size = page_size
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time
        # The name of the output stream.
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

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.mix_stream_id is not None:
            result['MixStreamId'] = self.mix_stream_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MixStreamId') is not None:
            self.mix_stream_id = m.get('MixStreamId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

