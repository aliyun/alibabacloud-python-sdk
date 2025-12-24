# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamsBlockListResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        stream_urls: main_models.DescribeLiveStreamsBlockListResponseBodyStreamUrls = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The main streaming domain.
        self.domain_name = domain_name
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The complete URL of each live stream.
        self.stream_urls = stream_urls
        # The total number of live stream URLs that meet the specified conditions.
        self.total_num = total_num
        # The total number of returned pages.
        self.total_page = total_page

    def validate(self):
        if self.stream_urls:
            self.stream_urls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_urls is not None:
            result['StreamUrls'] = self.stream_urls.to_map()

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamUrls') is not None:
            temp_model = main_models.DescribeLiveStreamsBlockListResponseBodyStreamUrls()
            self.stream_urls = temp_model.from_map(m.get('StreamUrls'))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeLiveStreamsBlockListResponseBodyStreamUrls(DaraModel):
    def __init__(
        self,
        stream_url: List[str] = None,
    ):
        self.stream_url = stream_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        return self

