# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ValidateAgentCodePackageFromOssRequest(DaraModel):
    def __init__(
        self,
        body: main_models.ValidateAgentCodePackageFromOssRequestBody = None,
    ):
        # The request body.
        # 
        # This parameter is required.
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
            temp_model = main_models.ValidateAgentCodePackageFromOssRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class ValidateAgentCodePackageFromOssRequestBody(DaraModel):
    def __init__(
        self,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
    ):
        # The name of the source OSS bucket.
        # 
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # The full object key of the source code package.
        # 
        # This parameter is required.
        self.oss_object_name = oss_object_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name

        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')

        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')

        return self

