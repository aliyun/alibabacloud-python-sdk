# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetSkillImportFileUrlResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSkillImportFileUrlResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data.
        self.data = data
        # The request ID.
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetSkillImportFileUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetSkillImportFileUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        max_size: str = None,
        oss_object_name: str = None,
        upload_url: str = None,
    ):
        # The Content-Type of the upload file.
        self.content_type = content_type
        # The maximum file size allowed for upload, in bytes.
        self.max_size = max_size
        # The OSS object name.
        self.oss_object_name = oss_object_name
        # The OSS pre-signed upload URL.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name

        if self.upload_url is not None:
            result['uploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')

        if m.get('uploadUrl') is not None:
            self.upload_url = m.get('uploadUrl')

        return self

