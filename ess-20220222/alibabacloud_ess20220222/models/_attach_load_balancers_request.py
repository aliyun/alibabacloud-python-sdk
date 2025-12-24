# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class AttachLoadBalancersRequest(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        client_token: str = None,
        force_attach: bool = None,
        load_balancer_configs: List[main_models.AttachLoadBalancersRequestLoadBalancerConfigs] = None,
        load_balancers: List[str] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # Specifies whether to attach the CLB instance to the scaling group in an asynchronous manner. If you attach the CLB instance from the scaling group in an asynchronous manner, the call is successful only after all operations are successful. If a specific operation fails, the call fails. We recommend that you set this parameter to true. Valid values:
        # 
        # *   true: attaches the CLB instance to the scaling group in an asynchronous manner. In this case, the ID of the scaling activity is returned.
        # *   false: does not attach the CLB instance to the scaling group in an asynchronous manner.
        # 
        # Default value: false.
        self.async_ = async_
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to add the existing instances in the scaling group as backend servers of the load balancer. Valid values:
        # 
        # *   true: If you set this parameter to `true`, the attachment of the load balancer entails the addition of the existing instances in the scaling group to the backend server groups of the load balancer.
        # 
        #     **
        # 
        #     **Note** If a load balancer is currently attached to your scaling group, and you only want to add the instances in your scaling group to the backend server groups of the load balancer, you can call this operation again and set ForceAttach request to true.
        # 
        # *   false: If you set this parameter to false, the attachment of the load balancer does not entail the addition of the existing instances in the scaling group to the backend server groups of the load balancer.
        # 
        # Default value: false.
        self.force_attach = force_attach
        # The configurations of the classic load balancer (CLB, formerly known as SLB) instance.
        self.load_balancer_configs = load_balancer_configs
        # The IDs of the load balancers that you want to attach to the scaling group.
        self.load_balancers = load_balancers
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        if self.load_balancer_configs:
            for v1 in self.load_balancer_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['Async'] = self.async_

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach

        result['LoadBalancerConfigs'] = []
        if self.load_balancer_configs is not None:
            for k1 in self.load_balancer_configs:
                result['LoadBalancerConfigs'].append(k1.to_map() if k1 else None)

        if self.load_balancers is not None:
            result['LoadBalancers'] = self.load_balancers

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')

        self.load_balancer_configs = []
        if m.get('LoadBalancerConfigs') is not None:
            for k1 in m.get('LoadBalancerConfigs'):
                temp_model = main_models.AttachLoadBalancersRequestLoadBalancerConfigs()
                self.load_balancer_configs.append(temp_model.from_map(k1))

        if m.get('LoadBalancers') is not None:
            self.load_balancers = m.get('LoadBalancers')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

class AttachLoadBalancersRequestLoadBalancerConfigs(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        weight: int = None,
    ):
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The weight of an Elastic Compute Service (ECS) instance or elastic container instance as a backend sever of the CLB instance. If an instance has a higher weight, more access traffic is routed to the instance. If an instance has zero weight, no access traffic is routed to the instance.
        # 
        # Valid values: 0 to 100.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

