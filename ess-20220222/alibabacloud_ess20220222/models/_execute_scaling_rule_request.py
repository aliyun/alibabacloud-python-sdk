# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteScalingRuleRequest(DaraModel):
    def __init__(
        self,
        breach_threshold: float = None,
        client_token: str = None,
        metric_value: float = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_rule_ari: str = None,
    ):
        # The threshold specified when the step scaling rule is executed. Valid values: -9.999999E18 to 9.999999E18.
        self.breach_threshold = breach_threshold
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # The metric value specified when the step scaling rule is executed. Valid values: -9.999999E18 to 9.999999E18.
        self.metric_value = metric_value
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique identifier of the scaling rule.
        # 
        # >  You can call this operation to execute simple scaling rules and step scaling rules. If you want to call this operation to execute a step scaling rule, you must specify `BreachThreshold` and `MetricValue`.
        # 
        # This parameter is required.
        self.scaling_rule_ari = scaling_rule_ari

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.breach_threshold is not None:
            result['BreachThreshold'] = self.breach_threshold

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.metric_value is not None:
            result['MetricValue'] = self.metric_value

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreachThreshold') is not None:
            self.breach_threshold = m.get('BreachThreshold')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('MetricValue') is not None:
            self.metric_value = m.get('MetricValue')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')

        return self

