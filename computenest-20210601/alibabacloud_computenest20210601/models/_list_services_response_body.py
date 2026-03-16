# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
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
        categories: str = None,
        commodity: main_models.ListServicesResponseBodyServicesCommodity = None,
        commodity_code: str = None,
        deploy_from: str = None,
        deploy_type: str = None,
        publish_time: str = None,
        score: int = None,
        service_id: str = None,
        service_infos: List[main_models.ListServicesResponseBodyServicesServiceInfos] = None,
        service_locale_configs: List[main_models.ListServicesResponseBodyServicesServiceLocaleConfigs] = None,
        service_product_url: str = None,
        service_type: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_name_eng: str = None,
        supplier_uid: int = None,
        supplier_url: str = None,
        tags: List[main_models.ListServicesResponseBodyServicesTags] = None,
        tenant_type: str = None,
        trial_duration: str = None,
        trial_type: str = None,
        version: str = None,
        version_name: str = None,
        virtual_internet_service: str = None,
    ):
        # The category of the service.
        self.categories = categories
        # The commodity details.
        self.commodity = commodity
        # The commodity code of the service in Alibaba Cloud Marketplace.
        self.commodity_code = commodity_code
        # Service deployment approach. Valid values:
        # - NoWhere
        # 
        # - Marketplace
        # 
        # - ComputeNest
        self.deploy_from = deploy_from
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        self.deploy_type = deploy_type
        # The time when the service was published.
        self.publish_time = publish_time
        # Service recommendation score.
        self.score = score
        # The service ID.
        self.service_id = service_id
        # The service information.
        self.service_infos = service_infos
        self.service_locale_configs = service_locale_configs
        # The URL of the service page.
        self.service_product_url = service_product_url
        # The type of the service. Valid values:
        # 
        # - private: The service is a private service and is deployed within the account of a customer.
        # - managed: The service is a fully managed service and is deployed within the account of a service provider.
        # - operation: The service is a hosted O&M service.
        self.service_type = service_type
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
        # The name of service provider.
        self.supplier_name_eng = supplier_name_eng
        # The Alibaba Cloud account ID of the service provider.
        self.supplier_uid = supplier_uid
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # The tags.
        self.tags = tags
        # The tenant type of the managed service. Valid values:
        # 
        # *   SingleTenant
        # *   MultiTenant
        self.tenant_type = tenant_type
        # The trial duration. Unit: day. The maximum trial duration cannot exceed 30 days.
        self.trial_duration = trial_duration
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type
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
        if self.categories is not None:
            result['Categories'] = self.categories

        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.deploy_from is not None:
            result['DeployFrom'] = self.deploy_from

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.score is not None:
            result['Score'] = self.score

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

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_name_eng is not None:
            result['SupplierNameEng'] = self.supplier_name_eng

        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid

        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_type is not None:
            result['TenantType'] = self.tenant_type

        if self.trial_duration is not None:
            result['TrialDuration'] = self.trial_duration

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        if self.version is not None:
            result['Version'] = self.version

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.virtual_internet_service is not None:
            result['VirtualInternetService'] = self.virtual_internet_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('Commodity') is not None:
            temp_model = main_models.ListServicesResponseBodyServicesCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DeployFrom') is not None:
            self.deploy_from = m.get('DeployFrom')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('Score') is not None:
            self.score = m.get('Score')

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

        if m.get('ServiceProductUrl') is not None:
            self.service_product_url = m.get('ServiceProductUrl')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierNameEng') is not None:
            self.supplier_name_eng = m.get('SupplierNameEng')

        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')

        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListServicesResponseBodyServicesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')

        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

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
        # 
        # >  This parameter is required.
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
        softwares: List[main_models.ListServicesResponseBodyServicesServiceInfosSoftwares] = None,
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
        # Service software information.
        self.softwares = softwares

    def validate(self):
        if self.softwares:
            for v1 in self.softwares:
                 if v1:
                    v1.validate()

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

        result['Softwares'] = []
        if self.softwares is not None:
            for k1 in self.softwares:
                result['Softwares'].append(k1.to_map() if k1 else None)

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

        self.softwares = []
        if m.get('Softwares') is not None:
            for k1 in m.get('Softwares'):
                temp_model = main_models.ListServicesResponseBodyServicesServiceInfosSoftwares()
                self.softwares.append(temp_model.from_map(k1))

        return self

class ListServicesResponseBodyServicesServiceInfosSoftwares(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The name of the software.
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

class ListServicesResponseBodyServicesCommodity(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        deploy_page: str = None,
    ):
        # The commodity code.
        self.commodity_code = commodity_code
        # Deploy Page.
        self.deploy_page = deploy_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.deploy_page is not None:
            result['DeployPage'] = self.deploy_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DeployPage') is not None:
            self.deploy_page = m.get('DeployPage')

        return self

