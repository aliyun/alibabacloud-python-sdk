# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetHotelNoticeV2ResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: main_models.GetHotelNoticeV2ResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetHotelNoticeV2ResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class GetHotelNoticeV2ResponseBodyResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        hotel_id: str = None,
        title: str = None,
    ):
        self.content = content
        self.hotel_id = hotel_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

