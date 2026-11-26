# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplacePersonalSourceObjectBindingsShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        object_bindings_shrink: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # token
        self.app_token = app_token
        # The object bindings.
        # 
        # This parameter is required.
        self.object_bindings_shrink = object_bindings_shrink
        # The code of the operator.
        self.ops_user_code = ops_user_code
        # The ID of the operator.
        self.ops_user_id = ops_user_id
        # The ID of the data source. The ID is unique within the tenant.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.object_bindings_shrink is not None:
            result['objectBindings'] = self.object_bindings_shrink

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('objectBindings') is not None:
            self.object_bindings_shrink = m.get('objectBindings')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

