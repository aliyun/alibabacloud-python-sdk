# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeEnvironmentFeatureResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeEnvironmentFeatureResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The struct returned.
        self.data = data
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeEnvironmentFeatureResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeEnvironmentFeatureResponseBodyData(DaraModel):
    def __init__(
        self,
        feature: main_models.DescribeEnvironmentFeatureResponseBodyDataFeature = None,
        feature_status: main_models.DescribeEnvironmentFeatureResponseBodyDataFeatureStatus = None,
        config: str = None,
    ):
        # The installation information about the feature.
        self.feature = feature
        # The status of the feature.
        self.feature_status = feature_status
        # The feature configurations.
        self.config = config

    def validate(self):
        if self.feature:
            self.feature.validate()
        if self.feature_status:
            self.feature_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature is not None:
            result['Feature'] = self.feature.to_map()

        if self.feature_status is not None:
            result['FeatureStatus'] = self.feature_status.to_map()

        if self.config is not None:
            result['config'] = self.config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feature') is not None:
            temp_model = main_models.DescribeEnvironmentFeatureResponseBodyDataFeature()
            self.feature = temp_model.from_map(m.get('Feature'))

        if m.get('FeatureStatus') is not None:
            temp_model = main_models.DescribeEnvironmentFeatureResponseBodyDataFeatureStatus()
            self.feature_status = temp_model.from_map(m.get('FeatureStatus'))

        if m.get('config') is not None:
            self.config = m.get('config')

        return self

class DescribeEnvironmentFeatureResponseBodyDataFeatureStatus(DaraModel):
    def __init__(
        self,
        bind_resource_id: str = None,
        feature_containers: List[main_models.DescribeEnvironmentFeatureResponseBodyDataFeatureStatusFeatureContainers] = None,
        ips: List[str] = None,
        name: str = None,
        namespace: str = None,
        security_group_id: str = None,
        status: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the resource.
        self.bind_resource_id = bind_resource_id
        # The containers of the feature.
        self.feature_containers = feature_containers
        # The IP address of the pod.
        self.ips = ips
        # The Kubernetes resource name of the feature.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The status of the agent. Valid values:
        # 
        # *   Success: The agent is running.
        # *   Failed: The agent failed to run.
        # *   Not Found: The agent is not installed.
        self.status = status
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.feature_containers:
            for v1 in self.feature_containers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_resource_id is not None:
            result['BindResourceId'] = self.bind_resource_id

        result['FeatureContainers'] = []
        if self.feature_containers is not None:
            for k1 in self.feature_containers:
                result['FeatureContainers'].append(k1.to_map() if k1 else None)

        if self.ips is not None:
            result['Ips'] = self.ips

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindResourceId') is not None:
            self.bind_resource_id = m.get('BindResourceId')

        self.feature_containers = []
        if m.get('FeatureContainers') is not None:
            for k1 in m.get('FeatureContainers'):
                temp_model = main_models.DescribeEnvironmentFeatureResponseBodyDataFeatureStatusFeatureContainers()
                self.feature_containers.append(temp_model.from_map(k1))

        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeEnvironmentFeatureResponseBodyDataFeatureStatusFeatureContainers(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        image: str = None,
        name: str = None,
    ):
        # The container parameters.
        self.args = args
        # The container image.
        self.image = image
        # The container name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.image is not None:
            result['Image'] = self.image

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeEnvironmentFeatureResponseBodyDataFeature(DaraModel):
    def __init__(
        self,
        alias: str = None,
        config: Dict[str, str] = None,
        description: str = None,
        environment_id: str = None,
        icon: str = None,
        language: str = None,
        latest_version: str = None,
        managed: bool = None,
        name: str = None,
        status: str = None,
        version: str = None,
    ):
        # The alias of the feature.
        self.alias = alias
        # The configuration of the feature.
        self.config = config
        # The description of the feature.
        self.description = description
        # The environment ID.
        self.environment_id = environment_id
        # The URL of the icon.
        self.icon = icon
        # The language.
        self.language = language
        # The latest version number.
        self.latest_version = latest_version
        # Indicates whether the component is fully managed.
        self.managed = managed
        # The name of the feature.
        self.name = name
        # The installation status of the agent.
        # 
        # *   Installing: The agent is being installed.
        # *   Success: The agent is installed.
        # *   Failed: The agent failed to be installed.
        # *   UnInstall: The agent is uninstalled or has not been installed.
        # *   Uninstalling: The agent is being uninstalled.
        # *   UnInstallFailed: The agent failed to be uninstalled.
        self.status = status
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.language is not None:
            result['Language'] = self.language

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.managed is not None:
            result['Managed'] = self.managed

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('Managed') is not None:
            self.managed = m.get('Managed')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

