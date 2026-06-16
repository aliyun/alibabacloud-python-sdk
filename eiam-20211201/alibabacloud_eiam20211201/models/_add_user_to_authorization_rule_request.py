# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class AddUserToAuthorizationRuleRequest(DaraModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        client_token: str = None,
        instance_id: str = None,
        user_id: str = None,
        validity_period: main_models.AddUserToAuthorizationRuleRequestValidityPeriod = None,
        validity_type: str = None,
    ):
        # The authorization rule ID.
        # 
        # This parameter is required.
        self.authorization_rule_id = authorization_rule_id
        # A client token that you provide to ensure the idempotence of the request. Make sure that the client token is unique for each request. The client token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The account ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The time range of the validity period. This parameter is valid only when **ValidityType** is set to **time_bound**.
        self.validity_period = validity_period
        # The type of the validity period for the relationship. Valid values:
        # 
        # - permanent: The authorization is permanent.
        # 
        # - time_bound: The authorization is valid for a custom time range.
        # 
        # This parameter is required.
        self.validity_type = validity_type

    def validate(self):
        if self.validity_period:
            self.validity_period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.validity_period is not None:
            result['ValidityPeriod'] = self.validity_period.to_map()

        if self.validity_type is not None:
            result['ValidityType'] = self.validity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('ValidityPeriod') is not None:
            temp_model = main_models.AddUserToAuthorizationRuleRequestValidityPeriod()
            self.validity_period = temp_model.from_map(m.get('ValidityPeriod'))

        if m.get('ValidityType') is not None:
            self.validity_type = m.get('ValidityType')

        return self

class AddUserToAuthorizationRuleRequestValidityPeriod(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end time of the validity period. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The start time of the validity period. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

