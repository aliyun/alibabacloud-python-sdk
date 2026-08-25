# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateIdentityProviderRequestBody = None,
    ):
        # The request body for updating the external identity provider.
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
            temp_model = main_models.UpdateIdentityProviderRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UpdateIdentityProviderRequestBody(DaraModel):
    def __init__(
        self,
        login_enabled: bool = None,
        metadata: main_models.UpdateIdentityProviderRequestBodyMetadata = None,
        sync_enabled: bool = None,
    ):
        # Specifies whether workspace users are allowed to log on through this external identity provider.
        self.login_enabled = login_enabled
        # The new application configuration of the external identity provider. If not specified, the existing configuration remains unchanged.
        self.metadata = metadata
        # Specifies whether to enable organization member synchronization. After this feature is enabled, the external identity provider synchronizes organization members as workspace users.
        self.sync_enabled = sync_enabled

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_enabled is not None:
            result['loginEnabled'] = self.login_enabled

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.sync_enabled is not None:
            result['syncEnabled'] = self.sync_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginEnabled') is not None:
            self.login_enabled = m.get('loginEnabled')

        if m.get('metadata') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBodyMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        return self

class UpdateIdentityProviderRequestBodyMetadata(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        app_secret: str = None,
        corp_id: str = None,
        encrypt_key: str = None,
        verification_token: str = None,
    ):
        # The App ID of the Lark application. This parameter is required when the binding type is Feishu.
        self.app_id = app_id
        # The AppKey of the DingTalk application. This parameter is required when the binding type is DingTalk.
        self.app_key = app_key
        # Required. The secret of the external identity provider application. This parameter is write-only and is not returned by query operations.
        self.app_secret = app_secret
        # The CorpId of the DingTalk organization. This parameter is required when the binding type is DingTalk.
        self.corp_id = corp_id
        # The data encryption key for event subscriptions. The value must be consistent with the one configured in the external identity provider application. This parameter is write-only and is not returned by query operations.
        self.encrypt_key = encrypt_key
        # The verification token for event subscriptions. The value must be consistent with the one configured in the external identity provider application. This parameter is write-only and is not returned by query operations.
        self.verification_token = verification_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.app_key is not None:
            result['appKey'] = self.app_key

        if self.app_secret is not None:
            result['appSecret'] = self.app_secret

        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key

        if self.verification_token is not None:
            result['verificationToken'] = self.verification_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')

        if m.get('appSecret') is not None:
            self.app_secret = m.get('appSecret')

        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')

        if m.get('verificationToken') is not None:
            self.verification_token = m.get('verificationToken')

        return self

