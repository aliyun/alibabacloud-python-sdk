# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectImageBasicInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dpi: str = None,
        http_status_code: int = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        size: str = None,
        success: bool = None,
        type: str = None,
    ):
        # The business error code. "OK" is returned if the request was successful.
        self.code = code
        # The image resolution (width × height), such as 1920 × 1080. This value is empty if the resolution cannot be identified.
        self.dpi = dpi
        # The HTTP status code. 200 is returned if the request was successful.
        self.http_status_code = http_status_code
        # The additional information. "success" is returned if the request was successful.
        self.message = message
        # The file name.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The file size in a human-readable format, such as 1.5 MB or 256 KB.
        self.size = size
        # Indicates whether the request was successful.
        self.success = success
        # The image format, such as JPEG, PNG, GIF, or WEBP. UNKNOWN is returned if the format cannot be identified.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dpi is not None:
            result['Dpi'] = self.dpi

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.success is not None:
            result['Success'] = self.success

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Dpi') is not None:
            self.dpi = m.get('Dpi')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

