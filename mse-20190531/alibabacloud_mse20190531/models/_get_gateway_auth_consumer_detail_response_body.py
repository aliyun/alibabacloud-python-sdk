# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetGatewayAuthConsumerDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetGatewayAuthConsumerDetailResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 is returned if the request is successful.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic part in the error message.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the \\*\\*%s\\*\\* variable in the **ErrMessage** parameter.
        # 
        # >  If the return value of the **ErrMessage** parameter is **The Value of Input Parameter %s is not valid** and the return value of the **DynamicMessage** parameter is **DtsJobId**, the specified **DtsJobId** parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error code that is returned.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetGatewayAuthConsumerDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetGatewayAuthConsumerDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        consumer_status: bool = None,
        description: str = None,
        encode_type: str = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        jwks: str = None,
        key_name: str = None,
        key_value: str = None,
        name: str = None,
        primary_user: str = None,
        resource_list: List[main_models.GetGatewayAuthConsumerDetailResponseBodyDataResourceList] = None,
        token_name: str = None,
        token_pass: bool = None,
        token_position: str = None,
        token_prefix: str = None,
        type: str = None,
    ):
        # The status of the consumer. Valid values:
        # 
        # *   true: enabled
        # *   false: disabled
        self.consumer_status = consumer_status
        # The description.
        self.description = description
        # The encryption type. Valid values:
        # 
        # *   RSA
        # *   OCT
        self.encode_type = encode_type
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The time when the consumer authentication record was created.
        self.gmt_create = gmt_create
        # The time when the consumer authentication record was modified.
        self.gmt_modified = gmt_modified
        # The ID of the consumer.
        self.id = id
        # The JWT public key. The JSON format is supported.
        self.jwks = jwks
        # The name of the key used for JWT-based identity authentication.
        self.key_name = key_name
        # The value of the key used for JWT-based identity authentication.
        self.key_value = key_value
        # The name of the consumer.
        self.name = name
        # The creator.
        self.primary_user = primary_user
        # The resource list.
        self.resource_list = resource_list
        # The names of the parameters that are required to verify each token. By default, each token is prefixed with Bearer and stored in the Authorization header, such as `Authorization: Bearer <Content of a token>`.
        self.token_name = token_name
        # Specifies whether to enable pass-through.
        self.token_pass = token_pass
        # The positions of the parameters that are required to verify each token. By default, each token is prefixed with Bearer and stored in the Authorization header, such as `Authorization: Bearer <Content of a token>`.
        self.token_position = token_position
        # The prefixes of the parameters that are required to verify each token. By default, each token is prefixed with Bearer and stored in the Authorization header, such as `Authorization: Bearer <Content of a token>`.
        self.token_prefix = token_prefix
        # The authentication type. Valid values:
        # 
        # *   JWT
        self.type = type

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_status is not None:
            result['ConsumerStatus'] = self.consumer_status

        if self.description is not None:
            result['Description'] = self.description

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.jwks is not None:
            result['Jwks'] = self.jwks

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_value is not None:
            result['KeyValue'] = self.key_value

        if self.name is not None:
            result['Name'] = self.name

        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        if self.token_name is not None:
            result['TokenName'] = self.token_name

        if self.token_pass is not None:
            result['TokenPass'] = self.token_pass

        if self.token_position is not None:
            result['TokenPosition'] = self.token_position

        if self.token_prefix is not None:
            result['TokenPrefix'] = self.token_prefix

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerStatus') is not None:
            self.consumer_status = m.get('ConsumerStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jwks') is not None:
            self.jwks = m.get('Jwks')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyValue') is not None:
            self.key_value = m.get('KeyValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.GetGatewayAuthConsumerDetailResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        if m.get('TokenName') is not None:
            self.token_name = m.get('TokenName')

        if m.get('TokenPass') is not None:
            self.token_pass = m.get('TokenPass')

        if m.get('TokenPosition') is not None:
            self.token_position = m.get('TokenPosition')

        if m.get('TokenPrefix') is not None:
            self.token_prefix = m.get('TokenPrefix')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetGatewayAuthConsumerDetailResponseBodyDataResourceList(DaraModel):
    def __init__(
        self,
        consumer_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        resource_status: bool = None,
        route_id: int = None,
        route_name: str = None,
    ):
        # The consumer ID.
        self.consumer_id = consumer_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The time when the resource associated with the consumer authentication record was created.
        self.gmt_create = gmt_create
        # The time when the resource associated with the consumer authentication record was modified.
        self.gmt_modified = gmt_modified
        # The ID of the authorized resource for the consumer.
        self.id = id
        # The resource authorization state. Valid values:
        # 
        # *   true: Resource authorization is enabled.
        # *   false: Resource authorization is disabled.
        self.resource_status = resource_status
        # The ID of the route.
        self.route_id = route_id
        # The name of the route.
        self.route_name = route_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.route_id is not None:
            result['RouteId'] = self.route_id

        if self.route_name is not None:
            result['RouteName'] = self.route_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')

        return self

