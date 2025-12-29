# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class GetSortScriptFileResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetSortScriptFileResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The content of the sort script.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.GetSortScriptFileResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class GetSortScriptFileResponseBodyResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        modify_time: str = None,
        version: int = None,
    ):
        # The script content that is encoded in the Base64 format.
        self.content = content
        # The time when the script was created.
        self.create_time = create_time
        # The time when the script was last modified.
        self.modify_time = modify_time
        # The version of the script content.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

