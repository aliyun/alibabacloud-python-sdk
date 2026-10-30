# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoadBalancerRequest(DaraModel):
    def __init__(
        self,
        billing_cycle: str = None,
        client_token: str = None,
        ens_region_id: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        load_balancer_type: str = None,
        network_id: str = None,
        pay_type: str = None,
        v_switch_id: str = None,
    ):
        # The billing cycle of the ELB instance.
        self.billing_cycle = billing_cycle
        # The client token that is used to ensure the idempotence of the request. This prevents duplicate operations caused by multiple retries.
        # - Generate the value from your client and ensure that it is unique among different requests. The client token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # - If you resubmit a request with a used client token and all other request parameters remain unchanged, the client receives the same response as the first request, and the server state remains unaffected.
        # 
        # - You can retry the request when the operation times out or the error code is PROCESSING, and the idempotence remains valid. If the HTTP status code 200 is returned, the client receives the same response after a retry, and the server state remains unaffected. If an HTTP 4xx status code is returned and the error code is not PROCESSING, the idempotence is invalid.
        # - The client token is valid for 10 minutes.
        self.client_token = client_token
        # The ENS edge zone ID. Not all ENS edge zones support creating an Edge Load Balancer (ELB) instance. Before calling this operation, verify that the target edge zone supports this feature.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The name of the load balancing instance. The name must be 1 to 80 characters in length, and can contain English letters and Chinese characters. If you do not specify this parameter, the system randomly allocates a name to the instance.
        # 
        # > The name cannot start with http:// or https://.
        self.load_balancer_name = load_balancer_name
        # The specification of the load balancing instance.
        # 
        # This parameter is required.
        self.load_balancer_spec = load_balancer_spec
        # The type of the edge load balancing (ELB) instance. Valid values:
        # - CLB: traditional load balancing instance.
        # - InternetDR: public pattern load balancing instance.
        self.load_balancer_type = load_balancer_type
        # The network ID of the edge load balancing (ELB) instance to be created.
        # 
        # This parameter is required.
        self.network_id = network_id
        # The billing method. Currently, only PostPaid (pay-as-you-go) is supported.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The ID of the vSwitch to which the VPC-connected instance belongs.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

