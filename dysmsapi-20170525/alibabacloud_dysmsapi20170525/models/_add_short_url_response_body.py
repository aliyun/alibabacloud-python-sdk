# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class AddShortUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AddShortUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
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
            temp_model = main_models.AddShortUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class AddShortUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        expire_date: str = None,
        short_url: str = None,
        source_url: str = None,
    ):
        # The time when the short URL expires.
        # 
        # > The value of **ExpireDate** is on the hour.
        self.expire_date = expire_date
        # The short URL.
        self.short_url = short_url
        # The source URL.
        self.source_url = source_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.short_url is not None:
            result['ShortUrl'] = self.short_url

        if self.source_url is not None:
            result['SourceUrl'] = self.source_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')

        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')

        return self

