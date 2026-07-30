# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOAuthAuthorizationSessionResponseBody(DaraModel):
    def __init__(
        self,
        authentication_token_id: str = None,
        authorization_url: str = None,
        consumer_id: str = None,
        consumer_type: str = None,
        creator_id: str = None,
        creator_type: str = None,
        credential_provider_identifier: str = None,
        error_code: str = None,
        error_description: str = None,
        expiration_time: int = None,
        instance_id: str = None,
        session_id: str = None,
        session_status: str = None,
        session_uri: str = None,
    ):
        # The authentication token ID.
        self.authentication_token_id = authentication_token_id
        # The user authorization URL.
        self.authorization_url = authorization_url
        # The authentication token consumer ID.
        self.consumer_id = consumer_id
        # The authentication token consumer type.
        self.consumer_type = consumer_type
        # The authentication token creator ID.
        self.creator_id = creator_id
        # The authentication token creator type.
        self.creator_type = creator_type
        # The credential provider business identifier.
        self.credential_provider_identifier = credential_provider_identifier
        # The error code.
        self.error_code = error_code
        # The error description.
        self.error_description = error_description
        # The authentication token expiration time. UNIX timestamp in milliseconds.
        self.expiration_time = expiration_time
        # The instance ID.
        self.instance_id = instance_id
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
        if self.authentication_token_id is not None:
            result['authenticationTokenId'] = self.authentication_token_id

        if self.authorization_url is not None:
            result['authorizationUrl'] = self.authorization_url

        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.consumer_type is not None:
            result['consumerType'] = self.consumer_type

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.creator_type is not None:
            result['creatorType'] = self.creator_type

        if self.credential_provider_identifier is not None:
            result['credentialProviderIdentifier'] = self.credential_provider_identifier

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_description is not None:
            result['errorDescription'] = self.error_description

        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_status is not None:
            result['sessionStatus'] = self.session_status

        if self.session_uri is not None:
            result['sessionUri'] = self.session_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationTokenId') is not None:
            self.authentication_token_id = m.get('authenticationTokenId')

        if m.get('authorizationUrl') is not None:
            self.authorization_url = m.get('authorizationUrl')

        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('consumerType') is not None:
            self.consumer_type = m.get('consumerType')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('creatorType') is not None:
            self.creator_type = m.get('creatorType')

        if m.get('credentialProviderIdentifier') is not None:
            self.credential_provider_identifier = m.get('credentialProviderIdentifier')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorDescription') is not None:
            self.error_description = m.get('errorDescription')

        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')

        if m.get('sessionUri') is not None:
            self.session_uri = m.get('sessionUri')

        return self

