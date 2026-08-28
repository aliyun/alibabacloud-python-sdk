# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UploadAgentSpecViaOssRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UploadAgentSpecViaOssRequestBody = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UploadAgentSpecViaOssRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UploadAgentSpecViaOssRequestBody(DaraModel):
    def __init__(
        self,
        oss_object_name: str = None,
        overwrite: bool = None,
        publish: bool = None,
    ):
        # The OSS object name (full path).
        # 
        # This parameter is required.
        self.oss_object_name = oss_object_name
        # Specifies whether to overwrite existing drafts. Default value: false.
        self.overwrite = overwrite
        # Specifies whether to publish immediately after upload. Default value: false.
        self.publish = publish

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name

        if self.overwrite is not None:
            result['overwrite'] = self.overwrite

        if self.publish is not None:
            result['publish'] = self.publish

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')

        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')

        if m.get('publish') is not None:
            self.publish = m.get('publish')

        return self

