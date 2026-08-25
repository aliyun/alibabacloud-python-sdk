# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ResetUserPasswordRequest(DaraModel):
    def __init__(
        self,
        body: main_models.ResetUserPasswordRequestBody = None,
    ):
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
            temp_model = main_models.ResetUserPasswordRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class ResetUserPasswordRequestBody(DaraModel):
    def __init__(
        self,
        agent_core_user_id: str = None,
        password: str = None,
        username: str = None,
    ):
        self.agent_core_user_id = agent_core_user_id
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_core_user_id is not None:
            result['agentCoreUserId'] = self.agent_core_user_id

        if self.password is not None:
            result['password'] = self.password

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentCoreUserId') is not None:
            self.agent_core_user_id = m.get('agentCoreUserId')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

