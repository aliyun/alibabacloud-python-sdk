# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetConsumerAuthorizationRuleResponseBody(DaraModel):
    def __init__(
        self,
        api_info: main_models.HttpApiApiInfo = None,
        consumer_authorization_rule_id: str = None,
        consumer_id: str = None,
        create_timestamp: int = None,
        deploy_status: str = None,
        environment_info: main_models.EnvironmentInfo = None,
        expire_mode: str = None,
        expire_status: str = None,
        expire_timestamp: int = None,
        gateway_info: main_models.GatewayInfo = None,
        request_id: str = None,
        resource_type: str = None,
        update_timestamp: int = None,
    ):
        # The API information.
        self.api_info = api_info
        # Filters the list of operations by a specific consumer authorization rule ID. Only authorized operations are returned in the response.
        self.consumer_authorization_rule_id = consumer_authorization_rule_id
        # The consumer ID.
        self.consumer_id = consumer_id
        # The creation timestamp. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The publishing status of the API in the current environment.
        self.deploy_status = deploy_status
        # The environment information.
        self.environment_info = environment_info
        # The expiry mode. Valid values: LongTerm and ShortTerm.
        self.expire_mode = expire_mode
        # The rule status.
        self.expire_status = expire_status
        # The expiration time.
        self.expire_timestamp = expire_timestamp
        # The gateway information.
        self.gateway_info = gateway_info
        # The request ID.
        self.request_id = request_id
        # The resource type.
        self.resource_type = resource_type
        # The update timestamp. Unit: milliseconds.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.api_info:
            self.api_info.validate()
        if self.environment_info:
            self.environment_info.validate()
        if self.gateway_info:
            self.gateway_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_info is not None:
            result['apiInfo'] = self.api_info.to_map()

        if self.consumer_authorization_rule_id is not None:
            result['consumerAuthorizationRuleId'] = self.consumer_authorization_rule_id

        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status

        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()

        if self.expire_mode is not None:
            result['expireMode'] = self.expire_mode

        if self.expire_status is not None:
            result['expireStatus'] = self.expire_status

        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiInfo') is not None:
            temp_model = main_models.HttpApiApiInfo()
            self.api_info = temp_model.from_map(m.get('apiInfo'))

        if m.get('consumerAuthorizationRuleId') is not None:
            self.consumer_authorization_rule_id = m.get('consumerAuthorizationRuleId')

        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')

        if m.get('environmentInfo') is not None:
            temp_model = main_models.EnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('expireMode') is not None:
            self.expire_mode = m.get('expireMode')

        if m.get('expireStatus') is not None:
            self.expire_status = m.get('expireStatus')

        if m.get('expireTimestamp') is not None:
            self.expire_timestamp = m.get('expireTimestamp')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.GatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

