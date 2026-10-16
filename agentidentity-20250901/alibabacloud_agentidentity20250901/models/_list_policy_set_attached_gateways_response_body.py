# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListPolicySetAttachedGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        attached_gateways: List[main_models.ListPolicySetAttachedGatewaysResponseBodyAttachedGateways] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of attached gateways.
        self.attached_gateways = attached_gateways
        # The maximum number of results to return per page.
        self.max_results = max_results
        # The token used for pagination. You do not need to specify this parameter for the first call. For subsequent calls, pass the NextToken value returned from the previous call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries that match the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.attached_gateways:
            for v1 in self.attached_gateways:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachedGateways'] = []
        if self.attached_gateways is not None:
            for k1 in self.attached_gateways:
                result['AttachedGateways'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attached_gateways = []
        if m.get('AttachedGateways') is not None:
            for k1 in m.get('AttachedGateways'):
                temp_model = main_models.ListPolicySetAttachedGatewaysResponseBodyAttachedGateways()
                self.attached_gateways.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPolicySetAttachedGatewaysResponseBodyAttachedGateways(DaraModel):
    def __init__(
        self,
        attached_policy_set_name: str = None,
        attached_time: str = None,
        enforcement_mode: str = None,
        gateway_arn: str = None,
        gateway_type: str = None,
    ):
        # The name of the policy set that is currently in effect on the gateway.
        self.attached_policy_set_name = attached_policy_set_name
        # The time when the policy set was attached to the gateway, in UTC and ISO 8601 format.
        self.attached_time = attached_time
        # The policy enforcement mode. Valid values:
        # 
        # - ENFORCE: Blocks non-compliant requests and allows compliant requests.
        # - LOG_ONLY: Only logs non-compliant requests without blocking them.
        self.enforcement_mode = enforcement_mode
        # The ARN of the target gateway.
        self.gateway_arn = gateway_arn
        # The gateway type. Valid values:
        # 
        # - AIGateway: Alibaba Cloud AI Gateway
        # - AgentRunMCP: AgentRun MCP tool
        self.gateway_type = gateway_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_policy_set_name is not None:
            result['AttachedPolicySetName'] = self.attached_policy_set_name

        if self.attached_time is not None:
            result['AttachedTime'] = self.attached_time

        if self.enforcement_mode is not None:
            result['EnforcementMode'] = self.enforcement_mode

        if self.gateway_arn is not None:
            result['GatewayArn'] = self.gateway_arn

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedPolicySetName') is not None:
            self.attached_policy_set_name = m.get('AttachedPolicySetName')

        if m.get('AttachedTime') is not None:
            self.attached_time = m.get('AttachedTime')

        if m.get('EnforcementMode') is not None:
            self.enforcement_mode = m.get('EnforcementMode')

        if m.get('GatewayArn') is not None:
            self.gateway_arn = m.get('GatewayArn')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        return self

