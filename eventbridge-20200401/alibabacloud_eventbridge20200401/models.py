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
        self.endpoint = endpoint
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
        invocation_rate_limit_per_second: int = None,
    ):
        self.api_destination_name = api_destination_name
        self.connection_name = connection_name
        self.description = description
        self.http_api_parameters = http_api_parameters
        self.invocation_rate_limit_per_second = invocation_rate_limit_per_second

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
        if self.invocation_rate_limit_per_second is not None:
            result['InvocationRateLimitPerSecond'] = self.invocation_rate_limit_per_second
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
        if m.get('InvocationRateLimitPerSecond') is not None:
            self.invocation_rate_limit_per_second = m.get('InvocationRateLimitPerSecond')
        return self


class CreateApiDestinationShrinkRequest(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        http_api_parameters_shrink: str = None,
        invocation_rate_limit_per_second: int = None,
    ):
        self.api_destination_name = api_destination_name
        self.connection_name = connection_name
        self.description = description
        self.http_api_parameters_shrink = http_api_parameters_shrink
        self.invocation_rate_limit_per_second = invocation_rate_limit_per_second

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
        if self.invocation_rate_limit_per_second is not None:
            result['InvocationRateLimitPerSecond'] = self.invocation_rate_limit_per_second
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
        if m.get('InvocationRateLimitPerSecond') is not None:
            self.invocation_rate_limit_per_second = m.get('InvocationRateLimitPerSecond')
        return self


class CreateApiDestinationResponseBodyDate(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
    ):
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
        self.code = code
        self.date = date
        self.message = message
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
        self.api_key_name = api_key_name
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
        self.password = password
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


class CreateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateConnectionRequestAuthParametersInvocationHttpParameters(TeaModel):
    def __init__(
        self,
        body_parameters: List[CreateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters] = None,
        header_parameters: List[CreateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters] = None,
        query_string_parameters: List[CreateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters] = None,
    ):
        self.body_parameters = body_parameters
        self.header_parameters = header_parameters
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
                temp_model = CreateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = CreateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = CreateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class CreateConnectionRequestAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        self.client_id = client_id
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.body_parameters = body_parameters
        self.header_parameters = header_parameters
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
        self.authorization_endpoint = authorization_endpoint
        self.client_parameters = client_parameters
        self.http_method = http_method
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
        invocation_http_parameters: CreateConnectionRequestAuthParametersInvocationHttpParameters = None,
        oauth_parameters: CreateConnectionRequestAuthParametersOAuthParameters = None,
    ):
        self.api_key_auth_parameters = api_key_auth_parameters
        self.authorization_type = authorization_type
        self.basic_auth_parameters = basic_auth_parameters
        self.invocation_http_parameters = invocation_http_parameters
        self.oauth_parameters = oauth_parameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.invocation_http_parameters:
            self.invocation_http_parameters.validate()
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
        if self.invocation_http_parameters is not None:
            result['InvocationHttpParameters'] = self.invocation_http_parameters.to_map()
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
        if m.get('InvocationHttpParameters') is not None:
            temp_model = CreateConnectionRequestAuthParametersInvocationHttpParameters()
            self.invocation_http_parameters = temp_model.from_map(m['InvocationHttpParameters'])
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
        self.network_type = network_type
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
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
        self.auth_parameters = auth_parameters
        self.connection_name = connection_name
        self.description = description
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
        self.auth_parameters_shrink = auth_parameters_shrink
        self.connection_name = connection_name
        self.description = description
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
        self.code = code
        self.data = data
        self.message = message
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
        self.description = description
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
        self.ip = ip
        self.method = method
        self.referer = referer
        self.security_config = security_config
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


class CreateEventSourceRequestSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: str = None,
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


class CreateEventSourceRequestSourceRabbitMQParameters(TeaModel):
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


class CreateEventSourceRequestSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: float = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
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
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        self.consume_position = consume_position
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


class CreateEventSourceRequest(TeaModel):
    def __init__(
        self,
        description: bytes = None,
        event_bus_name: bytes = None,
        event_source_name: bytes = None,
        source_http_event_parameters: CreateEventSourceRequestSourceHttpEventParameters = None,
        source_mnsparameters: CreateEventSourceRequestSourceMNSParameters = None,
        source_rabbit_mqparameters: CreateEventSourceRequestSourceRabbitMQParameters = None,
        source_rocket_mqparameters: CreateEventSourceRequestSourceRocketMQParameters = None,
        source_slsparameters: CreateEventSourceRequestSourceSLSParameters = None,
    ):
        # 事件源描述详情
        self.description = description
        self.event_bus_name = event_bus_name
        # 事件源英文Code
        self.event_source_name = event_source_name
        self.source_http_event_parameters = source_http_event_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # SourceSLSParameters
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
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
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
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
        return self


class CreateEventSourceShrinkRequest(TeaModel):
    def __init__(
        self,
        description: bytes = None,
        event_bus_name: bytes = None,
        event_source_name: bytes = None,
        source_http_event_parameters_shrink: str = None,
        source_mnsparameters_shrink: str = None,
        source_rabbit_mqparameters_shrink: str = None,
        source_rocket_mqparameters_shrink: str = None,
        source_slsparameters_shrink: str = None,
    ):
        # 事件源描述详情
        self.description = description
        self.event_bus_name = event_bus_name
        # 事件源英文Code
        self.event_source_name = event_source_name
        self.source_http_event_parameters_shrink = source_http_event_parameters_shrink
        self.source_mnsparameters_shrink = source_mnsparameters_shrink
        self.source_rabbit_mqparameters_shrink = source_rabbit_mqparameters_shrink
        self.source_rocket_mqparameters_shrink = source_rocket_mqparameters_shrink
        # SourceSLSParameters
        self.source_slsparameters_shrink = source_slsparameters_shrink

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
        if self.source_mnsparameters_shrink is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters_shrink
        if self.source_rabbit_mqparameters_shrink is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters_shrink
        if self.source_rocket_mqparameters_shrink is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters_shrink
        if self.source_slsparameters_shrink is not None:
            result['SourceSLSParameters'] = self.source_slsparameters_shrink
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
        if m.get('SourceMNSParameters') is not None:
            self.source_mnsparameters_shrink = m.get('SourceMNSParameters')
        if m.get('SourceRabbitMQParameters') is not None:
            self.source_rabbit_mqparameters_shrink = m.get('SourceRabbitMQParameters')
        if m.get('SourceRocketMQParameters') is not None:
            self.source_rocket_mqparameters_shrink = m.get('SourceRocketMQParameters')
        if m.get('SourceSLSParameters') is not None:
            self.source_slsparameters_shrink = m.get('SourceSLSParameters')
        return self


class CreateEventSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        event_source_arn: str = None,
    ):
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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


class CreateEventStreamingRequestRunOptionsDeadLetterQueue(TeaModel):
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


class CreateEventStreamingRequestRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: int = None,
        maximum_retry_attempts: int = None,
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


class CreateEventStreamingRequestRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: CreateEventStreamingRequestRunOptionsBatchWindow = None,
        dead_letter_queue: CreateEventStreamingRequestRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: CreateEventStreamingRequestRunOptionsRetryStrategy = None,
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


class CreateEventStreamingRequestSinkSinkDataHubParametersProject(TeaModel):
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


class CreateEventStreamingRequestSinkSinkDataHubParametersRoleName(TeaModel):
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


class CreateEventStreamingRequestSinkSinkDataHubParametersTopic(TeaModel):
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


class CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema(TeaModel):
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


class CreateEventStreamingRequestSinkSinkDataHubParametersTopicType(TeaModel):
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
        self.body = body
        self.project = project
        self.role_name = role_name
        self.topic = topic
        self.topic_schema = topic_schema
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


class CreateEventStreamingRequestSinkSinkFcParametersFunctionName(TeaModel):
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


class CreateEventStreamingRequestSinkSinkFcParametersInvocationType(TeaModel):
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


class CreateEventStreamingRequestSinkSinkFcParametersQualifier(TeaModel):
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


class CreateEventStreamingRequestSinkSinkFcParametersServiceName(TeaModel):
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


class CreateEventStreamingRequestSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkFcParametersBody = None,
        function_name: CreateEventStreamingRequestSinkSinkFcParametersFunctionName = None,
        invocation_type: CreateEventStreamingRequestSinkSinkFcParametersInvocationType = None,
        qualifier: CreateEventStreamingRequestSinkSinkFcParametersQualifier = None,
        service_name: CreateEventStreamingRequestSinkSinkFcParametersServiceName = None,
    ):
        self.body = body
        self.function_name = function_name
        self.invocation_type = invocation_type
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
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


class CreateEventStreamingRequestSinkSinkKafkaParametersAcks(TeaModel):
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


class CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId(TeaModel):
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


class CreateEventStreamingRequestSinkSinkKafkaParametersKey(TeaModel):
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


class CreateEventStreamingRequestSinkSinkKafkaParametersTopic(TeaModel):
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


class CreateEventStreamingRequestSinkSinkKafkaParametersValue(TeaModel):
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


class CreateEventStreamingRequestSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: CreateEventStreamingRequestSinkSinkKafkaParametersAcks = None,
        instance_id: CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId = None,
        key: CreateEventStreamingRequestSinkSinkKafkaParametersKey = None,
        topic: CreateEventStreamingRequestSinkSinkKafkaParametersTopic = None,
        value: CreateEventStreamingRequestSinkSinkKafkaParametersValue = None,
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


class CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(TeaModel):
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


class CreateEventStreamingRequestSinkSinkMNSParametersQueueName(TeaModel):
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


class CreateEventStreamingRequestSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkMNSParametersBody = None,
        is_base_64encode: CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: CreateEventStreamingRequestSinkSinkMNSParametersQueueName = None,
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


class CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersKeys(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersProperties(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersTags(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersTopic(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds(TeaModel):
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


class CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId(TeaModel):
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
        self.body = body
        self.instance_endpoint = instance_endpoint
        self.instance_id = instance_id
        self.instance_password = instance_password
        self.instance_type = instance_type
        self.instance_username = instance_username
        self.keys = keys
        self.network = network
        self.properties = properties
        self.security_group_id = security_group_id
        self.tags = tags
        self.topic = topic
        self.v_switch_ids = v_switch_ids
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


class CreateEventStreamingRequestSinkSinkSLSParametersLogStore(TeaModel):
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


class CreateEventStreamingRequestSinkSinkSLSParametersProject(TeaModel):
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


class CreateEventStreamingRequestSinkSinkSLSParametersRoleName(TeaModel):
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


class CreateEventStreamingRequestSinkSinkSLSParametersTopic(TeaModel):
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


class CreateEventStreamingRequestSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkSLSParametersBody = None,
        log_store: CreateEventStreamingRequestSinkSinkSLSParametersLogStore = None,
        project: CreateEventStreamingRequestSinkSinkSLSParametersProject = None,
        role_name: CreateEventStreamingRequestSinkSinkSLSParametersRoleName = None,
        topic: CreateEventStreamingRequestSinkSinkSLSParametersTopic = None,
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
        sink_kafka_parameters: CreateEventStreamingRequestSinkSinkKafkaParameters = None,
        sink_mnsparameters: CreateEventStreamingRequestSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: CreateEventStreamingRequestSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: CreateEventStreamingRequestSinkSinkRocketMQParameters = None,
        sink_slsparameters: CreateEventStreamingRequestSinkSinkSLSParameters = None,
    ):
        self.sink_data_hub_parameters = sink_data_hub_parameters
        self.sink_fc_parameters = sink_fc_parameters
        self.sink_kafka_parameters = sink_kafka_parameters
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        # Sink RocketMQ Parameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        # Sink SLS Parameters
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_data_hub_parameters:
            self.sink_data_hub_parameters.validate()
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
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
        self.consumer_group = consumer_group
        self.instance_id = instance_id
        self.network = network
        self.offset_reset = offset_reset
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        # VPC ID。
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


class CreateEventStreamingRequestSourceSourceMQTTParameters(TeaModel):
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


class CreateEventStreamingRequestSourceSourceRabbitMQParameters(TeaModel):
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
        self.auth_type = auth_type
        self.filter_sql = filter_sql
        self.filter_type = filter_type
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
        self.network = network
        self.offset = offset
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.tag = tag
        self.timestamp = timestamp
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
        self.consume_position = consume_position
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
        self.source_dtsparameters = source_dtsparameters
        self.source_kafka_parameters = source_kafka_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_mqttparameters = source_mqttparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
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


class CreateEventStreamingRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: CreateEventStreamingRequestRunOptions = None,
        sink: CreateEventStreamingRequestSink = None,
        source: CreateEventStreamingRequestSource = None,
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options = run_options
        self.sink = sink
        self.source = source

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()

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
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options_shrink = run_options_shrink
        self.sink_shrink = sink_shrink
        self.source_shrink = source_shrink

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
        return self


class CreateEventStreamingResponseBodyData(TeaModel):
    def __init__(
        self,
        event_streaming_arn: str = None,
    ):
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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


class CreateRuleRequestEventTargets(TeaModel):
    def __init__(
        self,
        dead_letter_queue: CreateRuleRequestEventTargetsDeadLetterQueue = None,
        endpoint: str = None,
        id: str = None,
        param_list: List[CreateRuleRequestEventTargetsParamList] = None,
        push_retry_strategy: str = None,
        type: str = None,
    ):
        self.dead_letter_queue = dead_letter_queue
        self.endpoint = endpoint
        self.id = id
        self.param_list = param_list
        self.push_retry_strategy = push_retry_strategy
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
        self.description = description
        self.event_bus_name = event_bus_name
        self.event_targets = event_targets
        self.filter_pattern = filter_pattern
        self.rule_name = rule_name
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
        self.description = description
        self.event_bus_name = event_bus_name
        self.event_targets_shrink = event_targets_shrink
        self.filter_pattern = filter_pattern
        self.rule_name = rule_name
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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


class CreateTargetsRequestTargetsParamList(TeaModel):
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


class CreateTargetsRequestTargets(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        id: str = None,
        param_list: List[CreateTargetsRequestTargetsParamList] = None,
        push_retry_strategy: str = None,
        type: str = None,
    ):
        self.endpoint = endpoint
        self.id = id
        self.param_list = param_list
        self.push_retry_strategy = push_retry_strategy
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
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = CreateTargetsRequestTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTargetsRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        targets: List[CreateTargetsRequestTargets] = None,
    ):
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name
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
                temp_model = CreateTargetsRequestTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class CreateTargetsShrinkRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        targets_shrink: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name
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


class CreateTargetsResponseBodyDataErrorEntries(TeaModel):
    def __init__(
        self,
        entry_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.entry_id = entry_id
        self.error_code = error_code
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


class CreateTargetsResponseBodyData(TeaModel):
    def __init__(
        self,
        error_entries: List[CreateTargetsResponseBodyDataErrorEntries] = None,
        error_entries_count: int = None,
    ):
        self.error_entries = error_entries
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
                temp_model = CreateTargetsResponseBodyDataErrorEntries()
                self.error_entries.append(temp_model.from_map(k))
        if m.get('ErrorEntriesCount') is not None:
            self.error_entries_count = m.get('ErrorEntriesCount')
        return self


class CreateTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = CreateTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTargetsResponseBody = None,
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
            temp_model = CreateTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiDestinationRequest(TeaModel):
    def __init__(
        self,
        api_destination_name: str = None,
        client_token: str = None,
    ):
        self.api_destination_name = api_destination_name
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteApiDestinationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
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
        self.code = code
        self.message = message
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        # 事件源ID
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.event_bus_name = event_bus_name
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name
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
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name
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
        self.entry_id = entry_id
        self.error_code = error_code
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
        self.error_entries = error_entries
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
        self.event_bus_name = event_bus_name
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.event_bus_name = event_bus_name
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        client_token: str = None,
    ):
        self.api_destination_name = api_destination_name
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class GetApiDestinationResponseBodyDataHttpApiParameters(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        method: str = None,
    ):
        self.endpoint = endpoint
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
        self.api_destination_name = api_destination_name
        self.connection_name = connection_name
        self.description = description
        self.gmt_create = gmt_create
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
        self.code = code
        self.data = data
        self.message = message
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
        self.api_key_name = api_key_name
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
        self.password = password
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


class GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParametersBodyParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        valu_valuee: str = None,
    ):
        self.key = key
        self.valu_valuee = valu_valuee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.valu_valuee is not None:
            result['ValuValuee'] = self.valu_valuee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ValuValuee') is not None:
            self.valu_valuee = m.get('ValuValuee')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParametersHeaderParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParametersQueryStringParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParameters(TeaModel):
    def __init__(
        self,
        body_parameters: List[GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParametersBodyParameters] = None,
        header_parameters: List[GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParametersHeaderParameters] = None,
        query_string_parameters: List[GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParametersQueryStringParameters] = None,
    ):
        self.body_parameters = body_parameters
        self.header_parameters = header_parameters
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
                temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        self.client_id = client_id
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.body_parameters = body_parameters
        self.header_parameters = header_parameters
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
        self.authorization_endpoint = authorization_endpoint
        self.client_parameters = client_parameters
        self.http_method = http_method
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
        invocation_http_parameters: GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParameters = None,
        oauth_parameters: GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters = None,
    ):
        self.api_key_auth_parameters = api_key_auth_parameters
        self.authorization_type = authorization_type
        self.basic_auth_parameters = basic_auth_parameters
        self.invocation_http_parameters = invocation_http_parameters
        self.oauth_parameters = oauth_parameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.invocation_http_parameters:
            self.invocation_http_parameters.validate()
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
        if self.invocation_http_parameters is not None:
            result['InvocationHttpParameters'] = self.invocation_http_parameters.to_map()
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
        if m.get('InvocationHttpParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersInvocationHttpParameters()
            self.invocation_http_parameters = temp_model.from_map(m['InvocationHttpParameters'])
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
        self.network_type = network_type
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
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
        api_destination_name: str = None,
        auth_parameters: GetConnectionResponseBodyDataConnectionsAuthParameters = None,
        connection_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        network_parameters: GetConnectionResponseBodyDataConnectionsNetworkParameters = None,
    ):
        self.api_destination_name = api_destination_name
        self.auth_parameters = auth_parameters
        self.connection_name = connection_name
        self.description = description
        self.gmt_create = gmt_create
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
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
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
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
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
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetConnectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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
        self.create_timestamp = create_timestamp
        self.description = description
        self.event_bus_arn = event_bus_arn
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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


class GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue(TeaModel):
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


class GetEventStreamingResponseBodyDataRunOptionsRetryStrategy(TeaModel):
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


class GetEventStreamingResponseBodyDataRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: GetEventStreamingResponseBodyDataRunOptionsBatchWindow = None,
        dead_letter_queue: GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: GetEventStreamingResponseBodyDataRunOptionsRetryStrategy = None,
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


class GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkFcParametersBody = None,
        function_name: GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName = None,
        invocation_type: GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType = None,
        qualifier: GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier = None,
        service_name: GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName = None,
    ):
        self.body = body
        self.function_name = function_name
        self.invocation_type = invocation_type
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
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


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks = None,
        instance_id: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId = None,
        key: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey = None,
        topic: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic = None,
        value: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue = None,
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


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody = None,
        is_base_64encode: GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName = None,
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


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic(TeaModel):
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


class GetEventStreamingResponseBodyDataSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody = None,
        log_store: GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore = None,
        project: GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject = None,
        role_name: GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName = None,
        topic: GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic = None,
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
        sink_kafka_parameters: GetEventStreamingResponseBodyDataSinkSinkKafkaParameters = None,
        sink_mnsparameters: GetEventStreamingResponseBodyDataSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters = None,
        sink_slsparameters: GetEventStreamingResponseBodyDataSinkSinkSLSParameters = None,
    ):
        self.sink_fc_parameters = sink_fc_parameters
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
        self.consumer_group = consumer_group
        self.instance_id = instance_id
        self.network = network
        self.offset_reset = offset_reset
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        # VPC ID。
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


class GetEventStreamingResponseBodyDataSourceSourceMQTTParameters(TeaModel):
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


class GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters(TeaModel):
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


class GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
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
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options = run_options
        self.sink = sink
        self.source = source
        self.status = status

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()

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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
        self.event_bus_name = event_bus_name
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
        # TEMPLATE
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


class GetRuleResponseBodyDataTargets(TeaModel):
    def __init__(
        self,
        dead_letter_queue: GetRuleResponseBodyDataTargetsDeadLetterQueue = None,
        detail_map: Dict[str, Any] = None,
        endpoint: str = None,
        id: str = None,
        param_list: List[GetRuleResponseBodyDataTargetsParamList] = None,
        push_retry_strategy: str = None,
        push_selector: str = None,
        type: str = None,
    ):
        self.dead_letter_queue = dead_letter_queue
        self.detail_map = detail_map
        self.endpoint = endpoint
        self.id = id
        self.param_list = param_list
        self.push_retry_strategy = push_retry_strategy
        self.push_selector = push_selector
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
        self.created_timestamp = created_timestamp
        self.description = description
        self.event_bus_name = event_bus_name
        self.filter_pattern = filter_pattern
        self.rule_arn = rule_arn
        self.rule_name = rule_name
        self.status = status
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
        self.event_source_name = event_source_name
        self.group_name = group_name
        self.name = name
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
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.arn = arn
        self.ctime = ctime
        self.description = description
        self.event_bus_name = event_bus_name
        self.event_types = event_types
        self.name = name
        self.status = status
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
        client_token: str = None,
        description: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.api_destination_name_prefix = api_destination_name_prefix
        self.client_token = client_token
        self.description = description
        self.max_results = max_results
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationNamePrefix') is not None:
            self.api_destination_name_prefix = m.get('ApiDestinationNamePrefix')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
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
        self.endpoint = endpoint
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
        self.api_destination_name = api_destination_name
        self.connection_name = connection_name
        self.description = description
        self.gmt_create = gmt_create
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
    ):
        self.api_destinations = api_destinations

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_destinations = []
        if m.get('ApiDestinations') is not None:
            for k in m.get('ApiDestinations'):
                temp_model = ListApiDestinationsResponseBodyDataApiDestinations()
                self.api_destinations.append(temp_model.from_map(k))
        return self


class ListApiDestinationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListApiDestinationsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        self.connection_name_prefix = connection_name_prefix
        self.max_results = max_results
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
        self.api_key_name = api_key_name
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
        self.password = password
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


class ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParametersBodyParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParametersHeaderParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParametersQueryStringParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParameters(TeaModel):
    def __init__(
        self,
        body_parameters: List[ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParametersBodyParameters] = None,
        header_parameters: List[ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParametersHeaderParameters] = None,
        query_string_parameters: List[ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParametersQueryStringParameters] = None,
    ):
        self.body_parameters = body_parameters
        self.header_parameters = header_parameters
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
                temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        self.client_id = client_id
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.body_parameters = body_parameters
        self.header_parameters = header_parameters
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
        self.authorization_endpoint = authorization_endpoint
        self.client_parameters = client_parameters
        self.http_method = http_method
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
        invocation_http_parameters: ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParameters = None,
        oauth_parameters: ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParameters = None,
    ):
        self.api_key_auth_parameters = api_key_auth_parameters
        self.authorization_type = authorization_type
        self.basic_auth_parameters = basic_auth_parameters
        self.invocation_http_parameters = invocation_http_parameters
        self.oauth_parameters = oauth_parameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.invocation_http_parameters:
            self.invocation_http_parameters.validate()
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
        if self.invocation_http_parameters is not None:
            result['InvocationHttpParameters'] = self.invocation_http_parameters.to_map()
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
        if m.get('InvocationHttpParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersInvocationHttpParameters()
            self.invocation_http_parameters = temp_model.from_map(m['InvocationHttpParameters'])
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
        self.network_type = network_type
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
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
        api_destination_name: str = None,
        auth_parameters: ListConnectionsResponseBodyDataConnectionsAuthParameters = None,
        connection_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        network_parameters: ListConnectionsResponseBodyDataConnectionsNetworkParameters = None,
    ):
        self.api_destination_name = api_destination_name
        self.auth_parameters = auth_parameters
        self.connection_name = connection_name
        self.description = description
        self.gmt_create = gmt_create
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
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
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
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
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
        self.connections = connections
        self.max_results = max_results
        self.next_token = next_token
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
        self.code = code
        self.data = data
        self.message = message
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
        self.limit = limit
        self.name_prefix = name_prefix
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
        self.create_timestamp = create_timestamp
        self.description = description
        self.event_bus_arn = event_bus_arn
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
        self.event_buses = event_buses
        self.next_token = next_token
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
    ):
        self.limit = limit
        self.name_prefix = name_prefix
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
        function_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName = None,
        invocation_type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType = None,
        qualifier: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier = None,
        service_name: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName = None,
    ):
        self.body = body
        self.function_name = function_name
        self.invocation_type = invocation_type
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
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
        sink_kafka_parameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters = None,
        sink_mnsparameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters = None,
        sink_slsparameters: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters = None,
    ):
        self.sink_fc_parameters = sink_fc_parameters
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
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
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
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options = run_options
        self.sink = sink
        self.source = source
        self.status = status

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()

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
        return self


class ListEventStreamingsResponseBodyData(TeaModel):
    def __init__(
        self,
        event_streamings: List[ListEventStreamingsResponseBodyDataEventStreamings] = None,
        next_token: str = None,
        total: int = None,
    ):
        self.event_streamings = event_streamings
        self.next_token = next_token
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
        self.event_bus_name = event_bus_name
        self.limit = limit
        self.next_token = next_token
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
        id: str = None,
        push_selector: str = None,
        type: str = None,
    ):
        self.endpoint = endpoint
        self.id = id
        self.push_selector = push_selector
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
        self.created_timestamp = created_timestamp
        self.description = description
        self.detail_map = detail_map
        self.event_bus_name = event_bus_name
        self.filter_pattern = filter_pattern
        self.rule_arn = rule_arn
        self.rule_name = rule_name
        self.status = status
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
        self.next_token = next_token
        self.rules = rules
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters(TeaModel):
    def __init__(
        self,
        ip: List[str] = None,
        method: List[str] = None,
        referer: List[str] = None,
        security_config: str = None,
        type: str = None,
    ):
        self.ip = ip
        self.method = method
        self.referer = referer
        self.security_config = security_config
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


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters(TeaModel):
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


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters(TeaModel):
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


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: float = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
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
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        self.consume_position = consume_position
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


class ListUserDefinedEventSourcesResponseBodyDataEventSourceList(TeaModel):
    def __init__(
        self,
        arn: str = None,
        ctime: float = None,
        event_bus_name: str = None,
        external_source_type: str = None,
        name: str = None,
        source_http_event_parameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters = None,
        source_mnsparameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters = None,
        source_rabbit_mqparameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters = None,
        source_rocket_mqparameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters = None,
        source_slsparameters: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters = None,
        status: str = None,
        type: str = None,
    ):
        self.arn = arn
        self.ctime = ctime
        self.event_bus_name = event_bus_name
        self.external_source_type = external_source_type
        self.name = name
        self.source_http_event_parameters = source_http_event_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # SourceSLSParameters
        self.source_slsparameters = source_slsparameters
        self.status = status
        self.type = type

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
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
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
        self.code = code
        self.message = message
        self.request_id = request_id
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


class StartEventStreamingRequest(TeaModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
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
        self.code = code
        self.message = message
        self.request_id = request_id
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


class UpdateApiDestinationRequestHttpApiParameters(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        method: str = None,
    ):
        self.endpoint = endpoint
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
        client_token: str = None,
        connection_name: str = None,
        description: str = None,
        http_api_parameters: UpdateApiDestinationRequestHttpApiParameters = None,
    ):
        self.api_destination_name = api_destination_name
        self.client_token = client_token
        self.connection_name = connection_name
        self.description = description
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        client_token: str = None,
        connection_name: str = None,
        description: str = None,
        http_api_parameters_shrink: str = None,
    ):
        self.api_destination_name = api_destination_name
        self.client_token = client_token
        self.connection_name = connection_name
        self.description = description
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        self.code = code
        self.message = message
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
        self.api_key_name = api_key_name
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
        self.password = password
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


class UpdateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateConnectionRequestAuthParametersInvocationHttpParameters(TeaModel):
    def __init__(
        self,
        body_parameters: List[UpdateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters] = None,
        header_parameters: List[UpdateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters] = None,
        query_string_parameters: List[UpdateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters] = None,
    ):
        self.body_parameters = body_parameters
        self.header_parameters = header_parameters
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
                temp_model = UpdateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = UpdateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = UpdateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class UpdateConnectionRequestAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        self.client_id = client_id
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.is_value_secret = is_value_secret
        self.key = key
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
        self.body_parameters = body_parameters
        self.header_parameters = header_parameters
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
        self.authorization_endpoint = authorization_endpoint
        self.client_parameters = client_parameters
        self.http_method = http_method
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
        invocation_http_parameters: UpdateConnectionRequestAuthParametersInvocationHttpParameters = None,
        oauth_parameters: UpdateConnectionRequestAuthParametersOAuthParameters = None,
    ):
        self.api_key_auth_parameters = api_key_auth_parameters
        self.authorization_type = authorization_type
        self.basic_auth_parameters = basic_auth_parameters
        self.invocation_http_parameters = invocation_http_parameters
        self.oauth_parameters = oauth_parameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.invocation_http_parameters:
            self.invocation_http_parameters.validate()
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
        if self.invocation_http_parameters is not None:
            result['InvocationHttpParameters'] = self.invocation_http_parameters.to_map()
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
        if m.get('InvocationHttpParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParametersInvocationHttpParameters()
            self.invocation_http_parameters = temp_model.from_map(m['InvocationHttpParameters'])
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
        self.network_type = network_type
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
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
        self.auth_parameters = auth_parameters
        self.connection_name = connection_name
        self.description = description
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
        self.auth_parameters_shrink = auth_parameters_shrink
        self.connection_name = connection_name
        self.description = description
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
        self.code = code
        self.message = message
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
        self.description = description
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.ip = ip
        self.method = method
        self.referer = referer
        self.security_config = security_config
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


class UpdateEventSourceRequestSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: str = None,
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


class UpdateEventSourceRequestSourceRabbitMQParameters(TeaModel):
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


class UpdateEventSourceRequestSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: float = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
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
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        self.consume_position = consume_position
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


class UpdateEventSourceRequest(TeaModel):
    def __init__(
        self,
        description: bytes = None,
        event_bus_name: bytes = None,
        event_source_name: bytes = None,
        source_http_event_parameters: UpdateEventSourceRequestSourceHttpEventParameters = None,
        source_mnsparameters: UpdateEventSourceRequestSourceMNSParameters = None,
        source_rabbit_mqparameters: UpdateEventSourceRequestSourceRabbitMQParameters = None,
        source_rocket_mqparameters: UpdateEventSourceRequestSourceRocketMQParameters = None,
        source_slsparameters: UpdateEventSourceRequestSourceSLSParameters = None,
    ):
        # 事件源描述详情
        self.description = description
        self.event_bus_name = event_bus_name
        # 事件源英文Code
        self.event_source_name = event_source_name
        self.source_http_event_parameters = source_http_event_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # SourceSLSParameters
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
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
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
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
        return self


class UpdateEventSourceShrinkRequest(TeaModel):
    def __init__(
        self,
        description: bytes = None,
        event_bus_name: bytes = None,
        event_source_name: bytes = None,
        source_http_event_parameters_shrink: str = None,
        source_mnsparameters_shrink: str = None,
        source_rabbit_mqparameters_shrink: str = None,
        source_rocket_mqparameters_shrink: str = None,
        source_slsparameters_shrink: str = None,
    ):
        # 事件源描述详情
        self.description = description
        self.event_bus_name = event_bus_name
        # 事件源英文Code
        self.event_source_name = event_source_name
        self.source_http_event_parameters_shrink = source_http_event_parameters_shrink
        self.source_mnsparameters_shrink = source_mnsparameters_shrink
        self.source_rabbit_mqparameters_shrink = source_rabbit_mqparameters_shrink
        self.source_rocket_mqparameters_shrink = source_rocket_mqparameters_shrink
        # SourceSLSParameters
        self.source_slsparameters_shrink = source_slsparameters_shrink

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
        if self.source_mnsparameters_shrink is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters_shrink
        if self.source_rabbit_mqparameters_shrink is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters_shrink
        if self.source_rocket_mqparameters_shrink is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters_shrink
        if self.source_slsparameters_shrink is not None:
            result['SourceSLSParameters'] = self.source_slsparameters_shrink
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
        if m.get('SourceMNSParameters') is not None:
            self.source_mnsparameters_shrink = m.get('SourceMNSParameters')
        if m.get('SourceRabbitMQParameters') is not None:
            self.source_rabbit_mqparameters_shrink = m.get('SourceRabbitMQParameters')
        if m.get('SourceRocketMQParameters') is not None:
            self.source_rocket_mqparameters_shrink = m.get('SourceRocketMQParameters')
        if m.get('SourceSLSParameters') is not None:
            self.source_slsparameters_shrink = m.get('SourceSLSParameters')
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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


class UpdateEventStreamingRequestRunOptionsDeadLetterQueue(TeaModel):
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


class UpdateEventStreamingRequestRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: int = None,
        maximum_retry_attempts: int = None,
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


class UpdateEventStreamingRequestRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: UpdateEventStreamingRequestRunOptionsBatchWindow = None,
        dead_letter_queue: UpdateEventStreamingRequestRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: UpdateEventStreamingRequestRunOptionsRetryStrategy = None,
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


class UpdateEventStreamingRequestSinkSinkFcParametersFunctionName(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkFcParametersInvocationType(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkFcParametersQualifier(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkFcParametersServiceName(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkFcParametersBody = None,
        function_name: UpdateEventStreamingRequestSinkSinkFcParametersFunctionName = None,
        invocation_type: UpdateEventStreamingRequestSinkSinkFcParametersInvocationType = None,
        qualifier: UpdateEventStreamingRequestSinkSinkFcParametersQualifier = None,
        service_name: UpdateEventStreamingRequestSinkSinkFcParametersServiceName = None,
    ):
        self.body = body
        self.function_name = function_name
        self.invocation_type = invocation_type
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
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


class UpdateEventStreamingRequestSinkSinkKafkaParametersAcks(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkKafkaParametersKey(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkKafkaParametersTopic(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkKafkaParametersValue(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: UpdateEventStreamingRequestSinkSinkKafkaParametersAcks = None,
        instance_id: UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId = None,
        key: UpdateEventStreamingRequestSinkSinkKafkaParametersKey = None,
        topic: UpdateEventStreamingRequestSinkSinkKafkaParametersTopic = None,
        value: UpdateEventStreamingRequestSinkSinkKafkaParametersValue = None,
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


class UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkMNSParametersQueueName(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkMNSParametersBody = None,
        is_base_64encode: UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: UpdateEventStreamingRequestSinkSinkMNSParametersQueueName = None,
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


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRocketMQParametersTags(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkSLSParametersLogStore(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkSLSParametersProject(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkSLSParametersRoleName(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkSLSParametersTopic(TeaModel):
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


class UpdateEventStreamingRequestSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkSLSParametersBody = None,
        log_store: UpdateEventStreamingRequestSinkSinkSLSParametersLogStore = None,
        project: UpdateEventStreamingRequestSinkSinkSLSParametersProject = None,
        role_name: UpdateEventStreamingRequestSinkSinkSLSParametersRoleName = None,
        topic: UpdateEventStreamingRequestSinkSinkSLSParametersTopic = None,
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
        sink_kafka_parameters: UpdateEventStreamingRequestSinkSinkKafkaParameters = None,
        sink_mnsparameters: UpdateEventStreamingRequestSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: UpdateEventStreamingRequestSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: UpdateEventStreamingRequestSinkSinkRocketMQParameters = None,
        sink_slsparameters: UpdateEventStreamingRequestSinkSinkSLSParameters = None,
    ):
        self.sink_fc_parameters = sink_fc_parameters
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


class UpdateEventStreamingRequestSourceSourceMNSParameters(TeaModel):
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


class UpdateEventStreamingRequestSourceSourceMQTTParameters(TeaModel):
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


class UpdateEventStreamingRequestSourceSourceRabbitMQParameters(TeaModel):
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


class UpdateEventStreamingRequestSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
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
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        self.source_dtsparameters = source_dtsparameters
        self.source_kafka_parameters = source_kafka_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_mqttparameters = source_mqttparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
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


class UpdateEventStreamingRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: UpdateEventStreamingRequestRunOptions = None,
        sink: UpdateEventStreamingRequestSink = None,
        source: UpdateEventStreamingRequestSource = None,
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options = run_options
        self.sink = sink
        self.source = source

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()

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
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options_shrink = run_options_shrink
        self.sink_shrink = sink_shrink
        self.source_shrink = source_shrink

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
        return self


class UpdateEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.description = description
        self.event_bus_name = event_bus_name
        self.filter_pattern = filter_pattern
        self.rule_name = rule_name
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
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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


