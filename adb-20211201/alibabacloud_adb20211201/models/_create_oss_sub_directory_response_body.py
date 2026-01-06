# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class CreateOssSubDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateOssSubDirectoryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # The response code. The status code 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The returned message.
        # 
        # *   If the request was successful, a **success** message is returned.
        # *   If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateOssSubDirectoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateOssSubDirectoryResponseBodyData(DaraModel):
    def __init__(
        self,
        client_crc: int = None,
        etag: str = None,
        request_id: str = None,
        server_crc: int = None,
    ):
        # The cyclic redundancy check (CRC) value on the client.
        self.client_crc = client_crc
        # The tag of the OSS path.
        self.etag = etag
        # The request ID.
        self.request_id = request_id
        # The CRC-64 value on the OSS bucket.
        self.server_crc = server_crc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_crc is not None:
            result['ClientCRC'] = self.client_crc

        if self.etag is not None:
            result['ETag'] = self.etag

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.server_crc is not None:
            result['ServerCRC'] = self.server_crc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientCRC') is not None:
            self.client_crc = m.get('ClientCRC')

        if m.get('ETag') is not None:
            self.etag = m.get('ETag')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServerCRC') is not None:
            self.server_crc = m.get('ServerCRC')

        return self

