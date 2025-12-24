# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreateCdsFileResponseBody(DaraModel):
    def __init__(
        self,
        file_model: main_models.CreateCdsFileResponseBodyFileModel = None,
        request_id: str = None,
    ):
        self.file_model = file_model
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.file_model:
            self.file_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_model is not None:
            result['FileModel'] = self.file_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileModel') is not None:
            temp_model = main_models.CreateCdsFileResponseBodyFileModel()
            self.file_model = temp_model.from_map(m.get('FileModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateCdsFileResponseBodyFileModel(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        upload_id: str = None,
        upload_url: str = None,
    ):
        self.file_id = file_id
        self.upload_id = upload_id
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        return self

