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
        # Ensures the idempotency of the request to avoid duplicate operations caused by multiple retries.
        # - Generate a parameter value from your client and ensure that the value is unique across different requests. The ClientToken value supports only ASCII characters and cannot exceed 64 characters in length.
        # 
        # - If you use a ClientToken that has been used before and the other request parameters remain unchanged, the client receives the same result as the first submission, with no impact on your server-side state.
        # 
        # - You can retry when the API times out or returns the PROCESSING error code, and idempotency takes effect. If the return result is an HTTP 200 status code, the retry returns the same result as the previous call with no impact on your server-side state. If the return result is an HTTP 4xx status code and the error code is not PROCESSING, idempotency does not take effect.
        # - The ClientToken is valid for 10 minutes.
        self.client_token = client_token
        # The ID of the ENS edge zone.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The name of the load balancing instance. The name must be 1 to 80 characters in length and can contain letters and Chinese characters. If you do not specify this parameter, the system automatically assigns an instance name.
        # 
        # > The name cannot start with `http://` or `https://`.
        self.load_balancer_name = load_balancer_name
        # The specification of the load balancing instance.
        # 
        # This parameter is required.
        self.load_balancer_spec = load_balancer_spec
        # The type of the Edge Load Balancing instance.
        # 
        # - CLB: Classic Load Balancing instance.
        # - InternetDR: Public pattern load balancing instance.
        self.load_balancer_type = load_balancer_type
        # The network ID of the Edge Load Balancing (ELB) instance to create.
        # 
        # This parameter is required.
        self.network_id = network_id
        # The billing type. PostPaid (currently the only supported type): pay-as-you-go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The ID of the vSwitch to which the VPC instance belongs.
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

