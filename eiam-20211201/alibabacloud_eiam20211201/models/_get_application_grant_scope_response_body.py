# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetApplicationGrantScopeResponseBody(DaraModel):
    def __init__(
        self,
        application_grant_scope: main_models.GetApplicationGrantScopeResponseBodyApplicationGrantScope = None,
        request_id: str = None,
    ):
        # The permissions of the Developer API feature.
        self.application_grant_scope = application_grant_scope
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_grant_scope:
            self.application_grant_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_grant_scope is not None:
            result['ApplicationGrantScope'] = self.application_grant_scope.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationGrantScope') is not None:
            temp_model = main_models.GetApplicationGrantScopeResponseBodyApplicationGrantScope()
            self.application_grant_scope = temp_model.from_map(m.get('ApplicationGrantScope'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationGrantScopeResponseBodyApplicationGrantScope(DaraModel):
    def __init__(
        self,
        grant_scopes: List[str] = None,
    ):
        # The permissions of the Developer API feature.
        self.grant_scopes = grant_scopes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')

        return self

