# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetDisasterRecoveryPlanResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetDisasterRecoveryPlanResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The response code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetDisasterRecoveryPlanResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetDisasterRecoveryPlanResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_sync_checkpoint: bool = None,
        create_time: str = None,
        ext_info: Dict[str, str] = None,
        instances: List[main_models.GetDisasterRecoveryPlanResponseBodyDataInstances] = None,
        plan_desc: str = None,
        plan_id: int = None,
        plan_name: str = None,
        plan_status: str = None,
        plan_type: str = None,
        sync_checkpoint_enabled: bool = None,
        update_time: str = None,
    ):
        # Indicates whether automatic consumer progress synchronization is enabled.
        # 
        # >  This parameter takes effect only when `syncCheckpointEnabled` is set to true.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.auto_sync_checkpoint = auto_sync_checkpoint
        # The time when the query task was created.
        self.create_time = create_time
        # The extended information.
        self.ext_info = ext_info
        # The instances involved in the Global Replicator task.
        self.instances = instances
        # The description of the Global Replicator task.
        self.plan_desc = plan_desc
        # The ID of the Global Replicator task.
        self.plan_id = plan_id
        # The name of the Global Replicator task.
        self.plan_name = plan_name
        # The status of the Global Replicator task. Valid values:
        # 
        # *   CREATED
        # *   RUNNING
        # *   DELETED
        self.plan_status = plan_status
        # The type of the Global Replicator task. Valid values:
        # 
        # *   ACTIVE_PASSIVE: one-way backup
        # *   ACTIVE_ACTIVE: two-way backup
        self.plan_type = plan_type
        # Indicates whether consumer progress synchronization is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.sync_checkpoint_enabled = sync_checkpoint_enabled
        # The time when the query task was last modified.
        self.update_time = update_time

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

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.ext_info is not None:
            result['extInfo'] = self.ext_info

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        if self.plan_desc is not None:
            result['planDesc'] = self.plan_desc

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.plan_name is not None:
            result['planName'] = self.plan_name

        if self.plan_status is not None:
            result['planStatus'] = self.plan_status

        if self.plan_type is not None:
            result['planType'] = self.plan_type

        if self.sync_checkpoint_enabled is not None:
            result['syncCheckpointEnabled'] = self.sync_checkpoint_enabled

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSyncCheckpoint') is not None:
            self.auto_sync_checkpoint = m.get('autoSyncCheckpoint')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.GetDisasterRecoveryPlanResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('planDesc') is not None:
            self.plan_desc = m.get('planDesc')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('planName') is not None:
            self.plan_name = m.get('planName')

        if m.get('planStatus') is not None:
            self.plan_status = m.get('planStatus')

        if m.get('planType') is not None:
            self.plan_type = m.get('planType')

        if m.get('syncCheckpointEnabled') is not None:
            self.sync_checkpoint_enabled = m.get('syncCheckpointEnabled')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetDisasterRecoveryPlanResponseBodyDataInstances(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        consumer_group_id: str = None,
        endpoint_url: str = None,
        instance_id: str = None,
        instance_role: str = None,
        instance_type: str = None,
        message_property: main_models.GetDisasterRecoveryPlanResponseBodyDataInstancesMessageProperty = None,
        network_type: str = None,
        password: str = None,
        region_id: str = None,
        security_group_id: str = None,
        username: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The authentication type.
        self.auth_type = auth_type
        # The consumer Group ID.
        self.consumer_group_id = consumer_group_id
        # The endpoint.
        self.endpoint_url = endpoint_url
        # The instance ID.
        self.instance_id = instance_id
        # The instance role.
        self.instance_role = instance_role
        # The instance type.
        self.instance_type = instance_type
        # The message attribute.
        self.message_property = message_property
        # The network type.
        self.network_type = network_type
        # The password used for authentication.
        self.password = password
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The username used for authentication.
        self.username = username
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
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
            temp_model = main_models.GetDisasterRecoveryPlanResponseBodyDataInstancesMessageProperty()
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

class GetDisasterRecoveryPlanResponseBodyDataInstancesMessageProperty(DaraModel):
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

