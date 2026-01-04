# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetApplicationGrantScopeRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        grant_scopes: List[str] = None,
        instance_id: str = None,
    ):
        # The ID of the application that you want to configure.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The permissions of the Developer API feature.
        self.grant_scopes = grant_scopes
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

