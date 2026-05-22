# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class GetServiceResponseBody(DaraModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        approval_type: str = None,
        build_info: str = None,
        build_parameters: str = None,
        categories: str = None,
        commodity: main_models.GetServiceResponseBodyCommodity = None,
        compliance_metadata: main_models.GetServiceResponseBodyComplianceMetadata = None,
        create_time: str = None,
        cross_region_connection_status: str = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        duration: int = None,
        entity_source: Dict[str, str] = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        pay_from_type: str = None,
        permission: str = None,
        policy_names: str = None,
        progress: int = None,
        publish_time: str = None,
        registration_id: str = None,
        request_id: str = None,
        resellable: bool = None,
        resource_group_id: str = None,
        secret_key: str = None,
        service_audit_document_url: str = None,
        service_discoverable: str = None,
        service_document_infos: List[main_models.GetServiceResponseBodyServiceDocumentInfos] = None,
        service_id: str = None,
        service_infos: List[main_models.GetServiceResponseBodyServiceInfos] = None,
        service_locale_configs: List[main_models.GetServiceResponseBodyServiceLocaleConfigs] = None,
        service_product_url: str = None,
        service_type: str = None,
        share_type: str = None,
        share_type_status: str = None,
        source_service_id: str = None,
        source_service_version: str = None,
        source_supplier_name: str = None,
        statistic: main_models.GetServiceResponseBodyStatistic = None,
        status: str = None,
        status_detail: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        support_contacts: List[main_models.GetServiceResponseBodySupportContacts] = None,
        tags: List[main_models.GetServiceResponseBodyTags] = None,
        tenant_type: str = None,
        test_status: str = None,
        trial_duration: int = None,
        trial_type: str = None,
        update_time: str = None,
        upgrade_metadata: str = None,
        version: str = None,
        version_name: str = None,
        virtual_internet_service: str = None,
        virtual_internet_service_id: str = None,
    ):
        # The alert configurations of the service.
        # 
        # >  This parameter takes effect only when you specify an alert policy for **PolicyNames**.
        self.alarm_metadata = alarm_metadata
        # The approval type of the service usage application. Valid values:
        # 
        # *   Manual: The application is manually approved.
        # *   AutoPass: The application is automatically approved.
        self.approval_type = approval_type
        # The information of build service information.
        self.build_info = build_info
        # The parameters for building the service
        self.build_parameters = build_parameters
        # The category of the service.
        self.categories = categories
        # The commodity details.
        self.commodity = commodity
        # Compliance check metadata.
        self.compliance_metadata = compliance_metadata
        # The time when the service was created.
        self.create_time = create_time
        # The binding configurations of the commodity module.
        self.cross_region_connection_status = cross_region_connection_status
        # The storage configurations of the service. The format in which the deployment information of a service is stored varies based on the deployment type of the service. In this case, the deployment information is stored in the JSON string format.
        self.deploy_metadata = deploy_metadata
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        # *   spi: The service is deployed by calling a service provider interface (SPI).
        # *   operation: The service is deployed by using a hosted O\\&M service.
        # *   container: The service is deployed by using a container.
        # *   pkg: The service is deployed by using a package.
        self.deploy_type = deploy_type
        # The duration for which hosted O\\&M is implemented. Unit: seconds.
        self.duration = duration
        # The report source.
        self.entity_source = entity_source
        # Indicates whether the hosted O\\&M feature is enabled for the service. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is returned if you set **ServiceType** to **private**.
        self.is_support_operated = is_support_operated
        # The license metadata.
        self.license_metadata = license_metadata
        # The logging configurations.
        self.log_metadata = log_metadata
        # The hosted O\\&M configurations.
        self.operation_metadata = operation_metadata
        # The source for which fees are generated. Valid values:
        # 
        # *   None: No fees are generated.
        # *   Marketplace: Fees are generated for Alibaba Cloud Marketplace.
        # *   Custom: The custom fees.
        self.pay_from_type = pay_from_type
        # The permissions on the service. Valid values:
        # 
        # *   Deployable: Permissions to deploy the service.
        # *   Accessible: Permissions to access the service.
        self.permission = permission
        # The policy name. The name can be up to 128 characters in length. Separate multiple names with commas (,). Only hosted O\\&M policies are supported.
        self.policy_names = policy_names
        # The deployment progress of the service instance. Unit: percentage.
        self.progress = progress
        # The time when the service was published.
        self.publish_time = publish_time
        # The registration ID.
        self.registration_id = registration_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the distribution is supported. Valid values:
        # 
        # *   false
        # *   true
        self.resellable = resellable
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.secret_key = secret_key
        # The URL of the service audit file.
        self.service_audit_document_url = service_audit_document_url
        # Indicates whether the service is visible. Valid values:
        # 
        # *   INVISIBLE
        # *   DISCOVERABLE
        self.service_discoverable = service_discoverable
        # Service document information.
        self.service_document_infos = service_document_infos
        # The service ID.
        self.service_id = service_id
        # The information about the service.
        self.service_infos = service_infos
        self.service_locale_configs = service_locale_configs
        # The URL of the service page.
        self.service_product_url = service_product_url
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        self.service_type = service_type
        # The permission type of the deployment URL. Valid values:
        # 
        # *   Public: All users can go to the URL to create a service instance or a trial service instance.
        # *   Restricted: Only users in the whitelist can go to the URL to create a service instance or a trial service instance.
        # *   OnlyFormalRestricted: Only users in the whitelist can go to the URL to create a service instance.
        # *   OnlyTrailRestricted: Only users in the whitelist can go to the URL to create a trial service instance.
        # *   Hidden: Users not in the whitelist cannot see the service details page when they go to the URL and cannot request deployment permissions.
        self.share_type = share_type
        # The share status of the instance.
        # 
        # > This parameter is discontinued.
        self.share_type_status = share_type_status
        # The ID of the distribution source service.
        self.source_service_id = source_service_id
        # The version of the distribution source service.
        self.source_service_version = source_service_version
        # The name of the distribution source service provider.
        self.source_supplier_name = source_supplier_name
        # The statistics.
        self.statistic = statistic
        # The status of the service. Valid values:
        # 
        # *   Draft: The service is a draft.
        # *   Submitted: The service is submitted for review. You cannot modify services in this state.
        # *   Approved: The service is approved. You cannot modify services in this state. You can publish services in this state.
        # *   Launching: The service is being published.
        # *   Online: The service is published.
        # *   Offline: The service is unpublished.
        self.status = status
        # The description of the service status.
        self.status_detail = status_detail
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # Contact information of the service provider.
        self.support_contacts = support_contacts
        # The service tags.
        self.tags = tags
        # The type of the tenant. Valid values:
        # 
        # *   SingleTenant
        # *   MultiTenant
        self.tenant_type = tenant_type
        # The status of the test. Valid values:
        # 
        # *   `CONFIG_IS_NULL`: No test configurations exist.
        # *   `SERVICE_TEST_SUCCEED`: The service passed the test.
        # *   `SERVICE_TSET_DOING`: The service does not pass the test.
        self.test_status = test_status
        # The trial duration. Unit: day. The maximum trial duration cannot exceed 30 days.
        self.trial_duration = trial_duration
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type
        # The time when the service was updated.
        self.update_time = update_time
        # The metadata about the upgrade.
        self.upgrade_metadata = upgrade_metadata
        # The service version.
        self.version = version
        # The version name.
        self.version_name = version_name
        # Indicates whether the service is a virtual Internet service. Valid values:
        # 
        # *   false
        # *   true
        self.virtual_internet_service = virtual_internet_service
        # The ID of the virtual Internet service.
        self.virtual_internet_service_id = virtual_internet_service_id

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.compliance_metadata:
            self.compliance_metadata.validate()
        if self.service_document_infos:
            for v1 in self.service_document_infos:
                 if v1:
                    v1.validate()
        if self.service_infos:
            for v1 in self.service_infos:
                 if v1:
                    v1.validate()
        if self.service_locale_configs:
            for v1 in self.service_locale_configs:
                 if v1:
                    v1.validate()
        if self.statistic:
            self.statistic.validate()
        if self.support_contacts:
            for v1 in self.support_contacts:
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
        if self.alarm_metadata is not None:
            result['AlarmMetadata'] = self.alarm_metadata

        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.build_info is not None:
            result['BuildInfo'] = self.build_info

        if self.build_parameters is not None:
            result['BuildParameters'] = self.build_parameters

        if self.categories is not None:
            result['Categories'] = self.categories

        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.compliance_metadata is not None:
            result['ComplianceMetadata'] = self.compliance_metadata.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_region_connection_status is not None:
            result['CrossRegionConnectionStatus'] = self.cross_region_connection_status

        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.entity_source is not None:
            result['EntitySource'] = self.entity_source

        if self.is_support_operated is not None:
            result['IsSupportOperated'] = self.is_support_operated

        if self.license_metadata is not None:
            result['LicenseMetadata'] = self.license_metadata

        if self.log_metadata is not None:
            result['LogMetadata'] = self.log_metadata

        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata

        if self.pay_from_type is not None:
            result['PayFromType'] = self.pay_from_type

        if self.permission is not None:
            result['Permission'] = self.permission

        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resellable is not None:
            result['Resellable'] = self.resellable

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.service_audit_document_url is not None:
            result['ServiceAuditDocumentUrl'] = self.service_audit_document_url

        if self.service_discoverable is not None:
            result['ServiceDiscoverable'] = self.service_discoverable

        result['ServiceDocumentInfos'] = []
        if self.service_document_infos is not None:
            for k1 in self.service_document_infos:
                result['ServiceDocumentInfos'].append(k1.to_map() if k1 else None)

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k1 in self.service_infos:
                result['ServiceInfos'].append(k1.to_map() if k1 else None)

        result['ServiceLocaleConfigs'] = []
        if self.service_locale_configs is not None:
            for k1 in self.service_locale_configs:
                result['ServiceLocaleConfigs'].append(k1.to_map() if k1 else None)

        if self.service_product_url is not None:
            result['ServiceProductUrl'] = self.service_product_url

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.share_type_status is not None:
            result['ShareTypeStatus'] = self.share_type_status

        if self.source_service_id is not None:
            result['SourceServiceId'] = self.source_service_id

        if self.source_service_version is not None:
            result['SourceServiceVersion'] = self.source_service_version

        if self.source_supplier_name is not None:
            result['SourceSupplierName'] = self.source_supplier_name

        if self.statistic is not None:
            result['Statistic'] = self.statistic.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url

        result['SupportContacts'] = []
        if self.support_contacts is not None:
            for k1 in self.support_contacts:
                result['SupportContacts'].append(k1.to_map() if k1 else None)

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_type is not None:
            result['TenantType'] = self.tenant_type

        if self.test_status is not None:
            result['TestStatus'] = self.test_status

        if self.trial_duration is not None:
            result['TrialDuration'] = self.trial_duration

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.upgrade_metadata is not None:
            result['UpgradeMetadata'] = self.upgrade_metadata

        if self.version is not None:
            result['Version'] = self.version

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.virtual_internet_service is not None:
            result['VirtualInternetService'] = self.virtual_internet_service

        if self.virtual_internet_service_id is not None:
            result['VirtualInternetServiceId'] = self.virtual_internet_service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMetadata') is not None:
            self.alarm_metadata = m.get('AlarmMetadata')

        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('BuildInfo') is not None:
            self.build_info = m.get('BuildInfo')

        if m.get('BuildParameters') is not None:
            self.build_parameters = m.get('BuildParameters')

        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('Commodity') is not None:
            temp_model = main_models.GetServiceResponseBodyCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('ComplianceMetadata') is not None:
            temp_model = main_models.GetServiceResponseBodyComplianceMetadata()
            self.compliance_metadata = temp_model.from_map(m.get('ComplianceMetadata'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossRegionConnectionStatus') is not None:
            self.cross_region_connection_status = m.get('CrossRegionConnectionStatus')

        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EntitySource') is not None:
            self.entity_source = m.get('EntitySource')

        if m.get('IsSupportOperated') is not None:
            self.is_support_operated = m.get('IsSupportOperated')

        if m.get('LicenseMetadata') is not None:
            self.license_metadata = m.get('LicenseMetadata')

        if m.get('LogMetadata') is not None:
            self.log_metadata = m.get('LogMetadata')

        if m.get('OperationMetadata') is not None:
            self.operation_metadata = m.get('OperationMetadata')

        if m.get('PayFromType') is not None:
            self.pay_from_type = m.get('PayFromType')

        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resellable') is not None:
            self.resellable = m.get('Resellable')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('ServiceAuditDocumentUrl') is not None:
            self.service_audit_document_url = m.get('ServiceAuditDocumentUrl')

        if m.get('ServiceDiscoverable') is not None:
            self.service_discoverable = m.get('ServiceDiscoverable')

        self.service_document_infos = []
        if m.get('ServiceDocumentInfos') is not None:
            for k1 in m.get('ServiceDocumentInfos'):
                temp_model = main_models.GetServiceResponseBodyServiceDocumentInfos()
                self.service_document_infos.append(temp_model.from_map(k1))

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k1 in m.get('ServiceInfos'):
                temp_model = main_models.GetServiceResponseBodyServiceInfos()
                self.service_infos.append(temp_model.from_map(k1))

        self.service_locale_configs = []
        if m.get('ServiceLocaleConfigs') is not None:
            for k1 in m.get('ServiceLocaleConfigs'):
                temp_model = main_models.GetServiceResponseBodyServiceLocaleConfigs()
                self.service_locale_configs.append(temp_model.from_map(k1))

        if m.get('ServiceProductUrl') is not None:
            self.service_product_url = m.get('ServiceProductUrl')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('ShareTypeStatus') is not None:
            self.share_type_status = m.get('ShareTypeStatus')

        if m.get('SourceServiceId') is not None:
            self.source_service_id = m.get('SourceServiceId')

        if m.get('SourceServiceVersion') is not None:
            self.source_service_version = m.get('SourceServiceVersion')

        if m.get('SourceSupplierName') is not None:
            self.source_supplier_name = m.get('SourceSupplierName')

        if m.get('Statistic') is not None:
            temp_model = main_models.GetServiceResponseBodyStatistic()
            self.statistic = temp_model.from_map(m.get('Statistic'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')

        self.support_contacts = []
        if m.get('SupportContacts') is not None:
            for k1 in m.get('SupportContacts'):
                temp_model = main_models.GetServiceResponseBodySupportContacts()
                self.support_contacts.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetServiceResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')

        if m.get('TestStatus') is not None:
            self.test_status = m.get('TestStatus')

        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpgradeMetadata') is not None:
            self.upgrade_metadata = m.get('UpgradeMetadata')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        if m.get('VirtualInternetService') is not None:
            self.virtual_internet_service = m.get('VirtualInternetService')

        if m.get('VirtualInternetServiceId') is not None:
            self.virtual_internet_service_id = m.get('VirtualInternetServiceId')

        return self

class GetServiceResponseBodyTags(DaraModel):
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

class GetServiceResponseBodySupportContacts(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of Contact information.
        self.type = type
        # The value of Contact information.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetServiceResponseBodyStatistic(DaraModel):
    def __init__(
        self,
        accumulative_instance_count: int = None,
        accumulative_poc_amount: float = None,
        accumulative_user_count: int = None,
        average_poc_amount: float = None,
        average_poc_duration: float = None,
        average_poc_unit_amount: float = None,
        deployed_service_instance_count: int = None,
        deployed_user_count: int = None,
        submitted_usage_count: int = None,
    ):
        # The total number of service instances that belong to the service. The service instances that are deleted are counted.
        self.accumulative_instance_count = accumulative_instance_count
        # The total amount consumed for trial service instances. Unit: CNY.
        self.accumulative_poc_amount = accumulative_poc_amount
        # The total number of users who use the service. The historical users are counted.
        self.accumulative_user_count = accumulative_user_count
        # The average amount consumed for trial service instances per instance. Unit: CNY.
        self.average_poc_amount = average_poc_amount
        # The average duration for which trial service instances are in use. Unit: Hour.
        self.average_poc_duration = average_poc_duration
        # The average amount consumed for trial service instances per a period of time. Unit: CNY.
        self.average_poc_unit_amount = average_poc_unit_amount
        # The number of online service instances. It means the number of service instances that are successfully deployed.
        self.deployed_service_instance_count = deployed_service_instance_count
        # The number of online users. It means the number of users who successfully deployed the service instances.
        self.deployed_user_count = deployed_user_count
        # The number of service applications that are in the Submitted state.
        self.submitted_usage_count = submitted_usage_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accumulative_instance_count is not None:
            result['AccumulativeInstanceCount'] = self.accumulative_instance_count

        if self.accumulative_poc_amount is not None:
            result['AccumulativePocAmount'] = self.accumulative_poc_amount

        if self.accumulative_user_count is not None:
            result['AccumulativeUserCount'] = self.accumulative_user_count

        if self.average_poc_amount is not None:
            result['AveragePocAmount'] = self.average_poc_amount

        if self.average_poc_duration is not None:
            result['AveragePocDuration'] = self.average_poc_duration

        if self.average_poc_unit_amount is not None:
            result['AveragePocUnitAmount'] = self.average_poc_unit_amount

        if self.deployed_service_instance_count is not None:
            result['DeployedServiceInstanceCount'] = self.deployed_service_instance_count

        if self.deployed_user_count is not None:
            result['DeployedUserCount'] = self.deployed_user_count

        if self.submitted_usage_count is not None:
            result['SubmittedUsageCount'] = self.submitted_usage_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccumulativeInstanceCount') is not None:
            self.accumulative_instance_count = m.get('AccumulativeInstanceCount')

        if m.get('AccumulativePocAmount') is not None:
            self.accumulative_poc_amount = m.get('AccumulativePocAmount')

        if m.get('AccumulativeUserCount') is not None:
            self.accumulative_user_count = m.get('AccumulativeUserCount')

        if m.get('AveragePocAmount') is not None:
            self.average_poc_amount = m.get('AveragePocAmount')

        if m.get('AveragePocDuration') is not None:
            self.average_poc_duration = m.get('AveragePocDuration')

        if m.get('AveragePocUnitAmount') is not None:
            self.average_poc_unit_amount = m.get('AveragePocUnitAmount')

        if m.get('DeployedServiceInstanceCount') is not None:
            self.deployed_service_instance_count = m.get('DeployedServiceInstanceCount')

        if m.get('DeployedUserCount') is not None:
            self.deployed_user_count = m.get('DeployedUserCount')

        if m.get('SubmittedUsageCount') is not None:
            self.submitted_usage_count = m.get('SubmittedUsageCount')

        return self

class GetServiceResponseBodyServiceLocaleConfigs(DaraModel):
    def __init__(
        self,
        en_value: str = None,
        original_value: str = None,
        zh_value: str = None,
    ):
        self.en_value = en_value
        self.original_value = original_value
        self.zh_value = zh_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.en_value is not None:
            result['EnValue'] = self.en_value

        if self.original_value is not None:
            result['OriginalValue'] = self.original_value

        if self.zh_value is not None:
            result['ZhValue'] = self.zh_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnValue') is not None:
            self.en_value = m.get('EnValue')

        if m.get('OriginalValue') is not None:
            self.original_value = m.get('OriginalValue')

        if m.get('ZhValue') is not None:
            self.zh_value = m.get('ZhValue')

        return self

class GetServiceResponseBodyServiceInfos(DaraModel):
    def __init__(
        self,
        agreements: List[main_models.GetServiceResponseBodyServiceInfosAgreements] = None,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
        softwares: List[main_models.GetServiceResponseBodyServiceInfosSoftwares] = None,
    ):
        # The agreement information about the service.
        self.agreements = agreements
        # The URL of the service icon.
        self.image = image
        # The language of the service. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        self.locale = locale
        # The URL of the detailed description of the service.
        self.long_description_url = long_description_url
        # The service name.
        self.name = name
        # The description of the service.
        self.short_description = short_description
        # The list of the information about the software in the service.
        self.softwares = softwares

    def validate(self):
        if self.agreements:
            for v1 in self.agreements:
                 if v1:
                    v1.validate()
        if self.softwares:
            for v1 in self.softwares:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Agreements'] = []
        if self.agreements is not None:
            for k1 in self.agreements:
                result['Agreements'].append(k1.to_map() if k1 else None)

        if self.image is not None:
            result['Image'] = self.image

        if self.locale is not None:
            result['Locale'] = self.locale

        if self.long_description_url is not None:
            result['LongDescriptionUrl'] = self.long_description_url

        if self.name is not None:
            result['Name'] = self.name

        if self.short_description is not None:
            result['ShortDescription'] = self.short_description

        result['Softwares'] = []
        if self.softwares is not None:
            for k1 in self.softwares:
                result['Softwares'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agreements = []
        if m.get('Agreements') is not None:
            for k1 in m.get('Agreements'):
                temp_model = main_models.GetServiceResponseBodyServiceInfosAgreements()
                self.agreements.append(temp_model.from_map(k1))

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        if m.get('LongDescriptionUrl') is not None:
            self.long_description_url = m.get('LongDescriptionUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')

        self.softwares = []
        if m.get('Softwares') is not None:
            for k1 in m.get('Softwares'):
                temp_model = main_models.GetServiceResponseBodyServiceInfosSoftwares()
                self.softwares.append(temp_model.from_map(k1))

        return self

class GetServiceResponseBodyServiceInfosSoftwares(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The name of the software
        self.name = name
        # The version of the software.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetServiceResponseBodyServiceInfosAgreements(DaraModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        # The agreement name.
        self.name = name
        # The agreement URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetServiceResponseBodyServiceDocumentInfos(DaraModel):
    def __init__(
        self,
        document_url: str = None,
        locale: str = None,
        template_name: str = None,
    ):
        # The URL that is used to access the document.
        self.document_url = document_url
        # The language of the return data. Valid values: zh-CN and en-US.
        self.locale = locale
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url

        if self.locale is not None:
            result['Locale'] = self.locale

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class GetServiceResponseBodyComplianceMetadata(DaraModel):
    def __init__(
        self,
        compliance_packs: List[str] = None,
    ):
        # The compliance package is selected.
        self.compliance_packs = compliance_packs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_packs is not None:
            result['CompliancePacks'] = self.compliance_packs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePacks') is not None:
            self.compliance_packs = m.get('CompliancePacks')

        return self

class GetServiceResponseBodyCommodity(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        components: List[str] = None,
        css_metadata: main_models.GetServiceResponseBodyCommodityCssMetadata = None,
        marketplace_metadata: main_models.GetServiceResponseBodyCommodityMarketplaceMetadata = None,
        metering_entities: List[main_models.GetServiceResponseBodyCommodityMeteringEntities] = None,
        saas_boost_metadata: str = None,
        specifications: List[main_models.GetServiceResponseBodyCommoditySpecifications] = None,
        type: str = None,
    ):
        # The billing method of the service. Valid values:
        # 
        # *   **PREPAY** (default): subscription.
        # *   **POSTPAY**: pay-as-you-go.
        self.charge_type = charge_type
        # The commodity code of the service in Alibaba Cloud Marketplace.
        self.commodity_code = commodity_code
        # The commodity modules.
        self.components = components
        # The configuration metadata related to Lingxiao.
        self.css_metadata = css_metadata
        # The metadata of Alibaba Cloud Marketplace.
        self.marketplace_metadata = marketplace_metadata
        # The information about the billable item.
        self.metering_entities = metering_entities
        # The configuration metadata related to Saas Boost.
        self.saas_boost_metadata = saas_boost_metadata
        # The specification details of the service in Alibaba Cloud Marketplace.
        self.specifications = specifications
        # The service type. Valid values:
        # 
        # *   marketplace: Alibaba Cloud Marketplace.
        # *   Css: Lingxiao.
        self.type = type

    def validate(self):
        if self.css_metadata:
            self.css_metadata.validate()
        if self.marketplace_metadata:
            self.marketplace_metadata.validate()
        if self.metering_entities:
            for v1 in self.metering_entities:
                 if v1:
                    v1.validate()
        if self.specifications:
            for v1 in self.specifications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.components is not None:
            result['Components'] = self.components

        if self.css_metadata is not None:
            result['CssMetadata'] = self.css_metadata.to_map()

        if self.marketplace_metadata is not None:
            result['MarketplaceMetadata'] = self.marketplace_metadata.to_map()

        result['MeteringEntities'] = []
        if self.metering_entities is not None:
            for k1 in self.metering_entities:
                result['MeteringEntities'].append(k1.to_map() if k1 else None)

        if self.saas_boost_metadata is not None:
            result['SaasBoostMetadata'] = self.saas_boost_metadata

        result['Specifications'] = []
        if self.specifications is not None:
            for k1 in self.specifications:
                result['Specifications'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Components') is not None:
            self.components = m.get('Components')

        if m.get('CssMetadata') is not None:
            temp_model = main_models.GetServiceResponseBodyCommodityCssMetadata()
            self.css_metadata = temp_model.from_map(m.get('CssMetadata'))

        if m.get('MarketplaceMetadata') is not None:
            temp_model = main_models.GetServiceResponseBodyCommodityMarketplaceMetadata()
            self.marketplace_metadata = temp_model.from_map(m.get('MarketplaceMetadata'))

        self.metering_entities = []
        if m.get('MeteringEntities') is not None:
            for k1 in m.get('MeteringEntities'):
                temp_model = main_models.GetServiceResponseBodyCommodityMeteringEntities()
                self.metering_entities.append(temp_model.from_map(k1))

        if m.get('SaasBoostMetadata') is not None:
            self.saas_boost_metadata = m.get('SaasBoostMetadata')

        self.specifications = []
        if m.get('Specifications') is not None:
            for k1 in m.get('Specifications'):
                temp_model = main_models.GetServiceResponseBodyCommoditySpecifications()
                self.specifications.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetServiceResponseBodyCommoditySpecifications(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        times: List[str] = None,
    ):
        # The commodity code.
        self.code = code
        # The specification name.
        self.name = name
        # The subscription duration. Unit: week or year.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class GetServiceResponseBodyCommodityMeteringEntities(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        name: str = None,
    ):
        # The ID of the billable item.
        self.entity_id = entity_id
        # The name of the billable item.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetServiceResponseBodyCommodityMarketplaceMetadata(DaraModel):
    def __init__(
        self,
        metering_entity_extra_infos: List[main_models.GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityExtraInfos] = None,
        metering_entity_mappings: List[main_models.GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityMappings] = None,
        specification_mappings: List[main_models.GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings] = None,
    ):
        # The configurations of the billable items.
        self.metering_entity_extra_infos = metering_entity_extra_infos
        # The billable items that are associated with the package.
        self.metering_entity_mappings = metering_entity_mappings
        # The mappings between the service specifications and the template or package.
        self.specification_mappings = specification_mappings

    def validate(self):
        if self.metering_entity_extra_infos:
            for v1 in self.metering_entity_extra_infos:
                 if v1:
                    v1.validate()
        if self.metering_entity_mappings:
            for v1 in self.metering_entity_mappings:
                 if v1:
                    v1.validate()
        if self.specification_mappings:
            for v1 in self.specification_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MeteringEntityExtraInfos'] = []
        if self.metering_entity_extra_infos is not None:
            for k1 in self.metering_entity_extra_infos:
                result['MeteringEntityExtraInfos'].append(k1.to_map() if k1 else None)

        result['MeteringEntityMappings'] = []
        if self.metering_entity_mappings is not None:
            for k1 in self.metering_entity_mappings:
                result['MeteringEntityMappings'].append(k1.to_map() if k1 else None)

        result['SpecificationMappings'] = []
        if self.specification_mappings is not None:
            for k1 in self.specification_mappings:
                result['SpecificationMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metering_entity_extra_infos = []
        if m.get('MeteringEntityExtraInfos') is not None:
            for k1 in m.get('MeteringEntityExtraInfos'):
                temp_model = main_models.GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityExtraInfos()
                self.metering_entity_extra_infos.append(temp_model.from_map(k1))

        self.metering_entity_mappings = []
        if m.get('MeteringEntityMappings') is not None:
            for k1 in m.get('MeteringEntityMappings'):
                temp_model = main_models.GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityMappings()
                self.metering_entity_mappings.append(temp_model.from_map(k1))

        self.specification_mappings = []
        if m.get('SpecificationMappings') is not None:
            for k1 in m.get('SpecificationMappings'):
                temp_model = main_models.GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings()
                self.specification_mappings.append(temp_model.from_map(k1))

        return self

class GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings(DaraModel):
    def __init__(
        self,
        specification_code: str = None,
        specification_name: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The specification code of the service in Alibaba Cloud Marketplace.
        self.specification_code = specification_code
        # The name of the specification package.
        self.specification_name = specification_name
        # The template name.
        self.template_name = template_name
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.specification_code is not None:
            result['SpecificationCode'] = self.specification_code

        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecificationCode') is not None:
            self.specification_code = m.get('SpecificationCode')

        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        return self

class GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityMappings(DaraModel):
    def __init__(
        self,
        entity_ids: str = None,
        specification_name: str = None,
        template_name: str = None,
    ):
        # The ID of the billable item.
        self.entity_ids = entity_ids
        # The name of the specification package.
        self.specification_name = specification_name
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_ids is not None:
            result['EntityIds'] = self.entity_ids

        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityIds') is not None:
            self.entity_ids = m.get('EntityIds')

        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityExtraInfos(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        metric_name: str = None,
        promql: str = None,
        type: str = None,
    ):
        # The ID of the billable item.
        self.entity_id = entity_id
        # The metric name.
        self.metric_name = metric_name
        # The custom prometheus statement.
        self.promql = promql
        # The metric.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.promql is not None:
            result['Promql'] = self.promql

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Promql') is not None:
            self.promql = m.get('Promql')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetServiceResponseBodyCommodityCssMetadata(DaraModel):
    def __init__(
        self,
        components_mappings: List[main_models.GetServiceResponseBodyCommodityCssMetadataComponentsMappings] = None,
        metering_entity_extra_infos: List[main_models.GetServiceResponseBodyCommodityCssMetadataMeteringEntityExtraInfos] = None,
        metering_entity_mappings: List[main_models.GetServiceResponseBodyCommodityCssMetadataMeteringEntityMappings] = None,
    ):
        # The mapping information about the billing items.
        self.components_mappings = components_mappings
        # Metering item configuration information.
        self.metering_entity_extra_infos = metering_entity_extra_infos
        # The binding relationship between package and measurement dimension.
        self.metering_entity_mappings = metering_entity_mappings

    def validate(self):
        if self.components_mappings:
            for v1 in self.components_mappings:
                 if v1:
                    v1.validate()
        if self.metering_entity_extra_infos:
            for v1 in self.metering_entity_extra_infos:
                 if v1:
                    v1.validate()
        if self.metering_entity_mappings:
            for v1 in self.metering_entity_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComponentsMappings'] = []
        if self.components_mappings is not None:
            for k1 in self.components_mappings:
                result['ComponentsMappings'].append(k1.to_map() if k1 else None)

        result['MeteringEntityExtraInfos'] = []
        if self.metering_entity_extra_infos is not None:
            for k1 in self.metering_entity_extra_infos:
                result['MeteringEntityExtraInfos'].append(k1.to_map() if k1 else None)

        result['MeteringEntityMappings'] = []
        if self.metering_entity_mappings is not None:
            for k1 in self.metering_entity_mappings:
                result['MeteringEntityMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components_mappings = []
        if m.get('ComponentsMappings') is not None:
            for k1 in m.get('ComponentsMappings'):
                temp_model = main_models.GetServiceResponseBodyCommodityCssMetadataComponentsMappings()
                self.components_mappings.append(temp_model.from_map(k1))

        self.metering_entity_extra_infos = []
        if m.get('MeteringEntityExtraInfos') is not None:
            for k1 in m.get('MeteringEntityExtraInfos'):
                temp_model = main_models.GetServiceResponseBodyCommodityCssMetadataMeteringEntityExtraInfos()
                self.metering_entity_extra_infos.append(temp_model.from_map(k1))

        self.metering_entity_mappings = []
        if m.get('MeteringEntityMappings') is not None:
            for k1 in m.get('MeteringEntityMappings'):
                temp_model = main_models.GetServiceResponseBodyCommodityCssMetadataMeteringEntityMappings()
                self.metering_entity_mappings.append(temp_model.from_map(k1))

        return self

class GetServiceResponseBodyCommodityCssMetadataMeteringEntityMappings(DaraModel):
    def __init__(
        self,
        entity_ids: str = None,
        specification_name: str = None,
        template_name: str = None,
    ):
        # The ID of the entity.
        self.entity_ids = entity_ids
        # The package name.
        self.specification_name = specification_name
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_ids is not None:
            result['EntityIds'] = self.entity_ids

        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityIds') is not None:
            self.entity_ids = m.get('EntityIds')

        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class GetServiceResponseBodyCommodityCssMetadataMeteringEntityExtraInfos(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        metric_name: str = None,
        promql: str = None,
        type: str = None,
    ):
        # The ID of the entity.
        self.entity_id = entity_id
        # Name of a measurement indicator.
        self.metric_name = metric_name
        # Custom PromQL.
        self.promql = promql
        # Measurement indicators.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.promql is not None:
            result['Promql'] = self.promql

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Promql') is not None:
            self.promql = m.get('Promql')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetServiceResponseBodyCommodityCssMetadataComponentsMappings(DaraModel):
    def __init__(
        self,
        mappings: Dict[str, str] = None,
        template_name: str = None,
    ):
        # The mappings.
        self.mappings = mappings
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mappings is not None:
            result['Mappings'] = self.mappings

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mappings') is not None:
            self.mappings = m.get('Mappings')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

