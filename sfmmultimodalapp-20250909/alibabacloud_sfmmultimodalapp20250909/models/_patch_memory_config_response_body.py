# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class PatchMemoryConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PatchMemoryConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.PatchMemoryConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PatchMemoryConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_update: bool = None,
        expiration_time: int = None,
        prompt: str = None,
        threshold: float = None,
        top_k: int = None,
        user_defined_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.auto_update = auto_update
        self.expiration_time = expiration_time
        self.prompt = prompt
        self.threshold = threshold
        self.top_k = top_k
        self.user_defined_id = user_defined_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auto_update is not None:
            result['AutoUpdate'] = self.auto_update

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.user_defined_id is not None:
            result['UserDefinedId'] = self.user_defined_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AutoUpdate') is not None:
            self.auto_update = m.get('AutoUpdate')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UserDefinedId') is not None:
            self.user_defined_id = m.get('UserDefinedId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

