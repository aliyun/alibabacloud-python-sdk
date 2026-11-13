# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UploadAgentSessionFileRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params: main_models.UploadAgentSessionFileRequestParams = None,
    ):
        self.id = id
        self.jsonrpc = jsonrpc
        # This parameter is required.
        self.params = params

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.params is not None:
            result['Params'] = self.params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Params') is not None:
            temp_model = main_models.UploadAgentSessionFileRequestParams()
            self.params = temp_model.from_map(m.get('Params'))

        return self

class UploadAgentSessionFileRequestParams(DaraModel):
    def __init__(
        self,
        content_md_5: str = None,
        name: str = None,
        session_id: str = None,
        size: int = None,
        upload_id: str = None,
        upload_mode: str = None,
    ):
        # This parameter is required.
        self.content_md_5 = content_md_5
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.session_id = session_id
        # This parameter is required.
        self.size = size
        self.upload_id = upload_id
        # This parameter is required.
        self.upload_mode = upload_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_md_5 is not None:
            result['ContentMd5'] = self.content_md_5

        if self.name is not None:
            result['Name'] = self.name

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.size is not None:
            result['Size'] = self.size

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        if self.upload_mode is not None:
            result['UploadMode'] = self.upload_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentMd5') is not None:
            self.content_md_5 = m.get('ContentMd5')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        if m.get('UploadMode') is not None:
            self.upload_mode = m.get('UploadMode')

        return self

