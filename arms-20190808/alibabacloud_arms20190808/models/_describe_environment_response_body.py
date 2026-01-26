# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeEnvironmentResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeEnvironmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnvironmentResponseBodyData(DaraModel):
    def __init__(
        self,
        bind_resource_id: str = None,
        bind_resource_profile: str = None,
        bind_resource_status: str = None,
        bind_resource_store_duration: str = None,
        bind_resource_type: str = None,
        bind_vpc_cidr: str = None,
        db_instance_status: str = None,
        environment_id: str = None,
        environment_name: str = None,
        environment_sub_type: str = None,
        environment_type: str = None,
        fee_package: str = None,
        grafa_data_source_name: str = None,
        grafana_datasource_uid: str = None,
        grafana_folder_title: str = None,
        grafana_folder_uid: str = None,
        grafana_folder_url: str = None,
        grafana_workspace_id: str = None,
        managed_type: str = None,
        prometheus_instance_id: str = None,
        prometheus_instance_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        tags: List[main_models.DescribeEnvironmentResponseBodyDataTags] = None,
        user_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # The ID of the resource associated with the environment, such as the ACK cluster ID or VPC ID.
        self.bind_resource_id = bind_resource_id
        # The profile of the resource.
        self.bind_resource_profile = bind_resource_profile
        # The status of the resource.
        self.bind_resource_status = bind_resource_status
        # The retention period of the resource. Unit: days.
        self.bind_resource_store_duration = bind_resource_store_duration
        # The resource type.
        self.bind_resource_type = bind_resource_type
        # The VPC CIDR block.
        self.bind_vpc_cidr = bind_vpc_cidr
        # The status of the database that is bound to the Prometheus instance.
        # 
        # Valid values:
        # 
        # *   UNINSTALLING
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   INSTALLING
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   UNINSTALLED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   RUNNING
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   MODIFYING
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.db_instance_status = db_instance_status
        # The ID of the environment instance.
        self.environment_id = environment_id
        # The environment name.
        self.environment_name = environment_name
        # Environment subtypes:
        # - CS: Currently supports ACK.
        # - ECS: ECS is currently supported.
        # - Cloud: Currently supports Cloud.
        self.environment_sub_type = environment_sub_type
        # The type of the environment. Valid values:
        # 
        # *   CS: Container Service for Kubernetes (ACK)
        # *   ECS: Elastic Compute Service
        # *   Cloud: cloud service
        self.environment_type = environment_type
        # The payable resource plan. Valid values:
        # 
        # *   If the EnvironmentType parameter is set to CS, set the value to CS_Basic or CS_Pro.
        # *   Otherwise, leave the parameter empty.
        self.fee_package = fee_package
        # The name of the Grafana data source.
        self.grafa_data_source_name = grafa_data_source_name
        # The unique ID of the Grafana data source.
        self.grafana_datasource_uid = grafana_datasource_uid
        # The name of the Grafana directory.
        self.grafana_folder_title = grafana_folder_title
        # The unique ID of the Grafana directory.
        self.grafana_folder_uid = grafana_folder_uid
        # The URL of the Grafana directory.
        self.grafana_folder_url = grafana_folder_url
        # The ID of the Grafana workspace.
        self.grafana_workspace_id = grafana_workspace_id
        # managed type:
        # - none: unmanaged. The default value for ACK clusters.
        # - agent: managed agent (including KSM). The default values for ASK, ACS, and AckOne clusters.
        # - agent-exporter: managed agent and exporters. The default value for the cloud service type.
        self.managed_type = managed_type
        # The ID of the Prometheus instance.
        self.prometheus_instance_id = prometheus_instance_id
        # The name of the Prometheus instance.
        self.prometheus_instance_name = prometheus_instance_name
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the security group associated with the environment.
        self.security_group_id = security_group_id
        # The tags.
        self.tags = tags
        # The user ID.
        self.user_id = user_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The ID of the vSwitch associated with the environment.
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_resource_id is not None:
            result['BindResourceId'] = self.bind_resource_id

        if self.bind_resource_profile is not None:
            result['BindResourceProfile'] = self.bind_resource_profile

        if self.bind_resource_status is not None:
            result['BindResourceStatus'] = self.bind_resource_status

        if self.bind_resource_store_duration is not None:
            result['BindResourceStoreDuration'] = self.bind_resource_store_duration

        if self.bind_resource_type is not None:
            result['BindResourceType'] = self.bind_resource_type

        if self.bind_vpc_cidr is not None:
            result['BindVpcCidr'] = self.bind_vpc_cidr

        if self.db_instance_status is not None:
            result['DbInstanceStatus'] = self.db_instance_status

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.environment_name is not None:
            result['EnvironmentName'] = self.environment_name

        if self.environment_sub_type is not None:
            result['EnvironmentSubType'] = self.environment_sub_type

        if self.environment_type is not None:
            result['EnvironmentType'] = self.environment_type

        if self.fee_package is not None:
            result['FeePackage'] = self.fee_package

        if self.grafa_data_source_name is not None:
            result['GrafaDataSourceName'] = self.grafa_data_source_name

        if self.grafana_datasource_uid is not None:
            result['GrafanaDatasourceUid'] = self.grafana_datasource_uid

        if self.grafana_folder_title is not None:
            result['GrafanaFolderTitle'] = self.grafana_folder_title

        if self.grafana_folder_uid is not None:
            result['GrafanaFolderUid'] = self.grafana_folder_uid

        if self.grafana_folder_url is not None:
            result['GrafanaFolderUrl'] = self.grafana_folder_url

        if self.grafana_workspace_id is not None:
            result['GrafanaWorkspaceId'] = self.grafana_workspace_id

        if self.managed_type is not None:
            result['ManagedType'] = self.managed_type

        if self.prometheus_instance_id is not None:
            result['PrometheusInstanceId'] = self.prometheus_instance_id

        if self.prometheus_instance_name is not None:
            result['PrometheusInstanceName'] = self.prometheus_instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindResourceId') is not None:
            self.bind_resource_id = m.get('BindResourceId')

        if m.get('BindResourceProfile') is not None:
            self.bind_resource_profile = m.get('BindResourceProfile')

        if m.get('BindResourceStatus') is not None:
            self.bind_resource_status = m.get('BindResourceStatus')

        if m.get('BindResourceStoreDuration') is not None:
            self.bind_resource_store_duration = m.get('BindResourceStoreDuration')

        if m.get('BindResourceType') is not None:
            self.bind_resource_type = m.get('BindResourceType')

        if m.get('BindVpcCidr') is not None:
            self.bind_vpc_cidr = m.get('BindVpcCidr')

        if m.get('DbInstanceStatus') is not None:
            self.db_instance_status = m.get('DbInstanceStatus')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('EnvironmentName') is not None:
            self.environment_name = m.get('EnvironmentName')

        if m.get('EnvironmentSubType') is not None:
            self.environment_sub_type = m.get('EnvironmentSubType')

        if m.get('EnvironmentType') is not None:
            self.environment_type = m.get('EnvironmentType')

        if m.get('FeePackage') is not None:
            self.fee_package = m.get('FeePackage')

        if m.get('GrafaDataSourceName') is not None:
            self.grafa_data_source_name = m.get('GrafaDataSourceName')

        if m.get('GrafanaDatasourceUid') is not None:
            self.grafana_datasource_uid = m.get('GrafanaDatasourceUid')

        if m.get('GrafanaFolderTitle') is not None:
            self.grafana_folder_title = m.get('GrafanaFolderTitle')

        if m.get('GrafanaFolderUid') is not None:
            self.grafana_folder_uid = m.get('GrafanaFolderUid')

        if m.get('GrafanaFolderUrl') is not None:
            self.grafana_folder_url = m.get('GrafanaFolderUrl')

        if m.get('GrafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('GrafanaWorkspaceId')

        if m.get('ManagedType') is not None:
            self.managed_type = m.get('ManagedType')

        if m.get('PrometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('PrometheusInstanceId')

        if m.get('PrometheusInstanceName') is not None:
            self.prometheus_instance_name = m.get('PrometheusInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeEnvironmentResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class DescribeEnvironmentResponseBodyDataTags(DaraModel):
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

