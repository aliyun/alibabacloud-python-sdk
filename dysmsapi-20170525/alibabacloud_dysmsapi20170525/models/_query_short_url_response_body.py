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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The details of the short URL.
        self.data = data
        # The returned message.
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
        # The time when the short URL was created.
        self.create_date = create_date
        # The time when the short URL expires.
        self.expire_date = expire_date
        # The PV.
        self.page_view_count = page_view_count
        # The short URL.
        self.short_url = short_url
        # The service name of the short URL.
        self.short_url_name = short_url_name
        # The status of the short URL. Valid values:
        # 
        # *   **expired**
        # *   **effective**
        # *   **audit**
        # *   **reject**
        self.short_url_status = short_url_status
        # The source address.
        self.source_url = source_url
        # The UV.
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

