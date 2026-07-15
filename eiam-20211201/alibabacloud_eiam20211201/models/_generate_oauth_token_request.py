# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GenerateOauthTokenRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        audience: str = None,
        grant_type: str = None,
        instance_id: str = None,
        requested_token_type: str = None,
        scope_values: List[str] = None,
        subject_token: str = None,
        subject_token_type: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The audience identifier of the resource server.
        # 
        # This parameter is required.
        self.audience = audience
        self.grant_type = grant_type
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.requested_token_type = requested_token_type
        # The permission scopes.
        # 
        # This parameter is required.
        self.scope_values = scope_values
        self.subject_token = subject_token
        self.subject_token_type = subject_token_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.audience is not None:
            result['Audience'] = self.audience

        if self.grant_type is not None:
            result['GrantType'] = self.grant_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.requested_token_type is not None:
            result['RequestedTokenType'] = self.requested_token_type

        if self.scope_values is not None:
            result['ScopeValues'] = self.scope_values

        if self.subject_token is not None:
            result['SubjectToken'] = self.subject_token

        if self.subject_token_type is not None:
            result['SubjectTokenType'] = self.subject_token_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Audience') is not None:
            self.audience = m.get('Audience')

        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestedTokenType') is not None:
            self.requested_token_type = m.get('RequestedTokenType')

        if m.get('ScopeValues') is not None:
            self.scope_values = m.get('ScopeValues')

        if m.get('SubjectToken') is not None:
            self.subject_token = m.get('SubjectToken')

        if m.get('SubjectTokenType') is not None:
            self.subject_token_type = m.get('SubjectTokenType')

        return self

