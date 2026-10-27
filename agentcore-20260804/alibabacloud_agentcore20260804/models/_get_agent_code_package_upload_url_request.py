# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetAgentCodePackageUploadUrlRequest(DaraModel):
    def __init__(
        self,
        body: main_models.GetAgentCodePackageUploadUrlRequestBody = None,
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
            temp_model = main_models.GetAgentCodePackageUploadUrlRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class GetAgentCodePackageUploadUrlRequestBody(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_size: int = None,
        format: str = None,
    ):
        # The filename of the code package.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The declared compressed size of the code package.
        # 
        # This parameter is required.
        self.file_size = file_size
        # The format of the code package.
        # 
        # This parameter is required.
        self.format = format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.format is not None:
            result['format'] = self.format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('format') is not None:
            self.format = m.get('format')

        return self

