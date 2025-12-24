# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamsOnlineListRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        only_stream: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        query_type: str = None,
        region_id: str = None,
        stream_name: str = None,
        stream_type: str = None,
    ):
        # The name of the application to which the live stream belongs. You can view the application name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to return only specific parameters. Valid values:
        # 
        # *   **yes**: returns only the DomainName, AppName, StreamName, and PublishTime parameters.
        # *   **no**: returns all parameters. This is the default value.
        self.only_stream = only_stream
        self.owner_id = owner_id
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Valid values: 1 to 3000. Default value: 2000.
        self.page_size = page_size
        # The mode in which stream names are matched. Valid values:
        # 
        # *   **fuzzy** (default): fuzzy match
        # *   **strict**: exact match
        self.query_type = query_type
        self.region_id = region_id
        # The name of the live stream. You can specify only one live stream. You can view the stream name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
        self.stream_name = stream_name
        # The type of the streams to query. Valid values:
        # 
        # *   **all** (default): all streams
        # *   **raw**: source streams
        # *   **trans**: transcoded streams
        self.stream_type = stream_type

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

        if self.only_stream is not None:
            result['OnlyStream'] = self.only_stream

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OnlyStream') is not None:
            self.only_stream = m.get('OnlyStream')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        return self

