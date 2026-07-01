# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QueryShortUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryShortUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The request status code.
        # 
        # - A successful request returns `OK`.
        # 
        # - For other error codes, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The details of the short link.
        self.data = data
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryShortUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryShortUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        expire_date: str = None,
        page_view_count: str = None,
        short_url: str = None,
        short_url_name: str = None,
        short_url_status: str = None,
        source_url: str = None,
        unique_visitor_count: str = None,
    ):
        # The creation date and time of the short link.
        self.create_date = create_date
        # The expiration date and time of the short link.
        self.expire_date = expire_date
        # The page view (PV) count for the short link.
        self.page_view_count = page_view_count
        # The generated short link.
        self.short_url = short_url
        # The name of the service that generated the short link.
        self.short_url_name = short_url_name
        # The short link status. Valid values:
        # 
        # - **expired**: The short link has expired.
        # 
        # - **effective**: The short link is active.
        # 
        # - **audit**: The short link is under review.
        # 
        # - **reject**: The short link was rejected.
        self.short_url_status = short_url_status
        # The source URL.
        self.source_url = source_url
        # The unique visitor (UV) count for the short link.
        self.unique_visitor_count = unique_visitor_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.page_view_count is not None:
            result['PageViewCount'] = self.page_view_count

        if self.short_url is not None:
            result['ShortUrl'] = self.short_url

        if self.short_url_name is not None:
            result['ShortUrlName'] = self.short_url_name

        if self.short_url_status is not None:
            result['ShortUrlStatus'] = self.short_url_status

        if self.source_url is not None:
            result['SourceUrl'] = self.source_url

        if self.unique_visitor_count is not None:
            result['UniqueVisitorCount'] = self.unique_visitor_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('PageViewCount') is not None:
            self.page_view_count = m.get('PageViewCount')

        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')

        if m.get('ShortUrlName') is not None:
            self.short_url_name = m.get('ShortUrlName')

        if m.get('ShortUrlStatus') is not None:
            self.short_url_status = m.get('ShortUrlStatus')

        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')

        if m.get('UniqueVisitorCount') is not None:
            self.unique_visitor_count = m.get('UniqueVisitorCount')

        return self

