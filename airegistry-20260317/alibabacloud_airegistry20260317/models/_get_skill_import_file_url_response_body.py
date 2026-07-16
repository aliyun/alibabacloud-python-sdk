# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_airegistry20260317 import models as main_models
from darabonba.model import DaraModel

class GetSkillImportFileUrlResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSkillImportFileUrlResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetSkillImportFileUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSkillImportFileUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        max_size: str = None,
        oss_object_name: str = None,
        upload_url: str = None,
    ):
        self.content_type = content_type
        self.max_size = max_size
        self.oss_object_name = oss_object_name
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.max_size is not None:
            result['MaxSize'] = self.max_size

        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name

        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')

        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        return self

