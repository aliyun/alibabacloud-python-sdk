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
        instance_id: str = None,
        scope_values: List[str] = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.audience = audience
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.scope_values = scope_values

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scope_values is not None:
            result['ScopeValues'] = self.scope_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Audience') is not None:
            self.audience = m.get('Audience')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScopeValues') is not None:
            self.scope_values = m.get('ScopeValues')

        return self

