# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class CreateAppGroupCredentialsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CreateAppGroupCredentialsResponseBodyResult = None,
    ):
        self.request_id = request_id
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
            temp_model = main_models.CreateAppGroupCredentialsResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class CreateAppGroupCredentialsResponseBodyResult(DaraModel):
    def __init__(
        self,
        app_group_id: int = None,
        enabled: bool = None,
        token: str = None,
        type: str = None,
    ):
        self.app_group_id = app_group_id
        self.enabled = enabled
        self.token = token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.token is not None:
            result['token'] = self.token

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

