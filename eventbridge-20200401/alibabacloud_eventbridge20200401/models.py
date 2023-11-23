# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateApiDestinationRequestHttpApiParameters(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        method: str = None,
    ):
        # The endpoint of the API destination. The endpoint can be up to 127 characters in length.
        self.endpoint = endpoint
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        # *   DELETE
        # *   PUT
        # *   PATCH
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class CreateApiDestinationRequest(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        http_api_parameters: CreateApiDestinationRequestHttpApiParameters = None,
    ):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        self.api_destination_name = api_destination_name
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # > 
        # >  Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        self.connection_name = connection_name
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the API destination.
        self.http_api_parameters = http_api_parameters

    def validate(self):
        if self.http_api_parameters:
            self.http_api_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.http_api_parameters is not None:
            result['HttpApiParameters'] = self.http_api_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpApiParameters') is not None:
            temp_model = CreateApiDestinationRequestHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
        return self


class CreateApiDestinationShrinkRequest(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        http_api_parameters_shrink: str = None,
    ):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        self.api_destination_name = api_destination_name
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # > 
        # >  Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        self.connection_name = connection_name
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the API destination.
        self.http_api_parameters_shrink = http_api_parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.http_api_parameters_shrink is not None:
            result['HttpApiParameters'] = self.http_api_parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpApiParameters') is not None:
            self.http_api_parameters_shrink = m.get('HttpApiParameters')
        return self


class CreateApiDestinationResponseBodyDate(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
    ):
        # The name of the API destination.
        self.api_destination_name = api_destination_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        return self


class CreateApiDestinationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        date: CreateApiDestinationResponseBodyDate = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The data returned if the API destination is created.
        self.date = date
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.date is not None:
            result['Date'] = self.date.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Date') is not None:
            temp_model = CreateApiDestinationResponseBodyDate()
            self.date = temp_model.from_map(m['Date'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApiDestinationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApiDestinationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateApiDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnectionRequestAuthParametersApiKeyAuthParameters(TeaModel):
    def __init__(
        self,
        api_key_name: str = None,
        api_key_value: str = None,
    ):
        # The key of the API key.
        self.api_key_name = api_key_name
        # The value of the API key.
        self.api_key_value = api_key_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateConnectionRequestAuthParametersBasicAuthParameters(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateConnectionRequestAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The AccessKey secret of the client.
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret
        # The key of the request body.
        self.key = key
        # The value of the request body.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret
        # The key of the request header.
        self.key = key
        # The value of the request header.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret
        # The key of the request path.
        self.key = key
        # The value of the request path.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters(TeaModel):
    def __init__(
        self,
        body_parameters: List[CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters] = None,
        header_parameters: List[CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters] = None,
        query_string_parameters: List[CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters] = None,
    ):
        # The parameters that are configured for the request body.
        self.body_parameters = body_parameters
        # The parameters that are configured for the request header.
        self.header_parameters = header_parameters
        # The parameters that are configured for the request path.
        self.query_string_parameters = query_string_parameters

    def validate(self):
        if self.body_parameters:
            for k in self.body_parameters:
                if k:
                    k.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.query_string_parameters:
            for k in self.query_string_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyParameters'] = []
        if self.body_parameters is not None:
            for k in self.body_parameters:
                result['BodyParameters'].append(k.to_map() if k else None)
        result['HeaderParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['HeaderParameters'].append(k.to_map() if k else None)
        result['QueryStringParameters'] = []
        if self.query_string_parameters is not None:
            for k in self.query_string_parameters:
                result['QueryStringParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body_parameters = []
        if m.get('BodyParameters') is not None:
            for k in m.get('BodyParameters'):
                temp_model = CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class CreateConnectionRequestAuthParametersOAuthParameters(TeaModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_parameters: CreateConnectionRequestAuthParametersOAuthParametersClientParameters = None,
        http_method: str = None,
        oauth_http_parameters: CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters = None,
    ):
        # The IP address of the authorized endpoint. The default value of a column can be up to 127 characters in length.
        self.authorization_endpoint = authorization_endpoint
        # The parameters that are configured for the client.
        self.client_parameters = client_parameters
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        # *   DELETE
        # *   PUT
        # *   PATCH
        self.http_method = http_method
        # The request parameters that are configured for OAuth authentication.
        self.oauth_http_parameters = oauth_http_parameters

    def validate(self):
        if self.client_parameters:
            self.client_parameters.validate()
        if self.oauth_http_parameters:
            self.oauth_http_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateConnectionRequestAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m['ClientParameters'])
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('OAuthHttpParameters') is not None:
            temp_model = CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m['OAuthHttpParameters'])
        return self


class CreateConnectionRequestAuthParameters(TeaModel):
    def __init__(
        self,
        api_key_auth_parameters: CreateConnectionRequestAuthParametersApiKeyAuthParameters = None,
        authorization_type: str = None,
        basic_auth_parameters: CreateConnectionRequestAuthParametersBasicAuthParameters = None,
        oauth_parameters: CreateConnectionRequestAuthParametersOAuthParameters = None,
    ):
        # The parameters that are configured for API key authentication.
        self.api_key_auth_parameters = api_key_auth_parameters
        # The authentication type. Valid values:
        # 
        # BASIC_AUTH: basic authentication.
        # 
        # Introduction: Basic authentication is a simple authentication scheme built into the HTTP protocol. When you use the HTTP protocol for communications, the authentication method that the HTTP server uses to authenticate user identities on the client is defined in the protocol. The request header is in the Authorization: Basic Base64-encoded string (Username:Password) format.
        # 
        # 1.  Username and Password are required.
        # 
        # API_KEY_AUTH: API key authentication.
        # 
        # Introduction: The request header is in the Token: Token value format.
        # 
        # *   ApiKeyName and ApiKeyValue are required.
        # 
        # OAUTH_AUTH: OAuth authentication.
        # 
        # Introduction: OAuth2.0 is an authentication mechanism. In normal cases, a system that does not use OAuth2.0 can access the resources of the server from the client. To ensure access security, access tokens are used to authenticate users in OAuth 2.0. The client must use an access token to access protected resources. This way, OAuth 2.0 protects resources from being accessed from malicious clients and improves system security.
        # 
        # *   AuthorizationEndpoint, OAuthHttpParameters, and HttpMethod are required.
        self.authorization_type = authorization_type
        # The parameters that are configured for basic authentication.
        self.basic_auth_parameters = basic_auth_parameters
        # The parameters that are configured for OAuth authentication.
        self.oauth_parameters = oauth_parameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.oauth_parameters:
            self.oauth_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateConnectionRequestAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('BasicAuthParameters') is not None:
            temp_model = CreateConnectionRequestAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
        if m.get('OAuthParameters') is not None:
            temp_model = CreateConnectionRequestAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
        return self


class CreateConnectionRequestNetworkParameters(TeaModel):
    def __init__(
        self,
        network_type: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitche_id: str = None,
    ):
        # The network type. Valid values:
        # 
        # PublicNetwork and PrivateNetwork.
        # 
        # *   Note: If you set this parameter to PrivateNetwork, you must configure VpcId, VswitcheId, and SecurityGroupId.
        self.network_type = network_type
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The VPC. ID
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitche_id = vswitche_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateConnectionRequest(TeaModel):
    def __init__(
        self,
        auth_parameters: CreateConnectionRequestAuthParameters = None,
        connection_name: str = None,
        description: str = None,
        network_parameters: CreateConnectionRequestNetworkParameters = None,
    ):
        # The parameters that are configured for authentication.
        self.auth_parameters = auth_parameters
        # The name of the connection. The name must be 2 to 127 characters in length.
        self.connection_name = connection_name
        # The description of the connection. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the network.
        self.network_parameters = network_parameters

    def validate(self):
        if self.auth_parameters:
            self.auth_parameters.validate()
        if self.network_parameters:
            self.network_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters is not None:
            result['AuthParameters'] = self.auth_parameters.to_map()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.network_parameters is not None:
            result['NetworkParameters'] = self.network_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            temp_model = CreateConnectionRequestAuthParameters()
            self.auth_parameters = temp_model.from_map(m['AuthParameters'])
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkParameters') is not None:
            temp_model = CreateConnectionRequestNetworkParameters()
            self.network_parameters = temp_model.from_map(m['NetworkParameters'])
        return self


class CreateConnectionShrinkRequest(TeaModel):
    def __init__(
        self,
        auth_parameters_shrink: str = None,
        connection_name: str = None,
        description: str = None,
        network_parameters_shrink: str = None,
    ):
        # The parameters that are configured for authentication.
        self.auth_parameters_shrink = auth_parameters_shrink
        # The name of the connection. The name must be 2 to 127 characters in length.
        self.connection_name = connection_name
        # The description of the connection. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the network.
        self.network_parameters_shrink = network_parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters_shrink is not None:
            result['AuthParameters'] = self.auth_parameters_shrink
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.network_parameters_shrink is not None:
            result['NetworkParameters'] = self.network_parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            self.auth_parameters_shrink = m.get('AuthParameters')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkParameters') is not None:
            self.network_parameters_shrink = m.get('NetworkParameters')
        return self


class CreateConnectionResponseBodyData(TeaModel):
    def __init__(
        self,
        connection_name: str = None,
    ):
        # The connection name.
        self.connection_name = connection_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        return self


class CreateConnectionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateConnectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateConnectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventBusRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
    ):
        # The description of the event bus.
        self.description = description
        # The name of the event bus.
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class CreateEventBusResponseBodyData(TeaModel):
    def __init__(
        self,
        event_bus_arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.event_bus_arn = event_bus_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')
        return self


class CreateEventBusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEventBusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. The value true indicates that the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateEventBusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventBusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEventBusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventSourceRequestSourceHttpEventParameters(TeaModel):
    def __init__(
        self,
        ip: List[str] = None,
        method: List[str] = None,
        referer: List[str] = None,
        security_config: str = None,
        type: str = None,
    ):
        # The CIDR block that is used for security settings. This parameter is required only if you set SecurityConfig to ip. You can enter a CIDR block or an IP address.
        self.ip = ip
        # The HTTP request method supported by the generated webhook URL. You can select multiple values. Valid values:
        # 
        # *   GET
        # *   POST
        # *   PUT
        # *   PATCH
        # *   DELETE
        # *   HEAD
        # *   OPTIONS
        # *   TRACE
        # *   CONNECT
        self.method = method
        # The security domain name. This parameter is required only if you set SecurityConfig to referer. You can enter a domain name.
        self.referer = referer
        # The type of security settings. Valid values:
        # 
        # *   none: No configuration is required.
        # *   ip: CIDR block.
        # *   referer: security domain name.
        self.security_config = security_config
        # The protocol type that is supported by the generated webhook URL. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # *   HTTP\&HTTPS
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.method is not None:
            result['Method'] = self.method
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.security_config is not None:
            result['SecurityConfig'] = self.security_config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SecurityConfig') is not None:
            self.security_config = m.get('SecurityConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateEventSourceRequestSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        maximum_tasks: int = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id
        # The maximum number of consumers.
        self.maximum_tasks = maximum_tasks
        # The network. Valid values: Default and PublicNetwork. Default value: Default. The value PublicNetwork indicates a self-managed network.
        self.network = network
        # The consumer offset.
        self.offset_reset = offset_reset
        # The ID of the region where the Message Queue for Apache Kafka instance resides.
        self.region_id = region_id
        # The ID of the security group to which the Message Queue for Apache Kafka instance belongs. This parameter is required only if you set Network to PublicNetwork.
        self.security_group_id = security_group_id
        # The name of the topic on the Message Queue for Apache Kafka instance.
        self.topic = topic
        # The ID of the vSwitch with which the Message Queue for Apache Kafka instance is associated. This parameter is required only if you set Network to PublicNetwork.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC in which the Message Queue for Apache Kafka instance resides. This parameter is required only if you set Network to PublicNetwork.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateEventSourceRequestSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable Base64 decoding. Valid values: true and false.
        self.is_base_64decode = is_base_64decode
        # The name of the MNS queue.
        self.queue_name = queue_name
        # The region where the MNS queue resides. Valid values: cn-qingdao, cn-beijing, cn-zhangjiakou, cn-huhehaote, cn-wulanchabu, cn-hangzhou, cn-shanghai, cn-shenzhen, cn-guangzhou, cn-chengdu, cn-hongkong, ap-southeast-1, ap-southeast-2, ap-southeast-3, ap-southeast-5, ap-northeast-1, eu-central-1, us-west-1, us-east-1, ap-south-1, me-east-1, and cn-north-2-gov-1.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEventSourceRequestSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # The ID of the Message Queue for RabbitMQ instance. For more information, see Limits.
        self.instance_id = instance_id
        # The name of the queue on the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.queue_name = queue_name
        # The ID of the region where the Message Queue for RabbitMQ instance resides.
        self.region_id = region_id
        # The name of the vhost of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class CreateEventSourceRequestSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        # The authentication type. You can set this parameter to ACL or leave this parameter empty.
        self.auth_type = auth_type
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id
        # The endpoint that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_endpoint = instance_endpoint
        # The ID of the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id
        # None.
        self.instance_network = instance_network
        # The password that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_password = instance_password
        # The ID of the security group to which the Message Queue for Apache RocketMQ instance belongs.
        self.instance_security_group_id = instance_security_group_id
        # The type of the Message Queue for Apache RocketMQ instance. Valid values:
        # 
        # *   Cloud\_4: Message Queue for Apache RocketMQ 4.0 instance.
        # *   Cloud\_5: Message Queue for Apache RocketMQ 5.0 instance.
        self.instance_type = instance_type
        # The username that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_username = instance_username
        # The ID of the vSwitch with which the Message Queue for Apache RocketMQ instance is associated.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The ID of the virtual private cloud (VPC) in which the Message Queue for Apache RocketMQ instance resides.
        self.instance_vpc_id = instance_vpc_id
        # The offset from which message consumption starts. Valid values: CONSUME_FROM_LAST_OFFSET: Start message consumption from the latest offset. CONSUME_FROM_FIRST_OFFSET: Start message consumption from the earliest offset. CONSUME_FROM_TIMESTAMP: Start message consumption from the offset at the specified point in time. Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset
        # The region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id
        # The tag that is used to filter messages.
        self.tag = tag
        # The timestamp that specifies the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The name of the topic on the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class CreateEventSourceRequestSourceSLSParameters(TeaModel):
    def __init__(
        self,
        consume_position: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The starting consumer offset. The value begin specifies the earliest offset, and the value end specifies the latest offset. You can also specify a time in seconds to start consumption.
        self.consume_position = consume_position
        # The Log Service Logstore.
        self.log_store = log_store
        # The Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console. For information about the permission policy of this role, see Create a custom event source of the Log Service type.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateEventSourceRequestSourceScheduledEventParameters(TeaModel):
    def __init__(
        self,
        schedule: str = None,
        time_zone: str = None,
        user_data: str = None,
    ):
        # The cron expression.
        self.schedule = schedule
        # The time zone in which the cron expression is executed.
        self.time_zone = time_zone
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateEventSourceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_source_name: str = None,
        source_http_event_parameters: CreateEventSourceRequestSourceHttpEventParameters = None,
        source_kafka_parameters: CreateEventSourceRequestSourceKafkaParameters = None,
        source_mnsparameters: CreateEventSourceRequestSourceMNSParameters = None,
        source_rabbit_mqparameters: CreateEventSourceRequestSourceRabbitMQParameters = None,
        source_rocket_mqparameters: CreateEventSourceRequestSourceRocketMQParameters = None,
        source_slsparameters: CreateEventSourceRequestSourceSLSParameters = None,
        source_scheduled_event_parameters: CreateEventSourceRequestSourceScheduledEventParameters = None,
    ):
        # The description of the event source.
        self.description = description
        # The name of the event bus with which the event source is associated.
        self.event_bus_name = event_bus_name
        # The name of the event source.
        self.event_source_name = event_source_name
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters = source_http_event_parameters
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters = source_kafka_parameters
        # The parameters that are configured if the event source is Message Service (MNS). If you specify MNS as the event source, you must configure RegionId, IsBase64Decode, and QueueName.
        self.source_mnsparameters = source_mnsparameters
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The parameters that are configured if the event source is Log Service.
        self.source_slsparameters = source_slsparameters
        # The parameters that are configured if the event source is scheduled events.
        self.source_scheduled_event_parameters = source_scheduled_event_parameters

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()
        if self.source_scheduled_event_parameters:
            self.source_scheduled_event_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        if self.source_scheduled_event_parameters is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('SourceHttpEventParameters') is not None:
            temp_model = CreateEventSourceRequestSourceHttpEventParameters()
            self.source_http_event_parameters = temp_model.from_map(m['SourceHttpEventParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = CreateEventSourceRequestSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = CreateEventSourceRequestSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = CreateEventSourceRequestSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = CreateEventSourceRequestSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = CreateEventSourceRequestSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        if m.get('SourceScheduledEventParameters') is not None:
            temp_model = CreateEventSourceRequestSourceScheduledEventParameters()
            self.source_scheduled_event_parameters = temp_model.from_map(m['SourceScheduledEventParameters'])
        return self


class CreateEventSourceShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_source_name: str = None,
        source_http_event_parameters_shrink: str = None,
        source_kafka_parameters_shrink: str = None,
        source_mnsparameters_shrink: str = None,
        source_rabbit_mqparameters_shrink: str = None,
        source_rocket_mqparameters_shrink: str = None,
        source_slsparameters_shrink: str = None,
        source_scheduled_event_parameters_shrink: str = None,
    ):
        # The description of the event source.
        self.description = description
        # The name of the event bus with which the event source is associated.
        self.event_bus_name = event_bus_name
        # The name of the event source.
        self.event_source_name = event_source_name
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters_shrink = source_http_event_parameters_shrink
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters_shrink = source_kafka_parameters_shrink
        # The parameters that are configured if the event source is Message Service (MNS). If you specify MNS as the event source, you must configure RegionId, IsBase64Decode, and QueueName.
        self.source_mnsparameters_shrink = source_mnsparameters_shrink
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters_shrink = source_rabbit_mqparameters_shrink
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters_shrink = source_rocket_mqparameters_shrink
        # The parameters that are configured if the event source is Log Service.
        self.source_slsparameters_shrink = source_slsparameters_shrink
        # The parameters that are configured if the event source is scheduled events.
        self.source_scheduled_event_parameters_shrink = source_scheduled_event_parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters_shrink is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters_shrink
        if self.source_kafka_parameters_shrink is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters_shrink
        if self.source_mnsparameters_shrink is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters_shrink
        if self.source_rabbit_mqparameters_shrink is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters_shrink
        if self.source_rocket_mqparameters_shrink is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters_shrink
        if self.source_slsparameters_shrink is not None:
            result['SourceSLSParameters'] = self.source_slsparameters_shrink
        if self.source_scheduled_event_parameters_shrink is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('SourceHttpEventParameters') is not None:
            self.source_http_event_parameters_shrink = m.get('SourceHttpEventParameters')
        if m.get('SourceKafkaParameters') is not None:
            self.source_kafka_parameters_shrink = m.get('SourceKafkaParameters')
        if m.get('SourceMNSParameters') is not None:
            self.source_mnsparameters_shrink = m.get('SourceMNSParameters')
        if m.get('SourceRabbitMQParameters') is not None:
            self.source_rabbit_mqparameters_shrink = m.get('SourceRabbitMQParameters')
        if m.get('SourceRocketMQParameters') is not None:
            self.source_rocket_mqparameters_shrink = m.get('SourceRocketMQParameters')
        if m.get('SourceSLSParameters') is not None:
            self.source_slsparameters_shrink = m.get('SourceSLSParameters')
        if m.get('SourceScheduledEventParameters') is not None:
            self.source_scheduled_event_parameters_shrink = m.get('SourceScheduledEventParameters')
        return self


class CreateEventSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        event_source_arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the resource.
        self.event_source_arn = event_source_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_arn is not None:
            result['EventSourceARN'] = self.event_source_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSourceARN') is not None:
            self.event_source_arn = m.get('EventSourceARN')
        return self


class CreateEventSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEventSourceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateEventSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEventSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventStreamingRequestRunOptionsBatchWindow(TeaModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        # The maximum number of events that is allowed in the batch window. When this threshold is reached, data in the window is pushed to the downstream service. If multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.count_based_window = count_based_window
        # The maximum period of time during which events are allowed in the batch window. Unit: seconds. When this threshold is reached, data in the window is pushed to the downstream service. If multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class CreateEventStreamingRequestRunOptionsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue.
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateEventStreamingRequestRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: int = None,
        maximum_retry_attempts: int = None,
        push_retry_strategy: str = None,
    ):
        # The maximum timeout period for a retry.
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        # The maximum number of retries.
        self.maximum_retry_attempts = maximum_retry_attempts
        # The retry policy. Valid values:
        # 
        # *   BACKOFF_RETRY
        # *   EXPONENTIAL_DECAY_RETRY
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class CreateEventStreamingRequestRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: CreateEventStreamingRequestRunOptionsBatchWindow = None,
        dead_letter_queue: CreateEventStreamingRequestRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: CreateEventStreamingRequestRunOptionsRetryStrategy = None,
    ):
        # The batch window.
        self.batch_window = batch_window
        # Specifies whether to enable dead-letter queues. By default, dead-letter queues are disabled. Messages that fail to be pushed are discarded after the maximum number of retries that is specified by the retry policy is reached.
        self.dead_letter_queue = dead_letter_queue
        # The exception tolerance policy. Valid values:
        # 
        # *   NONE: does not tolerate exceptions.
        # *   ALL: tolerates all exceptions.
        self.errors_tolerance = errors_tolerance
        # The maximum number of concurrent threads.
        self.maximum_tasks = maximum_tasks
        # The retry policy that you want to use if events fail to be pushed.
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = CreateEventStreamingRequestRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = CreateEventStreamingRequestRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = CreateEventStreamingRequestRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # None.
        self.template = template
        # The BLOB topic.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersProject(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the DataHub project.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The role name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the DataHub topic.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The TUBLE topic.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersTopicType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The topic type. Valid values:
        # 
        # *   TUPLE
        # *   BLOB
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkDataHubParametersBody = None,
        project: CreateEventStreamingRequestSinkSinkDataHubParametersProject = None,
        role_name: CreateEventStreamingRequestSinkSinkDataHubParametersRoleName = None,
        topic: CreateEventStreamingRequestSinkSinkDataHubParametersTopic = None,
        topic_schema: CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema = None,
        topic_type: CreateEventStreamingRequestSinkSinkDataHubParametersTopicType = None,
    ):
        # The BLOB topic.
        self.body = body
        # The name of the DataHub project.
        self.project = project
        # The role name.
        self.role_name = role_name
        # The name of the DataHub topic.
        self.topic = topic
        # The TUBLE topic.
        self.topic_schema = topic_schema
        # The topic type. Valid values:
        # 
        # *   TUPLE
        # *   BLOB
        self.topic_type = topic_type

    def validate(self):
        if self.body:
            self.body.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()
        if self.topic_schema:
            self.topic_schema.validate()
        if self.topic_type:
            self.topic_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.topic_schema is not None:
            result['TopicSchema'] = self.topic_schema.to_map()
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Project') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('TopicSchema') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema()
            self.topic_schema = temp_model.from_map(m['TopicSchema'])
        if m.get('TopicType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersTopicType()
            self.topic_type = temp_model.from_map(m['TopicType'])
        return self


class CreateEventStreamingRequestSinkSinkFcParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersConcurrency(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The delivery concurrency. Minimum value: 1.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The function name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The invocation method. Valid values: Sync and Async.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersQualifier(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The service version.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersServiceName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The service name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkFcParametersBody = None,
        concurrency: CreateEventStreamingRequestSinkSinkFcParametersConcurrency = None,
        function_name: CreateEventStreamingRequestSinkSinkFcParametersFunctionName = None,
        invocation_type: CreateEventStreamingRequestSinkSinkFcParametersInvocationType = None,
        qualifier: CreateEventStreamingRequestSinkSinkFcParametersQualifier = None,
        service_name: CreateEventStreamingRequestSinkSinkFcParametersServiceName = None,
    ):
        # The message body that you want to deliver to Function Compute.
        self.body = body
        # The delivery concurrency. Minimum value: 1.
        self.concurrency = concurrency
        # The function name.
        self.function_name = function_name
        # The invocation method. Valid values: Sync and Async.
        self.invocation_type = invocation_type
        # The service version.
        self.qualifier = qualifier
        # The service name.
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.concurrency:
            self.concurrency.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Concurrency') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m['Concurrency'])
        if m.get('FunctionName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class CreateEventStreamingRequestSinkSinkFnfParametersExecutionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The execution name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFnfParametersFlowName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The flow name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFnfParametersInput(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The input information of the execution.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFnfParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The role name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFnfParameters(TeaModel):
    def __init__(
        self,
        execution_name: CreateEventStreamingRequestSinkSinkFnfParametersExecutionName = None,
        flow_name: CreateEventStreamingRequestSinkSinkFnfParametersFlowName = None,
        input: CreateEventStreamingRequestSinkSinkFnfParametersInput = None,
        role_name: CreateEventStreamingRequestSinkSinkFnfParametersRoleName = None,
    ):
        # The execution name.
        self.execution_name = execution_name
        # The flow name.
        self.flow_name = flow_name
        # The input information of the execution.
        self.input = input
        # The role name.
        self.role_name = role_name

    def validate(self):
        if self.execution_name:
            self.execution_name.validate()
        if self.flow_name:
            self.flow_name.validate()
        if self.input:
            self.input.validate()
        if self.role_name:
            self.role_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name.to_map()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name.to_map()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m['ExecutionName'])
        if m.get('FlowName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m['FlowName'])
        if m.get('Input') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('RoleName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The ACK mode.
        # 
        # *   If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high.
        # *   If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader.
        # *   If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The instance ID.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The message key.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The topic name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersValue(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: CreateEventStreamingRequestSinkSinkKafkaParametersAcks = None,
        instance_id: CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId = None,
        key: CreateEventStreamingRequestSinkSinkKafkaParametersKey = None,
        topic: CreateEventStreamingRequestSinkSinkKafkaParametersTopic = None,
        value: CreateEventStreamingRequestSinkSinkKafkaParametersValue = None,
    ):
        # The acknowledgement (ACK) mode.
        # 
        # *   If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high.
        # *   If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader.
        # *   If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.acks = acks
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id
        # The message key.
        self.key = key
        # The topic name.
        self.topic = topic
        # The message body.
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class CreateEventStreamingRequestSinkSinkMNSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # Specifies that Base64 encoding is enabled.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The name of the MNS queue.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkMNSParametersBody = None,
        is_base_64encode: CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: CreateEventStreamingRequestSinkSinkMNSParametersQueueName = None,
    ):
        # The message body.
        self.body = body
        # Specifies whether to enable Base64 encoding.
        self.is_base_64encode = is_base_64encode
        # The name of the MNS queue.
        self.queue_name = queue_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The name of the exchange on the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The ID of the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The name of the queue on the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The rule that you want to use to route messages.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The type of the resource to which you want to deliver events. Valid values:
        # 
        # *   Exchange
        # *   Queue
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The name of the vhost of the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkRabbitMQParametersBody = None,
        exchange: CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange = None,
        instance_id: CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId = None,
        message_id: CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId = None,
        properties: CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties = None,
        queue_name: CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName = None,
        routing_key: CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        # The message body.
        self.body = body
        # The exchange to which you want to deliver events. This parameter is available only if you set TargetType to Exchange.
        self.exchange = exchange
        # The information about the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id
        # The message ID.
        self.message_id = message_id
        # The properties that you want to use to filter messages.
        self.properties = properties
        # The queue to which you want to deliver events. This parameter is available only if you set TargetType to Queue.
        self.queue_name = queue_name
        # The rule that you want to use to route messages. This parameter is available only if you set TargetType to Exchange.
        self.routing_key = routing_key
        # The type of the resource to which you want to deliver events.
        self.target_type = target_type
        # The name of the vhost of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The instance endpoint.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The instance password.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The instance type.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The instance username.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The network type. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The security group ID.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The name of the topic on the Message Queue for Apache RocketMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The vSwitch ID.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The VPC ID.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkRocketMQParametersBody = None,
        instance_endpoint: CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint = None,
        instance_id: CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId = None,
        instance_password: CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword = None,
        instance_type: CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType = None,
        instance_username: CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername = None,
        keys: CreateEventStreamingRequestSinkSinkRocketMQParametersKeys = None,
        network: CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork = None,
        properties: CreateEventStreamingRequestSinkSinkRocketMQParametersProperties = None,
        security_group_id: CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId = None,
        tags: CreateEventStreamingRequestSinkSinkRocketMQParametersTags = None,
        topic: CreateEventStreamingRequestSinkSinkRocketMQParametersTopic = None,
        v_switch_ids: CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds = None,
        vpc_id: CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId = None,
    ):
        # The message body.
        self.body = body
        # The instance endpoint.
        self.instance_endpoint = instance_endpoint
        # The parameters that are configured if you specify the event target as Message Queue for Apache RocketMQ.
        self.instance_id = instance_id
        # The instance password.
        self.instance_password = instance_password
        # The instance type.
        self.instance_type = instance_type
        # The instance username.
        self.instance_username = instance_username
        # The keys that you want to use to filter messages.
        self.keys = keys
        # The network type. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
        self.network = network
        # The properties that you want to use to filter messages.
        self.properties = properties
        # The security group ID.
        self.security_group_id = security_group_id
        # The tags that you want to use to filter messages.
        self.tags = tags
        # The topic on the Message Queue for Apache RocketMQ instance.
        self.topic = topic
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_endpoint:
            self.instance_endpoint.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.instance_password:
            self.instance_password.validate()
        if self.instance_type:
            self.instance_type.validate()
        if self.instance_username:
            self.instance_username.validate()
        if self.keys:
            self.keys.validate()
        if self.network:
            self.network.validate()
        if self.properties:
            self.properties.validate()
        if self.security_group_id:
            self.security_group_id.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()
        if self.vpc_id:
            self.vpc_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password.to_map()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type.to_map()
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceEndpoint') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint()
            self.instance_endpoint = temp_model.from_map(m['InstanceEndpoint'])
        if m.get('InstanceId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('InstancePassword') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword()
            self.instance_password = temp_model.from_map(m['InstancePassword'])
        if m.get('InstanceType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType()
            self.instance_type = temp_model.from_map(m['InstanceType'])
        if m.get('InstanceUsername') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername()
            self.instance_username = temp_model.from_map(m['InstanceUsername'])
        if m.get('Keys') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Network') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('Properties') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('SecurityGroupId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m['SecurityGroupId'])
        if m.get('Tags') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('VSwitchIds') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m['VSwitchIds'])
        if m.get('VpcId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId()
            self.vpc_id = temp_model.from_map(m['VpcId'])
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events.
        self.form = form
        # The template based on which you want to transform events.
        self.template = template
        # The value before transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The Simple Log Service Logstore.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersProject(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The Simple Log Service project.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The topic that you want to use to store logs. This parameter corresponds to the **topic** reserved field in Simple Log Service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkSLSParametersBody = None,
        log_store: CreateEventStreamingRequestSinkSinkSLSParametersLogStore = None,
        project: CreateEventStreamingRequestSinkSinkSLSParametersProject = None,
        role_name: CreateEventStreamingRequestSinkSinkSLSParametersRoleName = None,
        topic: CreateEventStreamingRequestSinkSinkSLSParametersTopic = None,
    ):
        # The message body that you want to deliver to Simple Log Service.
        self.body = body
        # The Simple Log Service Logstore.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name
        # The topic that you want to use to store logs. This parameter corresponds to the **topic** reserved field in Simple Log Service.
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class CreateEventStreamingRequestSink(TeaModel):
    def __init__(
        self,
        sink_data_hub_parameters: CreateEventStreamingRequestSinkSinkDataHubParameters = None,
        sink_fc_parameters: CreateEventStreamingRequestSinkSinkFcParameters = None,
        sink_fnf_parameters: CreateEventStreamingRequestSinkSinkFnfParameters = None,
        sink_kafka_parameters: CreateEventStreamingRequestSinkSinkKafkaParameters = None,
        sink_mnsparameters: CreateEventStreamingRequestSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: CreateEventStreamingRequestSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: CreateEventStreamingRequestSinkSinkRocketMQParameters = None,
        sink_slsparameters: CreateEventStreamingRequestSinkSinkSLSParameters = None,
    ):
        # The parameters that are configured if you specify the event target as DataHub.
        self.sink_data_hub_parameters = sink_data_hub_parameters
        # The parameters that are configured if you specify the event target as Function Compute.
        self.sink_fc_parameters = sink_fc_parameters
        # The parameters that are configured if you specify the event target as Serverless Workflow.
        self.sink_fnf_parameters = sink_fnf_parameters
        # The parameters that are configured if you specify the event target as Message Queue for Apache Kafka.
        self.sink_kafka_parameters = sink_kafka_parameters
        # The parameters that are configured if you specify the event target as MNS.
        self.sink_mnsparameters = sink_mnsparameters
        # The parameters that are configured if you specify the event target as Message Queue for RabbitMQ.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        # The parameters that are configured if you specify the event target as Message Queue for Apache RocketMQ.
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        # The parameters that are configured if you specify the event target as Simple Log Service.
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_data_hub_parameters:
            self.sink_data_hub_parameters.validate()
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_fnf_parameters:
            self.sink_fnf_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_data_hub_parameters is not None:
            result['SinkDataHubParameters'] = self.sink_data_hub_parameters.to_map()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_fnf_parameters is not None:
            result['SinkFnfParameters'] = self.sink_fnf_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SinkDataHubParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParameters()
            self.sink_data_hub_parameters = temp_model.from_map(m['SinkDataHubParameters'])
        if m.get('SinkFcParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkFnfParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m['SinkFnfParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class CreateEventStreamingRequestSourceSourceDTSParameters(TeaModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: int = None,
        password: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        # The URL and port number of the data subscription channel.
        self.broker_url = broker_url
        # The consumer offset. It is the timestamp that indicates when the SDK client consumes the first data record.
        self.init_check_point = init_check_point
        # The consumer group password.
        self.password = password
        # The consumer group ID.
        self.sid = sid
        # The task ID.
        self.task_id = task_id
        # The topic to which you want to subscribe by using the data subscription channel.
        self.topic = topic
        # The consumer group username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateEventStreamingRequestSourceSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group
        # The instance ID.
        self.instance_id = instance_id
        # The network type. Default value: Default. The value PublicNetwork specifies virtual private clouds (VPCs).
        self.network = network
        # The offset.
        self.offset_reset = offset_reset
        # The region ID.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The topic name.
        self.topic = topic
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateEventStreamingRequestSourceSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable Base64 encoding. Default value: true.
        self.is_base_64decode = is_base_64decode
        # The queue name.
        self.queue_name = queue_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEventStreamingRequestSourceSourceMQTTParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The topic in which messages are stored.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class CreateEventStreamingRequestSourceSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # The ID of the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id
        # The name of the queue on the Message Queue for RabbitMQ instance.
        self.queue_name = queue_name
        # The region ID. You can call the [describeregions](~~62010~~) operation to query the most recent region list.
        self.region_id = region_id
        # The name of the vhost of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class CreateEventStreamingRequestSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        filter_sql: str = None,
        filter_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        network: str = None,
        offset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The authentication method.
        self.auth_type = auth_type
        # The SQL statement that is used to filter messages.
        self.filter_sql = filter_sql
        # The message filter type.
        self.filter_type = filter_type
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id
        # The instance endpoint.
        self.instance_endpoint = instance_endpoint
        # The region where the Message Queue for Apache RocketMQ instance resides.
        self.instance_id = instance_id
        # The network type of the instance. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
        self.instance_network = instance_network
        # The instance password.
        self.instance_password = instance_password
        # The security group ID of the instance.
        self.instance_security_group_id = instance_security_group_id
        # The instance type.
        self.instance_type = instance_type
        # The instance username.
        self.instance_username = instance_username
        # The vSwitch ID of the instance.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The VPC ID of the instance.
        self.instance_vpc_id = instance_vpc_id
        # The network type. Valid values: PublicNetwork and PrivateNetwork.
        self.network = network
        # The offset from which message consumption starts. Valid values:
        # 
        # *   CONSUME_FROM_LAST_OFFSET: Start message consumption from the latest offset.
        # *   CONSUME_FROM_FIRST_OFFSET: Start message consumption from the earliest offset.
        # *   CONSUME_FROM_TIMESTAMP: Start message consumption from the offset at the specified point in time.
        # 
        # Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset
        # The region ID.
        self.region_id = region_id
        # The security group of the cross-border task.
        self.security_group_id = security_group_id
        # The tag that is used to filter messages.
        self.tag = tag
        # The timestamp that specifies the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The name of the topic on the Message Queue for Apache RocketMQ instance.
        self.topic = topic
        # The vSwitch ID of the cross-border task.
        self.v_switch_ids = v_switch_ids
        # The VPC ID of the cross-border task.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.filter_sql is not None:
            result['FilterSql'] = self.filter_sql
        if self.filter_type is not None:
            result['FilterType'] = self.filter_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('FilterSql') is not None:
            self.filter_sql = m.get('FilterSql')
        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateEventStreamingRequestSourceSourceSLSParameters(TeaModel):
    def __init__(
        self,
        consume_position: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start message consumption.
        self.consume_position = consume_position
        # The Simple Log Service Logstore.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateEventStreamingRequestSource(TeaModel):
    def __init__(
        self,
        source_dtsparameters: CreateEventStreamingRequestSourceSourceDTSParameters = None,
        source_kafka_parameters: CreateEventStreamingRequestSourceSourceKafkaParameters = None,
        source_mnsparameters: CreateEventStreamingRequestSourceSourceMNSParameters = None,
        source_mqttparameters: CreateEventStreamingRequestSourceSourceMQTTParameters = None,
        source_rabbit_mqparameters: CreateEventStreamingRequestSourceSourceRabbitMQParameters = None,
        source_rocket_mqparameters: CreateEventStreamingRequestSourceSourceRocketMQParameters = None,
        source_slsparameters: CreateEventStreamingRequestSourceSourceSLSParameters = None,
    ):
        # The parameters that are configured if you specify the event source as Data Transmission Service (DTS).
        self.source_dtsparameters = source_dtsparameters
        # The parameters that are configured if you specify the event source as Message Queue for Apache Kafka.
        self.source_kafka_parameters = source_kafka_parameters
        # The parameters that are configured if you specify the event source as Message Service (MNS).
        self.source_mnsparameters = source_mnsparameters
        # The parameters that are configured if you specify the event source as Message Queue for MQTT.
        self.source_mqttparameters = source_mqttparameters
        # The parameters that are configured if you specify the event source as Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # The parameters that are configured if you specify the event source as Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The parameters that are configured if you specify the event source as Simple Log Service.
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class CreateEventStreamingRequestTransforms(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateEventStreamingRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: CreateEventStreamingRequestRunOptions = None,
        sink: CreateEventStreamingRequestSink = None,
        source: CreateEventStreamingRequestSource = None,
        transforms: List[CreateEventStreamingRequestTransforms] = None,
    ):
        # The description of the event stream.
        self.description = description
        # The name of the event stream.
        self.event_streaming_name = event_streaming_name
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern
        # The parameters that are configured for the runtime environment.
        self.run_options = run_options
        # The event target. You must and can specify only one event target.
        self.sink = sink
        # The event provider, which is also known as the event source. You must and can specify only one event source.
        self.source = source
        self.transforms = transforms

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = CreateEventStreamingRequestRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = CreateEventStreamingRequestSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = CreateEventStreamingRequestSource()
            self.source = temp_model.from_map(m['Source'])
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = CreateEventStreamingRequestTransforms()
                self.transforms.append(temp_model.from_map(k))
        return self


class CreateEventStreamingShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options_shrink: str = None,
        sink_shrink: str = None,
        source_shrink: str = None,
        transforms_shrink: str = None,
    ):
        # The description of the event stream.
        self.description = description
        # The name of the event stream.
        self.event_streaming_name = event_streaming_name
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern
        # The parameters that are configured for the runtime environment.
        self.run_options_shrink = run_options_shrink
        # The event target. You must and can specify only one event target.
        self.sink_shrink = sink_shrink
        # The event provider, which is also known as the event source. You must and can specify only one event source.
        self.source_shrink = source_shrink
        self.transforms_shrink = transforms_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options_shrink is not None:
            result['RunOptions'] = self.run_options_shrink
        if self.sink_shrink is not None:
            result['Sink'] = self.sink_shrink
        if self.source_shrink is not None:
            result['Source'] = self.source_shrink
        if self.transforms_shrink is not None:
            result['Transforms'] = self.transforms_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            self.run_options_shrink = m.get('RunOptions')
        if m.get('Sink') is not None:
            self.sink_shrink = m.get('Sink')
        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')
        if m.get('Transforms') is not None:
            self.transforms_shrink = m.get('Transforms')
        return self


class CreateEventStreamingResponseBodyData(TeaModel):
    def __init__(
        self,
        event_streaming_arn: str = None,
    ):
        # The ARN of the event stream.
        self.event_streaming_arn = event_streaming_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_arn is not None:
            result['EventStreamingARN'] = self.event_streaming_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingARN') is not None:
            self.event_streaming_arn = m.get('EventStreamingARN')
        return self


class CreateEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEventStreamingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateEventStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequestEventTargetsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue. Events that are not processed or whose maximum retries are exceeded are written to the dead-letter queue. The ARN feature is supported by the following queue types: MNS and Message Queue for Apache RocketMQ.
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateRuleRequestEventTargetsParamList(TeaModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format that is used by the event target parameter. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.form = form
        # The resource parameter of the event target. For more information, see [Limits](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.resource_key = resource_key
        # The template that is used by the event target parameter.
        self.template = template
        # The value of the event target parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateRuleRequestEventTargets(TeaModel):
    def __init__(
        self,
        dead_letter_queue: CreateRuleRequestEventTargetsDeadLetterQueue = None,
        endpoint: str = None,
        errors_tolerance: str = None,
        id: str = None,
        param_list: List[CreateRuleRequestEventTargetsParamList] = None,
        push_retry_strategy: str = None,
        type: str = None,
    ):
        # The dead-letter queue. Events that are not processed or whose maximum retries are exceeded are written to the dead-letter queue. The dead-letter queue feature is supported by the following queue types: Message Queue for Apache RocketMQ, Message Service (MNS), Message Queue for Apache Kafka, and EventBridge.
        self.dead_letter_queue = dead_letter_queue
        # The endpoint of the event target.
        self.endpoint = endpoint
        # The fault tolerance policy. Valid values: ALL: allows fault tolerance. If an error occurs, the event processing is not blocked. If the message fails to be sent after the maximum number of retries specified by the retry policy is reached, the message is delivered to the dead-letter queue or discarded based on your configurations. NONE: does not allow fault tolerance. If an error occurs and the message fails to be sent after the maximum number of retries specified by the retry policy is reached, the event processing is blocked.
        self.errors_tolerance = errors_tolerance
        # The ID of the custom event target.
        self.id = id
        # The parameters that are configured for the event target.
        self.param_list = param_list
        # The retry policy that is used to push events. Valid values: BACKOFF_RETRY: backoff retry. If an event failed to be pushed, it can be retried up to three times. The interval between two consecutive retries is a random value between 10 and 20 seconds. EXPONENTIAL_DECAY_RETRY: exponential decay retry. If an event failed to be pushed, it can be retried up to 176 times. The interval between two consecutive retries exponentially increases to 512 seconds, and the total retry time is one day. The specific retry intervals are 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 512, ..., and 512 seconds. The interval of 512 seconds is used for 167 retries.
        self.push_retry_strategy = push_retry_strategy
        # The type of the event target. For more information, see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.type = type

    def validate(self):
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterQueue') is not None:
            temp_model = CreateRuleRequestEventTargetsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = CreateRuleRequestEventTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateRuleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_targets: List[CreateRuleRequestEventTargets] = None,
        filter_pattern: str = None,
        rule_name: str = None,
        status: str = None,
    ):
        # The description of the event bus.
        self.description = description
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event targets.
        self.event_targets = event_targets
        # The event pattern, in JSON format. Valid values: stringEqual and stringExpression. You can specify up to five expressions in the map data structure in each field.
        # 
        # You can specify up to five expressions in the map data structure in each field.
        self.filter_pattern = filter_pattern
        # The name of the event rule.
        self.rule_name = rule_name
        # The status of the event rule. Valid values: ENABLE: enables the event rule. It is the default status of the event rule. DISABLE: disables the event rule.
        self.status = status

    def validate(self):
        if self.event_targets:
            for k in self.event_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        result['EventTargets'] = []
        if self.event_targets is not None:
            for k in self.event_targets:
                result['EventTargets'].append(k.to_map() if k else None)
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        self.event_targets = []
        if m.get('EventTargets') is not None:
            for k in m.get('EventTargets'):
                temp_model = CreateRuleRequestEventTargets()
                self.event_targets.append(temp_model.from_map(k))
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_targets_shrink: str = None,
        filter_pattern: str = None,
        rule_name: str = None,
        status: str = None,
    ):
        # The description of the event bus.
        self.description = description
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event targets.
        self.event_targets_shrink = event_targets_shrink
        # The event pattern, in JSON format. Valid values: stringEqual and stringExpression. You can specify up to five expressions in the map data structure in each field.
        # 
        # You can specify up to five expressions in the map data structure in each field.
        self.filter_pattern = filter_pattern
        # The name of the event rule.
        self.rule_name = rule_name
        # The status of the event rule. Valid values: ENABLE: enables the event rule. It is the default status of the event rule. DISABLE: disables the event rule.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_targets_shrink is not None:
            result['EventTargets'] = self.event_targets_shrink
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventTargets') is not None:
            self.event_targets_shrink = m.get('EventTargets')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_arn: str = None,
    ):
        # The ARN of the event rule. The ARN is used for authorization.
        self.rule_arn = rule_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleForProductRequest(TeaModel):
    def __init__(
        self,
        product_name: str = None,
    ):
        # The name of the cloud service or the name of the service-linked role with which the cloud service is associated.
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class CreateServiceLinkedRoleForProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned message. If the request is successful, success is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateServiceLinkedRoleForProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceLinkedRoleForProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceLinkedRoleForProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiDestinationRequest(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
    ):
        # The name of the API destination.
        self.api_destination_name = api_destination_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        return self


class DeleteApiDestinationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApiDestinationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApiDestinationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteApiDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectionRequest(TeaModel):
    def __init__(
        self,
        connection_name: str = None,
    ):
        # The name of the connection that you want to delete.
        self.connection_name = connection_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        return self


class DeleteConnectionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventBusRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class DeleteEventBusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventBusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventBusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventSourceRequest(TeaModel):
    def __init__(
        self,
        event_source_name: str = None,
    ):
        # The name of the event source.
        self.event_source_name = event_source_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        return self


class DeleteEventSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventStreamingRequest(TeaModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
        # The name of the event stream that you want to delete.
        self.event_streaming_name = event_streaming_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class DeleteEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The name of the event rule that you want to delete.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTargetsRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        target_ids: List[str] = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The name of the event rule.
        self.rule_name = rule_name
        # The IDs of the event targets that you want to delete.
        self.target_ids = target_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')
        return self


class DeleteTargetsShrinkRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        target_ids_shrink: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The name of the event rule.
        self.rule_name = rule_name
        # The IDs of the event targets that you want to delete.
        self.target_ids_shrink = target_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.target_ids_shrink is not None:
            result['TargetIds'] = self.target_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('TargetIds') is not None:
            self.target_ids_shrink = m.get('TargetIds')
        return self


class DeleteTargetsResponseBodyDataErrorEntries(TeaModel):
    def __init__(
        self,
        entry_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The ID of the event body that failed to be processed.
        self.entry_id = entry_id
        # The returned error code.
        self.error_code = error_code
        # The returned error message.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DeleteTargetsResponseBodyData(TeaModel):
    def __init__(
        self,
        error_entries: List[DeleteTargetsResponseBodyDataErrorEntries] = None,
        error_entries_count: int = None,
    ):
        # The information about the event body that failed to be processed.
        self.error_entries = error_entries
        # The number of event bodies that failed to be processed. Valid values: 0: No event bodies failed to be processed. An integer other than 0: the number of event bodies that failed to be processed.
        self.error_entries_count = error_entries_count

    def validate(self):
        if self.error_entries:
            for k in self.error_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorEntries'] = []
        if self.error_entries is not None:
            for k in self.error_entries:
                result['ErrorEntries'].append(k.to_map() if k else None)
        if self.error_entries_count is not None:
            result['ErrorEntriesCount'] = self.error_entries_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_entries = []
        if m.get('ErrorEntries') is not None:
            for k in m.get('ErrorEntries'):
                temp_model = DeleteTargetsResponseBodyDataErrorEntries()
                self.error_entries.append(temp_model.from_map(k))
        if m.get('ErrorEntriesCount') is not None:
            self.error_entries_count = m.get('ErrorEntriesCount')
        return self


class DeleteTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTargetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableRuleRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The name of the event rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DisableRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. The value Success indicates that the request is successful.
        self.code = code
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRuleRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The name of the event rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class EnableRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. The value Success indicates that the request is successful.
        self.code = code
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApiDestinationRequest(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
    ):
        # The name of the API destination.
        self.api_destination_name = api_destination_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        return self


class GetApiDestinationResponseBodyDataHttpApiParameters(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        method: str = None,
    ):
        # The endpoint of the API destination.
        self.endpoint = endpoint
        # The HTTP request method. Valid values:
        # 
        # *   POST
        # *   GET
        # *   DELETE
        # *   PUT
        # *   HEAD
        # *   TRACE
        # *   PATCH
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class GetApiDestinationResponseBodyData(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        gmt_create: int = None,
        http_api_parameters: GetApiDestinationResponseBodyDataHttpApiParameters = None,
    ):
        # The name of the API destination.
        self.api_destination_name = api_destination_name
        # The connection name.
        self.connection_name = connection_name
        # The description of the API destination.
        self.description = description
        # The time when the API destination was created.
        self.gmt_create = gmt_create
        # The request parameters that are configured for the API destination.
        self.http_api_parameters = http_api_parameters

    def validate(self):
        if self.http_api_parameters:
            self.http_api_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.http_api_parameters is not None:
            result['HttpApiParameters'] = self.http_api_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('HttpApiParameters') is not None:
            temp_model = GetApiDestinationResponseBodyDataHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
        return self


class GetApiDestinationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetApiDestinationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetApiDestinationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApiDestinationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApiDestinationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetApiDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionRequest(TeaModel):
    def __init__(
        self,
        connection_name: str = None,
    ):
        # The connection name.
        self.connection_name = connection_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters(TeaModel):
    def __init__(
        self,
        api_key_name: str = None,
        api_key_value: str = None,
    ):
        # The key of the API key.
        self.api_key_name = api_key_name
        # The value of the API key.
        self.api_key_value = api_key_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters(TeaModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        # The password of basic authentication.
        self.password = password
        # The username of basic authentication.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The AccessKey secret of the client.
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret
        # The key of the request body.
        self.key = key
        # The value of the request body.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret
        # The key of the request header.
        self.key = key
        # The value of the request header.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret
        # The key of the request path.
        self.key = key
        # The value of the request path.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters(TeaModel):
    def __init__(
        self,
        body_parameters: List[GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters] = None,
        header_parameters: List[GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters] = None,
        query_string_parameters: List[GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters] = None,
    ):
        # The information about the request body.
        self.body_parameters = body_parameters
        # The information about the request header.
        self.header_parameters = header_parameters
        # The information about the request path.
        self.query_string_parameters = query_string_parameters

    def validate(self):
        if self.body_parameters:
            for k in self.body_parameters:
                if k:
                    k.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.query_string_parameters:
            for k in self.query_string_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyParameters'] = []
        if self.body_parameters is not None:
            for k in self.body_parameters:
                result['BodyParameters'].append(k.to_map() if k else None)
        result['HeaderParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['HeaderParameters'].append(k.to_map() if k else None)
        result['QueryStringParameters'] = []
        if self.query_string_parameters is not None:
            for k in self.query_string_parameters:
                result['QueryStringParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body_parameters = []
        if m.get('BodyParameters') is not None:
            for k in m.get('BodyParameters'):
                temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters(TeaModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_parameters: GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters = None,
        http_method: str = None,
        oauth_http_parameters: GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters = None,
    ):
        # The endpoint that is used to obtain the OAuth token.
        self.authorization_endpoint = authorization_endpoint
        # The information about the client.
        self.client_parameters = client_parameters
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        self.http_method = http_method
        # The request parameters of OAuth authentication.
        self.oauth_http_parameters = oauth_http_parameters

    def validate(self):
        if self.client_parameters:
            self.client_parameters.validate()
        if self.oauth_http_parameters:
            self.oauth_http_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m['ClientParameters'])
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('OAuthHttpParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m['OAuthHttpParameters'])
        return self


class GetConnectionResponseBodyDataConnectionsAuthParameters(TeaModel):
    def __init__(
        self,
        api_key_auth_parameters: GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters = None,
        authorization_type: str = None,
        basic_auth_parameters: GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters = None,
        oauth_parameters: GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters = None,
    ):
        # The information about API key authentication.
        self.api_key_auth_parameters = api_key_auth_parameters
        # The authentication method. Valid values:
        # 
        # *   BASIC_AUTH: basic authentication.
        # *   API_KEY_AUTH: API key authentication.
        # *   OAUTH_AUTH: OAuth authentication.
        self.authorization_type = authorization_type
        # The information about basic authentication.
        self.basic_auth_parameters = basic_auth_parameters
        # The information about OAuth authentication.
        self.oauth_parameters = oauth_parameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.oauth_parameters:
            self.oauth_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('BasicAuthParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
        if m.get('OAuthParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
        return self


class GetConnectionResponseBodyDataConnectionsNetworkParameters(TeaModel):
    def __init__(
        self,
        network_type: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitche_id: str = None,
    ):
        # *   PublicNetwork: the Internet.
        # *   PrivateNetwork: virtual private cloud (VPC).
        self.network_type = network_type
        # The security group ID.
        self.security_group_id = security_group_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitche_id = vswitche_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetConnectionResponseBodyDataConnections(TeaModel):
    def __init__(
        self,
        auth_parameters: GetConnectionResponseBodyDataConnectionsAuthParameters = None,
        connection_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        network_parameters: GetConnectionResponseBodyDataConnectionsNetworkParameters = None,
    ):
        # The authentication methods.
        self.auth_parameters = auth_parameters
        # The connection name.
        self.connection_name = connection_name
        # The connection description.
        self.description = description
        # The time when the connection was created.
        self.gmt_create = gmt_create
        # The data source ID.
        self.id = id
        # The information about the network.
        self.network_parameters = network_parameters

    def validate(self):
        if self.auth_parameters:
            self.auth_parameters.validate()
        if self.network_parameters:
            self.network_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters is not None:
            result['AuthParameters'] = self.auth_parameters.to_map()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.network_parameters is not None:
            result['NetworkParameters'] = self.network_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParameters()
            self.auth_parameters = temp_model.from_map(m['AuthParameters'])
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NetworkParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsNetworkParameters()
            self.network_parameters = temp_model.from_map(m['NetworkParameters'])
        return self


class GetConnectionResponseBodyData(TeaModel):
    def __init__(
        self,
        connections: List[GetConnectionResponseBodyDataConnections] = None,
    ):
        # The queried connections.
        self.connections = connections

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = GetConnectionResponseBodyDataConnections()
                self.connections.append(temp_model.from_map(k))
        return self


class GetConnectionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetConnectionResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_code = http_code
        # The returned message.
        self.message = message
        # The returned request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetConnectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventBusRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class GetEventBusResponseBodyData(TeaModel):
    def __init__(
        self,
        create_timestamp: int = None,
        description: str = None,
        event_bus_arn: str = None,
        event_bus_name: str = None,
    ):
        # The timestamp that indicates when the event bus was created.
        self.create_timestamp = create_timestamp
        # The description of the event bus.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.event_bus_arn = event_bus_arn
        # The name of the event bus.
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class GetEventBusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEventBusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value Success indicates that the request is successful.
        self.code = code
        # The data returned.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetEventBusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEventBusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEventBusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventStreamingRequest(TeaModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
        # The name of the event stream whose details you want to query.
        self.event_streaming_name = event_streaming_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class GetEventStreamingResponseBodyDataRunOptionsBatchWindow(TeaModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        # The maximum number of events that are allowed in the batch window. If this threshold is reached, data in the window is pushed downstream. When multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.count_based_window = count_based_window
        # The maximum period of time during which events are allowed in the batch window. Unit: seconds. If this threshold is reached, data in the window is pushed downstream. When multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue.
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetEventStreamingResponseBodyDataRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: float = None,
        maximum_retry_attempts: float = None,
        push_retry_strategy: str = None,
    ):
        # The maximum period of time during which retries are performed.
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        # The maximum number of retries.
        self.maximum_retry_attempts = maximum_retry_attempts
        # The retry policy. Valid values: BACKOFFRETRY and EXPONENTIALDECAY_RETRY.
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class GetEventStreamingResponseBodyDataRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: GetEventStreamingResponseBodyDataRunOptionsBatchWindow = None,
        dead_letter_queue: GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: GetEventStreamingResponseBodyDataRunOptionsRetryStrategy = None,
    ):
        # The batch window.
        self.batch_window = batch_window
        # Indicates whether dead-letter queues are enabled. By default, dead-letter queues are disabled. Messages that fail to be pushed after allowed retries as specified by the retry policy are discarded.
        self.dead_letter_queue = dead_letter_queue
        # The fault tolerance policy. The value NONE specifies that faults are not tolerated, and the value All specifies that all faults are tolerated.
        self.errors_tolerance = errors_tolerance
        # The concurrency level.
        self.maximum_tasks = maximum_tasks
        # The information about the retry policy that is used if the event fails to be pushed.
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The delivery concurrency. Minimum value: 1.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The function name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The invocation type.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The alias of the service to which the function belongs.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkFcParametersBody = None,
        concurrency: GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency = None,
        function_name: GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName = None,
        invocation_type: GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType = None,
        qualifier: GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier = None,
        service_name: GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName = None,
    ):
        # The message body that is sent to the function.
        self.body = body
        # The delivery concurrency. Minimum value: 1.
        self.concurrency = concurrency
        # The function name.
        self.function_name = function_name
        # The invocation type. Valid values: Sync: synchronous Async: asynchronous
        self.invocation_type = invocation_type
        # The alias of the service to which the function belongs.
        self.qualifier = qualifier
        # The service name.
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.concurrency:
            self.concurrency.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Concurrency') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m['Concurrency'])
        if m.get('FunctionName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The execution name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The flow name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The execution input information.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The role configuration.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParameters(TeaModel):
    def __init__(
        self,
        execution_name: GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName = None,
        flow_name: GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName = None,
        input: GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput = None,
        role_name: GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName = None,
    ):
        # The execution name.
        self.execution_name = execution_name
        # The flow name.
        self.flow_name = flow_name
        # The execution input information.
        self.input = input
        # The role name.
        self.role_name = role_name

    def validate(self):
        if self.execution_name:
            self.execution_name.validate()
        if self.flow_name:
            self.flow_name.validate()
        if self.input:
            self.input.validate()
        if self.role_name:
            self.role_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name.to_map()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name.to_map()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m['ExecutionName'])
        if m.get('FlowName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m['FlowName'])
        if m.get('Input') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('RoleName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The acknowledgment information.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The instance ID.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The message key.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The topic name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks = None,
        instance_id: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId = None,
        key: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey = None,
        topic: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic = None,
        value: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue = None,
    ):
        # The acknowledgment information.
        self.acks = acks
        # The target service type is Message Queue for Apache Kafka.
        self.instance_id = instance_id
        # The message key.
        self.key = key
        # The topic name.
        self.topic = topic
        # The message content.
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('Topic') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # Specifies that Base64 encoding is enabled.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the MNS queue.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody = None,
        is_base_64encode: GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName = None,
    ):
        # The message content.
        self.body = body
        # Indicates whether Base64 encoding is enabled.
        self.is_base_64encode = is_base_64encode
        # The target service type is MNS.
        self.queue_name = queue_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the exchange in the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The ID of the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The routing rule for the message.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The type of the resource to which the event is delivered. Valid values: Exchange: exchanges. Queue: queues.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The vhost name of the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody = None,
        exchange: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange = None,
        instance_id: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId = None,
        message_id: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId = None,
        properties: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties = None,
        queue_name: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName = None,
        routing_key: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        # The message content.
        self.body = body
        # The exchange mode. This parameter is available only if TargetType is set to Exchange.
        self.exchange = exchange
        # The target service type is Message Queue for RabbitMQ instance.
        self.instance_id = instance_id
        # The message ID.
        self.message_id = message_id
        # The tags that are used to filter messages.
        self.properties = properties
        # The queue mode. This parameter is available only if TargetType is set to Queue.
        self.queue_name = queue_name
        # The routing rule for the message. This parameter is available only if TargetType is set to Exchange.
        self.routing_key = routing_key
        # The target type.
        self.target_type = target_type
        # The name of the vhost of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody = None,
        instance_id: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId = None,
        keys: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys = None,
        properties: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties = None,
        tags: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags = None,
        topic: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic = None,
    ):
        # The message content.
        self.body = body
        # The target service type is Message Queue for Apache RocketMQ.
        self.instance_id = instance_id
        # The tags that are used to filter messages.
        self.keys = keys
        # The tags that are used to filter messages.
        self.properties = properties
        # The tags that are used to filter messages.
        self.tags = tags
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The Log Service Logstore.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The Log Service project.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the topic in which logs are stored. The topic corresponds to the topic reserved field in Log Service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody = None,
        log_store: GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore = None,
        project: GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject = None,
        role_name: GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName = None,
        topic: GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic = None,
    ):
        # The message content.
        self.body = body
        # The Simple Log Service Logstore.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name
        # The name of the topic in which logs are stored. The topic corresponds to the topic reserved field in Simple Log Service.
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class GetEventStreamingResponseBodyDataSink(TeaModel):
    def __init__(
        self,
        sink_fc_parameters: GetEventStreamingResponseBodyDataSinkSinkFcParameters = None,
        sink_fnf_parameters: GetEventStreamingResponseBodyDataSinkSinkFnfParameters = None,
        sink_kafka_parameters: GetEventStreamingResponseBodyDataSinkSinkKafkaParameters = None,
        sink_mnsparameters: GetEventStreamingResponseBodyDataSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters = None,
        sink_slsparameters: GetEventStreamingResponseBodyDataSinkSinkSLSParameters = None,
    ):
        # The parameters that are returned if the event target is Function Compute.
        self.sink_fc_parameters = sink_fc_parameters
        # The Sink Fnf parameters.
        self.sink_fnf_parameters = sink_fnf_parameters
        # The parameters that are returned if the event target is Message Queue for Apache Kafka.
        self.sink_kafka_parameters = sink_kafka_parameters
        # The parameters that are returned if the event target is Message Service (MNS).
        self.sink_mnsparameters = sink_mnsparameters
        # The parameters that are returned if the event target is Message Queue for RabbitMQ.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        # Sink RocketMQ Parameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        # Sink SLS Parameters
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_fnf_parameters:
            self.sink_fnf_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_fnf_parameters is not None:
            result['SinkFnfParameters'] = self.sink_fnf_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkFnfParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m['SinkFnfParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class GetEventStreamingResponseBodyDataSourceSourceDTSParameters(TeaModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: str = None,
        password: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        # The URL and port number of the data subscription channel.
        self.broker_url = broker_url
        # The consumer offset. A consumer offset is a timestamp that indicates when the SDK client consumes the first data record. The value is a UNIX timestamp.
        self.init_check_point = init_check_point
        # The password of the consumer group.
        self.password = password
        # The ID of the consumer group.
        self.sid = sid
        # The task ID.
        self.task_id = task_id
        # The topic to which you want to subscribe by using the data subscription channel.
        self.topic = topic
        # The account of the consumer group.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetEventStreamingResponseBodyDataSourceSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group
        # The instance ID.
        self.instance_id = instance_id
        # The network. Default value: Default. The value PublicNetwork specifies a virtual private cloud (VPC).
        self.network = network
        # The offset.
        self.offset_reset = offset_reset
        # The region ID of the Message Queue for Apache Kafka instance.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The name of the topic.
        self.topic = topic
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetEventStreamingResponseBodyDataSourceSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Indicates whether Base64 encoding is enabled.
        self.is_base_64decode = is_base_64decode
        # The name of the MNS queue.
        self.queue_name = queue_name
        # The region ID of the MNS queue.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetEventStreamingResponseBodyDataSourceSourceMQTTParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The region ID of the Message Queue for MQTT instance.
        self.region_id = region_id
        # The name of the topic in the Message Queue for MQTT instance.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # The ID of the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.queue_name = queue_name
        # The region ID of the Message Queue for RabbitMQ instance.
        self.region_id = region_id
        # The vhost name of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.auth_type = auth_type
        # The ID of the consumer group in the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id
        self.instance_endpoint = instance_endpoint
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.instance_id = instance_id
        self.instance_network = instance_network
        self.instance_password = instance_password
        self.instance_security_group_id = instance_security_group_id
        self.instance_type = instance_type
        self.instance_username = instance_username
        self.instance_vswitch_ids = instance_vswitch_ids
        self.instance_vpc_id = instance_vpc_id
        # The consumer offset of messages. Valid values: CONSUME_FROM_LAST_OFFSET: Start consumption from the latest offset. CONSUME_FROM_FIRST_OFFSET: Start consumption from the earliest offset. CONSUME_FROM_TIMESTAMP: Start consumption from the offset at the specified point in time.
        self.offset = offset
        # The region ID of the Message Queue for Apache RocketMQ instance.
        self.region_id = region_id
        # The tags that are used to filter messages.
        self.tag = tag
        # The timestamp of the offset from which consumption starts. This parameter is valid only if you set the Offset parameter to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetEventStreamingResponseBodyDataSourceSourceSLSParameters(TeaModel):
    def __init__(
        self,
        consume_position: str = None,
        consumer_group: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The starting consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start consumption.
        self.consume_position = consume_position
        # The consumer group.
        self.consumer_group = consumer_group
        # The Log Service Logstore.
        self.log_store = log_store
        # The Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetEventStreamingResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        source_dtsparameters: GetEventStreamingResponseBodyDataSourceSourceDTSParameters = None,
        source_kafka_parameters: GetEventStreamingResponseBodyDataSourceSourceKafkaParameters = None,
        source_mnsparameters: GetEventStreamingResponseBodyDataSourceSourceMNSParameters = None,
        source_mqttparameters: GetEventStreamingResponseBodyDataSourceSourceMQTTParameters = None,
        source_rabbit_mqparameters: GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters = None,
        source_rocket_mqparameters: GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters = None,
        source_slsparameters: GetEventStreamingResponseBodyDataSourceSourceSLSParameters = None,
    ):
        # The parameters that are returned if the event source is Data Transmission Service (DTS).
        self.source_dtsparameters = source_dtsparameters
        # Source Kafka Parameters
        self.source_kafka_parameters = source_kafka_parameters
        # Source MNS Parameters
        self.source_mnsparameters = source_mnsparameters
        # The parameters that are returned if the event source is Message Queue for MQTT.
        self.source_mqttparameters = source_mqttparameters
        # Source RabbitMQ Parameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # Source RocketMQ Parameters
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The parameters that are returned if the event provider is Simple Log Service.
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class GetEventStreamingResponseBodyDataTransforms(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetEventStreamingResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: GetEventStreamingResponseBodyDataRunOptions = None,
        sink: GetEventStreamingResponseBodyDataSink = None,
        source: GetEventStreamingResponseBodyDataSource = None,
        status: str = None,
        transforms: List[GetEventStreamingResponseBodyDataTransforms] = None,
    ):
        # The description of the event stream that is returned.
        self.description = description
        # The name of the event stream that is returned.
        self.event_streaming_name = event_streaming_name
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern
        # The parameters that are configured for the runtime environment.
        self.run_options = run_options
        # The event target.
        self.sink = sink
        # The event provider.
        self.source = source
        # The status of the event stream that is returned.
        self.status = status
        self.transforms = transforms

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = GetEventStreamingResponseBodyDataSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = GetEventStreamingResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = GetEventStreamingResponseBodyDataTransforms()
                self.transforms.append(temp_model.from_map(k))
        return self


class GetEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEventStreamingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For a list of error codes, see Error codes.
        self.code = code
        # The response parameters.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetEventStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The name of the event rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetRuleResponseBodyDataTargetsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the event source.
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetRuleResponseBodyDataTargetsParamList(TeaModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format that is used by the event target parameter. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.form = form
        # The resource parameter of the event target. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.resource_key = resource_key
        # The template that is used by the event target parameter.
        self.template = template
        # The value of the event target parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetRuleResponseBodyDataTargets(TeaModel):
    def __init__(
        self,
        dead_letter_queue: GetRuleResponseBodyDataTargetsDeadLetterQueue = None,
        detail_map: Dict[str, Any] = None,
        endpoint: str = None,
        errors_tolerance: str = None,
        id: str = None,
        param_list: List[GetRuleResponseBodyDataTargetsParamList] = None,
        push_retry_strategy: str = None,
        push_selector: str = None,
        type: str = None,
    ):
        # The ID of the custom event target.
        self.dead_letter_queue = dead_letter_queue
        # The information about the event target.
        self.detail_map = detail_map
        # The endpoint of the event target.
        self.endpoint = endpoint
        self.errors_tolerance = errors_tolerance
        # The ID of the custom event target.
        self.id = id
        # The parameters that are configured for the event target.
        self.param_list = param_list
        # The retry policy that is used to push events. Valid values: BACKOFF_RETRY: backoff retry. If an event failed to be pushed, it can be retried up to three times. The interval between two consecutive retries is a random value from 10 to 20. Unit: seconds. EXPONENTIAL_DECAY_RETRY: exponential decay retry. If an event failed to be pushed, it can be retried up to 176 times. The interval between two consecutive retries exponentially increases to 512 seconds, and the total retry time is one day. The specific retry intervals are 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 512, ..., and 512 seconds. The interval of 512 seconds is used for 167 retries.
        self.push_retry_strategy = push_retry_strategy
        # The transformer that is used to push events.
        self.push_selector = push_selector
        # The type of the event target. For more information, see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.type = type

    def validate(self):
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.detail_map is not None:
            result['DetailMap'] = self.detail_map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        if self.push_selector is not None:
            result['PushSelector'] = self.push_selector
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterQueue') is not None:
            temp_model = GetRuleResponseBodyDataTargetsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('DetailMap') is not None:
            self.detail_map = m.get('DetailMap')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = GetRuleResponseBodyDataTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('PushSelector') is not None:
            self.push_selector = m.get('PushSelector')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        description: str = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_arn: str = None,
        rule_name: str = None,
        status: str = None,
        targets: List[GetRuleResponseBodyDataTargets] = None,
    ):
        # The timestamp that indicates when the event rule was created.
        self.created_timestamp = created_timestamp
        # The description of the event rule.
        self.description = description
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event pattern, in JSON format. Valid values: stringEqual and stringExpression. You can specify up to five expressions in the map data structure in each field.
        # 
        # You can specify up to five expressions in the map data structure in each field.
        self.filter_pattern = filter_pattern
        # The Alibaba Cloud Resource Name (ARN) of the event rule.
        self.rule_arn = rule_arn
        # The name of the event rule.
        self.rule_name = rule_name
        # The status of the event rule. Valid values: ENABLE (default): The event rule is enabled. DISABLE: The event rule is disabled.
        self.status = status
        # The event targets.
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = GetRuleResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class GetRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes(TeaModel):
    def __init__(
        self,
        event_source_name: str = None,
        group_name: str = None,
        name: str = None,
        short_name: str = None,
    ):
        # The name of the event source.
        self.event_source_name = event_source_name
        # The name of the group to which the queried event type belongs.
        self.group_name = group_name
        # The full name of the queried event type.
        self.name = name
        # The short name of the queried event type.
        self.short_name = short_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        return self


class ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList(TeaModel):
    def __init__(
        self,
        arn: str = None,
        ctime: float = None,
        description: str = None,
        event_bus_name: str = None,
        event_types: List[ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes] = None,
        full_name: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.arn = arn
        # The time when the event source was created. Unit: milliseconds.
        self.ctime = ctime
        # The description of the queried event source.
        self.description = description
        # The name of the event source to which the queried event type belongs.
        self.event_bus_name = event_bus_name
        # The queried event types.
        self.event_types = event_types
        self.full_name = full_name
        # The name of the queried event source.
        self.name = name
        # The status of the queried event source. Valid value: Activated.
        self.status = status
        # The type of the queried event source.
        self.type = type

    def validate(self):
        if self.event_types:
            for k in self.event_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        result['EventTypes'] = []
        if self.event_types is not None:
            for k in self.event_types:
                result['EventTypes'].append(k.to_map() if k else None)
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        self.event_types = []
        if m.get('EventTypes') is not None:
            for k in m.get('EventTypes'):
                temp_model = ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes()
                self.event_types.append(temp_model.from_map(k))
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAliyunOfficialEventSourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        event_source_list: List[ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList] = None,
    ):
        # The name of the event source to which the queried event type belongs.
        self.event_source_list = event_source_list

    def validate(self):
        if self.event_source_list:
            for k in self.event_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventSourceList'] = []
        if self.event_source_list is not None:
            for k in self.event_source_list:
                result['EventSourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_source_list = []
        if m.get('EventSourceList') is not None:
            for k in m.get('EventSourceList'):
                temp_model = ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList()
                self.event_source_list.append(temp_model.from_map(k))
        return self


class ListAliyunOfficialEventSourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAliyunOfficialEventSourcesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListAliyunOfficialEventSourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAliyunOfficialEventSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAliyunOfficialEventSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAliyunOfficialEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApiDestinationsRequest(TeaModel):
    def __init__(
        self,
        api_destination_name_prefix: str = None,
        connection_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The prefix of the API destination name.
        self.api_destination_name_prefix = api_destination_name_prefix
        # The connection name.
        self.connection_name = connection_name
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging.
        # 
        # *   Default value: 10.
        self.max_results = max_results
        # If you set Limit and excess return values exist, this parameter is returned.
        # 
        # *   Default value: 0.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name_prefix is not None:
            result['ApiDestinationNamePrefix'] = self.api_destination_name_prefix
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationNamePrefix') is not None:
            self.api_destination_name_prefix = m.get('ApiDestinationNamePrefix')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListApiDestinationsResponseBodyDataApiDestinationsHttpApiParameters(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        method: str = None,
    ):
        # The endpoint of the API destination.
        self.endpoint = endpoint
        # The HTTP request method. Valid values:
        # 
        # - POST
        # 
        # - GET
        # 
        # - DELETE
        # 
        # - PUT
        # 
        # - HEAD
        # 
        # - TRACE
        # 
        # - PATCH
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class ListApiDestinationsResponseBodyDataApiDestinations(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        gmt_create: int = None,
        http_api_parameters: ListApiDestinationsResponseBodyDataApiDestinationsHttpApiParameters = None,
    ):
        # The name of the API destination.
        self.api_destination_name = api_destination_name
        # The connection name.
        self.connection_name = connection_name
        # The description of the connection.
        self.description = description
        # The time when the API destination was created.
        self.gmt_create = gmt_create
        # The request parameters that are configured for the API destination.
        self.http_api_parameters = http_api_parameters

    def validate(self):
        if self.http_api_parameters:
            self.http_api_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.http_api_parameters is not None:
            result['HttpApiParameters'] = self.http_api_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('HttpApiParameters') is not None:
            temp_model = ListApiDestinationsResponseBodyDataApiDestinationsHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
        return self


class ListApiDestinationsResponseBodyData(TeaModel):
    def __init__(
        self,
        api_destinations: List[ListApiDestinationsResponseBodyDataApiDestinations] = None,
        max_results: float = None,
        next_token: str = None,
        total: float = None,
    ):
        # The API destinations.
        self.api_destinations = api_destinations
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.api_destinations:
            for k in self.api_destinations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiDestinations'] = []
        if self.api_destinations is not None:
            for k in self.api_destinations:
                result['ApiDestinations'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_destinations = []
        if m.get('ApiDestinations') is not None:
            for k in m.get('ApiDestinations'):
                temp_model = ListApiDestinationsResponseBodyDataApiDestinations()
                self.api_destinations.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListApiDestinationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListApiDestinationsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListApiDestinationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApiDestinationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApiDestinationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApiDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionsRequest(TeaModel):
    def __init__(
        self,
        connection_name_prefix: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The key word that you specify to query connections. Connections can be queried by prefixes.
        self.connection_name_prefix = connection_name_prefix
        # The maximum number of entries to be returned in a single call. You can use this parameter and the NextToken parameter to implement paging.
        # 
        # *   Default value: 10.
        self.max_results = max_results
        # If you set the Limit parameter and excess return values exist, this parameter is returned.
        # 
        # *   Default value: 0.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_name_prefix is not None:
            result['ConnectionNamePrefix'] = self.connection_name_prefix
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionNamePrefix') is not None:
            self.connection_name_prefix = m.get('ConnectionNamePrefix')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters(TeaModel):
    def __init__(
        self,
        api_key_name: str = None,
        api_key_value: str = None,
    ):
        # The API key.
        self.api_key_name = api_key_name
        # The value of the API key.
        self.api_key_value = api_key_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListConnectionsResponseBodyDataConnectionsAuthParametersBasicAuthParameters(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The client key secret of the application.
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret
        # The key in the request body.
        self.key = key
        # The value of the key in the request body.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret
        # The key in the request header.
        self.key = key
        # The value of the key in the request header.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret
        # The key in the request path.
        self.key = key
        # The value of the key in the request path.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters(TeaModel):
    def __init__(
        self,
        body_parameters: List[ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters] = None,
        header_parameters: List[ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters] = None,
        query_string_parameters: List[ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters] = None,
    ):
        # The parameters that are configured for the request.
        self.body_parameters = body_parameters
        # The parameters that are configured for the request header.
        self.header_parameters = header_parameters
        # The parameters that are configured for the request path.
        self.query_string_parameters = query_string_parameters

    def validate(self):
        if self.body_parameters:
            for k in self.body_parameters:
                if k:
                    k.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.query_string_parameters:
            for k in self.query_string_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyParameters'] = []
        if self.body_parameters is not None:
            for k in self.body_parameters:
                result['BodyParameters'].append(k.to_map() if k else None)
        result['HeaderParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['HeaderParameters'].append(k.to_map() if k else None)
        result['QueryStringParameters'] = []
        if self.query_string_parameters is not None:
            for k in self.query_string_parameters:
                result['QueryStringParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body_parameters = []
        if m.get('BodyParameters') is not None:
            for k in m.get('BodyParameters'):
                temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParameters(TeaModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_parameters: ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters = None,
        http_method: str = None,
        oauth_http_parameters: ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters = None,
    ):
        # The endpoint that is used to obtain the OAuth token.
        self.authorization_endpoint = authorization_endpoint
        # The parameters that are configured for the client.
        self.client_parameters = client_parameters
        # The HTTP request method. Valid values:
        # 
        # - GET
        # 
        # - POST
        # 
        # - HEAD
        self.http_method = http_method
        # The request parameters for OAuth authentication.
        self.oauth_http_parameters = oauth_http_parameters

    def validate(self):
        if self.client_parameters:
            self.client_parameters.validate()
        if self.oauth_http_parameters:
            self.oauth_http_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m['ClientParameters'])
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('OAuthHttpParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m['OAuthHttpParameters'])
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParameters(TeaModel):
    def __init__(
        self,
        api_key_auth_parameters: ListConnectionsResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters = None,
        authorization_type: str = None,
        basic_auth_parameters: ListConnectionsResponseBodyDataConnectionsAuthParametersBasicAuthParameters = None,
        oauth_parameters: ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParameters = None,
    ):
        # The parameters that are configured for API key authentication.
        self.api_key_auth_parameters = api_key_auth_parameters
        # The authentication type. Valid values:
        # 
        # - BASIC_AUTH: basic authentication.
        # 
        # - API_KEY_AUTH: API key authentication.
        # 
        # - OAUTH_AUTH: OAuth authentication.
        self.authorization_type = authorization_type
        # The parameters that are configured for basic authentication.
        self.basic_auth_parameters = basic_auth_parameters
        # The parameters that are configured for OAuth authentication.
        self.oauth_parameters = oauth_parameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.oauth_parameters:
            self.oauth_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('BasicAuthParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
        if m.get('OAuthParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
        return self


class ListConnectionsResponseBodyDataConnectionsNetworkParameters(TeaModel):
    def __init__(
        self,
        network_type: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitche_id: str = None,
    ):
        # The network type. Valid values:PublicNetwork and PrivateNetwork.
        self.network_type = network_type
        # The security group ID.
        self.security_group_id = security_group_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitche_id = vswitche_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListConnectionsResponseBodyDataConnections(TeaModel):
    def __init__(
        self,
        auth_parameters: ListConnectionsResponseBodyDataConnectionsAuthParameters = None,
        connection_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        network_parameters: ListConnectionsResponseBodyDataConnectionsNetworkParameters = None,
    ):
        # The parameters that are configured for authentication.
        self.auth_parameters = auth_parameters
        # The connection name.
        self.connection_name = connection_name
        # The connection description.
        self.description = description
        # The time when the connection was created.
        self.gmt_create = gmt_create
        # The connection ID.
        self.id = id
        self.network_parameters = network_parameters

    def validate(self):
        if self.auth_parameters:
            self.auth_parameters.validate()
        if self.network_parameters:
            self.network_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters is not None:
            result['AuthParameters'] = self.auth_parameters.to_map()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.network_parameters is not None:
            result['NetworkParameters'] = self.network_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParameters()
            self.auth_parameters = temp_model.from_map(m['AuthParameters'])
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NetworkParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsNetworkParameters()
            self.network_parameters = temp_model.from_map(m['NetworkParameters'])
        return self


class ListConnectionsResponseBodyData(TeaModel):
    def __init__(
        self,
        connections: List[ListConnectionsResponseBodyDataConnections] = None,
        max_results: float = None,
        next_token: str = None,
        total: float = None,
    ):
        # The value of the key in the request path.
        self.connections = connections
        # The number of entries returned per page.
        self.max_results = max_results
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = ListConnectionsResponseBodyDataConnections()
                self.connections.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListConnectionsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. The value Success indicates that the request is successful.
        self.code = code
        # The information about the connections returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListConnectionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConnectionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventBusesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
    ):
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging. Note: Up to 100 entries can be returned in a call.
        self.limit = limit
        # The prefix of the names of the event buses that you want to query.
        self.name_prefix = name_prefix
        # If you set Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListEventBusesResponseBodyDataEventBuses(TeaModel):
    def __init__(
        self,
        create_timestamp: int = None,
        description: str = None,
        event_bus_arn: str = None,
        event_bus_name: str = None,
    ):
        # The timestamp that indicates when the event bus was created.
        self.create_timestamp = create_timestamp
        # The description of the queried event bus.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the queried event bus.
        self.event_bus_arn = event_bus_arn
        # The name of the queried event bus.
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class ListEventBusesResponseBodyData(TeaModel):
    def __init__(
        self,
        event_buses: List[ListEventBusesResponseBodyDataEventBuses] = None,
        next_token: str = None,
        total: int = None,
    ):
        # The timestamp that indicates when the event bus was created.
        self.event_buses = event_buses
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.event_buses:
            for k in self.event_buses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventBuses'] = []
        if self.event_buses is not None:
            for k in self.event_buses:
                result['EventBuses'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_buses = []
        if m.get('EventBuses') is not None:
            for k in m.get('EventBuses'):
                temp_model = ListEventBusesResponseBodyDataEventBuses()
                self.event_buses.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEventBusesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEventBusesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the event buses are successfully queried. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListEventBusesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEventBusesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventBusesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEventBusesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventStreamingsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
        sink_arn: str = None,
        source_arn: str = None,
    ):
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging. A maximum of 100 entries can be returned in a call.
        self.limit = limit
        # The name of the event stream that you want to query.
        self.name_prefix = name_prefix
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The ARN of the event target.
        self.sink_arn = sink_arn
        # The Alibaba Cloud Resource Name (ARN) of the event source.
        self.source_arn = source_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sink_arn is not None:
            result['SinkArn'] = self.sink_arn
        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SinkArn') is not None:
            self.sink_arn = m.get('SinkArn')
        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow(TeaModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        self.count_based_window = count_based_window
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: float = None,
        maximum_retry_attempts: float = None,
        push_retry_strategy: str = None,
    ):
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        self.maximum_retry_attempts = maximum_retry_attempts
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow = None,
        dead_letter_queue: ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy = None,
    ):
        self.batch_window = batch_window
        self.dead_letter_queue = dead_letter_queue
        self.errors_tolerance = errors_tolerance
        self.maximum_tasks = maximum_tasks
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody = None,
        concurrency: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency = None,
        function_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName = None,
        invocation_type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType = None,
        qualifier: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier = None,
        service_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName = None,
    ):
        self.body = body
        self.concurrency = concurrency
        self.function_name = function_name
        self.invocation_type = invocation_type
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.concurrency:
            self.concurrency.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Concurrency') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m['Concurrency'])
        if m.get('FunctionName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters(TeaModel):
    def __init__(
        self,
        execution_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName = None,
        flow_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName = None,
        input: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput = None,
        role_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName = None,
    ):
        self.execution_name = execution_name
        self.flow_name = flow_name
        self.input = input
        self.role_name = role_name

    def validate(self):
        if self.execution_name:
            self.execution_name.validate()
        if self.flow_name:
            self.flow_name.validate()
        if self.input:
            self.input.validate()
        if self.role_name:
            self.role_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name.to_map()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name.to_map()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m['ExecutionName'])
        if m.get('FlowName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m['FlowName'])
        if m.get('Input') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('RoleName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks = None,
        instance_id: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId = None,
        key: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey = None,
        topic: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic = None,
        value: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue = None,
    ):
        self.acks = acks
        self.instance_id = instance_id
        self.key = key
        self.topic = topic
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('Topic') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody = None,
        is_base_64encode: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName = None,
    ):
        self.body = body
        self.is_base_64encode = is_base_64encode
        self.queue_name = queue_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody = None,
        exchange: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange = None,
        instance_id: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId = None,
        message_id: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId = None,
        properties: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties = None,
        queue_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName = None,
        routing_key: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        self.body = body
        self.exchange = exchange
        self.instance_id = instance_id
        self.message_id = message_id
        self.properties = properties
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.target_type = target_type
        self.virtual_host_name = virtual_host_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody = None,
        instance_id: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId = None,
        keys: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys = None,
        properties: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties = None,
        tags: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags = None,
        topic: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic = None,
    ):
        self.body = body
        self.instance_id = instance_id
        self.keys = keys
        self.properties = properties
        self.tags = tags
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody = None,
        log_store: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore = None,
        project: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject = None,
        role_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName = None,
        topic: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic = None,
    ):
        self.body = body
        self.log_store = log_store
        self.project = project
        self.role_name = role_name
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSink(TeaModel):
    def __init__(
        self,
        sink_fc_parameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters = None,
        sink_fnf_parameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters = None,
        sink_kafka_parameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters = None,
        sink_mnsparameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters = None,
        sink_slsparameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters = None,
    ):
        self.sink_fc_parameters = sink_fc_parameters
        self.sink_fnf_parameters = sink_fnf_parameters
        self.sink_kafka_parameters = sink_kafka_parameters
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        # Sink RocketMQ Parameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        # Sink SLS Parameters
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_fnf_parameters:
            self.sink_fnf_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_fnf_parameters is not None:
            result['SinkFnfParameters'] = self.sink_fnf_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkFnfParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m['SinkFnfParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters(TeaModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: str = None,
        password: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        self.broker_url = broker_url
        self.init_check_point = init_check_point
        self.password = password
        self.sid = sid
        self.task_id = task_id
        self.topic = topic
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.consumer_group = consumer_group
        self.instance_id = instance_id
        self.network = network
        self.offset_reset = offset_reset
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        self.is_base_64decode = is_base_64decode
        self.queue_name = queue_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.region_id = region_id
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.auth_type = auth_type
        self.group_id = group_id
        self.instance_endpoint = instance_endpoint
        self.instance_id = instance_id
        self.instance_network = instance_network
        self.instance_password = instance_password
        self.instance_security_group_id = instance_security_group_id
        self.instance_type = instance_type
        self.instance_username = instance_username
        self.instance_vswitch_ids = instance_vswitch_ids
        self.instance_vpc_id = instance_vpc_id
        self.offset = offset
        self.region_id = region_id
        self.tag = tag
        self.timestamp = timestamp
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters(TeaModel):
    def __init__(
        self,
        consume_position: str = None,
        consumer_group: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        self.consume_position = consume_position
        self.consumer_group = consumer_group
        self.log_store = log_store
        self.project = project
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSource(TeaModel):
    def __init__(
        self,
        source_dtsparameters: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters = None,
        source_kafka_parameters: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters = None,
        source_mnsparameters: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters = None,
        source_mqttparameters: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters = None,
        source_rabbit_mqparameters: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters = None,
        source_rocket_mqparameters: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters = None,
        source_slsparameters: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters = None,
    ):
        self.source_dtsparameters = source_dtsparameters
        # Source Kafka Parameters
        self.source_kafka_parameters = source_kafka_parameters
        # Source MNS Parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_mqttparameters = source_mqttparameters
        # Source RabbitMQ Parameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # Source RocketMQ Parameters
        self.source_rocket_mqparameters = source_rocket_mqparameters
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsTransforms(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ListEventStreamingsResponseBodyDataEventStreamings(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: ListEventStreamingsResponseBodyDataEventStreamingsRunOptions = None,
        sink: ListEventStreamingsResponseBodyDataEventStreamingsSink = None,
        source: ListEventStreamingsResponseBodyDataEventStreamingsSource = None,
        status: str = None,
        transforms: List[ListEventStreamingsResponseBodyDataEventStreamingsTransforms] = None,
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options = run_options
        self.sink = sink
        self.source = source
        self.status = status
        self.transforms = transforms

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = ListEventStreamingsResponseBodyDataEventStreamingsTransforms()
                self.transforms.append(temp_model.from_map(k))
        return self


class ListEventStreamingsResponseBodyData(TeaModel):
    def __init__(
        self,
        event_streamings: List[ListEventStreamingsResponseBodyDataEventStreamings] = None,
        next_token: str = None,
        total: int = None,
    ):
        # The status of the event stream that is returned.
        self.event_streamings = event_streamings
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists. You must specify the pagination token in the next request.
        self.next_token = next_token
        # The total number of records.
        self.total = total

    def validate(self):
        if self.event_streamings:
            for k in self.event_streamings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventStreamings'] = []
        if self.event_streamings is not None:
            for k in self.event_streamings:
                result['EventStreamings'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_streamings = []
        if m.get('EventStreamings') is not None:
            for k in m.get('EventStreamings'):
                temp_model = ListEventStreamingsResponseBodyDataEventStreamings()
                self.event_streamings.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEventStreamingsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEventStreamingsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # Success: The request is successful.
        # 
        # Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code
        # The information about the event streams.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. The value true indicates that the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListEventStreamingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEventStreamingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventStreamingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEventStreamingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        limit: int = None,
        next_token: str = None,
        rule_name_prefix: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The maximum number of entries to be returned in a single call. You can use this parameter and the NextToken parameter to implement paging. A maximum of 100 entries can be returned in a single call.
        self.limit = limit
        # If you set the Limit parameter and excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The prefix of the rule name.
        self.rule_name_prefix = rule_name_prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.rule_name_prefix is not None:
            result['RuleNamePrefix'] = self.rule_name_prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RuleNamePrefix') is not None:
            self.rule_name_prefix = m.get('RuleNamePrefix')
        return self


class ListRulesResponseBodyDataRulesTargets(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        errors_tolerance: str = None,
        id: str = None,
        push_selector: str = None,
        type: str = None,
    ):
        # The endpoint of the event target.
        self.endpoint = endpoint
        self.errors_tolerance = errors_tolerance
        # The ID of the custom event target.
        self.id = id
        # The transformer that is used to push events.
        self.push_selector = push_selector
        # The type of the event target. For more information, see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.id is not None:
            result['Id'] = self.id
        if self.push_selector is not None:
            result['PushSelector'] = self.push_selector
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PushSelector') is not None:
            self.push_selector = m.get('PushSelector')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRulesResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        description: str = None,
        detail_map: Dict[str, Any] = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_arn: str = None,
        rule_name: str = None,
        status: str = None,
        targets: List[ListRulesResponseBodyDataRulesTargets] = None,
    ):
        # The creation timestamp.
        self.created_timestamp = created_timestamp
        # The rule description.
        self.description = description
        # The details of the event rule.
        self.detail_map = detail_map
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event pattern, in JSON format. Valid values: stringEqual pattern stringExpression pattern Each field can have a maximum of five expressions in the map data structure.
        # 
        # Each field can have a maximum of five expressions in the map data structure.
        self.filter_pattern = filter_pattern
        # The Alibaba Cloud Resource Name (ARN) of the rule.
        self.rule_arn = rule_arn
        # The name of the event rule.
        self.rule_name = rule_name
        # The status of the event rule. Valid values: ENABLE: The event rule is enabled. It is the default state of the event rule. DISABLE: The event rule is disabled.
        self.status = status
        # The event targets.
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.detail_map is not None:
            result['DetailMap'] = self.detail_map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DetailMap') is not None:
            self.detail_map = m.get('DetailMap')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = ListRulesResponseBodyDataRulesTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class ListRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        rules: List[ListRulesResponseBodyDataRules] = None,
        total: int = None,
    ):
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The rules.
        self.rules = rules
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. The value Success indicates that the request is successful.
        self.code = code
        # The data returned.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTargetsRequest(TeaModel):
    def __init__(
        self,
        arn: str = None,
        event_bus_name: str = None,
        limit: int = None,
        next_token: str = None,
        rule_name: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the event rule.
        self.arn = arn
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The maximum number of entries returned per page.
        self.limit = limit
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The name of the event rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListTargetsResponseBodyDataTargetsParamList(TeaModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.resource_key = resource_key
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTargetsResponseBodyDataTargets(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        errors_tolerance: str = None,
        event_bus_name: str = None,
        id: str = None,
        param_list: List[ListTargetsResponseBodyDataTargetsParamList] = None,
        rule_name: str = None,
        type: str = None,
    ):
        self.endpoint = endpoint
        self.errors_tolerance = errors_tolerance
        self.event_bus_name = event_bus_name
        self.id = id
        self.param_list = param_list
        self.rule_name = rule_name
        self.type = type

    def validate(self):
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = ListTargetsResponseBodyDataTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTargetsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        targets: List[ListTargetsResponseBodyDataTargets] = None,
        total: int = None,
    ):
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The name of the event rule.
        self.targets = targets
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = ListTargetsResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. Valid values:
        # 
        #     Success: The request is successful. 
        # 
        #     Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        #     true: The request is successful. 
        # 
        #     false: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTargetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDefinedEventSourcesRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging. Note: Up to 100 entries can be returned in a call.
        self.limit = limit
        # The name of the event source.
        self.name_prefix = name_prefix
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters(TeaModel):
    def __init__(
        self,
        ip: List[str] = None,
        method: List[str] = None,
        public_web_hook_url: List[str] = None,
        referer: List[str] = None,
        security_config: str = None,
        type: str = None,
        vpc_web_hook_url: List[str] = None,
    ):
        # The CIDR block that is used for security settings. This parameter is required only if SecurityConfig is set to ip. You can enter a CIDR block or an IP address.
        self.ip = ip
        # The HTTP request method that is supported by the generated webhook URL. You can select multiple values. Valid values:
        # 
        # *   GET
        # *   POST
        # *   PUT
        # *   PATCH
        # *   DELETE
        # *   HEAD
        # *   OPTIONS
        # *   TRACE
        # *   CONNECT
        self.method = method
        # The Internet request URL.
        self.public_web_hook_url = public_web_hook_url
        # The security domain name. This parameter is required only if SecurityConfig is set to referer. You can enter a domain name.
        self.referer = referer
        # The type of security settings. Valid values:
        # 
        # *   none: No configuration is required.
        # *   ip: CIDR block.
        # *   referer: security domain name.
        self.security_config = security_config
        # The protocol type that is supported by the generated webhook URL. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # *   HTTP\&HTTPS
        self.type = type
        # The internal request URL.
        self.vpc_web_hook_url = vpc_web_hook_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.method is not None:
            result['Method'] = self.method
        if self.public_web_hook_url is not None:
            result['PublicWebHookUrl'] = self.public_web_hook_url
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.security_config is not None:
            result['SecurityConfig'] = self.security_config
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_web_hook_url is not None:
            result['VpcWebHookUrl'] = self.vpc_web_hook_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('PublicWebHookUrl') is not None:
            self.public_web_hook_url = m.get('PublicWebHookUrl')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SecurityConfig') is not None:
            self.security_config = m.get('SecurityConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcWebHookUrl') is not None:
            self.vpc_web_hook_url = m.get('VpcWebHookUrl')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        maximum_tasks: int = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id
        # The maximum number of consumers.
        self.maximum_tasks = maximum_tasks
        # The network. Valid values: Default and PublicNetwork. Default value: Default. The value PublicNetwork indicates a self-managed network.
        self.network = network
        # The consumer offset.
        self.offset_reset = offset_reset
        # The region ID.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The topic name.
        self.topic = topic
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Indicates whether Base64 decoding is enabled. By default, Base64 decoding is enabled.
        self.is_base_64decode = is_base_64decode
        # The name of the MNS queue.
        self.queue_name = queue_name
        # The region where the MNS queue resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # The ID of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id
        # The name of the queue on the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.queue_name = queue_name
        # The ID of the region where the Message Queue for RabbitMQ instance resides.
        self.region_id = region_id
        # The name of the vhost of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: float = None,
        topic: str = None,
    ):
        # The authentication type. This parameter can be set to ACL or left empty.
        self.auth_type = auth_type
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id
        # The instance endpoint.
        self.instance_endpoint = instance_endpoint
        # The ID of the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id
        # The network that is used by the Message Queue for Apache RocketMQ instance.
        self.instance_network = instance_network
        # The instance password.
        self.instance_password = instance_password
        # The security group ID.
        self.instance_security_group_id = instance_security_group_id
        # The instance type. Valid values: CLOUD\_4, CLOUD\_5, and SELF_BUILT. The value CLOUD\_4 indicates that the instance is a Message Queue for Apache RocketMQ 4.0 instance. The value CLOUD\_5 indicates that the instance is a Message Queue for Apache RocketMQ 5.0 instance. The value SELF_BUILT indicates that the instance is a self-managed RocketMQ instance.
        self.instance_type = instance_type
        # The instance username.
        self.instance_username = instance_username
        # The vSwitch ID.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The virtual private cloud (VPC) ID.
        self.instance_vpc_id = instance_vpc_id
        # The offset from which messages are consumed. Valid values:
        # 
        # *   CONSUME_FROM_LAST_OFFSET: Messages are consumed from the latest offset.
        # *   CONSUME_FROM_FIRST_OFFSET: Messages are consumed from the earliest offset.
        # *   CONSUME_FROM_TIMESTAMP: Messages are consumed from the offset at the specified point in time.
        # 
        # Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset
        # The region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id
        # The tag that is used to filter messages.
        self.tag = tag
        # The timestamp that indicates the time from which messages are consumed. This parameter is valid only if Offset is set to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The name of the topic on the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters(TeaModel):
    def __init__(
        self,
        consume_position: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start message consumption.
        self.consume_position = consume_position
        # The Simple Log Service Logstore.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console. For information about the permission policy of this role, see Create a custom event source of the Log Service type.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters(TeaModel):
    def __init__(
        self,
        schedule: str = None,
        time_zone: str = None,
        user_data: str = None,
    ):
        # The cron expression.
        self.schedule = schedule
        # The time zone in which the cron expression is executed.
        self.time_zone = time_zone
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceList(TeaModel):
    def __init__(
        self,
        arn: str = None,
        ctime: float = None,
        event_bus_name: str = None,
        external_source_type: str = None,
        name: str = None,
        source_http_event_parameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters = None,
        source_kafka_parameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters = None,
        source_mnsparameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters = None,
        source_rabbit_mqparameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters = None,
        source_rocket_mqparameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters = None,
        source_slsparameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters = None,
        source_scheduled_event_parameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters = None,
        status: str = None,
        type: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the queried event source.
        self.arn = arn
        # The timestamp that indicates when the event source was created.
        self.ctime = ctime
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The type of the event source.
        self.external_source_type = external_source_type
        # The name of the queried event source.
        self.name = name
        # The parameters that are returned if HTTP events are specified as the event source.
        self.source_http_event_parameters = source_http_event_parameters
        # The parameters that are returned if Message Queue for Apache Kafka is specified as the event source.
        self.source_kafka_parameters = source_kafka_parameters
        # The parameters that are returned if Message Service (MNS) is specified as the event source.
        self.source_mnsparameters = source_mnsparameters
        # The parameters that are returned if Message Queue for RabbitMQ is specified as the event source.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # The parameters that are returned if Message Queue for Apache RocketMQ is specified as the event source.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The parameters that are returned if Simple Log Service is specified as the event source.
        self.source_slsparameters = source_slsparameters
        # The parameters that are returned if scheduled events are specified as the event source.
        self.source_scheduled_event_parameters = source_scheduled_event_parameters
        # The status of the queried event source. The returned value Activated indicates that the event source is activated.
        self.status = status
        # The type of the queried event source. The returned value UserDefined indicates that the event source is a custom event source.
        self.type = type

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()
        if self.source_scheduled_event_parameters:
            self.source_scheduled_event_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type
        if self.name is not None:
            result['Name'] = self.name
        if self.source_http_event_parameters is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        if self.source_scheduled_event_parameters is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceHttpEventParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters()
            self.source_http_event_parameters = temp_model.from_map(m['SourceHttpEventParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        if m.get('SourceScheduledEventParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters()
            self.source_scheduled_event_parameters = temp_model.from_map(m['SourceScheduledEventParameters'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListUserDefinedEventSourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        event_source_list: List[ListUserDefinedEventSourcesResponseBodyDataEventSourceList] = None,
    ):
        # The event sources.
        self.event_source_list = event_source_list

    def validate(self):
        if self.event_source_list:
            for k in self.event_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventSourceList'] = []
        if self.event_source_list is not None:
            for k in self.event_source_list:
                result['EventSourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_source_list = []
        if m.get('EventSourceList') is not None:
            for k in m.get('EventSourceList'):
                temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceList()
                self.event_source_list.append(temp_model.from_map(k))
        return self


class ListUserDefinedEventSourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListUserDefinedEventSourcesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserDefinedEventSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserDefinedEventSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseEventStreamingRequest(TeaModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
        # The name of the event stream that you want to stop.
        self.event_streaming_name = event_streaming_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class PauseEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PauseEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PauseEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PauseEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutTargetsRequestTargetsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue. Events that are not processed or whose maximum retries have been exceeded are written to the dead-letter queue.
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class PutTargetsRequestTargetsParamList(TeaModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to deliver events to the event target. For more information,see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.form = form
        # The resource parameter of the event target. For more information,see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.resource_key = resource_key
        # The template based on which events are delivered to the event target.
        self.template = template
        # The value of the event target parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PutTargetsRequestTargets(TeaModel):
    def __init__(
        self,
        dead_letter_queue: PutTargetsRequestTargetsDeadLetterQueue = None,
        endpoint: str = None,
        errors_tolerance: str = None,
        id: str = None,
        param_list: List[PutTargetsRequestTargetsParamList] = None,
        push_retry_strategy: str = None,
        type: str = None,
    ):
        # The dead-letter queue. Events that are not processed or whose maximum retries have been exceeded are written to the dead-letter queue. The dead-letter queue feature supports the following queue types: Message Queue for Apache RocketMQ, Message Service, Message Queue for Apache Kafka, and event bus.
        self.dead_letter_queue = dead_letter_queue
        # The endpoint of the event target.
        self.endpoint = endpoint
        # The fault tolerance policy. Valid values:
        # 
        # * **ALL**: ignores the error. Fault tolerance is allowed. If an error occurs, event processing is not blocked. If the message exceeds the number of retries specified by the retry policy, the message is delivered to a dead-letter queue or discarded based on your configurations.
        # 
        # * **NONE**: does not ignore the error. Fault tolerance is prohibited. If an error occurs and the message exceeds the number of retries specified by the retry policy, event processing is blocked.
        self.errors_tolerance = errors_tolerance
        # The ID of the custom event target.
        self.id = id
        # The parameters that are configured for the event target.
        self.param_list = param_list
        # The retry policy for pushing the event. Valid values:
        # 
        # * **BACKOFF_RETRY**: backoff retry. A failed event can be retried up to three times. The interval between two consecutive retries is a random value from 10 to 20. Unit: seconds.
        # 
        # * **EXPONENTIAL_DECAY_RETRY**: exponential decay retry. The request can be retried up to 176 times. The interval between two consecutive retries exponentially increases to 512 seconds, and the total retry time is one day. The specific retry intervals are 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 512, ..., and 512 seconds. The interval of 512 seconds can be used up to one hundred and sixty-seven times in total.
        self.push_retry_strategy = push_retry_strategy
        # The type of the event target. For more information, see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.type = type

    def validate(self):
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterQueue') is not None:
            temp_model = PutTargetsRequestTargetsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = PutTargetsRequestTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PutTargetsRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        targets: List[PutTargetsRequestTargets] = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The name of the event rule.
        self.rule_name = rule_name
        # The event targets to be created or updated. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = PutTargetsRequestTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class PutTargetsShrinkRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        targets_shrink: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The name of the event rule.
        self.rule_name = rule_name
        # The event targets to be created or updated. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.targets_shrink = targets_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        return self


class PutTargetsResponseBodyDataErrorEntries(TeaModel):
    def __init__(
        self,
        entry_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The ID of the failed event target.
        self.entry_id = entry_id
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class PutTargetsResponseBodyData(TeaModel):
    def __init__(
        self,
        error_entries: List[PutTargetsResponseBodyDataErrorEntries] = None,
        error_entries_count: int = None,
    ):
        # The ID of the failed event target.
        self.error_entries = error_entries
        # The number of failed event targets. Valid values:
        # 
        # *   0: All event targets succeeded.
        # *   An integer other than 0: indicates the number of failed event targets.
        self.error_entries_count = error_entries_count

    def validate(self):
        if self.error_entries:
            for k in self.error_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorEntries'] = []
        if self.error_entries is not None:
            for k in self.error_entries:
                result['ErrorEntries'].append(k.to_map() if k else None)
        if self.error_entries_count is not None:
            result['ErrorEntriesCount'] = self.error_entries_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_entries = []
        if m.get('ErrorEntries') is not None:
            for k in m.get('ErrorEntries'):
                temp_model = PutTargetsResponseBodyDataErrorEntries()
                self.error_entries.append(temp_model.from_map(k))
        if m.get('ErrorEntriesCount') is not None:
            self.error_entries_count = m.get('ErrorEntriesCount')
        return self


class PutTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PutTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # *   Success: The call succeeded.
        # *   Other codes: The call failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned result.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = PutTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PutTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutTargetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_source: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event ID.
        self.event_id = event_id
        self.event_source = event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        return self


class QueryEventResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code 200 indicates that the request was successful.
        self.code = code
        # The content of the event.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEventResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventTracesRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event ID.
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class QueryEventTracesResponseBodyData(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_time: int = None,
        endpoint: str = None,
        event_bus_name: str = None,
        event_id: str = None,
        event_source: str = None,
        notify_latency: str = None,
        notify_status: str = None,
        notify_time: int = None,
        received_time: int = None,
        rule_matching_time: str = None,
        rule_name: str = None,
    ):
        # The type of the event trace. Valid values: PutEvent: a delivery event. FilterEvent: a filtering event. PushEvent: a pushing event.
        self.action = action
        # The execution time of the event trace.
        self.action_time = action_time
        # The endpoint of the event target. This parameter is returned if the value of the Action parameter is PushEvent.
        self.endpoint = endpoint
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event ID.
        self.event_id = event_id
        # The name of the event source.
        self.event_source = event_source
        # The delivery delay of the event target. This parameter is returned if the value of the Action parameter is PushEvent.
        self.notify_latency = notify_latency
        # The event target delivery status.
        self.notify_status = notify_status
        # The delivery time of the event target. This parameter is returned if the value of the Action parameter is PushEvent.
        self.notify_time = notify_time
        # The time when the event was delivered to the event bus. This parameter is returned if the value of the Action parameter is PutEvent.
        self.received_time = received_time
        # The time when the event rule was matched. This parameter is returned if the value of the Action parameter is FilterEvent.
        self.rule_matching_time = rule_matching_time
        # The name of the event rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_time is not None:
            result['ActionTime'] = self.action_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.notify_latency is not None:
            result['NotifyLatency'] = self.notify_latency
        if self.notify_status is not None:
            result['NotifyStatus'] = self.notify_status
        if self.notify_time is not None:
            result['NotifyTime'] = self.notify_time
        if self.received_time is not None:
            result['ReceivedTime'] = self.received_time
        if self.rule_matching_time is not None:
            result['RuleMatchingTime'] = self.rule_matching_time
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('NotifyLatency') is not None:
            self.notify_latency = m.get('NotifyLatency')
        if m.get('NotifyStatus') is not None:
            self.notify_status = m.get('NotifyStatus')
        if m.get('NotifyTime') is not None:
            self.notify_time = m.get('NotifyTime')
        if m.get('ReceivedTime') is not None:
            self.received_time = m.get('ReceivedTime')
        if m.get('RuleMatchingTime') is not None:
            self.rule_matching_time = m.get('RuleMatchingTime')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class QueryEventTracesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryEventTracesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code 200 indicates that the request was successful.
        self.code = code
        # The name of the event source.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryEventTracesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventTracesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEventTracesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryEventTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTracedEventByEventIdRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_source: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event ID.
        self.event_id = event_id
        # The name of the event source.
        self.event_source = event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        return self


class QueryTracedEventByEventIdResponseBodyDataEvents(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_received_time: int = None,
        event_source: str = None,
        event_type: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event ID.
        self.event_id = event_id
        # The time when the event was delivered to the event bus.
        self.event_received_time = event_received_time
        # The name of the event source.
        self.event_source = event_source
        # The event type.
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_received_time is not None:
            result['EventReceivedTime'] = self.event_received_time
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.event_type is not None:
            result['EventType'] = self.event_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventReceivedTime') is not None:
            self.event_received_time = m.get('EventReceivedTime')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        return self


class QueryTracedEventByEventIdResponseBodyData(TeaModel):
    def __init__(
        self,
        events: List[QueryTracedEventByEventIdResponseBodyDataEvents] = None,
        next_token: str = None,
        total: int = None,
    ):
        # The events.
        self.events = events
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = QueryTracedEventByEventIdResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryTracedEventByEventIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryTracedEventByEventIdResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The total number of entries returned.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTracedEventByEventIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTracedEventByEventIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTracedEventByEventIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTracedEventByEventIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTracedEventsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        event_bus_name: str = None,
        event_source: str = None,
        event_type: str = None,
        limit: int = None,
        matched_rule: str = None,
        next_token: str = None,
        start_time: int = None,
    ):
        # The end of the time range when event traces are queried. Unit: milliseconds.
        self.end_time = end_time
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The name of the event source.
        self.event_source = event_source
        # The event type.
        self.event_type = event_type
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging. Up to 100 entries can be returned in a call.
        self.limit = limit
        # The name of the event rule that is matched.
        self.matched_rule = matched_rule
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The beginning of the time range to query event traces. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.matched_rule is not None:
            result['MatchedRule'] = self.matched_rule
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MatchedRule') is not None:
            self.matched_rule = m.get('MatchedRule')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryTracedEventsResponseBodyDataEvents(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_received_time: int = None,
        event_source: str = None,
        event_type: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event ID.
        self.event_id = event_id
        # The time when the event was delivered to the event bus.
        self.event_received_time = event_received_time
        # The name of the event source.
        self.event_source = event_source
        # The event type.
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_received_time is not None:
            result['EventReceivedTime'] = self.event_received_time
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.event_type is not None:
            result['EventType'] = self.event_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventReceivedTime') is not None:
            self.event_received_time = m.get('EventReceivedTime')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        return self


class QueryTracedEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        events: List[QueryTracedEventsResponseBodyDataEvents] = None,
        next_token: str = None,
        total: int = None,
    ):
        # The event type.
        self.events = events
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = QueryTracedEventsResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryTracedEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryTracedEventsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The data returned.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryTracedEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTracedEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTracedEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTracedEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartEventStreamingRequest(TeaModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
        # The name of the event stream that you want to enable.
        self.event_streaming_name = event_streaming_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class StartEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestEventPatternRequest(TeaModel):
    def __init__(
        self,
        event: str = None,
        event_pattern: str = None,
    ):
        # The event.
        self.event = event
        # The event pattern.
        self.event_pattern = event_pattern

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['Event'] = self.event
        if self.event_pattern is not None:
            result['EventPattern'] = self.event_pattern
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('EventPattern') is not None:
            self.event_pattern = m.get('EventPattern')
        return self


class TestEventPatternResponseBodyData(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # The value true indicates that the event pattern matches the provided JSON format. The value false indicates that the event pattern does not match the provided JSON format.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class TestEventPatternResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TestEventPatternResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned result.
        self.data = data
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TestEventPatternResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TestEventPatternResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TestEventPatternResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TestEventPatternResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApiDestinationRequestHttpApiParameters(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        method: str = None,
    ):
        # The endpoint of the API destination. The endpoint can be up to 127 characters in length.
        self.endpoint = endpoint
        # The HTTP request method. Valid values:
        # 
        # - GET
        # - POST
        # - HEAD
        # - DELETE
        # - PUT
        # - PATCH
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class UpdateApiDestinationRequest(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        http_api_parameters: UpdateApiDestinationRequestHttpApiParameters = None,
    ):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        self.api_destination_name = api_destination_name
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # Note: Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        self.connection_name = connection_name
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the API destination.
        self.http_api_parameters = http_api_parameters

    def validate(self):
        if self.http_api_parameters:
            self.http_api_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.http_api_parameters is not None:
            result['HttpApiParameters'] = self.http_api_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpApiParameters') is not None:
            temp_model = UpdateApiDestinationRequestHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
        return self


class UpdateApiDestinationShrinkRequest(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        http_api_parameters_shrink: str = None,
    ):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        self.api_destination_name = api_destination_name
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # Note: Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        self.connection_name = connection_name
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the API destination.
        self.http_api_parameters_shrink = http_api_parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.http_api_parameters_shrink is not None:
            result['HttpApiParameters'] = self.http_api_parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpApiParameters') is not None:
            self.http_api_parameters_shrink = m.get('HttpApiParameters')
        return self


class UpdateApiDestinationResponseBody(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # api-destination-name
        self.api_destination_name = api_destination_name
        # The response code. If the request is successful, Success is returned.
        self.code = code
        # The returned message. If the request is successful, success is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateApiDestinationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApiDestinationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateApiDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnectionRequestAuthParametersApiKeyAuthParameters(TeaModel):
    def __init__(
        self,
        api_key_name: str = None,
        api_key_value: str = None,
    ):
        # The key of the API key.
        self.api_key_name = api_key_name
        # The value of the API key.
        self.api_key_value = api_key_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateConnectionRequestAuthParametersBasicAuthParameters(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateConnectionRequestAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The AccessKey secret of the client.
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret
        # The key of the request body.
        self.key = key
        # The value of the request body.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret
        # The key of the request header.
        self.key = key
        # The value of the request header.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(TeaModel):
    def __init__(
        self,
        is_value_secret: str = None,
        key: str = None,
        value: str = None,
    ):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret
        # The key of the request path.
        self.key = key
        # The value of the request path.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters(TeaModel):
    def __init__(
        self,
        body_parameters: List[UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters] = None,
        header_parameters: List[UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters] = None,
        query_string_parameters: List[UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters] = None,
    ):
        # The parameters that are configured for the request body.
        self.body_parameters = body_parameters
        # The value of the request header.
        self.header_parameters = header_parameters
        # The parameters that are configured for the request path.
        self.query_string_parameters = query_string_parameters

    def validate(self):
        if self.body_parameters:
            for k in self.body_parameters:
                if k:
                    k.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.query_string_parameters:
            for k in self.query_string_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyParameters'] = []
        if self.body_parameters is not None:
            for k in self.body_parameters:
                result['BodyParameters'].append(k.to_map() if k else None)
        result['HeaderParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['HeaderParameters'].append(k.to_map() if k else None)
        result['QueryStringParameters'] = []
        if self.query_string_parameters is not None:
            for k in self.query_string_parameters:
                result['QueryStringParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body_parameters = []
        if m.get('BodyParameters') is not None:
            for k in m.get('BodyParameters'):
                temp_model = UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class UpdateConnectionRequestAuthParametersOAuthParameters(TeaModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_parameters: UpdateConnectionRequestAuthParametersOAuthParametersClientParameters = None,
        http_method: str = None,
        oauth_http_parameters: UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters = None,
    ):
        # The endpoint that is used to obtain the OAuth token. The endpoint can be up to 127 characters in length.
        self.authorization_endpoint = authorization_endpoint
        # The parameters that are configured for the client.
        self.client_parameters = client_parameters
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        # *   DELETE
        # *   PUT
        # *   PATCH
        self.http_method = http_method
        # The request parameters for OAuth authentication.
        self.oauth_http_parameters = oauth_http_parameters

    def validate(self):
        if self.client_parameters:
            self.client_parameters.validate()
        if self.oauth_http_parameters:
            self.oauth_http_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateConnectionRequestAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m['ClientParameters'])
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('OAuthHttpParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m['OAuthHttpParameters'])
        return self


class UpdateConnectionRequestAuthParameters(TeaModel):
    def __init__(
        self,
        api_key_auth_parameters: UpdateConnectionRequestAuthParametersApiKeyAuthParameters = None,
        authorization_type: str = None,
        basic_auth_parameters: UpdateConnectionRequestAuthParametersBasicAuthParameters = None,
        oauth_parameters: UpdateConnectionRequestAuthParametersOAuthParameters = None,
    ):
        # The parameters for API key authentication.
        self.api_key_auth_parameters = api_key_auth_parameters
        # The authentication type. Valid values:
        # 
        # BASIC_AUTH: basic authentication.
        # 
        # Introduction: Basic authentication is a simple authentication scheme built into the HTTP protocol. When you use the HTTP protocol for communications, the authentication method that the HTTP server uses to authenticate user identities on the client is defined in the protocol. The request header is in the Authorization: Basic Base64-encoded string (Username:Password) format.
        # 
        # 1.  Username and Password are required.
        # 
        # API_KEY_AUTH: API key authentication.
        # 
        # Introduction: The request header is in the Token : Token value format.
        # 
        # *   ApiKeyName and ApiKeyValue are required.
        # 
        # OAUTH_AUTH: OAuth authentication.
        # 
        # Introduction: OAuth2.0 is an authentication mechanism. In normal cases, a system that does not use OAuth2.0 can access the resources of the server from the client. To ensure access security, access tokens are used to identify users in OAuth 2.0. The client must use an access token to access protected resources. This way, OAuth 2.0 protects resources from being accessed from malicious clients and improves system security.
        # 
        # *   AuthorizationEndpoint, OAuthHttpParameters, and HttpMethod are required.
        self.authorization_type = authorization_type
        # The parameters that are configured for basic authentication.
        self.basic_auth_parameters = basic_auth_parameters
        # The parameters that are configured for OAuth authentication.
        self.oauth_parameters = oauth_parameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.oauth_parameters:
            self.oauth_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateConnectionRequestAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('BasicAuthParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
        if m.get('OAuthParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
        return self


class UpdateConnectionRequestNetworkParameters(TeaModel):
    def __init__(
        self,
        network_type: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitche_id: str = None,
    ):
        # PublicNetwork: the Internet.
        # 
        # PrivateNetwork: virtual private cloud (VPC).
        # 
        # Note: If you set this parameter to PrivateNetwork, you must configure VpcId, VswitcheId, and SecurityGroupId.
        self.network_type = network_type
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitche_id = vswitche_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateConnectionRequest(TeaModel):
    def __init__(
        self,
        auth_parameters: UpdateConnectionRequestAuthParameters = None,
        connection_name: str = None,
        description: str = None,
        network_parameters: UpdateConnectionRequestNetworkParameters = None,
    ):
        # The parameters that are configured for authentication.
        self.auth_parameters = auth_parameters
        # The name of the connection that you want to update. The name must be 2 to 127 characters in length.
        self.connection_name = connection_name
        # The description of the connection. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the network.
        self.network_parameters = network_parameters

    def validate(self):
        if self.auth_parameters:
            self.auth_parameters.validate()
        if self.network_parameters:
            self.network_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters is not None:
            result['AuthParameters'] = self.auth_parameters.to_map()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.network_parameters is not None:
            result['NetworkParameters'] = self.network_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParameters()
            self.auth_parameters = temp_model.from_map(m['AuthParameters'])
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkParameters') is not None:
            temp_model = UpdateConnectionRequestNetworkParameters()
            self.network_parameters = temp_model.from_map(m['NetworkParameters'])
        return self


class UpdateConnectionShrinkRequest(TeaModel):
    def __init__(
        self,
        auth_parameters_shrink: str = None,
        connection_name: str = None,
        description: str = None,
        network_parameters_shrink: str = None,
    ):
        # The parameters that are configured for authentication.
        self.auth_parameters_shrink = auth_parameters_shrink
        # The name of the connection that you want to update. The name must be 2 to 127 characters in length.
        self.connection_name = connection_name
        # The description of the connection. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the network.
        self.network_parameters_shrink = network_parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters_shrink is not None:
            result['AuthParameters'] = self.auth_parameters_shrink
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.network_parameters_shrink is not None:
            result['NetworkParameters'] = self.network_parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            self.auth_parameters_shrink = m.get('AuthParameters')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkParameters') is not None:
            self.network_parameters_shrink = m.get('NetworkParameters')
        return self


class UpdateConnectionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventBusRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
    ):
        # The description of the event bus.
        self.description = description
        # The name of the event bus.
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class UpdateEventBusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventBusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEventBusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventSourceRequestSourceHttpEventParameters(TeaModel):
    def __init__(
        self,
        ip: List[str] = None,
        method: List[str] = None,
        referer: List[str] = None,
        security_config: str = None,
        type: str = None,
    ):
        # The CIDR block that is used for security settings. This parameter is required only if SecurityConfig is set to ip. You can enter a CIDR block or an IP address.
        self.ip = ip
        # The HTTP request method supported by the generated webhook URL. You can select multiple values. Valid values:
        # 
        # *   GET
        # *   POST
        # *   PUT
        # *   PATCH
        # *   DELETE
        # *   HEAD
        # *   OPTIONS
        # *   TRACE
        # *   CONNECT
        self.method = method
        # The security domain name. This parameter is required only if SecurityConfig is set to referer. You can enter a domain name.
        self.referer = referer
        # The type of security settings. Valid values:
        # 
        # *   none: No configuration is required.
        # *   ip: CIDR block.
        # *   referer: security domain name.
        self.security_config = security_config
        # The protocol type that is supported by the generated webhook URL. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # *   HTTP\&HTTPS
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.method is not None:
            result['Method'] = self.method
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.security_config is not None:
            result['SecurityConfig'] = self.security_config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SecurityConfig') is not None:
            self.security_config = m.get('SecurityConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateEventSourceRequestSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        maximum_tasks: int = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id
        # The maximum number of consumers.
        self.maximum_tasks = maximum_tasks
        # The network. Valid values: Default and PublicNetwork. Default value: Default. The value PublicNetwork indicates a self-managed network.
        self.network = network
        # The consumer offset.
        self.offset_reset = offset_reset
        # The ID of the region where the Message Queue for Apache Kafka instance resides.
        self.region_id = region_id
        # The ID of the security group to which the Message Queue for Apache Kafka instance belongs. This parameter is required only if you set Network to PublicNetwork.
        self.security_group_id = security_group_id
        # The name of the topic on the Message Queue for Apache Kafka instance.
        self.topic = topic
        # The ID of the vSwitch with which the Message Queue for Apache Kafka instance is associated. This parameter is required only if you set Network to PublicNetwork.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC in which the Message Queue for Apache Kafka instance resides. This parameter is required only if you set Network to PublicNetwork.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateEventSourceRequestSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Indicates whether Base64 decoding is enabled. By default, Base64 decoding is enabled.
        self.is_base_64decode = is_base_64decode
        # The name of the MNS queue.
        self.queue_name = queue_name
        # The region where the MNS queue resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateEventSourceRequestSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # The ID of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id
        # The name of the queue on the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.queue_name = queue_name
        # The ID of the region where the Message Queue for RabbitMQ instance resides.
        self.region_id = region_id
        # The name of the vhost of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class UpdateEventSourceRequestSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        # The authentication type. You can set this parameter to ACL or leave this parameter empty.
        self.auth_type = auth_type
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id
        # The endpoint that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_endpoint = instance_endpoint
        # The ID of the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id
        # None.
        self.instance_network = instance_network
        # The password that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_password = instance_password
        # The ID of the security group to which the Message Queue for Apache RocketMQ instance belongs.
        self.instance_security_group_id = instance_security_group_id
        # The type of the Message Queue for Apache RocketMQ instance. Valid values:
        # 
        # *   Cloud\_4: Message Queue for Apache RocketMQ 4.0 instance.
        # *   Cloud\_5: Message Queue for Apache RocketMQ 5.0 instance.
        self.instance_type = instance_type
        # The username that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_username = instance_username
        # The ID of the vSwitch with which the Message Queue for Apache RocketMQ instance is associated.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The ID of the virtual private cloud (VPC) in which the Message Queue for Apache RocketMQ instance resides.
        self.instance_vpc_id = instance_vpc_id
        # The offset from which message consumption starts. Valid values:
        # 
        # *   CONSUME_FROM_LAST_OFFSET: Start message consumption from the latest offset.
        # *   CONSUME_FROM_FIRST_OFFSET: Start message consumption from the earliest offset.
        # *   CONSUME_FROM_TIMESTAMP: Start message consumption from the offset at the specified point in time.
        # 
        # Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset
        # The region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id
        # The tag that is used to filter messages.
        self.tag = tag
        # The timestamp that specifies the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The name of the topic on the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateEventSourceRequestSourceSLSParameters(TeaModel):
    def __init__(
        self,
        consume_position: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The starting consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start consumption.
        self.consume_position = consume_position
        # The Log Service Logstore.
        self.log_store = log_store
        # The Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console. For information about the permission policy of this role, see Create a custom event source of the Log Service type.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdateEventSourceRequestSourceScheduledEventParameters(TeaModel):
    def __init__(
        self,
        schedule: str = None,
        time_zone: str = None,
        user_data: str = None,
    ):
        # The cron expression.
        self.schedule = schedule
        # The time zone in which the cron expression is executed.
        self.time_zone = time_zone
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class UpdateEventSourceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_source_name: str = None,
        source_http_event_parameters: UpdateEventSourceRequestSourceHttpEventParameters = None,
        source_kafka_parameters: UpdateEventSourceRequestSourceKafkaParameters = None,
        source_mnsparameters: UpdateEventSourceRequestSourceMNSParameters = None,
        source_rabbit_mqparameters: UpdateEventSourceRequestSourceRabbitMQParameters = None,
        source_rocket_mqparameters: UpdateEventSourceRequestSourceRocketMQParameters = None,
        source_slsparameters: UpdateEventSourceRequestSourceSLSParameters = None,
        source_scheduled_event_parameters: UpdateEventSourceRequestSourceScheduledEventParameters = None,
    ):
        # The description of the event source.
        self.description = description
        # The event bus with which the event source is associated.
        self.event_bus_name = event_bus_name
        # The name of the event source.
        self.event_source_name = event_source_name
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters = source_http_event_parameters
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters = source_kafka_parameters
        # The parameters that are configured if the event source is Message Service (MNS).
        self.source_mnsparameters = source_mnsparameters
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # SourceSLSParameters
        self.source_slsparameters = source_slsparameters
        # The parameters that are configured if you specify scheduled events as the event source.
        self.source_scheduled_event_parameters = source_scheduled_event_parameters

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()
        if self.source_scheduled_event_parameters:
            self.source_scheduled_event_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        if self.source_scheduled_event_parameters is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('SourceHttpEventParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceHttpEventParameters()
            self.source_http_event_parameters = temp_model.from_map(m['SourceHttpEventParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        if m.get('SourceScheduledEventParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceScheduledEventParameters()
            self.source_scheduled_event_parameters = temp_model.from_map(m['SourceScheduledEventParameters'])
        return self


class UpdateEventSourceShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_source_name: str = None,
        source_http_event_parameters_shrink: str = None,
        source_kafka_parameters_shrink: str = None,
        source_mnsparameters_shrink: str = None,
        source_rabbit_mqparameters_shrink: str = None,
        source_rocket_mqparameters_shrink: str = None,
        source_slsparameters_shrink: str = None,
        source_scheduled_event_parameters_shrink: str = None,
    ):
        # The description of the event source.
        self.description = description
        # The event bus with which the event source is associated.
        self.event_bus_name = event_bus_name
        # The name of the event source.
        self.event_source_name = event_source_name
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters_shrink = source_http_event_parameters_shrink
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters_shrink = source_kafka_parameters_shrink
        # The parameters that are configured if the event source is Message Service (MNS).
        self.source_mnsparameters_shrink = source_mnsparameters_shrink
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters_shrink = source_rabbit_mqparameters_shrink
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters_shrink = source_rocket_mqparameters_shrink
        # SourceSLSParameters
        self.source_slsparameters_shrink = source_slsparameters_shrink
        # The parameters that are configured if you specify scheduled events as the event source.
        self.source_scheduled_event_parameters_shrink = source_scheduled_event_parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters_shrink is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters_shrink
        if self.source_kafka_parameters_shrink is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters_shrink
        if self.source_mnsparameters_shrink is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters_shrink
        if self.source_rabbit_mqparameters_shrink is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters_shrink
        if self.source_rocket_mqparameters_shrink is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters_shrink
        if self.source_slsparameters_shrink is not None:
            result['SourceSLSParameters'] = self.source_slsparameters_shrink
        if self.source_scheduled_event_parameters_shrink is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('SourceHttpEventParameters') is not None:
            self.source_http_event_parameters_shrink = m.get('SourceHttpEventParameters')
        if m.get('SourceKafkaParameters') is not None:
            self.source_kafka_parameters_shrink = m.get('SourceKafkaParameters')
        if m.get('SourceMNSParameters') is not None:
            self.source_mnsparameters_shrink = m.get('SourceMNSParameters')
        if m.get('SourceRabbitMQParameters') is not None:
            self.source_rabbit_mqparameters_shrink = m.get('SourceRabbitMQParameters')
        if m.get('SourceRocketMQParameters') is not None:
            self.source_rocket_mqparameters_shrink = m.get('SourceRocketMQParameters')
        if m.get('SourceSLSParameters') is not None:
            self.source_slsparameters_shrink = m.get('SourceSLSParameters')
        if m.get('SourceScheduledEventParameters') is not None:
            self.source_scheduled_event_parameters_shrink = m.get('SourceScheduledEventParameters')
        return self


class UpdateEventSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code
        # The result of the operation.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEventSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventStreamingRequestRunOptionsBatchWindow(TeaModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        # The maximum number of events that is allowed in the batch window. If the value specified by this parameter is reached, the data in the batch window is pushed to the downstream application. If multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.count_based_window = count_based_window
        # The maximum period of time during which events are allowed in the batch window. Unit: seconds. If the value specified by this parameter is reached, the data in the batch window is pushed to the downstream application. If multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class UpdateEventStreamingRequestRunOptionsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue.
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class UpdateEventStreamingRequestRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: int = None,
        maximum_retry_attempts: int = None,
        push_retry_strategy: str = None,
    ):
        # The maximum period of time during which retries are performed.
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        # The maximum number of retries.
        self.maximum_retry_attempts = maximum_retry_attempts
        # The retry policy that is used if an event failed to be pushed. Valid values: BACKOFF_RETRY and EXPONENTIAL_DECAY_RETRY.
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class UpdateEventStreamingRequestRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: UpdateEventStreamingRequestRunOptionsBatchWindow = None,
        dead_letter_queue: UpdateEventStreamingRequestRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: UpdateEventStreamingRequestRunOptionsRetryStrategy = None,
    ):
        # The information about the batch window.
        self.batch_window = batch_window
        # Specifies whether to enable dead-letter queues. By default, dead-letter queues are disabled. Messages that fail to be pushed are discarded after the maximum number of retries specified by the retry policy is reached.
        self.dead_letter_queue = dead_letter_queue
        # The fault tolerance policy. The value NONE specifies that faults are not tolerated, and the value All specifies that all faults are tolerated.
        self.errors_tolerance = errors_tolerance
        # The concurrency level.
        self.maximum_tasks = maximum_tasks
        # The information about the retry policy that is used if the event fails to be pushed.
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = UpdateEventStreamingRequestRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = UpdateEventStreamingRequestRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = UpdateEventStreamingRequestRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersConcurrency(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The delivery concurrency. Minimum value: 1.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the Function Compute function.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The invocation type. Valid values: Sync and Async.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersQualifier(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The alias of the service to which the function belongs.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersServiceName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the Function Compute service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkFcParametersBody = None,
        concurrency: UpdateEventStreamingRequestSinkSinkFcParametersConcurrency = None,
        function_name: UpdateEventStreamingRequestSinkSinkFcParametersFunctionName = None,
        invocation_type: UpdateEventStreamingRequestSinkSinkFcParametersInvocationType = None,
        qualifier: UpdateEventStreamingRequestSinkSinkFcParametersQualifier = None,
        service_name: UpdateEventStreamingRequestSinkSinkFcParametersServiceName = None,
    ):
        # The message body that is sent to the function.
        self.body = body
        # The information about the delivery concurrency.
        self.concurrency = concurrency
        # The information about the Function Compute function.
        self.function_name = function_name
        # The information about the invocation type.
        self.invocation_type = invocation_type
        # The information about the service to which the function belongs.
        self.qualifier = qualifier
        # The information about the Function Compute service.
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.concurrency:
            self.concurrency.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Concurrency') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m['Concurrency'])
        if m.get('FunctionName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFnfParametersFlowName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFnfParametersInput(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFnfParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFnfParameters(TeaModel):
    def __init__(
        self,
        execution_name: UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName = None,
        flow_name: UpdateEventStreamingRequestSinkSinkFnfParametersFlowName = None,
        input: UpdateEventStreamingRequestSinkSinkFnfParametersInput = None,
        role_name: UpdateEventStreamingRequestSinkSinkFnfParametersRoleName = None,
    ):
        self.execution_name = execution_name
        self.flow_name = flow_name
        self.input = input
        self.role_name = role_name

    def validate(self):
        if self.execution_name:
            self.execution_name.validate()
        if self.flow_name:
            self.flow_name.validate()
        if self.input:
            self.input.validate()
        if self.role_name:
            self.role_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name.to_map()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name.to_map()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m['ExecutionName'])
        if m.get('FlowName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m['FlowName'])
        if m.get('Input') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('RoleName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ACK mode. If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high. If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader. If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ID of the Message Queue for Apache Kafka instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The message key.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the topic in Message Queue for Apache Kafka instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersValue(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: UpdateEventStreamingRequestSinkSinkKafkaParametersAcks = None,
        instance_id: UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId = None,
        key: UpdateEventStreamingRequestSinkSinkKafkaParametersKey = None,
        topic: UpdateEventStreamingRequestSinkSinkKafkaParametersTopic = None,
        value: UpdateEventStreamingRequestSinkSinkKafkaParametersValue = None,
    ):
        # The information about the acknowledgment (ACK) mode. If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high. If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader. If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.acks = acks
        # The information about the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id
        # The information about the message key.
        self.key = key
        # The information about the topic in Message Queue for Apache Kafka instance.
        self.topic = topic
        # The information about the message value.
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('Topic') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class UpdateEventStreamingRequestSinkSinkMNSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # Specifies that Base64 encoding is enabled.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the queue in MNS.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkMNSParametersBody = None,
        is_base_64encode: UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: UpdateEventStreamingRequestSinkSinkMNSParametersQueueName = None,
    ):
        # The message content.
        self.body = body
        # Specifies whether to enable Base64 encoding.
        self.is_base_64encode = is_base_64encode
        # The information about the MNS queue.
        self.queue_name = queue_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the exchange in the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ID of the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The routing rule of the message.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The type of the resource to which events are delivered. Valid values: Exchange: exchanges. Queue: queues.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The vhost name of the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody = None,
        exchange: UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange = None,
        instance_id: UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId = None,
        message_id: UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId = None,
        properties: UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties = None,
        queue_name: UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName = None,
        routing_key: UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        # The message content.
        self.body = body
        # The information about the exchange to which events are delivered. This parameter is available only if you set TargetType to Exchange.
        self.exchange = exchange
        # The information about the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id
        # The message ID.
        self.message_id = message_id
        # The properties that are used to filter messages.
        self.properties = properties
        # The information about the queue to which events are delivered. This parameter is available only if you set TargetType to Queue.
        self.queue_name = queue_name
        # The information about the routing rule of the message. This parameter is available only if you set TargetType to Exchange.
        self.routing_key = routing_key
        # The information about the type of the resource to which events are delivered.
        self.target_type = target_type
        # The information about the vhost of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkRocketMQParametersBody = None,
        instance_id: UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId = None,
        keys: UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys = None,
        properties: UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties = None,
        tags: UpdateEventStreamingRequestSinkSinkRocketMQParametersTags = None,
        topic: UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic = None,
    ):
        # The message content.
        self.body = body
        # The parameters that are configured if the event target is Message Queue for Apache RocketMQ.
        self.instance_id = instance_id
        # The properties that are used to filter messages.
        self.keys = keys
        # The properties that are used to filter messages.
        self.properties = properties
        # The properties that are used to filter messages.
        self.tags = tags
        # The information about the topic in the Message Queue for Apache RocketMQ instance.
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before event transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The Log Service Logstore.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersProject(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The Log Service project.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the topic in which logs are stored. The topic corresponds to the topic reserved field in Log Service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkSLSParametersBody = None,
        log_store: UpdateEventStreamingRequestSinkSinkSLSParametersLogStore = None,
        project: UpdateEventStreamingRequestSinkSinkSLSParametersProject = None,
        role_name: UpdateEventStreamingRequestSinkSinkSLSParametersRoleName = None,
        topic: UpdateEventStreamingRequestSinkSinkSLSParametersTopic = None,
    ):
        # The message body that is sent to Log Service.
        self.body = body
        # The information about the Log Service Logstore.
        self.log_store = log_store
        # The information about the Log Service project.
        self.project = project
        # The information about the role. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.role_name = role_name
        # The information about the topic in which logs are stored. The topic corresponds to the topic reserved field in Log Service.
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class UpdateEventStreamingRequestSink(TeaModel):
    def __init__(
        self,
        sink_fc_parameters: UpdateEventStreamingRequestSinkSinkFcParameters = None,
        sink_fnf_parameters: UpdateEventStreamingRequestSinkSinkFnfParameters = None,
        sink_kafka_parameters: UpdateEventStreamingRequestSinkSinkKafkaParameters = None,
        sink_mnsparameters: UpdateEventStreamingRequestSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: UpdateEventStreamingRequestSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: UpdateEventStreamingRequestSinkSinkRocketMQParameters = None,
        sink_slsparameters: UpdateEventStreamingRequestSinkSinkSLSParameters = None,
    ):
        # The parameters that are configured if the event target is Function Compute.
        self.sink_fc_parameters = sink_fc_parameters
        self.sink_fnf_parameters = sink_fnf_parameters
        # The parameters that are configured if the event target is Message Queue for Apache Kafka.
        self.sink_kafka_parameters = sink_kafka_parameters
        # The parameters that are configured if the event target is MNS.
        self.sink_mnsparameters = sink_mnsparameters
        # The parameters that are configured if the event target is Message Queue for RabbitMQ.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        # Sink RocketMQ Parameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        # Sink SLS Parameters
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_fnf_parameters:
            self.sink_fnf_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_fnf_parameters is not None:
            result['SinkFnfParameters'] = self.sink_fnf_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkFnfParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m['SinkFnfParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class UpdateEventStreamingRequestSourceSourceDTSParameters(TeaModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: int = None,
        password: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        # The URL and port number of the data subscription channel.
        self.broker_url = broker_url
        # The consumer offset. A consumer offset is a timestamp that indicates when the SDK client consumes the first data record. The value is a UNIX timestamp.
        self.init_check_point = init_check_point
        # The password of the consumer group.
        self.password = password
        # The ID of the consumer group.
        self.sid = sid
        # The task ID.
        self.task_id = task_id
        # The topic to which you want to subscribe by using the data subscription channel.
        self.topic = topic
        # The username of the consumer group.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateEventStreamingRequestSourceSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id
        # The network. Default value: Default. The value PublicNetwork specifies a virtual private cloud (VPC).
        self.network = network
        # The offset.
        self.offset_reset = offset_reset
        # The ID of the region where the Message Queue for Apache Kafka instance resides.
        self.region_id = region_id
        # The ID of the security group to which the Message Queue for Apache Kafka instance belongs.
        self.security_group_id = security_group_id
        # The name of the topic in the Message Queue for Apache Kafka instance.
        self.topic = topic
        # The ID of the vSwitch with which the Message Queue for Apache Kafka instance is associated.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC to which the Message Queue for Apache Kafka instance belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateEventStreamingRequestSourceSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable Base64 encoding. Default value: true.
        self.is_base_64decode = is_base_64decode
        # The queue name.
        self.queue_name = queue_name
        # The ID of the region where the MNS queue resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateEventStreamingRequestSourceSourceMQTTParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The ID of the Message Queue for MQTT instance.
        self.instance_id = instance_id
        # The ID of the region where the Message Queue for MQTT resides.
        self.region_id = region_id
        # The name of the topic in the Message Queue for MQTT instance.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateEventStreamingRequestSourceSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # The ID of the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.queue_name = queue_name
        # The ID of the region where the Message Queue for RabbitMQ instance resides.
        self.region_id = region_id
        # The vhost name of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class UpdateEventStreamingRequestSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.auth_type = auth_type
        # The ID of the consumer group in the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id
        self.instance_endpoint = instance_endpoint
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.instance_id = instance_id
        self.instance_network = instance_network
        self.instance_password = instance_password
        self.instance_security_group_id = instance_security_group_id
        self.instance_type = instance_type
        self.instance_username = instance_username
        self.instance_vswitch_ids = instance_vswitch_ids
        self.instance_vpc_id = instance_vpc_id
        # The consumer offset of the message. Valid values: CONSUME_FROM_LAST_OFFSET: consumes messages from the latest offset. CONSUME_FROM_FIRST_OFFSET: consumes messages from the earliest offset. CONSUME_FROM_TIMESTAMP: consumes messages from the offset at the specified point in time. Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset
        # The ID of the region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id
        # The tags that are used to filter messages.
        self.tag = tag
        # The timestamp that indicates the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateEventStreamingRequestSourceSourceSLSParameters(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdateEventStreamingRequestSource(TeaModel):
    def __init__(
        self,
        source_dtsparameters: UpdateEventStreamingRequestSourceSourceDTSParameters = None,
        source_kafka_parameters: UpdateEventStreamingRequestSourceSourceKafkaParameters = None,
        source_mnsparameters: UpdateEventStreamingRequestSourceSourceMNSParameters = None,
        source_mqttparameters: UpdateEventStreamingRequestSourceSourceMQTTParameters = None,
        source_rabbit_mqparameters: UpdateEventStreamingRequestSourceSourceRabbitMQParameters = None,
        source_rocket_mqparameters: UpdateEventStreamingRequestSourceSourceRocketMQParameters = None,
        source_slsparameters: UpdateEventStreamingRequestSourceSourceSLSParameters = None,
    ):
        # The parameters that are configured if the event source is Data Transmission Service (DTS).
        self.source_dtsparameters = source_dtsparameters
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters = source_kafka_parameters
        # The parameters that are configured if the event source is Message Service (MNS).
        self.source_mnsparameters = source_mnsparameters
        # The parameters that are configured if the event source is Message Queue for MQTT.
        self.source_mqttparameters = source_mqttparameters
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The parameters that are configured if the event source is Log Service.
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class UpdateEventStreamingRequestTransforms(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class UpdateEventStreamingRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: UpdateEventStreamingRequestRunOptions = None,
        sink: UpdateEventStreamingRequestSink = None,
        source: UpdateEventStreamingRequestSource = None,
        transforms: List[UpdateEventStreamingRequestTransforms] = None,
    ):
        # The description of the event stream.
        self.description = description
        # The name of the event stream.
        self.event_streaming_name = event_streaming_name
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern
        # The parameters that are configured for the runtime environment.
        self.run_options = run_options
        # The event target. You must and can specify only one event target.
        self.sink = sink
        # The event source, which is also known as the event source. You must and can specify only one event source.
        self.source = source
        self.transforms = transforms

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = UpdateEventStreamingRequestRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = UpdateEventStreamingRequestSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = UpdateEventStreamingRequestSource()
            self.source = temp_model.from_map(m['Source'])
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = UpdateEventStreamingRequestTransforms()
                self.transforms.append(temp_model.from_map(k))
        return self


class UpdateEventStreamingShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options_shrink: str = None,
        sink_shrink: str = None,
        source_shrink: str = None,
        transforms_shrink: str = None,
    ):
        # The description of the event stream.
        self.description = description
        # The name of the event stream.
        self.event_streaming_name = event_streaming_name
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern
        # The parameters that are configured for the runtime environment.
        self.run_options_shrink = run_options_shrink
        # The event target. You must and can specify only one event target.
        self.sink_shrink = sink_shrink
        # The event source, which is also known as the event source. You must and can specify only one event source.
        self.source_shrink = source_shrink
        self.transforms_shrink = transforms_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options_shrink is not None:
            result['RunOptions'] = self.run_options_shrink
        if self.sink_shrink is not None:
            result['Sink'] = self.sink_shrink
        if self.source_shrink is not None:
            result['Source'] = self.source_shrink
        if self.transforms_shrink is not None:
            result['Transforms'] = self.transforms_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            self.run_options_shrink = m.get('RunOptions')
        if m.get('Sink') is not None:
            self.sink_shrink = m.get('Sink')
        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')
        if m.get('Transforms') is not None:
            self.transforms_shrink = m.get('Transforms')
        return self


class UpdateEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_name: str = None,
        status: str = None,
    ):
        # The description of the event bus.
        self.description = description
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event pattern, in JSON format. Valid values: stringEqual stringExpression Each field can have a maximum of five expressions in the map data structure.
        # 
        # Each field can have a maximum of five expressions in the map data structure.
        self.filter_pattern = filter_pattern
        # The name of the event rule.
        self.rule_name = rule_name
        # The status of the event rule. Valid values: ENABLE: The event rule is enabled. It is the default state of the event rule. DISABLE: The event rule is disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code 200 indicates that the request was successful.
        self.code = code
        # The result of the operation.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


