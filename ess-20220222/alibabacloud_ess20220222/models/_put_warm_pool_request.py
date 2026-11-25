# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class PutWarmPoolRequest(DaraModel):
    def __init__(
        self,
        capacity_options: main_models.PutWarmPoolRequestCapacityOptions = None,
        client_token: str = None,
        instance_reuse_policy: main_models.PutWarmPoolRequestInstanceReusePolicy = None,
        pool_state: str = None,
        region_id: str = None,
        scaling_group_id: str = None,
    ):
        # The capacity options for the warm pool.
        self.capacity_options = capacity_options
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must ensure that it is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # The instance reclaim policy.
        self.instance_reuse_policy = instance_reuse_policy
        # The state of instances in the warm pool. Valid values:
        # 
        # - Running: The instances are in the running state. This state allows faster scale-out, but you are charged for the full cost of the instances.
        # - Stopped: The instances are in the economical mode. You are charged only for resources such as cloud disks, elastic IP addresses (EIPs), and snapshots of the instances. However, instance startup may fail during scale-out due to insufficient inventory.
        # 
        # Default value: Stopped.
        self.pool_state = pool_state
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        if self.capacity_options:
            self.capacity_options.validate()
        if self.instance_reuse_policy:
            self.instance_reuse_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_options is not None:
            result['CapacityOptions'] = self.capacity_options.to_map()

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_reuse_policy is not None:
            result['InstanceReusePolicy'] = self.instance_reuse_policy.to_map()

        if self.pool_state is not None:
            result['PoolState'] = self.pool_state

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityOptions') is not None:
            temp_model = main_models.PutWarmPoolRequestCapacityOptions()
            self.capacity_options = temp_model.from_map(m.get('CapacityOptions'))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceReusePolicy') is not None:
            temp_model = main_models.PutWarmPoolRequestInstanceReusePolicy()
            self.instance_reuse_policy = temp_model.from_map(m.get('InstanceReusePolicy'))

        if m.get('PoolState') is not None:
            self.pool_state = m.get('PoolState')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

class PutWarmPoolRequestInstanceReusePolicy(DaraModel):
    def __init__(
        self,
        reuse_on_scale_in: bool = None,
    ):
        # Specifies whether instances are reclaimed to the warm pool when the scaling group scales in. Valid values:
        # 
        # - true: Instances are reclaimed to the warm pool.
        # - false: Instances are not reclaimed to the warm pool.
        # 
        # Default value: false.
        self.reuse_on_scale_in = reuse_on_scale_in

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reuse_on_scale_in is not None:
            result['ReuseOnScaleIn'] = self.reuse_on_scale_in

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReuseOnScaleIn') is not None:
            self.reuse_on_scale_in = m.get('ReuseOnScaleIn')

        return self

class PutWarmPoolRequestCapacityOptions(DaraModel):
    def __init__(
        self,
        desired_group_prepared_capacity: int = None,
        min_capacity: int = None,
    ):
        # The expected number of instances to be warmed. The system maintains the sum of the current number of instances in the scaling group and the number of instances in the warm pool at this value. Instances that exceed the current number of instances in the scaling group are scaled out into the warm pool in advance. When traffic peaks occur, instances can be quickly added from the warm pool, avoiding the wait time caused by creating instances on demand.
        # 
        # Default value: the maximum number of instances in the scaling group, which is specified by `MaxSize`.
        # > The value of `DesiredGroupPreparedCapacity` must be less than or equal to the maximum number of instances in the scaling group, which is specified by `MaxSize`.
        self.desired_group_prepared_capacity = desired_group_prepared_capacity
        # The minimum number of instances in the warm pool. The system always keeps at least this number of warmed instances in the warm pool to ensure that instances can be quickly added from the warm pool during scale-out.
        # 
        # Default value: 0.
        # 
        # > The value of `MinCapacity` must be less than or equal to the value of `DesiredGroupPreparedCapacity`.
        self.min_capacity = min_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desired_group_prepared_capacity is not None:
            result['DesiredGroupPreparedCapacity'] = self.desired_group_prepared_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesiredGroupPreparedCapacity') is not None:
            self.desired_group_prepared_capacity = m.get('DesiredGroupPreparedCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        return self

