# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTrafficMatchRuleToTrafficMarkingPolicyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_marking_policy_id: str = None,
        traffic_match_rule_description: str = None,
        traffic_match_rule_id: str = None,
        traffic_match_rule_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system does not add a traffic categorization rule to the traffic marking policy. Instead, the system checks whether the required request parameters are specified, whether the request format is valid, and whether the business restrictions are met. If the request fails the dry run, an error message is returned. If the request passes the dry run, the error code `DryRunOperation` is returned.
        # - **false** (default): sends a normal request. After the request passes the check, the traffic categorization rule is added to the traffic marking policy.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the traffic marking policy.
        # 
        # This parameter is required.
        self.traffic_marking_policy_id = traffic_marking_policy_id
        # The description of the traffic classification rule.
        # 
        # The description can be empty or 1 to 256 characters in length and cannot start with http:// or https://.
        self.traffic_match_rule_description = traffic_match_rule_description
        # The ID of the traffic classification rule.
        # 
        # This parameter is required.
        self.traffic_match_rule_id = traffic_match_rule_id
        # The name of the traffic classification rule.
        # 
        # The name can be empty or 1 to 128 characters in length and cannot start with http:// or https://.
        self.traffic_match_rule_name = traffic_match_rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id

        if self.traffic_match_rule_description is not None:
            result['TrafficMatchRuleDescription'] = self.traffic_match_rule_description

        if self.traffic_match_rule_id is not None:
            result['TrafficMatchRuleId'] = self.traffic_match_rule_id

        if self.traffic_match_rule_name is not None:
            result['TrafficMatchRuleName'] = self.traffic_match_rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')

        if m.get('TrafficMatchRuleDescription') is not None:
            self.traffic_match_rule_description = m.get('TrafficMatchRuleDescription')

        if m.get('TrafficMatchRuleId') is not None:
            self.traffic_match_rule_id = m.get('TrafficMatchRuleId')

        if m.get('TrafficMatchRuleName') is not None:
            self.traffic_match_rule_name = m.get('TrafficMatchRuleName')

        return self

