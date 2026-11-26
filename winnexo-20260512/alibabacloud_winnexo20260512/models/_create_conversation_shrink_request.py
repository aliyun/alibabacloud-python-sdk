# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConversationShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        metadata: str = None,
        object_id: str = None,
        operating_object_name_shrink: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
    ):
        # The platform application token issued by the console. If specified, the operation is executed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The reserved field.
        self.metadata = metadata
        # The primary key ID of the associated variable.
        self.object_id = object_id
        # The name of the operation object.
        self.operating_object_name_shrink = operating_object_name_shrink
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The tenant ID.
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

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.operating_object_name_shrink is not None:
            result['operatingObjectName'] = self.operating_object_name_shrink

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name_shrink = m.get('operatingObjectName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

