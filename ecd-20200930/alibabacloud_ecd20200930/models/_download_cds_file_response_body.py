# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DownloadCdsFileResponseBody(DaraModel):
    def __init__(
        self,
        download_file_model: main_models.DownloadCdsFileResponseBodyDownloadFileModel = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The download URL of the file.
        self.download_file_model = download_file_model
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.download_file_model:
            self.download_file_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_file_model is not None:
            result['DownloadFileModel'] = self.download_file_model.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadFileModel') is not None:
            temp_model = main_models.DownloadCdsFileResponseBodyDownloadFileModel()
            self.download_file_model = temp_model.from_map(m.get('DownloadFileModel'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DownloadCdsFileResponseBodyDownloadFileModel(DaraModel):
    def __init__(
        self,
        download_type: str = None,
        download_url: str = None,
        expiration_second: str = None,
        expiration_time: str = None,
        file_id: str = None,
        size: int = None,
        stream_url: str = None,
    ):
        # This parameter is deprecated.
        self.download_type = download_type
        # The download URL.
        self.download_url = download_url
        # This parameter is deprecated.
        self.expiration_second = expiration_second
        # The validity period of the download URL.
        self.expiration_time = expiration_time
        # The file ID.
        self.file_id = file_id
        # The size of the file. Unit: bytes.
        self.size = size
        # This parameter is deprecated.
        self.stream_url = stream_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_type is not None:
            result['DownloadType'] = self.download_type

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expiration_second is not None:
            result['ExpirationSecond'] = self.expiration_second

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.size is not None:
            result['Size'] = self.size

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadType') is not None:
            self.download_type = m.get('DownloadType')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpirationSecond') is not None:
            self.expiration_second = m.get('ExpirationSecond')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        return self

