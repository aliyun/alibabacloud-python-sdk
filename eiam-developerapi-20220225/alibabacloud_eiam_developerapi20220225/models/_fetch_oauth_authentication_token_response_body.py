# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class FetchOAuthAuthenticationTokenResponseBody(DaraModel):
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
        oauth_access_token_content: main_models.FetchOAuthAuthenticationTokenResponseBodyOauthAccessTokenContent = None,
        oauth_authorization_session: main_models.FetchOAuthAuthenticationTokenResponseBodyOauthAuthorizationSession = None,
        revoked: bool = None,
        update_time: int = None,
    ):
        # The authentication token ID.
        self.authentication_token_id = authentication_token_id
        # The authentication token type.
        # 
        # > The value is fixed as `oauth_access_token`, indicating an OAuth Access Token type authentication token.
        self.authentication_token_type = authentication_token_type
        # The consumer ID of the authentication token.
        self.consumer_id = consumer_id
        # The consumer type of the authentication token.
        self.consumer_type = consumer_type
        # The creation time of the authentication token. This value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The creator ID of the authentication token.
        self.creator_id = creator_id
        # The creator type of the authentication token.
        self.creator_type = creator_type
        # The credential provider ID.
        self.credential_provider_id = credential_provider_id
        # The expiration time of the authentication token. This value is a UNIX timestamp in milliseconds.
        self.expiration_time = expiration_time
        # The instance ID.
        self.instance_id = instance_id
        # The content of the OAuth Access Token type authentication token.
        self.oauth_access_token_content = oauth_access_token_content
        # The authorization session of the OAuth user_federation flow. Returned during first-time authorization or when user interaction is required.
        self.oauth_authorization_session = oauth_authorization_session
        # Indicates whether the authentication token is revoked.
        self.revoked = revoked
        # The update time of the authentication token. This value is a UNIX timestamp in milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.oauth_access_token_content:
            self.oauth_access_token_content.validate()
        if self.oauth_authorization_session:
            self.oauth_authorization_session.validate()

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

        if self.oauth_access_token_content is not None:
            result['oauthAccessTokenContent'] = self.oauth_access_token_content.to_map()

        if self.oauth_authorization_session is not None:
            result['oauthAuthorizationSession'] = self.oauth_authorization_session.to_map()

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

        if m.get('oauthAccessTokenContent') is not None:
            temp_model = main_models.FetchOAuthAuthenticationTokenResponseBodyOauthAccessTokenContent()
            self.oauth_access_token_content = temp_model.from_map(m.get('oauthAccessTokenContent'))

        if m.get('oauthAuthorizationSession') is not None:
            temp_model = main_models.FetchOAuthAuthenticationTokenResponseBodyOauthAuthorizationSession()
            self.oauth_authorization_session = temp_model.from_map(m.get('oauthAuthorizationSession'))

        if m.get('revoked') is not None:
            self.revoked = m.get('revoked')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class FetchOAuthAuthenticationTokenResponseBodyOauthAuthorizationSession(DaraModel):
    def __init__(
        self,
        authorization_url: str = None,
        session_id: str = None,
        session_status: str = None,
        session_uri: str = None,
    ):
        # The user authorization URL.
        self.authorization_url = authorization_url
        # The authorization session ID.
        self.session_id = session_id
        # The authorization session status.
        self.session_status = session_status
        # The authorization session URI.
        self.session_uri = session_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_url is not None:
            result['authorizationUrl'] = self.authorization_url

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_status is not None:
            result['sessionStatus'] = self.session_status

        if self.session_uri is not None:
            result['sessionUri'] = self.session_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationUrl') is not None:
            self.authorization_url = m.get('authorizationUrl')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')

        if m.get('sessionUri') is not None:
            self.session_uri = m.get('sessionUri')

        return self

class FetchOAuthAuthenticationTokenResponseBodyOauthAccessTokenContent(DaraModel):
    def __init__(
        self,
        access_token_value: str = None,
        scope: str = None,
        token_type: str = None,
    ):
        # The access_token field in the OAuth protocol token endpoint response.
        self.access_token_value = access_token_value
        # The scope field in the OAuth protocol token endpoint response.
        self.scope = scope
        # The token_type field in the OAuth protocol token endpoint response.
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_value is not None:
            result['accessTokenValue'] = self.access_token_value

        if self.scope is not None:
            result['scope'] = self.scope

        if self.token_type is not None:
            result['tokenType'] = self.token_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessTokenValue') is not None:
            self.access_token_value = m.get('accessTokenValue')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('tokenType') is not None:
            self.token_type = m.get('tokenType')

        return self

