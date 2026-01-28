# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateAuthorizationRuleApplicationAttachmentRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        authorization_rule_id: str = None,
        client_token: str = None,
        instance_id: str = None,
        validity_period: main_models.UpdateAuthorizationRuleApplicationAttachmentRequestValidityPeriod = None,
        validity_type: str = None,
    ):
        # 应用 ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # 授权规则标识。
        # 
        # This parameter is required.
        self.authorization_rule_id = authorization_rule_id
        # This parameter is required.
        self.client_token = client_token
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 有效周期，当validityPeriodType为custom有效。
        self.validity_period = validity_period
        # 有效期类型，枚举值：permanent（永久），time_bound（自定义时间范围）。
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.validity_period is not None:
            result['ValidityPeriod'] = self.validity_period.to_map()

        if self.validity_type is not None:
            result['ValidityType'] = self.validity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ValidityPeriod') is not None:
            temp_model = main_models.UpdateAuthorizationRuleApplicationAttachmentRequestValidityPeriod()
            self.validity_period = temp_model.from_map(m.get('ValidityPeriod'))

        if m.get('ValidityType') is not None:
            self.validity_type = m.get('ValidityType')

        return self

class UpdateAuthorizationRuleApplicationAttachmentRequestValidityPeriod(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # 授权规则生效结束时间，采用unix纪元精确到毫秒。
        self.end_time = end_time
        # 授权规则生效开始时间，采用unix纪元精确到毫秒。
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

