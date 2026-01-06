# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class GetConnectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetConnectionResponseBodyData = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.GetConnectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetConnectionResponseBodyData(DaraModel):
    def __init__(
        self,
        connections: List[main_models.GetConnectionResponseBodyDataConnections] = None,
    ):
        # The queried connections.
        self.connections = connections

    def validate(self):
        if self.connections:
            for v1 in self.connections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Connections'] = []
        if self.connections is not None:
            for k1 in self.connections:
                result['Connections'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k1 in m.get('Connections'):
                temp_model = main_models.GetConnectionResponseBodyDataConnections()
                self.connections.append(temp_model.from_map(k1))

        return self

class GetConnectionResponseBodyDataConnections(DaraModel):
    def __init__(
        self,
        auth_parameters: main_models.GetConnectionResponseBodyDataConnectionsAuthParameters = None,
        connection_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        network_parameters: main_models.GetConnectionResponseBodyDataConnectionsNetworkParameters = None,
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
            temp_model = main_models.GetConnectionResponseBodyDataConnectionsAuthParameters()
            self.auth_parameters = temp_model.from_map(m.get('AuthParameters'))

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NetworkParameters') is not None:
            temp_model = main_models.GetConnectionResponseBodyDataConnectionsNetworkParameters()
            self.network_parameters = temp_model.from_map(m.get('NetworkParameters'))

        return self

class GetConnectionResponseBodyDataConnectionsNetworkParameters(DaraModel):
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

class GetConnectionResponseBodyDataConnectionsAuthParameters(DaraModel):
    def __init__(
        self,
        api_key_auth_parameters: main_models.GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters = None,
        authorization_type: str = None,
        basic_auth_parameters: main_models.GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters = None,
        oauth_parameters: main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters = None,
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
            temp_model = main_models.GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m.get('ApiKeyAuthParameters'))

        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')

        if m.get('BasicAuthParameters') is not None:
            temp_model = main_models.GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m.get('BasicAuthParameters'))

        if m.get('OAuthParameters') is not None:
            temp_model = main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m.get('OAuthParameters'))

        return self

class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_parameters: main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters = None,
        http_method: str = None,
        oauth_http_parameters: main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters = None,
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
            temp_model = main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m.get('ClientParameters'))

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('OAuthHttpParameters') is not None:
            temp_model = main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m.get('OAuthHttpParameters'))

        return self

class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters(DaraModel):
    def __init__(
        self,
        body_parameters: List[main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters] = None,
        header_parameters: List[main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters] = None,
        query_string_parameters: List[main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters] = None,
    ):
        # The information about the request body.
        self.body_parameters = body_parameters
        # The information about the request header.
        self.header_parameters = header_parameters
        # The information about the request path.
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
                temp_model = main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k1))

        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k1 in m.get('HeaderParameters'):
                temp_model = main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k1))

        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k1 in m.get('QueryStringParameters'):
                temp_model = main_models.GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k1))

        return self

class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(DaraModel):
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

class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(DaraModel):
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

class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(DaraModel):
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

class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters(DaraModel):
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

class GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters(DaraModel):
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

class GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters(DaraModel):
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

