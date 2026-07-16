# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GetServiceResponseBody(DaraModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        categories: str = None,
        commodity: main_models.GetServiceResponseBodyCommodity = None,
        compliance_metadata: main_models.GetServiceResponseBodyComplianceMetadata = None,
        deploy_from: str = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        duration: int = None,
        instance_role_infos: List[main_models.GetServiceResponseBodyInstanceRoleInfos] = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        permission: str = None,
        policy_names: str = None,
        publish_time: str = None,
        request_id: str = None,
        service_document_infos: List[main_models.GetServiceResponseBodyServiceDocumentInfos] = None,
        service_id: str = None,
        service_infos: List[main_models.GetServiceResponseBodyServiceInfos] = None,
        service_locale_configs: List[main_models.GetServiceResponseBodyServiceLocaleConfigs] = None,
        service_product_url: str = None,
        service_type: str = None,
        share_type: str = None,
        status: str = None,
        supplier_desc: str = None,
        supplier_logo: str = None,
        supplier_name: str = None,
        supplier_uid: int = None,
        supplier_url: str = None,
        support_contacts: List[main_models.GetServiceResponseBodySupportContacts] = None,
        tags: List[main_models.GetServiceResponseBodyTags] = None,
        tenant_type: str = None,
        trial_duration: int = None,
        trial_type: str = None,
        version: str = None,
        version_name: str = None,
    ):
        # The alert configuration of the service.
        # 
        # > This configuration takes effect only if you configure an alert policy in **PolicyNames**.
        self.alarm_metadata = alarm_metadata
        # The service category name.
        self.categories = categories
        # The commodity specifications.
        self.commodity = commodity
        # The compliance package metadata.
        self.compliance_metadata = compliance_metadata
        # The deployment channel. Valid values:
        # 
        # - NoWhere: The service has no deployment channel.
        # 
        # - Marketplace: The service is deployed from Alibaba Cloud Marketplace.
        # 
        # - ComputeNest: The service is deployed from Compute Nest.
        self.deploy_from = deploy_from
        # The deployment configuration of the service. The configuration is stored as a JSON string. The data format of the string varies based on the deployment type.
        self.deploy_metadata = deploy_metadata
        # The deployment type. Valid values:
        # 
        # - ros: The service is deployed using ROS.
        # 
        # - terraform: The service is deployed using Terraform.
        # 
        # - spi: The service is deployed by calling a Service Provider Interface (SPI).
        # 
        # - operation: The service is an Alibaba Cloud Managed Services deployment.
        # 
        # - container: The service is deployed using a container.
        # 
        # - pkg: The service is a package service.
        self.deploy_type = deploy_type
        # The duration of the Alibaba Cloud Managed Services. Unit: seconds.
        self.duration = duration
        # The information about the roles that are created in the service template.
        self.instance_role_infos = instance_role_infos
        # Specifies whether to enable Alibaba Cloud Managed Services. Default value: false. Valid values:
        # 
        # - true: enabled.
        # 
        # - false: disabled.
        # 
        # > This parameter is required when **ServiceType** is set to **private**.
        self.is_support_operated = is_support_operated
        # The license metadata.
        self.license_metadata = license_metadata
        # The application log configuration.
        self.log_metadata = log_metadata
        # The O\\&M configuration.
        self.operation_metadata = operation_metadata
        # The permission type. Valid values:
        # 
        # - Deployable: The service is deployable.
        # 
        # - Accessible: The service is accessible.
        self.permission = permission
        # The policy names. A single policy name can be up to 128 characters in length. Separate multiple names with commas (,). Only policies related to Alibaba Cloud Managed Services are supported.
        self.policy_names = policy_names
        # The time when the service was published.
        self.publish_time = publish_time
        # The request ID.
        self.request_id = request_id
        # The service documents.
        self.service_document_infos = service_document_infos
        # The service ID.
        self.service_id = service_id
        # The service information.
        self.service_infos = service_infos
        # The multilingual configurations of the service.
        self.service_locale_configs = service_locale_configs
        # The URL of the product page.
        self.service_product_url = service_product_url
        # The service type. Valid values:
        # 
        # - private: The service is deployed in the user\\"s account.
        # 
        # - managed: The service is hosted in the service provider\\"s account.
        # 
        # - operation: The service is an Alibaba Cloud Managed Service.
        self.service_type = service_type
        # The share type. Valid values:
        # 
        # - Public: The service is public. Formal and trial deployments are not restricted.
        # 
        # - Restricted: The service is restricted. Formal and trial deployments are restricted.
        # 
        # - OnlyFormalRestricted: Only formal deployments are restricted.
        # 
        # - OnlyTrialRestricted: Only trial deployments are restricted.
        # 
        # - Hidden: The service is hidden, is not visible, and you cannot request permissions for deployment.
        self.share_type = share_type
        # The status of the service. Valid values:
        # 
        # - Draft: The service is in the draft state.
        # 
        # - Beta: The service is in a pre-release state. The service cannot be modified but can be shared with other users.
        # 
        # - Submitted: The service is submitted for approval. The service cannot be modified.
        # 
        # - Approved: The service is approved. The service cannot be modified but can be published.
        # 
        # - Launching: The service is being published.
        # 
        # - Online: The service is published.
        # 
        # - Offline: The service is unpublished.
        # 
        # - Creating: The service is being created.
        # 
        # - CreateFailed: The service failed to be created.
        # 
        # - Updating: The service is being updated.
        # 
        # - UpdateFailed: The service failed to be updated.
        self.status = status
        # The description of the service provider.
        self.supplier_desc = supplier_desc
        # The icon of the service provider.
        self.supplier_logo = supplier_logo
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The Alibaba Cloud account ID of the service provider.
        self.supplier_uid = supplier_uid
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # The contact information of the service provider.
        self.support_contacts = support_contacts
        # The service tags.
        self.tags = tags
        # The tenant type. Valid values:
        # 
        # - SingleTenant: The service is a single-tenant service.
        # 
        # - MultiTenant: The service is a multitenancy service.
        self.tenant_type = tenant_type
        # The trial duration in days. The maximum trial duration is 30 days.
        self.trial_duration = trial_duration
        # The trial type. Valid values:
        # 
        # - Trial: The service supports trial.
        # 
        # - NotTrial: The service does not support trial.
        self.trial_type = trial_type
        # The service version.
        self.version = version
        # The version name.
        self.version_name = version_name

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.compliance_metadata:
            self.compliance_metadata.validate()
        if self.instance_role_infos:
            for v1 in self.instance_role_infos:
                 if v1:
                    v1.validate()
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

        if self.categories is not None:
            result['Categories'] = self.categories

        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.compliance_metadata is not None:
            result['ComplianceMetadata'] = self.compliance_metadata.to_map()

        if self.deploy_from is not None:
            result['DeployFrom'] = self.deploy_from

        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.duration is not None:
            result['Duration'] = self.duration

        result['InstanceRoleInfos'] = []
        if self.instance_role_infos is not None:
            for k1 in self.instance_role_infos:
                result['InstanceRoleInfos'].append(k1.to_map() if k1 else None)

        if self.is_support_operated is not None:
            result['IsSupportOperated'] = self.is_support_operated

        if self.license_metadata is not None:
            result['LicenseMetadata'] = self.license_metadata

        if self.log_metadata is not None:
            result['LogMetadata'] = self.log_metadata

        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata

        if self.permission is not None:
            result['Permission'] = self.permission

        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_desc is not None:
            result['SupplierDesc'] = self.supplier_desc

        if self.supplier_logo is not None:
            result['SupplierLogo'] = self.supplier_logo

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid

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

        if self.trial_duration is not None:
            result['TrialDuration'] = self.trial_duration

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        if self.version is not None:
            result['Version'] = self.version

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMetadata') is not None:
            self.alarm_metadata = m.get('AlarmMetadata')

        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('Commodity') is not None:
            temp_model = main_models.GetServiceResponseBodyCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('ComplianceMetadata') is not None:
            temp_model = main_models.GetServiceResponseBodyComplianceMetadata()
            self.compliance_metadata = temp_model.from_map(m.get('ComplianceMetadata'))

        if m.get('DeployFrom') is not None:
            self.deploy_from = m.get('DeployFrom')

        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        self.instance_role_infos = []
        if m.get('InstanceRoleInfos') is not None:
            for k1 in m.get('InstanceRoleInfos'):
                temp_model = main_models.GetServiceResponseBodyInstanceRoleInfos()
                self.instance_role_infos.append(temp_model.from_map(k1))

        if m.get('IsSupportOperated') is not None:
            self.is_support_operated = m.get('IsSupportOperated')

        if m.get('LicenseMetadata') is not None:
            self.license_metadata = m.get('LicenseMetadata')

        if m.get('LogMetadata') is not None:
            self.log_metadata = m.get('LogMetadata')

        if m.get('OperationMetadata') is not None:
            self.operation_metadata = m.get('OperationMetadata')

        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierDesc') is not None:
            self.supplier_desc = m.get('SupplierDesc')

        if m.get('SupplierLogo') is not None:
            self.supplier_logo = m.get('SupplierLogo')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')

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

        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

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
        # The type of the contact information.
        self.type = type
        # The contact information.
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

class GetServiceResponseBodyServiceLocaleConfigs(DaraModel):
    def __init__(
        self,
        en_value: str = None,
        original_value: str = None,
        zh_value: str = None,
    ):
        # The English value of the service information.
        self.en_value = en_value
        # The raw data value of the service information.
        self.original_value = original_value
        # The Chinese value of the service information.
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
        name: str = None,
        short_description: str = None,
        softwares: List[main_models.GetServiceResponseBodyServiceInfosSoftwares] = None,
    ):
        # The service agreements.
        self.agreements = agreements
        # The URL of the service icon.
        self.image = image
        # The language of the service configuration. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US: English.
        self.locale = locale
        # The service name.
        self.name = name
        # The summary of the service.
        self.short_description = short_description
        # The service software.
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
        # The software name.
        self.name = name
        # The software version.
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
        # The document URL.
        self.document_url = document_url
        # The language of the service document. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US: English.
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

class GetServiceResponseBodyInstanceRoleInfos(DaraModel):
    def __init__(
        self,
        policy_document: str = None,
        principals: List[str] = None,
        role_name: str = None,
        template_name: str = None,
    ):
        # The content of the control policy.
        self.policy_document = policy_document
        # The information about the RAM entity.
        self.principals = principals
        # The role name.
        self.role_name = role_name
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.principals is not None:
            result['Principals'] = self.principals

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('Principals') is not None:
            self.principals = m.get('Principals')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class GetServiceResponseBodyComplianceMetadata(DaraModel):
    def __init__(
        self,
        compliance_packs: List[str] = None,
    ):
        # The list of compliance packages.
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
        css_metadata: main_models.GetServiceResponseBodyCommodityCssMetadata = None,
        deploy_page: str = None,
        marketplace_metadata: main_models.GetServiceResponseBodyCommodityMarketplaceMetadata = None,
        order_time: Dict[str, List[str]] = None,
        saas_boost_metadata: str = None,
        specifications: List[main_models.GetServiceResponseBodyCommoditySpecifications] = None,
        type: str = None,
    ):
        # The billing method.
        # 
        # Valid values:
        # 
        # **PREPAY** (default): subscription.
        # 
        # **POSTPAY**: pay-as-you-go.
        self.charge_type = charge_type
        # The commodity code.
        self.commodity_code = commodity_code
        # The Lingxiao configuration metadata.
        self.css_metadata = css_metadata
        # The deployment page.
        self.deploy_page = deploy_page
        # The Alibaba Cloud Marketplace metadata.
        self.marketplace_metadata = marketplace_metadata
        # The order time.
        self.order_time = order_time
        # The SaasBoost configuration metadata.
        self.saas_boost_metadata = saas_boost_metadata
        # The Alibaba Cloud Marketplace specification details.
        self.specifications = specifications
        # The type.
        # 
        # Valid values:
        # 
        # Marketplace: Alibaba Cloud Marketplace.
        # 
        # Css: Lingxiao.
        self.type = type

    def validate(self):
        if self.css_metadata:
            self.css_metadata.validate()
        if self.marketplace_metadata:
            self.marketplace_metadata.validate()
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

        if self.css_metadata is not None:
            result['CssMetadata'] = self.css_metadata.to_map()

        if self.deploy_page is not None:
            result['DeployPage'] = self.deploy_page

        if self.marketplace_metadata is not None:
            result['MarketplaceMetadata'] = self.marketplace_metadata.to_map()

        if self.order_time is not None:
            result['OrderTime'] = self.order_time

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

        if m.get('CssMetadata') is not None:
            temp_model = main_models.GetServiceResponseBodyCommodityCssMetadata()
            self.css_metadata = temp_model.from_map(m.get('CssMetadata'))

        if m.get('DeployPage') is not None:
            self.deploy_page = m.get('DeployPage')

        if m.get('MarketplaceMetadata') is not None:
            temp_model = main_models.GetServiceResponseBodyCommodityMarketplaceMetadata()
            self.marketplace_metadata = temp_model.from_map(m.get('MarketplaceMetadata'))

        if m.get('OrderTime') is not None:
            self.order_time = m.get('OrderTime')

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
        # The purchasable duration. Unit: week or year.
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

class GetServiceResponseBodyCommodityMarketplaceMetadata(DaraModel):
    def __init__(
        self,
        specification_mappings: List[main_models.GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings] = None,
    ):
        # The mapping between commodity specifications and templates or packages.
        self.specification_mappings = specification_mappings

    def validate(self):
        if self.specification_mappings:
            for v1 in self.specification_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SpecificationMappings'] = []
        if self.specification_mappings is not None:
            for k1 in self.specification_mappings:
                result['SpecificationMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
    ):
        # The specification code of the Alibaba Cloud Marketplace commodity.
        self.specification_code = specification_code
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
        if self.specification_code is not None:
            result['SpecificationCode'] = self.specification_code

        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecificationCode') is not None:
            self.specification_code = m.get('SpecificationCode')

        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class GetServiceResponseBodyCommodityCssMetadata(DaraModel):
    def __init__(
        self,
        components_mappings: List[main_models.GetServiceResponseBodyCommodityCssMetadataComponentsMappings] = None,
    ):
        # The billing item mappings.
        self.components_mappings = components_mappings

    def validate(self):
        if self.components_mappings:
            for v1 in self.components_mappings:
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components_mappings = []
        if m.get('ComponentsMappings') is not None:
            for k1 in m.get('ComponentsMappings'):
                temp_model = main_models.GetServiceResponseBodyCommodityCssMetadataComponentsMappings()
                self.components_mappings.append(temp_model.from_map(k1))

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

