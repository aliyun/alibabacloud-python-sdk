# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayAuthConsumerRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        description: str = None,
        encode_type: str = None,
        gateway_unique_id: str = None,
        id: int = None,
        jwks: str = None,
        key_name: str = None,
        key_value: str = None,
        token_name: str = None,
        token_pass: bool = None,
        token_position: str = None,
        token_prefix: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The description of the consumer.
        self.description = description
        # The encryption type. Valid values:
        # 
        # *   RSA
        # *   OCT
        self.encode_type = encode_type
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the consumer.
        # 
        # This parameter is required.
        self.id = id
        # The JWT public key. The JSON format is supported.
        self.jwks = jwks
        # The name of the key used for JWT-based identity authentication.
        self.key_name = key_name
        # The value of the key used for JWT-based identity authentication.
        self.key_value = key_value
        # The names of the parameters that are required to verify each token. By default, each token is prefixed with Bearer and stored in the Authorization header, such as `Authorization: Bearer <Content of a token>`.
        self.token_name = token_name
        # Specifies whether to enable pass-through.
        self.token_pass = token_pass
        # The positions of the parameters that are required to verify each token. By default, each token is prefixed with Bearer and stored in the Authorization header, such as `Authorization: Bearer <Content of a token>`.
        self.token_position = token_position
        # The prefixes of the parameters that are required to verify each token. By default, each token is prefixed with Bearer and stored in the Authorization header, such as `Authorization: Bearer <Content of a token>`.
        self.token_prefix = token_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.description is not None:
            result['Description'] = self.description

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        if self.jwks is not None:
            result['Jwks'] = self.jwks

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_value is not None:
            result['KeyValue'] = self.key_value

        if self.token_name is not None:
            result['TokenName'] = self.token_name

        if self.token_pass is not None:
            result['TokenPass'] = self.token_pass

        if self.token_position is not None:
            result['TokenPosition'] = self.token_position

        if self.token_prefix is not None:
            result['TokenPrefix'] = self.token_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jwks') is not None:
            self.jwks = m.get('Jwks')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyValue') is not None:
            self.key_value = m.get('KeyValue')

        if m.get('TokenName') is not None:
            self.token_name = m.get('TokenName')

        if m.get('TokenPass') is not None:
            self.token_pass = m.get('TokenPass')

        if m.get('TokenPosition') is not None:
            self.token_position = m.get('TokenPosition')

        if m.get('TokenPrefix') is not None:
            self.token_prefix = m.get('TokenPrefix')

        return self

