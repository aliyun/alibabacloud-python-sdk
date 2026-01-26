# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEnvironmentsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListEnvironmentsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.ListEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEnvironmentsResponseBodyData(DaraModel):
    def __init__(
        self,
        environments: List[main_models.ListEnvironmentsResponseBodyDataEnvironments] = None,
        total: int = None,
    ):
        # The queried environments.
        self.environments = environments
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.environments:
            for v1 in self.environments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Environments'] = []
        if self.environments is not None:
            for k1 in self.environments:
                result['Environments'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.environments = []
        if m.get('Environments') is not None:
            for k1 in m.get('Environments'):
                temp_model = main_models.ListEnvironmentsResponseBodyDataEnvironments()
                self.environments.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListEnvironmentsResponseBodyDataEnvironments(DaraModel):
    def __init__(
        self,
        addons: List[main_models.ListEnvironmentsResponseBodyDataEnvironmentsAddons] = None,
        bind_resource_id: str = None,
        bind_resource_profile: str = None,
        bind_resource_type: str = None,
        bind_vpc_cidr: str = None,
        create_time: str = None,
        created_user_id: str = None,
        environment_id: str = None,
        environment_name: str = None,
        environment_type: str = None,
        features: List[main_models.ListEnvironmentsResponseBodyDataEnvironmentsFeatures] = None,
        fee_package: str = None,
        grafana_datasource_uid: str = None,
        grafana_folder_title: str = None,
        grafana_folder_uid: str = None,
        latest_release_create_time: str = None,
        managed_type: str = None,
        prometheus_id: int = None,
        prometheus_instance_id: str = None,
        region_id: str = None,
        release_count: int = None,
        resource_group_id: str = None,
        tags: List[main_models.ListEnvironmentsResponseBodyDataEnvironmentsTags] = None,
        user_id: str = None,
    ):
        # The add-ons.
        self.addons = addons
        # The ID of the resource bound to the environment instance. The resource can be a Kubernetes cluster or a VPC.
        self.bind_resource_id = bind_resource_id
        # The profile that is bound to the resource.
        self.bind_resource_profile = bind_resource_profile
        # The resource type.
        self.bind_resource_type = bind_resource_type
        # The CIDR block that is bound to the VPC.
        self.bind_vpc_cidr = bind_vpc_cidr
        # The time when the environment instance was created.
        self.create_time = create_time
        # The user ID.
        self.created_user_id = created_user_id
        # The ID of the environment instance.
        self.environment_id = environment_id
        # The name of the environment instance.
        self.environment_name = environment_name
        # The type of the environment instance. Valid values:
        # 
        # *   CS: Container Service
        # *   ECS: Elastic Compute Service
        # *   Cloud: cloud service
        self.environment_type = environment_type
        # The parameters of the feature.
        self.features = features
        # The payable resource plan.
        # 
        # *   If the EnvironmentType parameter is set to CS, set the value to CS_Basic or CS_Pro.
        # *   Otherwise, leave the parameter empty.
        self.fee_package = fee_package
        # The unique ID of the Grafana data source.
        self.grafana_datasource_uid = grafana_datasource_uid
        # The name of the Grafana directory.
        self.grafana_folder_title = grafana_folder_title
        # The unique ID of the Grafana directory.
        self.grafana_folder_uid = grafana_folder_uid
        # The time when the last add-on was created.
        self.latest_release_create_time = latest_release_create_time
        # Indicates whether agents or exporters are managed. Valid values:
        # 
        # *   none: No. By default, no managed agents or exporters are provided for ACK clusters.
        # *   agent: Agents are managed. By default, managed agents are provided for ASK clusters, ACS clusters, and ACK One clusters.
        # *   agent-exproter: Agents and exporters are managed. By default, managed agents and exporters are provided for cloud services.
        self.managed_type = managed_type
        # The Prometheus ID.
        self.prometheus_id = prometheus_id
        # The ID of the Prometheus instance.
        self.prometheus_instance_id = prometheus_instance_id
        # The region ID.
        self.region_id = region_id
        # The number of installed add-ons.
        self.release_count = release_count
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the environment resource.
        self.tags = tags
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.addons:
            for v1 in self.addons:
                 if v1:
                    v1.validate()
        if self.features:
            for v1 in self.features:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addons'] = []
        if self.addons is not None:
            for k1 in self.addons:
                result['Addons'].append(k1.to_map() if k1 else None)

        if self.bind_resource_id is not None:
            result['BindResourceId'] = self.bind_resource_id

        if self.bind_resource_profile is not None:
            result['BindResourceProfile'] = self.bind_resource_profile

        if self.bind_resource_type is not None:
            result['BindResourceType'] = self.bind_resource_type

        if self.bind_vpc_cidr is not None:
            result['BindVpcCidr'] = self.bind_vpc_cidr

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_user_id is not None:
            result['CreatedUserId'] = self.created_user_id

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.environment_name is not None:
            result['EnvironmentName'] = self.environment_name

        if self.environment_type is not None:
            result['EnvironmentType'] = self.environment_type

        result['Features'] = []
        if self.features is not None:
            for k1 in self.features:
                result['Features'].append(k1.to_map() if k1 else None)

        if self.fee_package is not None:
            result['FeePackage'] = self.fee_package

        if self.grafana_datasource_uid is not None:
            result['GrafanaDatasourceUid'] = self.grafana_datasource_uid

        if self.grafana_folder_title is not None:
            result['GrafanaFolderTitle'] = self.grafana_folder_title

        if self.grafana_folder_uid is not None:
            result['GrafanaFolderUid'] = self.grafana_folder_uid

        if self.latest_release_create_time is not None:
            result['LatestReleaseCreateTime'] = self.latest_release_create_time

        if self.managed_type is not None:
            result['ManagedType'] = self.managed_type

        if self.prometheus_id is not None:
            result['PrometheusId'] = self.prometheus_id

        if self.prometheus_instance_id is not None:
            result['PrometheusInstanceId'] = self.prometheus_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_count is not None:
            result['ReleaseCount'] = self.release_count

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addons = []
        if m.get('Addons') is not None:
            for k1 in m.get('Addons'):
                temp_model = main_models.ListEnvironmentsResponseBodyDataEnvironmentsAddons()
                self.addons.append(temp_model.from_map(k1))

        if m.get('BindResourceId') is not None:
            self.bind_resource_id = m.get('BindResourceId')

        if m.get('BindResourceProfile') is not None:
            self.bind_resource_profile = m.get('BindResourceProfile')

        if m.get('BindResourceType') is not None:
            self.bind_resource_type = m.get('BindResourceType')

        if m.get('BindVpcCidr') is not None:
            self.bind_vpc_cidr = m.get('BindVpcCidr')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedUserId') is not None:
            self.created_user_id = m.get('CreatedUserId')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('EnvironmentName') is not None:
            self.environment_name = m.get('EnvironmentName')

        if m.get('EnvironmentType') is not None:
            self.environment_type = m.get('EnvironmentType')

        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.ListEnvironmentsResponseBodyDataEnvironmentsFeatures()
                self.features.append(temp_model.from_map(k1))

        if m.get('FeePackage') is not None:
            self.fee_package = m.get('FeePackage')

        if m.get('GrafanaDatasourceUid') is not None:
            self.grafana_datasource_uid = m.get('GrafanaDatasourceUid')

        if m.get('GrafanaFolderTitle') is not None:
            self.grafana_folder_title = m.get('GrafanaFolderTitle')

        if m.get('GrafanaFolderUid') is not None:
            self.grafana_folder_uid = m.get('GrafanaFolderUid')

        if m.get('LatestReleaseCreateTime') is not None:
            self.latest_release_create_time = m.get('LatestReleaseCreateTime')

        if m.get('ManagedType') is not None:
            self.managed_type = m.get('ManagedType')

        if m.get('PrometheusId') is not None:
            self.prometheus_id = m.get('PrometheusId')

        if m.get('PrometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('PrometheusInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseCount') is not None:
            self.release_count = m.get('ReleaseCount')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListEnvironmentsResponseBodyDataEnvironmentsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListEnvironmentsResponseBodyDataEnvironmentsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListEnvironmentsResponseBodyDataEnvironmentsFeatures(DaraModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        icon: str = None,
        name: str = None,
    ):
        # The alias of the feature.
        self.alias = alias
        # The description of the feature.
        self.description = description
        # The URL of the icon.
        self.icon = icon
        # The name of the feature.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListEnvironmentsResponseBodyDataEnvironmentsAddons(DaraModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        icon: str = None,
        name: str = None,
    ):
        # The alias of the add-on.
        self.alias = alias
        # The description of the add-on.
        self.description = description
        # The URL of the icon.
        self.icon = icon
        # The name of the add-on.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

