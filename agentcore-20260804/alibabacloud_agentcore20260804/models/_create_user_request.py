# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateUserRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateUserRequestBody = None,
        client_token: str = None,
    ):
        # The request body for creating a user.
        self.body = body
        # Not supported.
        self.client_token = client_token

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

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateUserRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateUserRequestBody(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        name: str = None,
        note: str = None,
        password: str = None,
    ):
        # The display name of the user. The display name must be 1 to 32 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The email address of the user. The email address can be up to 256 characters in length.
        self.email = email
        # The username. The username must be unique within the workspace and can contain only lowercase letters, digits, and hyphens. It must start and end with a lowercase letter or digit and be 1 to 32 characters in length. Reserved names such as manager, admin, or names starting with worker- cannot be used.
        # 
        # This parameter is required.
        self.name = name
        # The remarks of the user. The remarks can be up to 1024 characters in length.
        self.note = note
        # The initial password of the user. The password must be 8 to 32 characters in length and contain uppercase letters, lowercase letters, digits, and special characters. The password cannot contain the username. If this parameter is not specified, the server generates a random password and returns it in the initialPassword field of the response.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.email is not None:
            result['email'] = self.email

        if self.name is not None:
            result['name'] = self.name

        if self.note is not None:
            result['note'] = self.note

        if self.password is not None:
            result['password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('note') is not None:
            self.note = m.get('note')

        if m.get('password') is not None:
            self.password = m.get('password')

        return self

