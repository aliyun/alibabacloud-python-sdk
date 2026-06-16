# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class StartInstanceRefreshRequest(DaraModel):
    def __init__(
        self,
        checkpoint_pause_time: int = None,
        checkpoints: List[main_models.StartInstanceRefreshRequestCheckpoints] = None,
        client_token: str = None,
        desired_configuration: main_models.StartInstanceRefreshRequestDesiredConfiguration = None,
        max_healthy_percentage: int = None,
        min_healthy_percentage: int = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        skip_matching: bool = None,
        strategy: str = None,
    ):
        # The duration for which the task is paused when a checkpoint is reached.
        # - Unit: minutes.
        # - Valid values: 1 to 2880.
        #  - Default value: 60.
        self.checkpoint_pause_time = checkpoint_pause_time
        # The checkpoints for the refresh task. When the percentage of new instances reaches a specified value during the instance refresh, the task is automatically paused for CheckpointPauseTime minutes.
        self.checkpoints = checkpoints
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # The desired configuration for the instance refresh.
        # 
        # > - You cannot specify ScalingConfigurationId, ImageId, LaunchTemplateId, and Containers at the same time. If this parameter is left empty, the currently active configuration of the scaling group is used for the refresh.
        # > - After the instance refresh task is completed, the active scaling configuration of the scaling group is updated to this configuration.
        self.desired_configuration = desired_configuration
        # The maximum percentage by which the number of instances in the scaling group can exceed the scaling group capacity during the instance refresh. Valid values: 100 to 200.
        # Default value: 120.
        # 
        # > When MinHealthyPercentage = MaxHealthyPercentage = 100, one instance is refreshed at a time.
        self.max_healthy_percentage = max_healthy_percentage
        # The minimum percentage of instances that must remain in service in the scaling group during the instance refresh. Valid values: 0 to 100.
        # Default value: 80.
        self.min_healthy_percentage = min_healthy_percentage
        self.owner_id = owner_id
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # Specifies whether to skip instances that already match the desired configuration.
        # 
        # > The system determines whether an instance matches based on the ID of the desired scaling configuration, not by comparing individual configuration items.
        # 
        # Valid values:
        # 
        # - true: Instances that were already created with the desired configuration are skipped.
        # - false: All instances in the scaling group are refreshed when the instance refresh task starts.
        # 
        # Default value: true.
        self.skip_matching = skip_matching
        self.strategy = strategy

    def validate(self):
        if self.checkpoints:
            for v1 in self.checkpoints:
                 if v1:
                    v1.validate()
        if self.desired_configuration:
            self.desired_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint_pause_time is not None:
            result['CheckpointPauseTime'] = self.checkpoint_pause_time

        result['Checkpoints'] = []
        if self.checkpoints is not None:
            for k1 in self.checkpoints:
                result['Checkpoints'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.desired_configuration is not None:
            result['DesiredConfiguration'] = self.desired_configuration.to_map()

        if self.max_healthy_percentage is not None:
            result['MaxHealthyPercentage'] = self.max_healthy_percentage

        if self.min_healthy_percentage is not None:
            result['MinHealthyPercentage'] = self.min_healthy_percentage

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.skip_matching is not None:
            result['SkipMatching'] = self.skip_matching

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckpointPauseTime') is not None:
            self.checkpoint_pause_time = m.get('CheckpointPauseTime')

        self.checkpoints = []
        if m.get('Checkpoints') is not None:
            for k1 in m.get('Checkpoints'):
                temp_model = main_models.StartInstanceRefreshRequestCheckpoints()
                self.checkpoints.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DesiredConfiguration') is not None:
            temp_model = main_models.StartInstanceRefreshRequestDesiredConfiguration()
            self.desired_configuration = temp_model.from_map(m.get('DesiredConfiguration'))

        if m.get('MaxHealthyPercentage') is not None:
            self.max_healthy_percentage = m.get('MaxHealthyPercentage')

        if m.get('MinHealthyPercentage') is not None:
            self.min_healthy_percentage = m.get('MinHealthyPercentage')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('SkipMatching') is not None:
            self.skip_matching = m.get('SkipMatching')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class StartInstanceRefreshRequestDesiredConfiguration(DaraModel):
    def __init__(
        self,
        containers: List[main_models.StartInstanceRefreshRequestDesiredConfigurationContainers] = None,
        image_id: str = None,
        launch_template_id: str = None,
        launch_template_overrides: List[main_models.StartInstanceRefreshRequestDesiredConfigurationLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        scaling_configuration_id: str = None,
    ):
        # The list of containers included in the instance.
        # 
        # > - This parameter is supported only for Elastic Container Instance (ECI) scaling groups.
        # > - Only the container configurations that match `Container.Name` in the current scaling configuration container list are refreshed.
        self.containers = containers
        # The image ID.
        # 
        # 
        # 
        # > - After the instance refresh task is completed, the image in the currently active configuration of the scaling group is updated to this image.
        # > - This parameter is not supported when the instance configuration source of the scaling group is a launch template.
        self.image_id = image_id
        # The ID of the launch template from which the scaling group obtains launch configuration information.
        self.launch_template_id = launch_template_id
        # The instance type information that overrides the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version of the launch template. Valid values:
        # 
        # - A fixed template version number.
        # - Default: always uses the default version of the template.
        # - Latest: always uses the latest version of the template.
        # 
        # > When the version is set to Default or Latest, the instance refresh task does not support rollback.
        self.launch_template_version = launch_template_version
        # The ID of the scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id

    def validate(self):
        if self.containers:
            for v1 in self.containers:
                 if v1:
                    v1.validate()
        if self.launch_template_overrides:
            for v1 in self.launch_template_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Containers'] = []
        if self.containers is not None:
            for k1 in self.containers:
                result['Containers'].append(k1.to_map() if k1 else None)

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k1 in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k1.to_map() if k1 else None)

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.containers = []
        if m.get('Containers') is not None:
            for k1 in m.get('Containers'):
                temp_model = main_models.StartInstanceRefreshRequestDesiredConfigurationContainers()
                self.containers.append(temp_model.from_map(k1))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k1 in m.get('LaunchTemplateOverrides'):
                temp_model = main_models.StartInstanceRefreshRequestDesiredConfigurationLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k1))

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        return self

class StartInstanceRefreshRequestDesiredConfigurationLaunchTemplateOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        # The instance type that overrides the instance type specified in the launch template.
        # 
        # > This parameter takes effect only when the LaunchTemplateId parameter specifies a launch template.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

class StartInstanceRefreshRequestDesiredConfigurationContainers(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        commands: List[str] = None,
        environment_vars: List[main_models.StartInstanceRefreshRequestDesiredConfigurationContainersEnvironmentVars] = None,
        image: str = None,
        name: str = None,
    ):
        # The arguments of the container startup command. You can specify up to 10 arguments.
        self.args = args
        # The startup commands of the container. You can specify up to 20 commands. Each command can contain up to 256 characters.
        self.commands = commands
        # The environment variable information.
        self.environment_vars = environment_vars
        # The container image.
        self.image = image
        # The custom container name.
        self.name = name

    def validate(self):
        if self.environment_vars:
            for v1 in self.environment_vars:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.commands is not None:
            result['Commands'] = self.commands

        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k1 in self.environment_vars:
                result['EnvironmentVars'].append(k1.to_map() if k1 else None)

        if self.image is not None:
            result['Image'] = self.image

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k1 in m.get('EnvironmentVars'):
                temp_model = main_models.StartInstanceRefreshRequestDesiredConfigurationContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k1))

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class StartInstanceRefreshRequestDesiredConfigurationContainersEnvironmentVars(DaraModel):
    def __init__(
        self,
        field_ref_field_path: str = None,
        key: str = None,
        value: str = None,
    ):
        # > This parameter is not available for use.
        self.field_ref_field_path = field_ref_field_path
        # The name of the environment variable. The name must be 1 to 128 characters in length and can contain digits, letters, and underscores (_). It cannot start with a digit.
        self.key = key
        # The value of the environment variable. The value can be 0 to 256 characters in length.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_ref_field_path is not None:
            result['FieldRefFieldPath'] = self.field_ref_field_path

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRefFieldPath') is not None:
            self.field_ref_field_path = m.get('FieldRefFieldPath')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class StartInstanceRefreshRequestCheckpoints(DaraModel):
    def __init__(
        self,
        percentage: int = None,
    ):
        # The percentage of new instances relative to the total number of instances in the scaling group. The task is automatically paused when this percentage is reached. Valid values: 1 to 100 (%).
        # 
        # > The values must be specified in ascending order, and the last value must be 100.
        self.percentage = percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.percentage is not None:
            result['Percentage'] = self.percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        return self

