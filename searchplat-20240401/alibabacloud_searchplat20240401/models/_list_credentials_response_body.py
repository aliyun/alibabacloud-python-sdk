# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class ListCredentialsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListCredentialsResponseBodyResult] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The returned result.
        self.result = result
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListCredentialsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListCredentialsResponseBodyResult(DaraModel):
    def __init__(
        self,
        app_group_id: int = None,
        enabled: bool = None,
        token: str = None,
        type: str = None,
    ):
        # The workspace ID.
        self.app_group_id = app_group_id
        # Indicates whether the credential is enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.enabled = enabled
        # The access credential token.
        self.token = token
        # The credential type.
        # 
        # - api-token.
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

