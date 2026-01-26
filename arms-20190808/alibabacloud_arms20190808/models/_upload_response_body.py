# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class UploadResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        upload_result: main_models.UploadResponseBodyUploadResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned data.
        self.upload_result = upload_result

    def validate(self):
        if self.upload_result:
            self.upload_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upload_result is not None:
            result['UploadResult'] = self.upload_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadResult') is not None:
            temp_model = main_models.UploadResponseBodyUploadResult()
            self.upload_result = temp_model.from_map(m.get('UploadResult'))

        return self

class UploadResponseBodyUploadResult(DaraModel):
    def __init__(
        self,
        fid: str = None,
        file_name: str = None,
        upload_time: str = None,
    ):
        # The ID of the SourceMap file.
        self.fid = fid
        # The name of the SourceMap file.
        self.file_name = file_name
        # The time when the file was uploaded.
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fid is not None:
            result['Fid'] = self.fid

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fid') is not None:
            self.fid = m.get('Fid')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        return self

