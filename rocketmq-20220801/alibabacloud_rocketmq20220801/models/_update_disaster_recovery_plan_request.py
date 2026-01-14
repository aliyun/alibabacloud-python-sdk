# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class UpdateDisasterRecoveryPlanRequest(DaraModel):
    def __init__(
        self,
        auto_sync_checkpoint: bool = None,
        instances: List[main_models.UpdateDisasterRecoveryPlanRequestInstances] = None,
        plan_desc: str = None,
        plan_name: str = None,
        plan_type: str = None,
        sync_checkpoint_enabled: bool = None,
    ):
        # Specifies whether to enable automatic consumer progress synchronization.
        # 
        # >  This parameter takes effect only when you set `syncCheckpointEnabled` to true.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.auto_sync_checkpoint = auto_sync_checkpoint
        # The instances involved in the Global Replicator task. After you create a Global Replicator task, you cannot change the instances involved in the task. You can change only the message attribute and authentication type of the task.
        self.instances = instances
        # The description of the Global Replicator task.
        self.plan_desc = plan_desc
        # The name of the Global Replicator task.
        self.plan_name = plan_name
        # The type of the Global Replicator task. After you create a Global Replicator task, you cannot change the type of the task. Valid values:
        # 
        # *   ACTIVE_PASSIVE: one-way backup
        # *   ACTIVE_ACTIVE: two-way backup
        self.plan_type = plan_type
        # Specifies whether to enable consumer progress synchronization.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.sync_checkpoint_enabled = sync_checkpoint_enabled

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_sync_checkpoint is not None:
            result['autoSyncCheckpoint'] = self.auto_sync_checkpoint

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        if self.plan_desc is not None:
            result['planDesc'] = self.plan_desc

        if self.plan_name is not None:
            result['planName'] = self.plan_name

        if self.plan_type is not None:
            result['planType'] = self.plan_type

        if self.sync_checkpoint_enabled is not None:
            result['syncCheckpointEnabled'] = self.sync_checkpoint_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSyncCheckpoint') is not None:
            self.auto_sync_checkpoint = m.get('autoSyncCheckpoint')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.UpdateDisasterRecoveryPlanRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('planDesc') is not None:
            self.plan_desc = m.get('planDesc')

        if m.get('planName') is not None:
            self.plan_name = m.get('planName')

        if m.get('planType') is not None:
            self.plan_type = m.get('planType')

        if m.get('syncCheckpointEnabled') is not None:
            self.sync_checkpoint_enabled = m.get('syncCheckpointEnabled')

        return self

class UpdateDisasterRecoveryPlanRequestInstances(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        consumer_group_id: str = None,
        endpoint_url: str = None,
        instance_id: str = None,
        instance_role: str = None,
        instance_type: str = None,
        message_property: main_models.UpdateDisasterRecoveryPlanRequestInstancesMessageProperty = None,
        network_type: str = None,
        password: str = None,
        region_id: str = None,
        security_group_id: str = None,
        username: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The authentication type. Valid values:
        # 
        # *   NO_AUTH: no authentication
        # *   ACL_AUTH: access control list (ACL)-based authentication
        # 
        # <!---->
        # 
        # *
        # *
        self.auth_type = auth_type
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The instance endpoint. This parameter is required only if you set instanceType to EXTERNAL_ROCKETMQ.
        self.endpoint_url = endpoint_url
        # The instance ID.
        self.instance_id = instance_id
        # The instance role. Valid values:
        # 
        # *   ACTIVE: primary instance
        # *   Passive: secondary instance
        self.instance_role = instance_role
        # The instance type. Valid values:
        # 
        # *   ALIYUN_ROCKETMQ: ApsaraMQ for RocketMQ instance
        # *   EXTERNAL_ROCKETMQ: open source RocketMQ cluster
        self.instance_type = instance_type
        # The message attribute. When you synchronize a message to the destination cluster, the system automatically adds the attribute to the message for SQL-based filtering.
        self.message_property = message_property
        # The network type. This parameter is required only if you set instanceType to EXTERNAL_ROCKETMQ. Valid values:
        # 
        # *   TCP_INTERNET: Internet over TCP
        # *   TCP_VPC: virtual private cloud (VPC) over TCP.
        self.network_type = network_type
        # The password used for authentication. This parameter is required only if you set authType to ACL_AUTH.
        self.password = password
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The ID of the security group to which the instance belongs. This parameter is required only if you set instanceType to EXTERNAL_ROCKETMQ and networkType to TCP_VPC.
        self.security_group_id = security_group_id
        # The username used for authentication. This parameter is required only if you set authType to ACL_AUTH.
        self.username = username
        # The ID of the vSwitch with which the instance is associated. This parameter is required only if you set instanceType to EXTERNAL_ROCKETMQ and networkType to TCP_VPC.
        self.v_switch_id = v_switch_id
        # The ID of the VPC with which the instance is associated. This parameter is required only if you set instanceType to EXTERNAL_ROCKETMQ and networkType to TCP_VPC.
        self.vpc_id = vpc_id

    def validate(self):
        if self.message_property:
            self.message_property.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_role is not None:
            result['instanceRole'] = self.instance_role

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.message_property is not None:
            result['messageProperty'] = self.message_property.to_map()

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.password is not None:
            result['password'] = self.password

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.username is not None:
            result['username'] = self.username

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceRole') is not None:
            self.instance_role = m.get('instanceRole')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('messageProperty') is not None:
            temp_model = main_models.UpdateDisasterRecoveryPlanRequestInstancesMessageProperty()
            self.message_property = temp_model.from_map(m.get('messageProperty'))

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('username') is not None:
            self.username = m.get('username')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class UpdateDisasterRecoveryPlanRequestInstancesMessageProperty(DaraModel):
    def __init__(
        self,
        property_key: str = None,
        property_value: str = None,
    ):
        # The attribute key.
        self.property_key = property_key
        # The attribute value.
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_key is not None:
            result['propertyKey'] = self.property_key

        if self.property_value is not None:
            result['propertyValue'] = self.property_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyKey') is not None:
            self.property_key = m.get('propertyKey')

        if m.get('propertyValue') is not None:
            self.property_value = m.get('propertyValue')

        return self

