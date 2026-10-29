# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeComfyUserDataUploadUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        expired_time: str = None,
        message: str = None,
        request_id: str = None,
        upload_url: str = None,
    ):
        # The error code.
        self.code = code
        # The expiration time of the upload URL. The time is in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format.
        self.expired_time = expired_time
        # The message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The URL for uploading user files.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        return self

