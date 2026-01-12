# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class AddImages2LibResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.AddImages2LibResponseBodyData = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code
        self.code = code
        # The data returned.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # The message that is returned in response to the request.
        self.msg = msg
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Success indicator.
        self.success = success

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AddImages2LibResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddImages2LibResponseBodyData(DaraModel):
    def __init__(
        self,
        img_id: str = None,
    ):
        # The id of the uploaded image.
        self.img_id = img_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.img_id is not None:
            result['ImgId'] = self.img_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImgId') is not None:
            self.img_id = m.get('ImgId')

        return self

