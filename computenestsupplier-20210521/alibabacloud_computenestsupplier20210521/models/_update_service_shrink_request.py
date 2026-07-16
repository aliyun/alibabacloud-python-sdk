# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceShrinkRequest(DaraModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        approval_type: str = None,
        build_parameters: str = None,
        client_token: str = None,
        commodity_shrink: str = None,
        compliance_metadata_shrink: str = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        dry_run: bool = None,
        duration: int = None,
        is_default: bool = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        policy_names: str = None,
        region_id: str = None,
        resellable: bool = None,
        service_id: str = None,
        service_info: List[main_models.UpdateServiceShrinkRequestServiceInfo] = None,
        service_locale_configs: List[main_models.UpdateServiceShrinkRequestServiceLocaleConfigs] = None,
        service_type: str = None,
        service_version: str = None,
        share_type: str = None,
        tenant_type: str = None,
        trial_duration: int = None,
        update_option_shrink: str = None,
        upgrade_metadata: str = None,
        version_name: str = None,
    ):
        # The alert configurations for the service.
        # 
        # > This configuration takes effect only after you configure an alert-related access policy for **PolicyNames**.
        self.alarm_metadata = alarm_metadata
        # The approval type for service usage requests. Valid values:
        # 
        # - Manual: The request is manually approved.
        # 
        # - AutoPass: The request is automatically approved.
        self.approval_type = approval_type
        # The parameters for building the service.
        self.build_parameters = build_parameters
        # A client token to ensure that the request is idempotent. You can use a client to generate the token. Make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The commodity information.
        self.commodity_shrink = commodity_shrink
        # The compliance check metadata.
        self.compliance_metadata_shrink = compliance_metadata_shrink
        # The information about the service deployment configuration. The data format varies based on the deployment type. The value is a JSON string.
        self.deploy_metadata = deploy_metadata
        # The deployment type. Valid values:
        # 
        # - ros: The service is deployed using ROS.
        # 
        # - terraform: The service is deployed using Terraform.
        # 
        # - spi: The service is deployed by calling an SPI.
        # 
        # - operation: The service is an O\\&M service.
        # 
        # - container: The service is deployed using containers.
        # 
        # - pkg: The service is a package service.
        self.deploy_type = deploy_type
        # Specifies whether to perform a dry run for the request. A dry run checks the permissions and the instance status. Valid values:
        # 
        # - true: sends the request but does not update the service.
        # 
        # - false: sends the request. If the check is successful, the service is updated.
        self.dry_run = dry_run
        # The O\\&M duration. Unit: seconds.
        self.duration = duration
        self.is_default = is_default
        # Specifies whether to enable O\\&M. Default value: false. Valid values:
        # 
        # - true: enables O\\&M.
        # 
        # - false: disables O\\&M.
        # 
        # > This parameter is required when **ServiceType** is set to **private**.
        self.is_support_operated = is_support_operated
        # The license metadata.
        self.license_metadata = license_metadata
        # The application log configurations.
        self.log_metadata = log_metadata
        # The O\\&M configuration.
        self.operation_metadata = operation_metadata
        # The policy name. The name of a single policy can be up to 128 characters in length. If you specify multiple policies, separate them with commas (,). Only O\\&M-related policies are supported.
        self.policy_names = policy_names
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to enable distribution. Valid values:
        # 
        # - false: Distribution is not enabled.
        # 
        # - true: Distribution is enabled.
        self.resellable = resellable
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service details.
        self.service_info = service_info
        # The multilingual configurations of the service.
        self.service_locale_configs = service_locale_configs
        # The service type. Valid values:
        # 
        # - private: The service instance is deployed in the user account.
        # 
        # - managed: The service instance is deployed in the service provider account.
        # 
        # - operation: The service instance is an O\\&M instance.
        # 
        # - poc: The service instance is a trial instance.
        self.service_type = service_type
        # The service version.
        self.service_version = service_version
        # The sharing type. Valid values:
        # 
        # - Public: The service is public. Formal and trial deployments are not restricted.
        # 
        # - Restricted: The service is restricted. Formal and trial deployments are restricted.
        # 
        # - OnlyFormalRestricted: Only formal deployments are restricted.
        # 
        # - OnlyTrailRestricted: Only trial deployments are restricted.
        # 
        # - Hidden: The service is hidden. You cannot view the service or request deployment permissions.
        self.share_type = share_type
        # The tenant type. Valid values:
        # 
        # - SingleTenant: The service is single-tenant.
        # 
        # - MultiTenant: The service is multi-tenant.
        self.tenant_type = tenant_type
        # The trial duration. Unit: days. The maximum trial duration is 30 days.
        self.trial_duration = trial_duration
        # The update options.
        self.update_option_shrink = update_option_shrink
        # The upgrade metadata.
        self.upgrade_metadata = upgrade_metadata
        # The version name.
        self.version_name = version_name

    def validate(self):
        if self.service_info:
            for v1 in self.service_info:
                 if v1:
                    v1.validate()
        if self.service_locale_configs:
            for v1 in self.service_locale_configs:
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

        if self.commodity_shrink is not None:
            result['Commodity'] = self.commodity_shrink

        if self.compliance_metadata_shrink is not None:
            result['ComplianceMetadata'] = self.compliance_metadata_shrink

        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

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

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k1 in self.service_info:
                result['ServiceInfo'].append(k1.to_map() if k1 else None)

        result['ServiceLocaleConfigs'] = []
        if self.service_locale_configs is not None:
            for k1 in self.service_locale_configs:
                result['ServiceLocaleConfigs'].append(k1.to_map() if k1 else None)

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.tenant_type is not None:
            result['TenantType'] = self.tenant_type

        if self.trial_duration is not None:
            result['TrialDuration'] = self.trial_duration

        if self.update_option_shrink is not None:
            result['UpdateOption'] = self.update_option_shrink

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

        if m.get('Commodity') is not None:
            self.commodity_shrink = m.get('Commodity')

        if m.get('ComplianceMetadata') is not None:
            self.compliance_metadata_shrink = m.get('ComplianceMetadata')

        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

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

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k1 in m.get('ServiceInfo'):
                temp_model = main_models.UpdateServiceShrinkRequestServiceInfo()
                self.service_info.append(temp_model.from_map(k1))

        self.service_locale_configs = []
        if m.get('ServiceLocaleConfigs') is not None:
            for k1 in m.get('ServiceLocaleConfigs'):
                temp_model = main_models.UpdateServiceShrinkRequestServiceLocaleConfigs()
                self.service_locale_configs.append(temp_model.from_map(k1))

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')

        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')

        if m.get('UpdateOption') is not None:
            self.update_option_shrink = m.get('UpdateOption')

        if m.get('UpgradeMetadata') is not None:
            self.upgrade_metadata = m.get('UpgradeMetadata')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class UpdateServiceShrinkRequestServiceLocaleConfigs(DaraModel):
    def __init__(
        self,
        en_value: str = None,
        original_value: str = None,
        zh_value: str = None,
    ):
        # The English value of the business information.
        self.en_value = en_value
        # The raw data value of the business information.
        self.original_value = original_value
        # The Chinese value of the business information.
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

class UpdateServiceShrinkRequestServiceInfo(DaraModel):
    def __init__(
        self,
        agreements: List[main_models.UpdateServiceShrinkRequestServiceInfoAgreements] = None,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
        softwares: List[main_models.UpdateServiceShrinkRequestServiceInfoSoftwares] = None,
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
        self.locale = locale
        # The URL of the detailed description of the service.
        self.long_description_url = long_description_url
        # The service name.
        self.name = name
        # The description of the service.
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
                temp_model = main_models.UpdateServiceShrinkRequestServiceInfoAgreements()
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
                temp_model = main_models.UpdateServiceShrinkRequestServiceInfoSoftwares()
                self.softwares.append(temp_model.from_map(k1))

        return self

class UpdateServiceShrinkRequestServiceInfoSoftwares(DaraModel):
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

class UpdateServiceShrinkRequestServiceInfoAgreements(DaraModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        # The name of the agreement document.
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

