# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class GetOssUploadTokenResult(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        upload_info: main_models.UploadInfo = None,
    ):
        self.request_id = request_id
        # This parameter is required.
        self.upload_info = upload_info

    def validate(self):
        if self.upload_info:
            self.upload_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.upload_info is not None:
            result['uploadInfo'] = self.upload_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('uploadInfo') is not None:
            temp_model = main_models.UploadInfo()
            self.upload_info = temp_model.from_map(m.get('uploadInfo'))

        return self

