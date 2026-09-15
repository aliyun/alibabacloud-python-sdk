# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateUserRequestBody = None,
        client_token: str = None,
    ):
        # The request body for updating a user.
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
            temp_model = main_models.UpdateUserRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateUserRequestBody(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        note: str = None,
    ):
        # The display name of the user. The name must be 1 to 32 characters in length. At least one of displayName, email, and note must be specified.
        self.display_name = display_name
        # The email address of the user. The address can be up to 256 characters in length.
        self.email = email
        # The note for the user. The note can be up to 1,024 characters in length.
        self.note = note

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

        if self.note is not None:
            result['note'] = self.note

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('note') is not None:
            self.note = m.get('note')

        return self

