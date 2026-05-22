# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServicesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        services: List[main_models.ListServicesResponseBodyServices] = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The services.
        self.services = services
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.services:
            for v1 in self.services:
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

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

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

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServicesResponseBodyServices(DaraModel):
    def __init__(
        self,
        approval_type: str = None,
        artifact_id: str = None,
        artifact_version: str = None,
        build_info: str = None,
        categories: str = None,
        commodity: main_models.ListServicesResponseBodyServicesCommodity = None,
        commodity_code: str = None,
        create_time: str = None,
        default_version: bool = None,
        deploy_type: str = None,
        has_beta: bool = None,
        has_draft: bool = None,
        latest_resell_source_service_version: str = None,
        publish_time: str = None,
        relation_type: str = None,
        resell_apply_status: str = None,
        resell_service_id: str = None,
        resource_group_id: str = None,
        service_discoverable: str = None,
        service_id: str = None,
        service_infos: List[main_models.ListServicesResponseBodyServicesServiceInfos] = None,
        service_locale_configs: List[main_models.ListServicesResponseBodyServicesServiceLocaleConfigs] = None,
        service_type: str = None,
        share_type: str = None,
        source_image: str = None,
        source_service_id: str = None,
        source_service_version: str = None,
        source_supplier_name: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        tags: List[main_models.ListServicesResponseBodyServicesTags] = None,
        tenant_type: str = None,
        trial_type: str = None,
        update_time: str = None,
        version: str = None,
        version_name: str = None,
        virtual_internet_service: str = None,
    ):
        # The approval type for applications for using the service. Valid values:
        # 
        # *   Manual: The applications are manual reviewed.
        # *   AutoPass: The applications are automatically approved.
        self.approval_type = approval_type
        # The ID of the artifact.
        self.artifact_id = artifact_id
        # The version of the artifact.
        self.artifact_version = artifact_version
        # The informathon for build service.
        self.build_info = build_info
        # The category of the service.
        self.categories = categories
        # The commodity details.
        self.commodity = commodity
        # The commodity code of the service in Alibaba Cloud Marketplace.
        self.commodity_code = commodity_code
        # The time when the service was created.
        self.create_time = create_time
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false
        # *   true
        self.default_version = default_version
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        # *   spi: The service is deployed by calling the Service Provider Interface (SPI).
        # *   operation: The service is deployed by using a hosted O\\&M service.
        # *   container: The service is deployed by using a container.
        # *
        self.deploy_type = deploy_type
        # Indicates whether the service has a beta version. Valid values:
        # 
        # *   true
        # *   false
        self.has_beta = has_beta
        # Indicates whether the service has a draft version. Valid values:
        # 
        # *   true
        # *   false
        self.has_draft = has_draft
        # The latest version of the distribution source service.
        self.latest_resell_source_service_version = latest_resell_source_service_version
        # The time when the service was published.
        self.publish_time = publish_time
        # The purpose of the artifact. Valid values:
        # 
        # *   ServiceDeployment: The artifact is used to create service instances.
        # *   ServiceUpgrade: The artifact is used to upgrade service instances.
        self.relation_type = relation_type
        # The state of distribution authorization of the service. Valid values:
        # 
        # *   CanApply: Distributors can apply for distribution permissions.
        # *   Applied: The application for distribution permissions is submitted.
        # *   Approved: The application for distribution permissions is approved.
        self.resell_apply_status = resell_apply_status
        # The ID of the distribution service.
        self.resell_service_id = resell_service_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Indicates whether the service is visible. Valid values:
        # 
        # *   INVISIBLE
        # *   DISCOVERABLE
        self.service_discoverable = service_discoverable
        # The service ID.
        self.service_id = service_id
        # The information about the service.
        self.service_infos = service_infos
        self.service_locale_configs = service_locale_configs
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        self.service_type = service_type
        # The permission type of the deployment URL. Valid values:
        # 
        # *   Public: All users can go to the URL to create a formal service instance or a trial service instance.
        # *   Restricted: Only users in the whitelist can go to the URL to create a formal service instance or a trial service instance.
        # *   OnlyFormalRestricted: Only users in the whitelist can go to the URL to create a formal service instance.
        # *   OnlyTrailRestricted: Only users in the whitelist can go to the URL to create a trial service instance.
        # *   Hidden: Users not in the whitelist cannot see the service details page when they go to the URL and cannot request deployment permissions.
        self.share_type = share_type
        # The source image.
        self.source_image = source_image
        # The ID of the distribution source service.
        self.source_service_id = source_service_id
        # The version of the distribution source service.
        self.source_service_version = source_service_version
        # The name of the distribution source service provider.
        self.source_supplier_name = source_supplier_name
        # The state of the service. Valid values:
        # 
        # *   Draft: The service is a draft.
        # *   Submitted: The service is submitted for review. You cannot modify services in this state.
        # *   Approved: The service is approved. You cannot modify services in this state. You can publish services in this state.
        # *   Launching: The service is being published.
        # *   Online: The service is published.
        # *   Offline: The service is unpublished.
        self.status = status
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # The service tags.
        self.tags = tags
        # The tenant type of the managed service. Valid values:
        # 
        # *   SingleTenant
        # *   MultiTenant
        self.tenant_type = tenant_type
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type
        # The time when the service was modified.
        self.update_time = update_time
        # The version of the service.
        self.version = version
        # The custom version name defined by the service provider.
        self.version_name = version_name
        # Indicates whether the service is a virtual Internet service. Valid values:
        # 
        # *   false
        # *   true
        self.virtual_internet_service = virtual_internet_service

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.service_infos:
            for v1 in self.service_infos:
                 if v1:
                    v1.validate()
        if self.service_locale_configs:
            for v1 in self.service_locale_configs:
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
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version

        if self.build_info is not None:
            result['BuildInfo'] = self.build_info

        if self.categories is not None:
            result['Categories'] = self.categories

        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.has_beta is not None:
            result['HasBeta'] = self.has_beta

        if self.has_draft is not None:
            result['HasDraft'] = self.has_draft

        if self.latest_resell_source_service_version is not None:
            result['LatestResellSourceServiceVersion'] = self.latest_resell_source_service_version

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.resell_apply_status is not None:
            result['ResellApplyStatus'] = self.resell_apply_status

        if self.resell_service_id is not None:
            result['ResellServiceId'] = self.resell_service_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_discoverable is not None:
            result['ServiceDiscoverable'] = self.service_discoverable

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

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.source_image is not None:
            result['SourceImage'] = self.source_image

        if self.source_service_id is not None:
            result['SourceServiceId'] = self.source_service_id

        if self.source_service_version is not None:
            result['SourceServiceVersion'] = self.source_service_version

        if self.source_supplier_name is not None:
            result['SourceSupplierName'] = self.source_supplier_name

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_type is not None:
            result['TenantType'] = self.tenant_type

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version is not None:
            result['Version'] = self.version

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.virtual_internet_service is not None:
            result['VirtualInternetService'] = self.virtual_internet_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')

        if m.get('BuildInfo') is not None:
            self.build_info = m.get('BuildInfo')

        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('Commodity') is not None:
            temp_model = main_models.ListServicesResponseBodyServicesCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('HasBeta') is not None:
            self.has_beta = m.get('HasBeta')

        if m.get('HasDraft') is not None:
            self.has_draft = m.get('HasDraft')

        if m.get('LatestResellSourceServiceVersion') is not None:
            self.latest_resell_source_service_version = m.get('LatestResellSourceServiceVersion')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('ResellApplyStatus') is not None:
            self.resell_apply_status = m.get('ResellApplyStatus')

        if m.get('ResellServiceId') is not None:
            self.resell_service_id = m.get('ResellServiceId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceDiscoverable') is not None:
            self.service_discoverable = m.get('ServiceDiscoverable')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k1 in m.get('ServiceInfos'):
                temp_model = main_models.ListServicesResponseBodyServicesServiceInfos()
                self.service_infos.append(temp_model.from_map(k1))

        self.service_locale_configs = []
        if m.get('ServiceLocaleConfigs') is not None:
            for k1 in m.get('ServiceLocaleConfigs'):
                temp_model = main_models.ListServicesResponseBodyServicesServiceLocaleConfigs()
                self.service_locale_configs.append(temp_model.from_map(k1))

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('SourceImage') is not None:
            self.source_image = m.get('SourceImage')

        if m.get('SourceServiceId') is not None:
            self.source_service_id = m.get('SourceServiceId')

        if m.get('SourceServiceVersion') is not None:
            self.source_service_version = m.get('SourceServiceVersion')

        if m.get('SourceSupplierName') is not None:
            self.source_supplier_name = m.get('SourceSupplierName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListServicesResponseBodyServicesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        if m.get('VirtualInternetService') is not None:
            self.virtual_internet_service = m.get('VirtualInternetService')

        return self

class ListServicesResponseBodyServicesTags(DaraModel):
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

class ListServicesResponseBodyServicesServiceLocaleConfigs(DaraModel):
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

class ListServicesResponseBodyServicesServiceInfos(DaraModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
    ):
        # The URL of the service icon.
        self.image = image
        # The language of the service. Valid values:
        # 
        # *   zh-CN: Chinese.
        # *   en-US: English.
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

class ListServicesResponseBodyServicesCommodity(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        saas_boost_metadata: str = None,
        type: str = None,
    ):
        # The commodity code.
        self.commodity_code = commodity_code
        # The configuration metadata related to Saas Boost.
        self.saas_boost_metadata = saas_boost_metadata
        # The platform type. Valid values:
        # 
        # *   marketplace: Alibaba Cloud Marketplace.
        # *   Css: Lingxiao.
        # *   SaasBoost: Saas Boost.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.saas_boost_metadata is not None:
            result['SaasBoostMetadata'] = self.saas_boost_metadata

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('SaasBoostMetadata') is not None:
            self.saas_boost_metadata = m.get('SaasBoostMetadata')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

