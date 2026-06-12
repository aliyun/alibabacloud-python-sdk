# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class CreateServiceRequest(DaraModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        approval_type: str = None,
        build_parameters: str = None,
        client_token: str = None,
        compliance_metadata: main_models.CreateServiceRequestComplianceMetadata = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        dry_run: bool = None,
        duration: int = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        policy_names: str = None,
        region_id: str = None,
        resellable: bool = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_info: List[main_models.CreateServiceRequestServiceInfo] = None,
        service_type: str = None,
        share_type: str = None,
        source_service_id: str = None,
        source_service_version: str = None,
        tag: List[main_models.CreateServiceRequestTag] = None,
        tenant_type: str = None,
        trial_duration: int = None,
        upgrade_metadata: str = None,
        version_name: str = None,
    ):
        # The alert configurations for the service.
        # 
        # > This configuration takes effect only after an alert-related access policy is configured in \\`PolicyNames\\`.
        self.alarm_metadata = alarm_metadata
        # The approval type for service usage requests. Valid values:
        # 
        # - Manual: The request requires manual approval.
        # 
        # - AutoPass: The request is automatically approved.
        self.approval_type = approval_type
        # The parameters for building the service.
        self.build_parameters = build_parameters
        # A client token used to ensure the idempotence of the request. Generate a unique value for this parameter from your client. \\`ClientToken\\` supports only ASCII characters.
        self.client_token = client_token
        # The compliance check metadata.
        self.compliance_metadata = compliance_metadata
        # The deployment configuration of the service. The information stored varies by deployment type. Different deployment types have different data formats. The data is stored in a JSON string.
        self.deploy_metadata = deploy_metadata
        # The deployment type. Valid values:
        # 
        # - ros: The service is deployed using ROS.
        # 
        # - terraform: The service is deployed using Terraform.
        # 
        # - ack: The service is deployed using ACK.
        # 
        # - spi: The service is deployed by invoking an SPI.
        # 
        # - operation: The service is an O\\&M service.
        # 
        # This parameter is required.
        self.deploy_type = deploy_type
        # Specifies whether to perform a dry run to check the request.
        self.dry_run = dry_run
        # The O\\&M duration. Unit: seconds.
        self.duration = duration
        # Specifies whether to enable O\\&M. Default value: false. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # > This parameter is required when \\`ServiceType\\` is set to \\`private\\`.
        self.is_support_operated = is_support_operated
        # The license metadata.
        self.license_metadata = license_metadata
        # The application log configuration.
        self.log_metadata = log_metadata
        # The O\\&M configuration.
        self.operation_metadata = operation_metadata
        # The policy name. The name of a single policy can be up to 128 characters in length. Separate multiple names with commas (,). Only policies related to O\\&M parameters are supported.
        self.policy_names = policy_names
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether the service can be distributed. Valid values:
        # 
        # - false: The service cannot be distributed.
        # 
        # - true: The service can be distributed.
        self.resellable = resellable
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The service ID.
        self.service_id = service_id
        # The service details.
        self.service_info = service_info
        # The service type. Valid values:
        # 
        # - private: The service instance is deployed in the user\\"s account.
        # 
        # - managed: The service instance is managed in the service provider\\"s account.
        # 
        # - operation: An O\\&M service instance.
        # 
        # - poc: A trial service instance.
        self.service_type = service_type
        # The sharing type. Valid values:
        # 
        # - Public: The service is public. Full and trial deployments are not restricted.
        # 
        # - Restricted: The service is restricted. Full and trial deployments are restricted.
        # 
        # - OnlyFormalRestricted: Only full deployments are restricted.
        # 
        # - OnlyTrailRestricted: Only trial deployments are restricted.
        # 
        # - Hidden: The service is hidden. It is not visible and you cannot request deployment permissions.
        self.share_type = share_type
        # The ID of the source service for distribution.
        self.source_service_id = source_service_id
        # The version of the source service for distribution.
        self.source_service_version = source_service_version
        # The custom tags.
        self.tag = tag
        # The tenant type. Valid values:
        # 
        # - SingleTenant: Single-tenant.
        # 
        # - MultiTenant: Multitenant.
        self.tenant_type = tenant_type
        # The trial duration. Unit: days. The maximum trial duration is 30 days.
        self.trial_duration = trial_duration
        # The upgrade metadata.
        self.upgrade_metadata = upgrade_metadata
        # The version name.
        self.version_name = version_name

    def validate(self):
        if self.compliance_metadata:
            self.compliance_metadata.validate()
        if self.service_info:
            for v1 in self.service_info:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
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

        if self.build_parameters is not None:
            result['BuildParameters'] = self.build_parameters

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compliance_metadata is not None:
            result['ComplianceMetadata'] = self.compliance_metadata.to_map()

        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.is_support_operated is not None:
            result['IsSupportOperated'] = self.is_support_operated

        if self.license_metadata is not None:
            result['LicenseMetadata'] = self.license_metadata

        if self.log_metadata is not None:
            result['LogMetadata'] = self.log_metadata

        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata

        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resellable is not None:
            result['Resellable'] = self.resellable

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k1 in self.service_info:
                result['ServiceInfo'].append(k1.to_map() if k1 else None)

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.source_service_id is not None:
            result['SourceServiceId'] = self.source_service_id

        if self.source_service_version is not None:
            result['SourceServiceVersion'] = self.source_service_version

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tenant_type is not None:
            result['TenantType'] = self.tenant_type

        if self.trial_duration is not None:
            result['TrialDuration'] = self.trial_duration

        if self.upgrade_metadata is not None:
            result['UpgradeMetadata'] = self.upgrade_metadata

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMetadata') is not None:
            self.alarm_metadata = m.get('AlarmMetadata')

        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('BuildParameters') is not None:
            self.build_parameters = m.get('BuildParameters')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ComplianceMetadata') is not None:
            temp_model = main_models.CreateServiceRequestComplianceMetadata()
            self.compliance_metadata = temp_model.from_map(m.get('ComplianceMetadata'))

        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('IsSupportOperated') is not None:
            self.is_support_operated = m.get('IsSupportOperated')

        if m.get('LicenseMetadata') is not None:
            self.license_metadata = m.get('LicenseMetadata')

        if m.get('LogMetadata') is not None:
            self.log_metadata = m.get('LogMetadata')

        if m.get('OperationMetadata') is not None:
            self.operation_metadata = m.get('OperationMetadata')

        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resellable') is not None:
            self.resellable = m.get('Resellable')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k1 in m.get('ServiceInfo'):
                temp_model = main_models.CreateServiceRequestServiceInfo()
                self.service_info.append(temp_model.from_map(k1))

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('SourceServiceId') is not None:
            self.source_service_id = m.get('SourceServiceId')

        if m.get('SourceServiceVersion') is not None:
            self.source_service_version = m.get('SourceServiceVersion')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateServiceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')

        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')

        if m.get('UpgradeMetadata') is not None:
            self.upgrade_metadata = m.get('UpgradeMetadata')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class CreateServiceRequestTag(DaraModel):
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

class CreateServiceRequestServiceInfo(DaraModel):
    def __init__(
        self,
        agreements: List[main_models.CreateServiceRequestServiceInfoAgreements] = None,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
        softwares: List[main_models.CreateServiceRequestServiceInfoSoftwares] = None,
    ):
        # The information about the service agreements.
        self.agreements = agreements
        # The URL of the service icon.
        self.image = image
        # The language of the service. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US: English.
        # 
        # This parameter is required.
        self.locale = locale
        # The detailed description of the service.
        self.long_description_url = long_description_url
        # The service name.
        # 
        # This parameter is required.
        self.name = name
        # A brief description of the service.
        self.short_description = short_description
        # The information about the software used in the service.
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
                temp_model = main_models.CreateServiceRequestServiceInfoAgreements()
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
                temp_model = main_models.CreateServiceRequestServiceInfoSoftwares()
                self.softwares.append(temp_model.from_map(k1))

        return self

class CreateServiceRequestServiceInfoSoftwares(DaraModel):
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

class CreateServiceRequestServiceInfoAgreements(DaraModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        # The name of the agreement.
        self.name = name
        # The URL of the agreement.
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

class CreateServiceRequestComplianceMetadata(DaraModel):
    def __init__(
        self,
        compliance_packs: List[str] = None,
    ):
        # The selected compliance packages.
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

