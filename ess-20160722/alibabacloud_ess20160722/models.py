# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AttachInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class AttachInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class AttachInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScalingConfigurationRequestDataDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: str = None,
        device: str = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.device = device
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.device is not None:
            result['Device'] = self.device
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateScalingConfigurationRequestSystemDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        size: int = None,
    ):
        self.category = category
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateScalingConfigurationRequest(TeaModel):
    def __init__(
        self,
        data_disk: List[CreateScalingConfigurationRequestDataDisk] = None,
        system_disk: CreateScalingConfigurationRequestSystemDisk = None,
        image_id: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        security_group_id: str = None,
    ):
        self.data_disk = data_disk
        self.system_disk = system_disk
        # This parameter is required.
        self.image_id = image_id
        # This parameter is required.
        self.instance_type = instance_type
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.io_optimized = io_optimized
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_configuration_name = scaling_configuration_name
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # This parameter is required.
        self.security_group_id = security_group_id

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = CreateScalingConfigurationRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('SystemDisk') is not None:
            temp_model = CreateScalingConfigurationRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class CreateScalingConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_configuration_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_configuration_id = scaling_configuration_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        return self


class CreateScalingConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScalingConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScalingGroupRequest(TeaModel):
    def __init__(
        self,
        removal_policy: List[str] = None,
        dbinstance_ids: str = None,
        default_cooldown: int = None,
        load_balancer_ids: str = None,
        max_size: int = None,
        min_size: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_name: str = None,
        v_switch_id: str = None,
    ):
        self.removal_policy = removal_policy
        self.dbinstance_ids = dbinstance_ids
        self.default_cooldown = default_cooldown
        self.load_balancer_ids = load_balancer_ids
        # This parameter is required.
        self.max_size = max_size
        # This parameter is required.
        self.min_size = min_size
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_name = scaling_group_name
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.removal_policy is not None:
            result['RemovalPolicy'] = self.removal_policy
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemovalPolicy') is not None:
            self.removal_policy = m.get('RemovalPolicy')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateScalingGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_group_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class CreateScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScalingRuleRequest(TeaModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        cooldown: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        scaling_rule_name: str = None,
    ):
        # This parameter is required.
        self.adjustment_type = adjustment_type
        # This parameter is required.
        self.adjustment_value = adjustment_value
        self.cooldown = cooldown
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class CreateScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_rule_ari: str = None,
        scaling_rule_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_rule_ari = scaling_rule_ari
        self.scaling_rule_id = scaling_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        return self


class CreateScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledTaskRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheduled_action: str = None,
        scheduled_task_name: str = None,
        task_enabled: bool = None,
    ):
        self.description = description
        self.launch_expiration_time = launch_expiration_time
        self.launch_time = launch_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.recurrence_end_time = recurrence_end_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scheduled_action = scheduled_action
        self.scheduled_task_name = scheduled_task_name
        self.task_enabled = task_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')
        return self


class CreateScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scheduled_task_id: str = None,
    ):
        self.request_id = request_id
        self.scheduled_task_id = scheduled_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        return self


class CreateScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScalingConfigurationRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_configuration_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_configuration_id = scaling_configuration_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        return self


class DeleteScalingConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScalingConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScalingConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScalingGroupRequest(TeaModel):
    def __init__(
        self,
        force_delete: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.force_delete = force_delete
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_delete is not None:
            result['ForceDelete'] = self.force_delete
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceDelete') is not None:
            self.force_delete = m.get('ForceDelete')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DeleteScalingGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScalingRuleRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_rule_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_rule_id = scaling_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        return self


class DeleteScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduledTaskRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheduled_task_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scheduled_task_id = scheduled_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        return self


class DeleteScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountAttributesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAccountAttributesResponseBody(TeaModel):
    def __init__(
        self,
        max_number_of_dbinstances: int = None,
        max_number_of_load_balancers: int = None,
        max_number_of_max_size: int = None,
        max_number_of_min_size: int = None,
        max_number_of_scaling_configurations: int = None,
        max_number_of_scaling_groups: int = None,
        max_number_of_scaling_instances: int = None,
        max_number_of_scaling_rules: int = None,
        max_number_of_scheduled_tasks: int = None,
    ):
        self.max_number_of_dbinstances = max_number_of_dbinstances
        self.max_number_of_load_balancers = max_number_of_load_balancers
        self.max_number_of_max_size = max_number_of_max_size
        self.max_number_of_min_size = max_number_of_min_size
        self.max_number_of_scaling_configurations = max_number_of_scaling_configurations
        self.max_number_of_scaling_groups = max_number_of_scaling_groups
        self.max_number_of_scaling_instances = max_number_of_scaling_instances
        self.max_number_of_scaling_rules = max_number_of_scaling_rules
        self.max_number_of_scheduled_tasks = max_number_of_scheduled_tasks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_number_of_dbinstances is not None:
            result['MaxNumberOfDBInstances'] = self.max_number_of_dbinstances
        if self.max_number_of_load_balancers is not None:
            result['MaxNumberOfLoadBalancers'] = self.max_number_of_load_balancers
        if self.max_number_of_max_size is not None:
            result['MaxNumberOfMaxSize'] = self.max_number_of_max_size
        if self.max_number_of_min_size is not None:
            result['MaxNumberOfMinSize'] = self.max_number_of_min_size
        if self.max_number_of_scaling_configurations is not None:
            result['MaxNumberOfScalingConfigurations'] = self.max_number_of_scaling_configurations
        if self.max_number_of_scaling_groups is not None:
            result['MaxNumberOfScalingGroups'] = self.max_number_of_scaling_groups
        if self.max_number_of_scaling_instances is not None:
            result['MaxNumberOfScalingInstances'] = self.max_number_of_scaling_instances
        if self.max_number_of_scaling_rules is not None:
            result['MaxNumberOfScalingRules'] = self.max_number_of_scaling_rules
        if self.max_number_of_scheduled_tasks is not None:
            result['MaxNumberOfScheduledTasks'] = self.max_number_of_scheduled_tasks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxNumberOfDBInstances') is not None:
            self.max_number_of_dbinstances = m.get('MaxNumberOfDBInstances')
        if m.get('MaxNumberOfLoadBalancers') is not None:
            self.max_number_of_load_balancers = m.get('MaxNumberOfLoadBalancers')
        if m.get('MaxNumberOfMaxSize') is not None:
            self.max_number_of_max_size = m.get('MaxNumberOfMaxSize')
        if m.get('MaxNumberOfMinSize') is not None:
            self.max_number_of_min_size = m.get('MaxNumberOfMinSize')
        if m.get('MaxNumberOfScalingConfigurations') is not None:
            self.max_number_of_scaling_configurations = m.get('MaxNumberOfScalingConfigurations')
        if m.get('MaxNumberOfScalingGroups') is not None:
            self.max_number_of_scaling_groups = m.get('MaxNumberOfScalingGroups')
        if m.get('MaxNumberOfScalingInstances') is not None:
            self.max_number_of_scaling_instances = m.get('MaxNumberOfScalingInstances')
        if m.get('MaxNumberOfScalingRules') is not None:
            self.max_number_of_scaling_rules = m.get('MaxNumberOfScalingRules')
        if m.get('MaxNumberOfScheduledTasks') is not None:
            self.max_number_of_scheduled_tasks = m.get('MaxNumberOfScheduledTasks')
        return self


class DescribeAccountAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccountAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCapacityHistoryRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCapacityHistoryResponseBodyCapacityHistoryItemsCapacityHistoryModel(TeaModel):
    def __init__(
        self,
        attached_capacity: int = None,
        auto_created_capacity: int = None,
        scaling_group_id: str = None,
        timestamp: str = None,
        total_capacity: int = None,
    ):
        self.attached_capacity = attached_capacity
        self.auto_created_capacity = auto_created_capacity
        self.scaling_group_id = scaling_group_id
        self.timestamp = timestamp
        self.total_capacity = total_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attached_capacity is not None:
            result['AttachedCapacity'] = self.attached_capacity
        if self.auto_created_capacity is not None:
            result['AutoCreatedCapacity'] = self.auto_created_capacity
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedCapacity') is not None:
            self.attached_capacity = m.get('AttachedCapacity')
        if m.get('AutoCreatedCapacity') is not None:
            self.auto_created_capacity = m.get('AutoCreatedCapacity')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        return self


class DescribeCapacityHistoryResponseBodyCapacityHistoryItems(TeaModel):
    def __init__(
        self,
        capacity_history_model: List[DescribeCapacityHistoryResponseBodyCapacityHistoryItemsCapacityHistoryModel] = None,
    ):
        self.capacity_history_model = capacity_history_model

    def validate(self):
        if self.capacity_history_model:
            for k in self.capacity_history_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CapacityHistoryModel'] = []
        if self.capacity_history_model is not None:
            for k in self.capacity_history_model:
                result['CapacityHistoryModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.capacity_history_model = []
        if m.get('CapacityHistoryModel') is not None:
            for k in m.get('CapacityHistoryModel'):
                temp_model = DescribeCapacityHistoryResponseBodyCapacityHistoryItemsCapacityHistoryModel()
                self.capacity_history_model.append(temp_model.from_map(k))
        return self


class DescribeCapacityHistoryResponseBody(TeaModel):
    def __init__(
        self,
        capacity_history_items: DescribeCapacityHistoryResponseBodyCapacityHistoryItems = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.capacity_history_items = capacity_history_items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.capacity_history_items:
            self.capacity_history_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity_history_items is not None:
            result['CapacityHistoryItems'] = self.capacity_history_items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityHistoryItems') is not None:
            temp_model = DescribeCapacityHistoryResponseBodyCapacityHistoryItems()
            self.capacity_history_items = temp_model.from_map(m['CapacityHistoryItems'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCapacityHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCapacityHistoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCapacityHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLimitationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeLimitationResponseBody(TeaModel):
    def __init__(
        self,
        max_number_of_dbinstances: int = None,
        max_number_of_load_balancers: int = None,
        max_number_of_max_size: int = None,
        max_number_of_min_size: int = None,
        max_number_of_scaling_configurations: int = None,
        max_number_of_scaling_groups: int = None,
        max_number_of_scaling_instances: int = None,
        max_number_of_scaling_rules: int = None,
        max_number_of_scheduled_tasks: int = None,
    ):
        self.max_number_of_dbinstances = max_number_of_dbinstances
        self.max_number_of_load_balancers = max_number_of_load_balancers
        self.max_number_of_max_size = max_number_of_max_size
        self.max_number_of_min_size = max_number_of_min_size
        self.max_number_of_scaling_configurations = max_number_of_scaling_configurations
        self.max_number_of_scaling_groups = max_number_of_scaling_groups
        self.max_number_of_scaling_instances = max_number_of_scaling_instances
        self.max_number_of_scaling_rules = max_number_of_scaling_rules
        self.max_number_of_scheduled_tasks = max_number_of_scheduled_tasks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_number_of_dbinstances is not None:
            result['MaxNumberOfDBInstances'] = self.max_number_of_dbinstances
        if self.max_number_of_load_balancers is not None:
            result['MaxNumberOfLoadBalancers'] = self.max_number_of_load_balancers
        if self.max_number_of_max_size is not None:
            result['MaxNumberOfMaxSize'] = self.max_number_of_max_size
        if self.max_number_of_min_size is not None:
            result['MaxNumberOfMinSize'] = self.max_number_of_min_size
        if self.max_number_of_scaling_configurations is not None:
            result['MaxNumberOfScalingConfigurations'] = self.max_number_of_scaling_configurations
        if self.max_number_of_scaling_groups is not None:
            result['MaxNumberOfScalingGroups'] = self.max_number_of_scaling_groups
        if self.max_number_of_scaling_instances is not None:
            result['MaxNumberOfScalingInstances'] = self.max_number_of_scaling_instances
        if self.max_number_of_scaling_rules is not None:
            result['MaxNumberOfScalingRules'] = self.max_number_of_scaling_rules
        if self.max_number_of_scheduled_tasks is not None:
            result['MaxNumberOfScheduledTasks'] = self.max_number_of_scheduled_tasks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxNumberOfDBInstances') is not None:
            self.max_number_of_dbinstances = m.get('MaxNumberOfDBInstances')
        if m.get('MaxNumberOfLoadBalancers') is not None:
            self.max_number_of_load_balancers = m.get('MaxNumberOfLoadBalancers')
        if m.get('MaxNumberOfMaxSize') is not None:
            self.max_number_of_max_size = m.get('MaxNumberOfMaxSize')
        if m.get('MaxNumberOfMinSize') is not None:
            self.max_number_of_min_size = m.get('MaxNumberOfMinSize')
        if m.get('MaxNumberOfScalingConfigurations') is not None:
            self.max_number_of_scaling_configurations = m.get('MaxNumberOfScalingConfigurations')
        if m.get('MaxNumberOfScalingGroups') is not None:
            self.max_number_of_scaling_groups = m.get('MaxNumberOfScalingGroups')
        if m.get('MaxNumberOfScalingInstances') is not None:
            self.max_number_of_scaling_instances = m.get('MaxNumberOfScalingInstances')
        if m.get('MaxNumberOfScalingRules') is not None:
            self.max_number_of_scaling_rules = m.get('MaxNumberOfScalingRules')
        if m.get('MaxNumberOfScheduledTasks') is not None:
            self.max_number_of_scheduled_tasks = m.get('MaxNumberOfScheduledTasks')
        return self


class DescribeLimitationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLimitationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLimitationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingActivitiesRequest(TeaModel):
    def __init__(
        self,
        scaling_activity_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        status_code: str = None,
    ):
        self.scaling_activity_id = scaling_activity_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DescribeScalingActivitiesResponseBodyScalingActivitiesScalingActivity(TeaModel):
    def __init__(
        self,
        attached_capacity: str = None,
        auto_created_capacity: str = None,
        cause: str = None,
        description: str = None,
        end_time: str = None,
        progress: int = None,
        scaling_activity_id: str = None,
        scaling_group_id: str = None,
        start_time: str = None,
        status_code: str = None,
        status_message: str = None,
        total_capacity: str = None,
    ):
        self.attached_capacity = attached_capacity
        self.auto_created_capacity = auto_created_capacity
        self.cause = cause
        self.description = description
        self.end_time = end_time
        self.progress = progress
        self.scaling_activity_id = scaling_activity_id
        self.scaling_group_id = scaling_group_id
        self.start_time = start_time
        self.status_code = status_code
        self.status_message = status_message
        self.total_capacity = total_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attached_capacity is not None:
            result['AttachedCapacity'] = self.attached_capacity
        if self.auto_created_capacity is not None:
            result['AutoCreatedCapacity'] = self.auto_created_capacity
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedCapacity') is not None:
            self.attached_capacity = m.get('AttachedCapacity')
        if m.get('AutoCreatedCapacity') is not None:
            self.auto_created_capacity = m.get('AutoCreatedCapacity')
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        return self


class DescribeScalingActivitiesResponseBodyScalingActivities(TeaModel):
    def __init__(
        self,
        scaling_activity: List[DescribeScalingActivitiesResponseBodyScalingActivitiesScalingActivity] = None,
    ):
        self.scaling_activity = scaling_activity

    def validate(self):
        if self.scaling_activity:
            for k in self.scaling_activity:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScalingActivity'] = []
        if self.scaling_activity is not None:
            for k in self.scaling_activity:
                result['ScalingActivity'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scaling_activity = []
        if m.get('ScalingActivity') is not None:
            for k in m.get('ScalingActivity'):
                temp_model = DescribeScalingActivitiesResponseBodyScalingActivitiesScalingActivity()
                self.scaling_activity.append(temp_model.from_map(k))
        return self


class DescribeScalingActivitiesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_activities: DescribeScalingActivitiesResponseBodyScalingActivities = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_activities = scaling_activities
        self.total_count = total_count

    def validate(self):
        if self.scaling_activities:
            self.scaling_activities.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activities is not None:
            result['ScalingActivities'] = self.scaling_activities.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivities') is not None:
            temp_model = DescribeScalingActivitiesResponseBodyScalingActivities()
            self.scaling_activities = temp_model.from_map(m['ScalingActivities'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScalingActivitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingActivitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingActivitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingActivityDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_activity_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DescribeScalingActivityDetailResponseBody(TeaModel):
    def __init__(
        self,
        detail: str = None,
        scaling_activity_id: str = None,
    ):
        self.detail = detail
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DescribeScalingActivityDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingActivityDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingActivityDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingConfigurationsRequest(TeaModel):
    def __init__(
        self,
        scaling_configuration_id: List[str] = None,
        scaling_configuration_name: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_configuration_name = scaling_configuration_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisksDataDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        device: str = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.category = category
        self.device = device
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.device is not None:
            result['Device'] = self.device
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisks(TeaModel):
    def __init__(
        self,
        data_disk: List[DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisksDataDisk] = None,
    ):
        self.data_disk = data_disk

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisksDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfiguration(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        data_disks: DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisks = None,
        image_id: str = None,
        instance_generation: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        lifecycle_state: str = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        security_group_id: str = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
    ):
        self.creation_time = creation_time
        self.data_disks = data_disks
        self.image_id = image_id
        self.instance_generation = instance_generation
        self.instance_type = instance_type
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.io_optimized = io_optimized
        self.lifecycle_state = lifecycle_state
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_configuration_name = scaling_configuration_name
        self.scaling_group_id = scaling_group_id
        self.security_group_id = security_group_id
        self.system_disk_category = system_disk_category
        self.system_disk_size = system_disk_size

    def validate(self):
        if self.data_disks:
            self.data_disks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_generation is not None:
            result['InstanceGeneration'] = self.instance_generation
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataDisks') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisks()
            self.data_disks = temp_model.from_map(m['DataDisks'])
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceGeneration') is not None:
            self.instance_generation = m.get('InstanceGeneration')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurations(TeaModel):
    def __init__(
        self,
        scaling_configuration: List[DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfiguration] = None,
    ):
        self.scaling_configuration = scaling_configuration

    def validate(self):
        if self.scaling_configuration:
            for k in self.scaling_configuration:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScalingConfiguration'] = []
        if self.scaling_configuration is not None:
            for k in self.scaling_configuration:
                result['ScalingConfiguration'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scaling_configuration = []
        if m.get('ScalingConfiguration') is not None:
            for k in m.get('ScalingConfiguration'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfiguration()
                self.scaling_configuration.append(temp_model.from_map(k))
        return self


class DescribeScalingConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_configurations: DescribeScalingConfigurationsResponseBodyScalingConfigurations = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_configurations = scaling_configurations
        self.total_count = total_count

    def validate(self):
        if self.scaling_configurations:
            self.scaling_configurations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_configurations is not None:
            result['ScalingConfigurations'] = self.scaling_configurations.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingConfigurations') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurations()
            self.scaling_configurations = temp_model.from_map(m['ScalingConfigurations'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScalingConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingConfigurationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingGroupsRequest(TeaModel):
    def __init__(
        self,
        scaling_group_id: List[str] = None,
        scaling_group_name: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        self.scaling_group_id = scaling_group_id
        self.scaling_group_name = scaling_group_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DescribeScalingGroupsResponseBodyScalingGroupsScalingGroupDBInstanceIds(TeaModel):
    def __init__(
        self,
        dbinstance_id: List[str] = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeScalingGroupsResponseBodyScalingGroupsScalingGroupLoadBalancerIds(TeaModel):
    def __init__(
        self,
        load_balancer_id: List[str] = None,
    ):
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeScalingGroupsResponseBodyScalingGroupsScalingGroupRemovalPolicies(TeaModel):
    def __init__(
        self,
        removal_policy: List[str] = None,
    ):
        self.removal_policy = removal_policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.removal_policy is not None:
            result['RemovalPolicy'] = self.removal_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemovalPolicy') is not None:
            self.removal_policy = m.get('RemovalPolicy')
        return self


class DescribeScalingGroupsResponseBodyScalingGroupsScalingGroup(TeaModel):
    def __init__(
        self,
        active_capacity: int = None,
        active_scaling_configuration_id: str = None,
        creation_time: str = None,
        dbinstance_ids: DescribeScalingGroupsResponseBodyScalingGroupsScalingGroupDBInstanceIds = None,
        default_cooldown: int = None,
        lifecycle_state: str = None,
        load_balancer_ids: DescribeScalingGroupsResponseBodyScalingGroupsScalingGroupLoadBalancerIds = None,
        max_size: int = None,
        min_size: int = None,
        pending_capacity: int = None,
        region_id: str = None,
        removal_policies: DescribeScalingGroupsResponseBodyScalingGroupsScalingGroupRemovalPolicies = None,
        removing_capacity: int = None,
        scaling_group_id: str = None,
        scaling_group_name: str = None,
        total_capacity: int = None,
        v_switch_id: str = None,
    ):
        self.active_capacity = active_capacity
        self.active_scaling_configuration_id = active_scaling_configuration_id
        self.creation_time = creation_time
        self.dbinstance_ids = dbinstance_ids
        self.default_cooldown = default_cooldown
        self.lifecycle_state = lifecycle_state
        self.load_balancer_ids = load_balancer_ids
        self.max_size = max_size
        self.min_size = min_size
        self.pending_capacity = pending_capacity
        self.region_id = region_id
        self.removal_policies = removal_policies
        self.removing_capacity = removing_capacity
        self.scaling_group_id = scaling_group_id
        self.scaling_group_name = scaling_group_name
        self.total_capacity = total_capacity
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.dbinstance_ids:
            self.dbinstance_ids.validate()
        if self.load_balancer_ids:
            self.load_balancer_ids.validate()
        if self.removal_policies:
            self.removal_policies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_capacity is not None:
            result['ActiveCapacity'] = self.active_capacity
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids.to_map()
        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids.to_map()
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.pending_capacity is not None:
            result['PendingCapacity'] = self.pending_capacity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.removal_policies is not None:
            result['RemovalPolicies'] = self.removal_policies.to_map()
        if self.removing_capacity is not None:
            result['RemovingCapacity'] = self.removing_capacity
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCapacity') is not None:
            self.active_capacity = m.get('ActiveCapacity')
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBInstanceIds') is not None:
            temp_model = DescribeScalingGroupsResponseBodyScalingGroupsScalingGroupDBInstanceIds()
            self.dbinstance_ids = temp_model.from_map(m['DBInstanceIds'])
        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('LoadBalancerIds') is not None:
            temp_model = DescribeScalingGroupsResponseBodyScalingGroupsScalingGroupLoadBalancerIds()
            self.load_balancer_ids = temp_model.from_map(m['LoadBalancerIds'])
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('PendingCapacity') is not None:
            self.pending_capacity = m.get('PendingCapacity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemovalPolicies') is not None:
            temp_model = DescribeScalingGroupsResponseBodyScalingGroupsScalingGroupRemovalPolicies()
            self.removal_policies = temp_model.from_map(m['RemovalPolicies'])
        if m.get('RemovingCapacity') is not None:
            self.removing_capacity = m.get('RemovingCapacity')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeScalingGroupsResponseBodyScalingGroups(TeaModel):
    def __init__(
        self,
        scaling_group: List[DescribeScalingGroupsResponseBodyScalingGroupsScalingGroup] = None,
    ):
        self.scaling_group = scaling_group

    def validate(self):
        if self.scaling_group:
            for k in self.scaling_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScalingGroup'] = []
        if self.scaling_group is not None:
            for k in self.scaling_group:
                result['ScalingGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scaling_group = []
        if m.get('ScalingGroup') is not None:
            for k in m.get('ScalingGroup'):
                temp_model = DescribeScalingGroupsResponseBodyScalingGroupsScalingGroup()
                self.scaling_group.append(temp_model.from_map(k))
        return self


class DescribeScalingGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_groups: DescribeScalingGroupsResponseBodyScalingGroups = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_groups = scaling_groups
        self.total_count = total_count

    def validate(self):
        if self.scaling_groups:
            self.scaling_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_groups is not None:
            result['ScalingGroups'] = self.scaling_groups.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingGroups') is not None:
            temp_model = DescribeScalingGroupsResponseBodyScalingGroups()
            self.scaling_groups = temp_model.from_map(m['ScalingGroups'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScalingGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        creation_type: str = None,
        health_status: str = None,
        lifecycle_state: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.creation_type = creation_type
        self.health_status = health_status
        self.lifecycle_state = lifecycle_state
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.creation_type is not None:
            result['CreationType'] = self.creation_type
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeScalingInstancesResponseBodyScalingInstancesScalingInstance(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        creation_type: str = None,
        health_status: str = None,
        instance_id: str = None,
        lifecycle_state: str = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
    ):
        self.creation_time = creation_time
        self.creation_type = creation_type
        self.health_status = health_status
        self.instance_id = instance_id
        self.lifecycle_state = lifecycle_state
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.creation_type is not None:
            result['CreationType'] = self.creation_type
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeScalingInstancesResponseBodyScalingInstances(TeaModel):
    def __init__(
        self,
        scaling_instance: List[DescribeScalingInstancesResponseBodyScalingInstancesScalingInstance] = None,
    ):
        self.scaling_instance = scaling_instance

    def validate(self):
        if self.scaling_instance:
            for k in self.scaling_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScalingInstance'] = []
        if self.scaling_instance is not None:
            for k in self.scaling_instance:
                result['ScalingInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scaling_instance = []
        if m.get('ScalingInstance') is not None:
            for k in m.get('ScalingInstance'):
                temp_model = DescribeScalingInstancesResponseBodyScalingInstancesScalingInstance()
                self.scaling_instance.append(temp_model.from_map(k))
        return self


class DescribeScalingInstancesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_instances: DescribeScalingInstancesResponseBodyScalingInstances = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_instances = scaling_instances
        self.total_count = total_count

    def validate(self):
        if self.scaling_instances:
            self.scaling_instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_instances is not None:
            result['ScalingInstances'] = self.scaling_instances.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingInstances') is not None:
            temp_model = DescribeScalingInstancesResponseBodyScalingInstances()
            self.scaling_instances = temp_model.from_map(m['ScalingInstances'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScalingInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingRulesRequest(TeaModel):
    def __init__(
        self,
        scaling_rule_ari: List[str] = None,
        scaling_rule_id: List[str] = None,
        scaling_rule_name: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.scaling_rule_ari = scaling_rule_ari
        self.scaling_rule_id = scaling_rule_id
        self.scaling_rule_name = scaling_rule_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeScalingRulesResponseBodyScalingRulesScalingRule(TeaModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        cooldown: int = None,
        max_size: int = None,
        min_size: int = None,
        scaling_group_id: str = None,
        scaling_rule_ari: str = None,
        scaling_rule_id: str = None,
        scaling_rule_name: str = None,
    ):
        self.adjustment_type = adjustment_type
        self.adjustment_value = adjustment_value
        self.cooldown = cooldown
        self.max_size = max_size
        self.min_size = min_size
        self.scaling_group_id = scaling_group_id
        self.scaling_rule_ari = scaling_rule_ari
        self.scaling_rule_id = scaling_rule_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class DescribeScalingRulesResponseBodyScalingRules(TeaModel):
    def __init__(
        self,
        scaling_rule: List[DescribeScalingRulesResponseBodyScalingRulesScalingRule] = None,
    ):
        self.scaling_rule = scaling_rule

    def validate(self):
        if self.scaling_rule:
            for k in self.scaling_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScalingRule'] = []
        if self.scaling_rule is not None:
            for k in self.scaling_rule:
                result['ScalingRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scaling_rule = []
        if m.get('ScalingRule') is not None:
            for k in m.get('ScalingRule'):
                temp_model = DescribeScalingRulesResponseBodyScalingRulesScalingRule()
                self.scaling_rule.append(temp_model.from_map(k))
        return self


class DescribeScalingRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_rules: DescribeScalingRulesResponseBodyScalingRules = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_rules = scaling_rules
        self.total_count = total_count

    def validate(self):
        if self.scaling_rules:
            self.scaling_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_rules is not None:
            result['ScalingRules'] = self.scaling_rules.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingRules') is not None:
            temp_model = DescribeScalingRulesResponseBodyScalingRules()
            self.scaling_rules = temp_model.from_map(m['ScalingRules'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScalingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduledTasksRequest(TeaModel):
    def __init__(
        self,
        scheduled_action: List[str] = None,
        scheduled_task_id: List[str] = None,
        scheduled_task_name: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.scheduled_action = scheduled_action
        self.scheduled_task_id = scheduled_task_id
        self.scheduled_task_name = scheduled_task_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeScheduledTasksResponseBodyScheduledTasksScheduledTask(TeaModel):
    def __init__(
        self,
        description: str = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        scheduled_action: str = None,
        scheduled_task_id: str = None,
        scheduled_task_name: str = None,
        task_enabled: bool = None,
    ):
        self.description = description
        self.launch_expiration_time = launch_expiration_time
        self.launch_time = launch_time
        self.recurrence_end_time = recurrence_end_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value
        self.scheduled_action = scheduled_action
        self.scheduled_task_id = scheduled_task_id
        self.scheduled_task_name = scheduled_task_name
        self.task_enabled = task_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')
        return self


class DescribeScheduledTasksResponseBodyScheduledTasks(TeaModel):
    def __init__(
        self,
        scheduled_task: List[DescribeScheduledTasksResponseBodyScheduledTasksScheduledTask] = None,
    ):
        self.scheduled_task = scheduled_task

    def validate(self):
        if self.scheduled_task:
            for k in self.scheduled_task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScheduledTask'] = []
        if self.scheduled_task is not None:
            for k in self.scheduled_task:
                result['ScheduledTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scheduled_task = []
        if m.get('ScheduledTask') is not None:
            for k in m.get('ScheduledTask'):
                temp_model = DescribeScheduledTasksResponseBodyScheduledTasksScheduledTask()
                self.scheduled_task.append(temp_model.from_map(k))
        return self


class DescribeScheduledTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scheduled_tasks: DescribeScheduledTasksResponseBodyScheduledTasks = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scheduled_tasks = scheduled_tasks
        self.total_count = total_count

    def validate(self):
        if self.scheduled_tasks:
            self.scheduled_tasks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scheduled_tasks is not None:
            result['ScheduledTasks'] = self.scheduled_tasks.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduledTasks') is not None:
            temp_model = DescribeScheduledTasksResponseBodyScheduledTasks()
            self.scheduled_tasks = temp_model.from_map(m['ScheduledTasks'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScheduledTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScheduledTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScheduledTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DetachInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DetachInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableScalingGroupRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DisableScalingGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableScalingGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        active_scaling_configuration_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.active_scaling_configuration_id = active_scaling_configuration_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class EnableScalingGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteScalingRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_rule_ari: str = None,
    ):
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_rule_ari = scaling_rule_ari

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        return self


class ExecuteScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class ExecuteScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScalingGroupRequest(TeaModel):
    def __init__(
        self,
        removal_policy: List[str] = None,
        active_scaling_configuration_id: str = None,
        default_cooldown: int = None,
        max_size: int = None,
        min_size: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        scaling_group_name: str = None,
    ):
        self.removal_policy = removal_policy
        self.active_scaling_configuration_id = active_scaling_configuration_id
        self.default_cooldown = default_cooldown
        self.max_size = max_size
        self.min_size = min_size
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        self.scaling_group_name = scaling_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.removal_policy is not None:
            result['RemovalPolicy'] = self.removal_policy
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id
        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemovalPolicy') is not None:
            self.removal_policy = m.get('RemovalPolicy')
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')
        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        return self


class ModifyScalingGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScalingRuleRequest(TeaModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        cooldown: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_rule_id: str = None,
        scaling_rule_name: str = None,
    ):
        self.adjustment_type = adjustment_type
        self.adjustment_value = adjustment_value
        self.cooldown = cooldown
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_rule_id = scaling_rule_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class ModifyScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScheduledTaskRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheduled_action: str = None,
        scheduled_task_id: str = None,
        scheduled_task_name: str = None,
        task_enabled: bool = None,
    ):
        self.description = description
        self.launch_expiration_time = launch_expiration_time
        self.launch_time = launch_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.recurrence_end_time = recurrence_end_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheduled_action = scheduled_action
        # This parameter is required.
        self.scheduled_task_id = scheduled_task_id
        self.scheduled_task_name = scheduled_task_name
        self.task_enabled = task_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')
        return self


class ModifyScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class RemoveInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class RemoveInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyAuthenticationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uid: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class VerifyAuthenticationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyAuthenticationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyAuthenticationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyAuthenticationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyUserRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class VerifyUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


