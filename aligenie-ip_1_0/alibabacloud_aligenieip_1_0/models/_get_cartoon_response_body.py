# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetCartoonResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: main_models.GetCartoonResponseBodyResult = None,
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
            temp_model = main_models.GetCartoonResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class GetCartoonResponseBodyResult(DaraModel):
    def __init__(
        self,
        start_video_md_5: str = None,
        start_video_url: str = None,
    ):
        self.start_video_md_5 = start_video_md_5
        self.start_video_url = start_video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.start_video_md_5 is not None:
            result['StartVideoMd5'] = self.start_video_md_5

        if self.start_video_url is not None:
            result['StartVideoUrl'] = self.start_video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartVideoMd5') is not None:
            self.start_video_md_5 = m.get('StartVideoMd5')

        if m.get('StartVideoUrl') is not None:
            self.start_video_url = m.get('StartVideoUrl')

        return self

