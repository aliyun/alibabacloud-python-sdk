# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstancesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_instances: List[main_models.ListServiceInstancesResponseBodyServiceInstances] = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about service instances.
        self.service_instances = service_instances
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.service_instances:
            for v1 in self.service_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServiceInstances'] = []
        if self.service_instances is not None:
            for k1 in self.service_instances:
                result['ServiceInstances'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.service_instances = []
        if m.get('ServiceInstances') is not None:
            for k1 in m.get('ServiceInstances'):
                temp_model = main_models.ListServiceInstancesResponseBodyServiceInstances()
                self.service_instances.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServiceInstancesResponseBodyServiceInstances(DaraModel):
    def __init__(
        self,
        biz_status: str = None,
        create_time: str = None,
        enable_instance_ops: bool = None,
        end_time: str = None,
        granted_permission: main_models.ListServiceInstancesResponseBodyServiceInstancesGrantedPermission = None,
        market_instance_id: str = None,
        name: str = None,
        operated_service_instance_id: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        order_id: str = None,
        outputs: str = None,
        parameters: str = None,
        pay_type: str = None,
        policy_names: str = None,
        progress: int = None,
        resource_group_id: str = None,
        resources: str = None,
        service: main_models.ListServiceInstancesResponseBodyServiceInstancesService = None,
        service_instance_id: str = None,
        service_type: str = None,
        source: str = None,
        status: str = None,
        status_detail: str = None,
        support_trial_to_private: bool = None,
        tags: List[main_models.ListServiceInstancesResponseBodyServiceInstancesTags] = None,
        template_name: str = None,
        update_time: str = None,
    ):
        # The business state of the service instance. Valid values:
        # 
        # *   Normal
        # *   Renewing
        # *   RenewFailed
        # *   Expired
        self.biz_status = biz_status
        # The time when the service instance was created.
        self.create_time = create_time
        # Indicates whether the service instance supports the hosted O\\&M feature. Valid values:
        # 
        # *   true
        # *   false
        self.enable_instance_ops = enable_instance_ops
        # The time when the service instance expires.
        self.end_time = end_time
        self.granted_permission = granted_permission
        # The ID of the Alibaba Cloud Marketplace instance.
        self.market_instance_id = market_instance_id
        # The name of the service instance.
        self.name = name
        # The ID of the managed service instance.
        self.operated_service_instance_id = operated_service_instance_id
        # The end of the time range during which hosted O\\&M is implemented.
        self.operation_end_time = operation_end_time
        # The beginning of the time range during which hosted O\\&M is implemented.
        self.operation_start_time = operation_start_time
        # The order ID.
        self.order_id = order_id
        # The information returned after the service instance is created.
        self.outputs = outputs
        # The parameters of the service instance.
        self.parameters = parameters
        # The billing method. Valid values:
        # 
        # *   Permanent: Once you purchase the service, you can use it permanently.
        # *   Subscription: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a subscription basis.
        # *   PayAsYouGo: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a pay-as-you-go basis.
        # *   CustomFixTime: You are charged for the service based on a custom duration fixed by the service provider.
        self.pay_type = pay_type
        self.policy_names = policy_names
        # The deployment progress of the service instance, in percentage.
        self.progress = progress
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resources.
        self.resources = resources
        # The services.
        self.service = service
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        # *   poc: The service is a trial service.
        self.service_type = service_type
        # The source from which the service instance is created.
        self.source = source
        # The state of the service instance. Valid values:
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
        # The description of the deployment of the service instance.
        self.status_detail = status_detail
        # Is it supported to convert from trial to formal
        self.support_trial_to_private = support_trial_to_private
        # The custom tags.
        self.tags = tags
        # The template name.
        self.template_name = template_name
        # The time when the service instance was updated.
        self.update_time = update_time

    def validate(self):
        if self.granted_permission:
            self.granted_permission.validate()
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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.granted_permission is not None:
            result['GrantedPermission'] = self.granted_permission.to_map()

        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id

        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time

        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names

        if self.progress is not None:
            result['Progress'] = self.progress

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

        if self.support_trial_to_private is not None:
            result['SupportTrialToPrivate'] = self.support_trial_to_private

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GrantedPermission') is not None:
            temp_model = main_models.ListServiceInstancesResponseBodyServiceInstancesGrantedPermission()
            self.granted_permission = temp_model.from_map(m.get('GrantedPermission'))

        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')

        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')

        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('Service') is not None:
            temp_model = main_models.ListServiceInstancesResponseBodyServiceInstancesService()
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

        if m.get('SupportTrialToPrivate') is not None:
            self.support_trial_to_private = m.get('SupportTrialToPrivate')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListServiceInstancesResponseBodyServiceInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListServiceInstancesResponseBodyServiceInstancesTags(DaraModel):
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

class ListServiceInstancesResponseBodyServiceInstancesService(DaraModel):
    def __init__(
        self,
        commodity: main_models.ListServiceInstancesResponseBodyServiceInstancesServiceCommodity = None,
        deploy_type: str = None,
        publish_time: str = None,
        service_id: str = None,
        service_infos: List[main_models.ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos] = None,
        service_type: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        version: str = None,
        version_name: str = None,
    ):
        # The commodity details.
        self.commodity = commodity
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        # *   ack: The service is deployed by using Alibaba Cloud Container Service for Kubernetes (ACK).
        # *   spi: The service is deployed by calling the Service Provider Interface (SPI).
        # *   operation: The service is deployed by using a hosted O\\&M service.
        self.deploy_type = deploy_type
        # The time when the service was published.
        self.publish_time = publish_time
        # The service ID.
        self.service_id = service_id
        # The information about the service.
        self.service_infos = service_infos
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        self.service_type = service_type
        # The service state.
        self.status = status
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # The service version.
        self.version = version
        # The custom version name defined by the service provider.
        self.version_name = version_name

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.service_infos:
            for v1 in self.service_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k1 in self.service_infos:
                result['ServiceInfos'].append(k1.to_map() if k1 else None)

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url

        if self.version is not None:
            result['Version'] = self.version

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            temp_model = main_models.ListServiceInstancesResponseBodyServiceInstancesServiceCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k1 in m.get('ServiceInfos'):
                temp_model = main_models.ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k1))

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos(DaraModel):
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
        # The name of the service.
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

class ListServiceInstancesResponseBodyServiceInstancesServiceCommodity(DaraModel):
    def __init__(
        self,
        saas_boost_metadata: str = None,
        type: str = None,
    ):
        # The configuration metadata related to SaaS Boost.
        self.saas_boost_metadata = saas_boost_metadata
        # The platform type. Valid values:
        # 
        # *   marketplace: Alibaba Cloud Marketplace.
        # *   Css: Lingxiao.
        # *   SaasBoost: SaaS Boost.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.saas_boost_metadata is not None:
            result['SaasBoostMetadata'] = self.saas_boost_metadata

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaasBoostMetadata') is not None:
            self.saas_boost_metadata = m.get('SaasBoostMetadata')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListServiceInstancesResponseBodyServiceInstancesGrantedPermission(DaraModel):
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

