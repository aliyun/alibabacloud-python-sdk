# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentitydata20251127 import models as main_models
from darabonba.model import DaraModel

class CompleteResourceTokenAuthRequest(DaraModel):
    def __init__(
        self,
        session_uri: str = None,
        user_identifier: main_models.CompleteResourceTokenAuthRequestUserIdentifier = None,
    ):
        self.session_uri = session_uri
        self.user_identifier = user_identifier

    def validate(self):
        if self.user_identifier:
            self.user_identifier.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_uri is not None:
            result['SessionURI'] = self.session_uri

        if self.user_identifier is not None:
            result['UserIdentifier'] = self.user_identifier.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionURI') is not None:
            self.session_uri = m.get('SessionURI')

        if m.get('UserIdentifier') is not None:
            temp_model = main_models.CompleteResourceTokenAuthRequestUserIdentifier()
            self.user_identifier = temp_model.from_map(m.get('UserIdentifier'))

        return self

class CompleteResourceTokenAuthRequestUserIdentifier(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_jwt: str = None,
    ):
        self.user_id = user_id
        self.user_jwt = user_jwt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_jwt is not None:
            result['UserJWT'] = self.user_jwt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserJWT') is not None:
            self.user_jwt = m.get('UserJWT')

        return self

