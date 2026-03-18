# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class ObtainJwtAuthenticationTokenByDerivedShortTokenResponseBody(DaraModel):
    def __init__(
        self,
        authentication_token_id: str = None,
        authentication_token_type: str = None,
        consumer_id: str = None,
        consumer_type: str = None,
        create_time: int = None,
        creator_id: str = None,
        creator_type: str = None,
        credential_provider_id: str = None,
        expiration_time: int = None,
        instance_id: str = None,
        jwt_content: main_models.ObtainJwtAuthenticationTokenByDerivedShortTokenResponseBodyJwtContent = None,
        revoked: bool = None,
        update_time: int = None,
    ):
        self.authentication_token_id = authentication_token_id
        self.authentication_token_type = authentication_token_type
        self.consumer_id = consumer_id
        self.consumer_type = consumer_type
        self.create_time = create_time
        self.creator_id = creator_id
        self.creator_type = creator_type
        self.credential_provider_id = credential_provider_id
        self.expiration_time = expiration_time
        # EIAM实例ID。
        self.instance_id = instance_id
        self.jwt_content = jwt_content
        self.revoked = revoked
        self.update_time = update_time

    def validate(self):
        if self.jwt_content:
            self.jwt_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_token_id is not None:
            result['authenticationTokenId'] = self.authentication_token_id

        if self.authentication_token_type is not None:
            result['authenticationTokenType'] = self.authentication_token_type

        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.consumer_type is not None:
            result['consumerType'] = self.consumer_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.creator_type is not None:
            result['creatorType'] = self.creator_type

        if self.credential_provider_id is not None:
            result['credentialProviderId'] = self.credential_provider_id

        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.jwt_content is not None:
            result['jwtContent'] = self.jwt_content.to_map()

        if self.revoked is not None:
            result['revoked'] = self.revoked

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationTokenId') is not None:
            self.authentication_token_id = m.get('authenticationTokenId')

        if m.get('authenticationTokenType') is not None:
            self.authentication_token_type = m.get('authenticationTokenType')

        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('consumerType') is not None:
            self.consumer_type = m.get('consumerType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('creatorType') is not None:
            self.creator_type = m.get('creatorType')

        if m.get('credentialProviderId') is not None:
            self.credential_provider_id = m.get('credentialProviderId')

        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('jwtContent') is not None:
            temp_model = main_models.ObtainJwtAuthenticationTokenByDerivedShortTokenResponseBodyJwtContent()
            self.jwt_content = temp_model.from_map(m.get('jwtContent'))

        if m.get('revoked') is not None:
            self.revoked = m.get('revoked')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class ObtainJwtAuthenticationTokenByDerivedShortTokenResponseBodyJwtContent(DaraModel):
    def __init__(
        self,
        derived_short_token: str = None,
        jwt_value: str = None,
    ):
        self.derived_short_token = derived_short_token
        self.jwt_value = jwt_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.derived_short_token is not None:
            result['derivedShortToken'] = self.derived_short_token

        if self.jwt_value is not None:
            result['jwtValue'] = self.jwt_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('derivedShortToken') is not None:
            self.derived_short_token = m.get('derivedShortToken')

        if m.get('jwtValue') is not None:
            self.jwt_value = m.get('jwtValue')

        return self

