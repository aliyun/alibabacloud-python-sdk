# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class GetServiceInstanceResponseBody(DaraModel):
    def __init__(
        self,
        biz_status: str = None,
        create_time: str = None,
        enable_instance_ops: bool = None,
        enable_user_prometheus: bool = None,
        end_time: str = None,
        grafana_dash_board_url: str = None,
        granted_permission: main_models.GetServiceInstanceResponseBodyGrantedPermission = None,
        is_operated: bool = None,
        license_metadata: str = None,
        name: str = None,
        network_config: main_models.GetServiceInstanceResponseBodyNetworkConfig = None,
        operated_service_instance_id: str = None,
        operation_end_time: str = None,
        operation_extra_info: str = None,
        operation_start_time: str = None,
        outputs: str = None,
        parameters: str = None,
        pay_type: str = None,
        policy_names: str = None,
        predefined_parameter_name: str = None,
        progress: int = None,
        rd_account_login_url: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resources: str = None,
        service: main_models.GetServiceInstanceResponseBodyService = None,
        service_instance_id: str = None,
        service_type: str = None,
        source: str = None,
        status: str = None,
        status_detail: str = None,
        supplier_uid: int = None,
        tags: List[main_models.GetServiceInstanceResponseBodyTags] = None,
        template_name: str = None,
        update_time: str = None,
        user_id: int = None,
    ):
        # The business status of the service instance. Valid values:
        # 
        # *   Normal: The service instance is normal.
        # *   Renewing: The service instance is being renewed.
        # *   RenewFailed: The service instance failed to be renewed.
        # *   Expired: The service instance expired.
        self.biz_status = biz_status
        # The time when the service instance was created.
        self.create_time = create_time
        # Indicates whether the service instance supports the hosted O\\&M feature. Valid values:
        # 
        # *   true
        # *   false
        self.enable_instance_ops = enable_instance_ops
        # Indicates whether the Prometheus monitoring feature is enabled on the user side.
        self.enable_user_prometheus = enable_user_prometheus
        # The time when the service instance expires.
        self.end_time = end_time
        # The URL of the Grafana dashboard.
        self.grafana_dash_board_url = grafana_dash_board_url
        self.granted_permission = granted_permission
        # Indicates whether the hosted O\\&M feature is enabled for the service instance. Valid values:
        # 
        # *   true
        # *   false
        self.is_operated = is_operated
        # The license metadata.
        self.license_metadata = license_metadata
        # The name of the service instance.
        self.name = name
        # The network configurations.
        # 
        # >  This parameter is discontinued.
        self.network_config = network_config
        # The ID of the service instance that is used to implement hosted O\\&M.
        self.operated_service_instance_id = operated_service_instance_id
        # The end of the time range during which hosted O\\&M is implemented.
        self.operation_end_time = operation_end_time
        # Operate extra info
        self.operation_extra_info = operation_extra_info
        # The beginning of the time range during which hosted O\\&M is implemented.
        self.operation_start_time = operation_start_time
        # The outputs returned from creating the service instance.
        # 
        # *   If the service is deployed by using a ROS template, all output fields of the template are returned.
        # *   If the service is deployed by calling an SPI operation, the output fields of the service provider and for the Compute Nest additional features are returned.
        self.outputs = outputs
        # The parameters that are specified to deploy the service instance.
        self.parameters = parameters
        # The billing method of the service. Valid values:
        # 
        # *   Permanent: Once you purchase the service, you can use it permanently.
        # *   Subscription: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a subscription basis.
        # *   PayAsYouGo: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a pay-as-you-go basis.
        # *   CustomFixTime: You are charged for the service based on a custom duration fixed by the service provider.
        self.pay_type = pay_type
        self.policy_names = policy_names
        # The package name.
        self.predefined_parameter_name = predefined_parameter_name
        # The deployment progress of the service instance. Unit: percentage.
        self.progress = progress
        # The logon URL for the accounts in the resource directory corresponding to the service instance.
        self.rd_account_login_url = rd_account_login_url
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The list of resources.
        self.resources = resources
        # The information about the service to which the service instance belongs.
        self.service = service
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        # *   poc: The service is a trial service.
        self.service_type = service_type
        # The source of the service instance. Valid values:
        # 
        # *   User: Compute Nest customer
        # *   Market: Alibaba Cloud Marketplace
        # *   Supplier: Compute Nest service provider
        self.source = source
        # The deployment state of the service instance. Valid values:
        # 
        # *   Created
        # *   Deploying
        # *   DeployedFailed
        # *   Deployed
        # *   Upgrading
        # *   Deleting
        # *   Deleted
        # *   DeletedFailed
        self.status = status
        # The description of the deployment state of the service instance.
        self.status_detail = status_detail
        # The Alibaba Cloud account ID of the service provider.
        self.supplier_uid = supplier_uid
        # The custom tags.
        self.tags = tags
        # The template name.
        self.template_name = template_name
        # The time when the service instance was updated.
        self.update_time = update_time
        # The Alibaba Cloud account ID of the user.
        self.user_id = user_id

    def validate(self):
        if self.granted_permission:
            self.granted_permission.validate()
        if self.network_config:
            self.network_config.validate()
        if self.service:
            self.service.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops

        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.grafana_dash_board_url is not None:
            result['GrafanaDashBoardUrl'] = self.grafana_dash_board_url

        if self.granted_permission is not None:
            result['GrantedPermission'] = self.granted_permission.to_map()

        if self.is_operated is not None:
            result['IsOperated'] = self.is_operated

        if self.license_metadata is not None:
            result['LicenseMetadata'] = self.license_metadata

        if self.name is not None:
            result['Name'] = self.name

        if self.network_config is not None:
            result['NetworkConfig'] = self.network_config.to_map()

        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id

        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time

        if self.operation_extra_info is not None:
            result['OperationExtraInfo'] = self.operation_extra_info

        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names

        if self.predefined_parameter_name is not None:
            result['PredefinedParameterName'] = self.predefined_parameter_name

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.rd_account_login_url is not None:
            result['RdAccountLoginUrl'] = self.rd_account_login_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.service is not None:
            result['Service'] = self.service.to_map()

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail

        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')

        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GrafanaDashBoardUrl') is not None:
            self.grafana_dash_board_url = m.get('GrafanaDashBoardUrl')

        if m.get('GrantedPermission') is not None:
            temp_model = main_models.GetServiceInstanceResponseBodyGrantedPermission()
            self.granted_permission = temp_model.from_map(m.get('GrantedPermission'))

        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')

        if m.get('LicenseMetadata') is not None:
            self.license_metadata = m.get('LicenseMetadata')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkConfig') is not None:
            temp_model = main_models.GetServiceInstanceResponseBodyNetworkConfig()
            self.network_config = temp_model.from_map(m.get('NetworkConfig'))

        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')

        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')

        if m.get('OperationExtraInfo') is not None:
            self.operation_extra_info = m.get('OperationExtraInfo')

        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')

        if m.get('PredefinedParameterName') is not None:
            self.predefined_parameter_name = m.get('PredefinedParameterName')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RdAccountLoginUrl') is not None:
            self.rd_account_login_url = m.get('RdAccountLoginUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('Service') is not None:
            temp_model = main_models.GetServiceInstanceResponseBodyService()
            self.service = temp_model.from_map(m.get('Service'))

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')

        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetServiceInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetServiceInstanceResponseBodyTags(DaraModel):
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

class GetServiceInstanceResponseBodyService(DaraModel):
    def __init__(
        self,
        deploy_metadata: str = None,
        deploy_type: str = None,
        publish_time: str = None,
        service_doc_url: str = None,
        service_id: str = None,
        service_infos: List[main_models.GetServiceInstanceResponseBodyServiceServiceInfos] = None,
        service_product_url: str = None,
        service_type: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        upgradable_service_infos: List[main_models.GetServiceInstanceResponseBodyServiceUpgradableServiceInfos] = None,
        upgradable_service_versions: List[str] = None,
        version: str = None,
        version_name: str = None,
    ):
        # The storage configurations of the service. The format in which the deployment information of a service is stored varies based on the deployment type of the service. In this case, the deployment information is stored in the JSON string format.
        self.deploy_metadata = deploy_metadata
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        # *   ack: The service is deployed by using Container Service for Kubernetes (ACK).
        # *   spi: The service is deployed by calling a service provider interface (SPI).
        # *   operation: The service is deployed by using a hosted O\\&M service.
        self.deploy_type = deploy_type
        # The time when the service was published.
        self.publish_time = publish_time
        # The URL of the service documentation.
        self.service_doc_url = service_doc_url
        # The service ID.
        self.service_id = service_id
        # The information about the service.
        self.service_infos = service_infos
        # The URL of the service page.
        self.service_product_url = service_product_url
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        self.service_type = service_type
        # The status of the service. Valid values:
        # 
        # Draft: The registration request of the service is pending to be submitted.
        # 
        # Submitted: The registration request of the service is submitted.
        # 
        # Approved: The registration request of the service is approved.
        # 
        # Online: The service is published.
        # 
        # Offline: The service is unpublished.
        # 
        # Deleted: The service is deleted.
        # 
        # Launching: The service is being published.
        self.status = status
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # The upgradable service Info.
        self.upgradable_service_infos = upgradable_service_infos
        # The service versions that can be updated.
        self.upgradable_service_versions = upgradable_service_versions
        # The service version.
        self.version = version
        # The custom version name defined by the service provider.
        self.version_name = version_name

    def validate(self):
        if self.service_infos:
            for v1 in self.service_infos:
                 if v1:
                    v1.validate()
        if self.upgradable_service_infos:
            for v1 in self.upgradable_service_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.service_doc_url is not None:
            result['ServiceDocUrl'] = self.service_doc_url

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k1 in self.service_infos:
                result['ServiceInfos'].append(k1.to_map() if k1 else None)

        if self.service_product_url is not None:
            result['ServiceProductUrl'] = self.service_product_url

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url

        result['UpgradableServiceInfos'] = []
        if self.upgradable_service_infos is not None:
            for k1 in self.upgradable_service_infos:
                result['UpgradableServiceInfos'].append(k1.to_map() if k1 else None)

        if self.upgradable_service_versions is not None:
            result['UpgradableServiceVersions'] = self.upgradable_service_versions

        if self.version is not None:
            result['Version'] = self.version

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('ServiceDocUrl') is not None:
            self.service_doc_url = m.get('ServiceDocUrl')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k1 in m.get('ServiceInfos'):
                temp_model = main_models.GetServiceInstanceResponseBodyServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k1))

        if m.get('ServiceProductUrl') is not None:
            self.service_product_url = m.get('ServiceProductUrl')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')

        self.upgradable_service_infos = []
        if m.get('UpgradableServiceInfos') is not None:
            for k1 in m.get('UpgradableServiceInfos'):
                temp_model = main_models.GetServiceInstanceResponseBodyServiceUpgradableServiceInfos()
                self.upgradable_service_infos.append(temp_model.from_map(k1))

        if m.get('UpgradableServiceVersions') is not None:
            self.upgradable_service_versions = m.get('UpgradableServiceVersions')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class GetServiceInstanceResponseBodyServiceUpgradableServiceInfos(DaraModel):
    def __init__(
        self,
        version: str = None,
        version_name: str = None,
    ):
        # The upgradable service version.
        self.version = version
        # The version name of an upgradable service version.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.version is not None:
            result['Version'] = self.version

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class GetServiceInstanceResponseBodyServiceServiceInfos(DaraModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
    ):
        # The URL of the service icon.
        self.image = image
        # The language of the service instance.
        self.locale = locale
        # The service name.
        self.name = name
        # The description of the service.
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['Image'] = self.image

        if self.locale is not None:
            result['Locale'] = self.locale

        if self.name is not None:
            result['Name'] = self.name

        if self.short_description is not None:
            result['ShortDescription'] = self.short_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')

        return self

class GetServiceInstanceResponseBodyNetworkConfig(DaraModel):
    def __init__(
        self,
        endpoint_id: str = None,
        endpoint_service_id: str = None,
        private_vpc_connections: List[main_models.GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections] = None,
        reverse_private_vpc_connections: List[main_models.GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections] = None,
    ):
        # The ID of the endpoint for the private connection.
        # 
        # >  This parameter is discontinued.
        self.endpoint_id = endpoint_id
        # The ID of the endpoint service for the private connection.
        # 
        # >  This parameter is discontinued.
        self.endpoint_service_id = endpoint_service_id
        # The information about private connections.
        self.private_vpc_connections = private_vpc_connections
        # The information about the reverse private connection.
        self.reverse_private_vpc_connections = reverse_private_vpc_connections

    def validate(self):
        if self.private_vpc_connections:
            for v1 in self.private_vpc_connections:
                 if v1:
                    v1.validate()
        if self.reverse_private_vpc_connections:
            for v1 in self.reverse_private_vpc_connections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_service_id is not None:
            result['EndpointServiceId'] = self.endpoint_service_id

        result['PrivateVpcConnections'] = []
        if self.private_vpc_connections is not None:
            for k1 in self.private_vpc_connections:
                result['PrivateVpcConnections'].append(k1.to_map() if k1 else None)

        result['ReversePrivateVpcConnections'] = []
        if self.reverse_private_vpc_connections is not None:
            for k1 in self.reverse_private_vpc_connections:
                result['ReversePrivateVpcConnections'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointServiceId') is not None:
            self.endpoint_service_id = m.get('EndpointServiceId')

        self.private_vpc_connections = []
        if m.get('PrivateVpcConnections') is not None:
            for k1 in m.get('PrivateVpcConnections'):
                temp_model = main_models.GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections()
                self.private_vpc_connections.append(temp_model.from_map(k1))

        self.reverse_private_vpc_connections = []
        if m.get('ReversePrivateVpcConnections') is not None:
            for k1 in m.get('ReversePrivateVpcConnections'):
                temp_model = main_models.GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections()
                self.reverse_private_vpc_connections.append(temp_model.from_map(k1))

        return self

class GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections(DaraModel):
    def __init__(
        self,
        endpoint_id: str = None,
        endpoint_service_id: str = None,
    ):
        # The ID of the endpoint for the reverse private connection.
        self.endpoint_id = endpoint_id
        # The ID of the endpoint service for the reverse private connection.
        self.endpoint_service_id = endpoint_service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_service_id is not None:
            result['EndpointServiceId'] = self.endpoint_service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointServiceId') is not None:
            self.endpoint_service_id = m.get('EndpointServiceId')

        return self

class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections(DaraModel):
    def __init__(
        self,
        connection_configs: List[main_models.GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs] = None,
        endpoint_id: str = None,
        endpoint_service_id: str = None,
        private_zone_name: str = None,
    ):
        # The network configurations, which are mainly used for the private connection.
        self.connection_configs = connection_configs
        # The ID of the endpoint for the private connection.
        self.endpoint_id = endpoint_id
        # The ID of the endpoint service for the private connection.
        self.endpoint_service_id = endpoint_service_id
        # The custom domain name.
        self.private_zone_name = private_zone_name

    def validate(self):
        if self.connection_configs:
            for v1 in self.connection_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConnectionConfigs'] = []
        if self.connection_configs is not None:
            for k1 in self.connection_configs:
                result['ConnectionConfigs'].append(k1.to_map() if k1 else None)

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_service_id is not None:
            result['EndpointServiceId'] = self.endpoint_service_id

        if self.private_zone_name is not None:
            result['PrivateZoneName'] = self.private_zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_configs = []
        if m.get('ConnectionConfigs') is not None:
            for k1 in m.get('ConnectionConfigs'):
                temp_model = main_models.GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs()
                self.connection_configs.append(temp_model.from_map(k1))

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointServiceId') is not None:
            self.endpoint_service_id = m.get('EndpointServiceId')

        if m.get('PrivateZoneName') is not None:
            self.private_zone_name = m.get('PrivateZoneName')

        return self

class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs(DaraModel):
    def __init__(
        self,
        connect_bandwidth: int = None,
        domain_name: str = None,
        endpoint_ips: List[str] = None,
        ingress_endpoint_status: str = None,
        network_service_status: str = None,
        security_groups: List[str] = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
    ):
        # The bandwidth limit for the private connection established based on the private network interconnection mode of Compute Nest.
        self.connect_bandwidth = connect_bandwidth
        # The domain name.
        self.domain_name = domain_name
        # The IP addresses of the endpoints for private connections.
        self.endpoint_ips = endpoint_ips
        # The status of the Ingress endpoint. Valid values:
        # 
        # *   Ready: The Ingress endpoint is connected.
        # *   Pending: The Ingress endpoint is being connected.
        # *   Failed: The Ingress endpoint fails to be connected.
        # *   Deleted: The Ingress endpoint is deleted.
        # *   Deleting: The Ingress endpoint is being deleted.
        self.ingress_endpoint_status = ingress_endpoint_status
        # The status of the network service. Valid values:
        # 
        # *   Ready: The network service is connected.
        # *   Pending: The network service is being connected.
        # *   Failed: The network service fails to be connected.
        # *   Deleted: The network service is deleted.
        # *   Deleting: The network service is being deleted.
        self.network_service_status = network_service_status
        # The names of the security groups.
        self.security_groups = security_groups
        # The names of the vSwitches.
        self.v_switches = v_switches
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.endpoint_ips is not None:
            result['EndpointIps'] = self.endpoint_ips

        if self.ingress_endpoint_status is not None:
            result['IngressEndpointStatus'] = self.ingress_endpoint_status

        if self.network_service_status is not None:
            result['NetworkServiceStatus'] = self.network_service_status

        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups

        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndpointIps') is not None:
            self.endpoint_ips = m.get('EndpointIps')

        if m.get('IngressEndpointStatus') is not None:
            self.ingress_endpoint_status = m.get('IngressEndpointStatus')

        if m.get('NetworkServiceStatus') is not None:
            self.network_service_status = m.get('NetworkServiceStatus')

        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')

        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetServiceInstanceResponseBodyGrantedPermission(DaraModel):
    def __init__(
        self,
        operation_end_time: str = None,
        policy_names: str = None,
    ):
        self.operation_end_time = operation_end_time
        self.policy_names = policy_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time

        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')

        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')

        return self

