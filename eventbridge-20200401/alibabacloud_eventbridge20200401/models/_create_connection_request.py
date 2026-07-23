# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateConnectionRequest(DaraModel):
    def __init__(
        self,
        auth_parameters: main_models.CreateConnectionRequestAuthParameters = None,
        connection_name: str = None,
        description: str = None,
        network_parameters: main_models.CreateConnectionRequestNetworkParameters = None,
        parameters: Any = None,
        type: str = None,
    ):
        # The authentication configuration.
        self.auth_parameters = auth_parameters
        # The connection configuration name. Maximum length: 127 characters. Minimum length: 2 characters.
        # 
        # This parameter is required.
        self.connection_name = connection_name
        # The description of the connection configuration. Maximum length: 255 characters.
        self.description = description
        # The network configuration.
        # 
        # This parameter is required.
        self.network_parameters = network_parameters
        # The data source connection parameters (JSON object). This parameter is required when Type is set to a data source type. This parameter is not required for the Http type. For specific field definitions, call the GetConnectionType operation and refer to ParamsSchema in the response.
        self.parameters = parameters
        # The connection type. Valid values: MySQL, PostgreSQL, Elasticsearch, and Http. This parameter is required for data source connections. If this parameter is not specified, the default value Http is used. The Http type is used for HTTP protocol targets such as API Destination. Data source types are used for data connections in the integration marketplace.
        self.type = type

    def validate(self):
        if self.auth_parameters:
            self.auth_parameters.validate()
        if self.network_parameters:
            self.network_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_parameters is not None:
            result['AuthParameters'] = self.auth_parameters.to_map()

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.description is not None:
            result['Description'] = self.description

        if self.network_parameters is not None:
            result['NetworkParameters'] = self.network_parameters.to_map()

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            temp_model = main_models.CreateConnectionRequestAuthParameters()
            self.auth_parameters = temp_model.from_map(m.get('AuthParameters'))

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NetworkParameters') is not None:
            temp_model = main_models.CreateConnectionRequestNetworkParameters()
            self.network_parameters = temp_model.from_map(m.get('NetworkParameters'))

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateConnectionRequestNetworkParameters(DaraModel):
    def __init__(
        self,
        network_type: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitche_id: str = None,
    ):
        # - Public network: PublicNetwork
        # 
        # - Virtual private cloud (VPC): PrivateNetwork
        # 
        # >Notice: If you select PrivateNetwork, VpcId, VswitcheId, and SecurityGroupId are required.
        # 
        # This parameter is required.
        self.network_type = network_type
        # The security group ID.
        self.security_group_id = security_group_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitche_id = vswitche_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitche_id is not None:
            result['VswitcheId'] = self.vswitche_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitcheId') is not None:
            self.vswitche_id = m.get('VswitcheId')

        return self

class CreateConnectionRequestAuthParameters(DaraModel):
    def __init__(
        self,
        api_key_auth_parameters: main_models.CreateConnectionRequestAuthParametersApiKeyAuthParameters = None,
        authorization_type: str = None,
        basic_auth_parameters: main_models.CreateConnectionRequestAuthParametersBasicAuthParameters = None,
        oauth_parameters: main_models.CreateConnectionRequestAuthParametersOAuthParameters = None,
    ):
        # The API key authentication configuration.
        self.api_key_auth_parameters = api_key_auth_parameters
        # The authentication type:
        # 
        # - BASIC: BASIC_AUTH. This authorization method is a basic authorization method implemented by browsers in compliance with the HTTP protocol. During HTTP communication, the HTTP protocol defines a basic authentication method that allows an HTTP server to authenticate clients. Add `Authorization: Basic Base64Encoded(username:password)` in the fixed format to the request header. Username and Password are required.
        # 
        # - API KEY: API_KEY_AUTH. Add `Token: TokenValue` in the fixed format to the request header. ApiKeyName and ApiKeyValue are required.
        # 
        # - OAUTH: OAUTH_AUTH. OAuth 2.0 is an authorization mechanism. In a system that does not use an authorization mechanism such as OAuth 2.0, the client can directly access resources on the resource server. To ensure secure data access, an Access Token mechanism is added. The client must carry an Access Token to access protected resources. OAuth 2.0 prevents resources from being accessed by malicious clients, which improves system security. AuthorizationEndpoint, OAuthHttpParameters, and HttpMethod are required.
        self.authorization_type = authorization_type
        # The basic authentication configuration.
        self.basic_auth_parameters = basic_auth_parameters
        # The OAuth authentication configuration.
        self.oauth_parameters = oauth_parameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.oauth_parameters:
            self.oauth_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_auth_parameters is not None:
            result['ApiKeyAuthParameters'] = self.api_key_auth_parameters.to_map()

        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type

        if self.basic_auth_parameters is not None:
            result['BasicAuthParameters'] = self.basic_auth_parameters.to_map()

        if self.oauth_parameters is not None:
            result['OAuthParameters'] = self.oauth_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyAuthParameters') is not None:
            temp_model = main_models.CreateConnectionRequestAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m.get('ApiKeyAuthParameters'))

        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')

        if m.get('BasicAuthParameters') is not None:
            temp_model = main_models.CreateConnectionRequestAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m.get('BasicAuthParameters'))

        if m.get('OAuthParameters') is not None:
            temp_model = main_models.CreateConnectionRequestAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m.get('OAuthParameters'))

        return self

class CreateConnectionRequestAuthParametersOAuthParameters(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_parameters: main_models.CreateConnectionRequestAuthParametersOAuthParametersClientParameters = None,
        http_method: str = None,
        oauth_http_parameters: main_models.CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters = None,
    ):
        # The authorization endpoint URL. Maximum length: 127 characters.
        self.authorization_endpoint = authorization_endpoint
        # The client parameter configuration.
        self.client_parameters = client_parameters
        # The HTTP method. Valid values:
        # 
        # - GET
        # - POST
        # - HEAD
        # - DELETE
        # - PUT
        # - PATCH
        self.http_method = http_method
        # The OAuth authentication request parameters.
        self.oauth_http_parameters = oauth_http_parameters

    def validate(self):
        if self.client_parameters:
            self.client_parameters.validate()
        if self.oauth_http_parameters:
            self.oauth_http_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_endpoint is not None:
            result['AuthorizationEndpoint'] = self.authorization_endpoint

        if self.client_parameters is not None:
            result['ClientParameters'] = self.client_parameters.to_map()

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.oauth_http_parameters is not None:
            result['OAuthHttpParameters'] = self.oauth_http_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('AuthorizationEndpoint')

        if m.get('ClientParameters') is not None:
            temp_model = main_models.CreateConnectionRequestAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m.get('ClientParameters'))

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('OAuthHttpParameters') is not None:
            temp_model = main_models.CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m.get('OAuthHttpParameters'))

        return self

class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters(DaraModel):
    def __init__(
        self,
        body_parameters: List[main_models.CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters] = None,
        header_parameters: List[main_models.CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters] = None,
        query_string_parameters: List[main_models.CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters] = None,
    ):
        # The list of body request parameter configurations.
        self.body_parameters = body_parameters
        # The list of header parameter configurations.
        self.header_parameters = header_parameters
        # The structure of the URI of the request path parameters.
        self.query_string_parameters = query_string_parameters

    def validate(self):
        if self.body_parameters:
            for v1 in self.body_parameters:
                 if v1:
                    v1.validate()
        if self.header_parameters:
            for v1 in self.header_parameters:
                 if v1:
                    v1.validate()
        if self.query_string_parameters:
            for v1 in self.query_string_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BodyParameters'] = []
        if self.body_parameters is not None:
            for k1 in self.body_parameters:
                result['BodyParameters'].append(k1.to_map() if k1 else None)

        result['HeaderParameters'] = []
        if self.header_parameters is not None:
            for k1 in self.header_parameters:
                result['HeaderParameters'].append(k1.to_map() if k1 else None)

        result['QueryStringParameters'] = []
        if self.query_string_parameters is not None:
            for k1 in self.query_string_parameters:
                result['QueryStringParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body_parameters = []
        if m.get('BodyParameters') is not None:
            for k1 in m.get('BodyParameters'):
                temp_model = main_models.CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k1))

        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k1 in m.get('HeaderParameters'):
                temp_model = main_models.CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k1))

        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k1 in m.get('QueryStringParameters'):
                temp_model = main_models.CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k1))

        return self

class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(DaraModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether the value is a secret.
        self.is_value_secret = is_value_secret
        # The key of the URI of the request path parameter.
        self.key = key
        # The value of the URI of the request path parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(DaraModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether the value is a secret.
        self.is_value_secret = is_value_secret
        # The key of the header parameter.
        self.key = key
        # The value of the header parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(DaraModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether the value is a secret.
        self.is_value_secret = is_value_secret
        # The key of the body request parameter.
        self.key = key
        # The value of the body request parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateConnectionRequestAuthParametersOAuthParametersClientParameters(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The client secret of the application.
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientID'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientID') is not None:
            self.client_id = m.get('ClientID')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        return self

class CreateConnectionRequestAuthParametersBasicAuthParameters(DaraModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        # The password for basic authentication.
        self.password = password
        # The username for basic authentication.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['Password'] = self.password

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class CreateConnectionRequestAuthParametersApiKeyAuthParameters(DaraModel):
    def __init__(
        self,
        api_key_name: str = None,
        api_key_value: str = None,
    ):
        # The key name of the API key.
        self.api_key_name = api_key_name
        # The value of the API key.
        self.api_key_value = api_key_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_name is not None:
            result['ApiKeyName'] = self.api_key_name

        if self.api_key_value is not None:
            result['ApiKeyValue'] = self.api_key_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyName') is not None:
            self.api_key_name = m.get('ApiKeyName')

        if m.get('ApiKeyValue') is not None:
            self.api_key_value = m.get('ApiKeyValue')

        return self

