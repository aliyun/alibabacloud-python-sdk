# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class ContinueDeployServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        parameters: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.parameters = parameters
        self.region_id = region_id
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ContinueDeployServiceInstanceResponseBodyDryRunResult(TeaModel):
    def __init__(
        self,
        parameters_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
    ):
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters_allowed_to_be_modified is not None:
            result['ParametersAllowedToBeModified'] = self.parameters_allowed_to_be_modified
        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified
        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')
        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')
        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')
        return self


class ContinueDeployServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        dry_run_result: ContinueDeployServiceInstanceResponseBodyDryRunResult = None,
        request_id: str = None,
        service_instance_id: str = None,
    ):
        self.dry_run_result = dry_run_result
        self.request_id = request_id
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.dry_run_result:
            self.dry_run_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run_result is not None:
            result['DryRunResult'] = self.dry_run_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRunResult') is not None:
            temp_model = ContinueDeployServiceInstanceResponseBodyDryRunResult()
            self.dry_run_result = temp_model.from_map(m['DryRunResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ContinueDeployServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ContinueDeployServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ContinueDeployServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateArtifactRequestArtifactProperty(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_version: str = None,
        file_script_metadata: str = None,
        image_id: str = None,
        region_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        script_metadata: str = None,
        tag: str = None,
        url: str = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_version = commodity_version
        self.file_script_metadata = file_script_metadata
        self.image_id = image_id
        self.region_id = region_id
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.script_metadata = script_metadata
        self.tag = tag
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_version is not None:
            result['CommodityVersion'] = self.commodity_version
        if self.file_script_metadata is not None:
            result['FileScriptMetadata'] = self.file_script_metadata
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.script_metadata is not None:
            result['ScriptMetadata'] = self.script_metadata
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityVersion') is not None:
            self.commodity_version = m.get('CommodityVersion')
        if m.get('FileScriptMetadata') is not None:
            self.file_script_metadata = m.get('FileScriptMetadata')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('ScriptMetadata') is not None:
            self.script_metadata = m.get('ScriptMetadata')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateArtifactRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property: CreateArtifactRequestArtifactProperty = None,
        artifact_type: str = None,
        description: str = None,
        name: str = None,
        support_region_ids: List[str] = None,
        version_name: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_property = artifact_property
        self.artifact_type = artifact_type
        self.description = description
        self.name = name
        self.support_region_ids = support_region_ids
        self.version_name = version_name

    def validate(self):
        if self.artifact_property:
            self.artifact_property.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property.to_map()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            temp_model = CreateArtifactRequestArtifactProperty()
            self.artifact_property = temp_model.from_map(m['ArtifactProperty'])
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateArtifactShrinkRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property_shrink: str = None,
        artifact_type: str = None,
        description: str = None,
        name: str = None,
        support_region_ids: List[str] = None,
        version_name: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_property_shrink = artifact_property_shrink
        self.artifact_type = artifact_type
        self.description = description
        self.name = name
        self.support_region_ids = support_region_ids
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property_shrink is not None:
            result['ArtifactProperty'] = self.artifact_property_shrink
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property_shrink = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateArtifactResponseBody(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property: str = None,
        artifact_type: str = None,
        artifact_version: str = None,
        description: str = None,
        gmt_modified: str = None,
        max_version: int = None,
        name: str = None,
        request_id: str = None,
        status: str = None,
        support_region_ids: str = None,
        version_name: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_property = artifact_property
        self.artifact_type = artifact_type
        self.artifact_version = artifact_version
        self.description = description
        self.gmt_modified = gmt_modified
        self.max_version = max_version
        self.name = name
        self.request_id = request_id
        self.status = status
        self.support_region_ids = support_region_ids
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateArtifactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequestServiceInfo(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.image = image
        self.locale = locale
        self.long_description_url = long_description_url
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        return self


class CreateServiceRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        approval_type: str = None,
        client_token: str = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        duration: int = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        policy_names: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_info: List[CreateServiceRequestServiceInfo] = None,
        service_type: str = None,
        share_type: str = None,
        source_service_id: str = None,
        source_service_version: str = None,
        tag: List[CreateServiceRequestTag] = None,
        tenant_type: str = None,
        trial_duration: int = None,
        upgrade_metadata: str = None,
        version_name: str = None,
    ):
        self.alarm_metadata = alarm_metadata
        self.approval_type = approval_type
        self.client_token = client_token
        self.deploy_metadata = deploy_metadata
        self.deploy_type = deploy_type
        self.duration = duration
        self.is_support_operated = is_support_operated
        self.license_metadata = license_metadata
        self.log_metadata = log_metadata
        self.operation_metadata = operation_metadata
        self.policy_names = policy_names
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.service_id = service_id
        self.service_info = service_info
        self.service_type = service_type
        self.share_type = share_type
        self.source_service_id = source_service_id
        self.source_service_version = source_service_version
        self.tag = tag
        self.tenant_type = tenant_type
        self.trial_duration = trial_duration
        self.upgrade_metadata = upgrade_metadata
        self.version_name = version_name

    def validate(self):
        if self.service_info:
            for k in self.service_info:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_metadata is not None:
            result['AlarmMetadata'] = self.alarm_metadata
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k in self.service_info:
                result['ServiceInfo'].append(k.to_map() if k else None)
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
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k in m.get('ServiceInfo'):
                temp_model = CreateServiceRequestServiceInfo()
                self.service_info.append(temp_model.from_map(k))
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
            for k in m.get('Tag'):
                temp_model = CreateServiceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')
        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')
        if m.get('UpgradeMetadata') is not None:
            self.upgrade_metadata = m.get('UpgradeMetadata')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_id: str = None,
        status: str = None,
        version: str = None,
    ):
        self.request_id = request_id
        self.service_id = service_id
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceInstanceRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        name: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        tag: List[CreateServiceInstanceRequestTag] = None,
        template_name: str = None,
        user_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.name = name
        self.parameters = parameters
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.service_id = service_id
        self.service_version = service_version
        self.specification_name = specification_name
        self.tag = tag
        self.template_name = template_name
        self.user_id = user_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateServiceInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateServiceInstanceShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateServiceInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        name: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        tag: List[CreateServiceInstanceShrinkRequestTag] = None,
        template_name: str = None,
        user_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.name = name
        self.parameters_shrink = parameters_shrink
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.service_id = service_id
        self.service_version = service_version
        self.specification_name = specification_name
        self.tag = tag
        self.template_name = template_name
        self.user_id = user_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateServiceInstanceShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_instance_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.service_instance_id = service_instance_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteArtifactRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_version: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_version = artifact_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        return self


class DeleteArtifactResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteArtifactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.service_id = service_id
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: List[str] = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class DeleteServiceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_name: str = None,
        artifact_version: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_name = artifact_name
        self.artifact_version = artifact_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_name is not None:
            result['ArtifactName'] = self.artifact_name
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactName') is not None:
            self.artifact_name = m.get('ArtifactName')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        return self


class GetArtifactResponseBody(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property: str = None,
        artifact_type: str = None,
        artifact_version: str = None,
        description: str = None,
        gmt_modified: str = None,
        max_version: int = None,
        name: str = None,
        progress: str = None,
        request_id: str = None,
        status: str = None,
        support_region_ids: str = None,
        version_name: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_property = artifact_property
        self.artifact_type = artifact_type
        self.artifact_version = artifact_version
        self.description = description
        self.gmt_modified = gmt_modified
        self.max_version = max_version
        self.name = name
        self.progress = progress
        self.request_id = request_id
        self.status = status
        self.support_region_ids = support_region_ids
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArtifactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactRepositoryCredentialsRequest(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        deploy_region_id: str = None,
    ):
        self.artifact_type = artifact_type
        self.deploy_region_id = deploy_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        return self


class GetArtifactRepositoryCredentialsResponseBodyAvailableResources(TeaModel):
    def __init__(
        self,
        path: str = None,
        region_id: str = None,
        repository_name: str = None,
    ):
        self.path = path
        self.region_id = region_id
        self.repository_name = repository_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repository_name is not None:
            result['RepositoryName'] = self.repository_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepositoryName') is not None:
            self.repository_name = m.get('RepositoryName')
        return self


class GetArtifactRepositoryCredentialsResponseBodyCredentials(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        password: str = None,
        security_token: str = None,
        username: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.password = password
        self.security_token = security_token
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.password is not None:
            result['Password'] = self.password
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetArtifactRepositoryCredentialsResponseBody(TeaModel):
    def __init__(
        self,
        available_resources: List[GetArtifactRepositoryCredentialsResponseBodyAvailableResources] = None,
        credentials: GetArtifactRepositoryCredentialsResponseBodyCredentials = None,
        expire_date: str = None,
        request_id: str = None,
    ):
        self.available_resources = available_resources
        self.credentials = credentials
        self.expire_date = expire_date
        self.request_id = request_id

    def validate(self):
        if self.available_resources:
            for k in self.available_resources:
                if k:
                    k.validate()
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableResources'] = []
        if self.available_resources is not None:
            for k in self.available_resources:
                result['AvailableResources'].append(k.to_map() if k else None)
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_resources = []
        if m.get('AvailableResources') is not None:
            for k in m.get('AvailableResources'):
                temp_model = GetArtifactRepositoryCredentialsResponseBodyAvailableResources()
                self.available_resources.append(temp_model.from_map(k))
        if m.get('Credentials') is not None:
            temp_model = GetArtifactRepositoryCredentialsResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetArtifactRepositoryCredentialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArtifactRepositoryCredentialsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetArtifactRepositoryCredentialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRequest(TeaModel):
    def __init__(
        self,
        filter_ali_uid: bool = None,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        shared_account_type: str = None,
        show_detail: List[str] = None,
    ):
        self.filter_ali_uid = filter_ali_uid
        self.region_id = region_id
        self.service_id = service_id
        self.service_version = service_version
        self.shared_account_type = shared_account_type
        self.show_detail = show_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_ali_uid is not None:
            result['FilterAliUid'] = self.filter_ali_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.shared_account_type is not None:
            result['SharedAccountType'] = self.shared_account_type
        if self.show_detail is not None:
            result['ShowDetail'] = self.show_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterAliUid') is not None:
            self.filter_ali_uid = m.get('FilterAliUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SharedAccountType') is not None:
            self.shared_account_type = m.get('SharedAccountType')
        if m.get('ShowDetail') is not None:
            self.show_detail = m.get('ShowDetail')
        return self


class GetServiceResponseBodyCommodityEntities(TeaModel):
    def __init__(
        self,
        entity_ids: List[str] = None,
        predefined_parameter_name: str = None,
        template_name: str = None,
    ):
        self.entity_ids = entity_ids
        self.predefined_parameter_name = predefined_parameter_name
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_ids is not None:
            result['EntityIds'] = self.entity_ids
        if self.predefined_parameter_name is not None:
            result['PredefinedParameterName'] = self.predefined_parameter_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityIds') is not None:
            self.entity_ids = m.get('EntityIds')
        if m.get('PredefinedParameterName') is not None:
            self.predefined_parameter_name = m.get('PredefinedParameterName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceResponseBodyCommoditySpecifications(TeaModel):
    def __init__(
        self,
        predefined_parameter_name: str = None,
        specification_code: str = None,
        template_name: str = None,
    ):
        self.predefined_parameter_name = predefined_parameter_name
        self.specification_code = specification_code
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_parameter_name is not None:
            result['PredefinedParameterName'] = self.predefined_parameter_name
        if self.specification_code is not None:
            result['SpecificationCode'] = self.specification_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedParameterName') is not None:
            self.predefined_parameter_name = m.get('PredefinedParameterName')
        if m.get('SpecificationCode') is not None:
            self.specification_code = m.get('SpecificationCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceResponseBodyServiceInfos(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.image = image
        self.locale = locale
        self.long_description_url = long_description_url
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        return self


class GetServiceResponseBodyStatistic(TeaModel):
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
        self.accumulative_instance_count = accumulative_instance_count
        self.accumulative_poc_amount = accumulative_poc_amount
        self.accumulative_user_count = accumulative_user_count
        self.average_poc_amount = average_poc_amount
        self.average_poc_duration = average_poc_duration
        self.average_poc_unit_amount = average_poc_unit_amount
        self.deployed_service_instance_count = deployed_service_instance_count
        self.deployed_user_count = deployed_user_count
        self.submitted_usage_count = submitted_usage_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBody(TeaModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        approval_type: str = None,
        commodity_code: str = None,
        commodity_entities: List[GetServiceResponseBodyCommodityEntities] = None,
        commodity_specifications: List[GetServiceResponseBodyCommoditySpecifications] = None,
        create_time: str = None,
        default_license_days: int = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        duration: int = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        pay_from_type: str = None,
        pay_type: str = None,
        permission: str = None,
        policy_names: str = None,
        progress: int = None,
        publish_time: str = None,
        registration_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        service_doc_url: str = None,
        service_id: str = None,
        service_infos: List[GetServiceResponseBodyServiceInfos] = None,
        service_product_url: str = None,
        service_type: str = None,
        share_type: str = None,
        source_service_id: str = None,
        source_service_version: str = None,
        source_supplier_name: str = None,
        statistic: GetServiceResponseBodyStatistic = None,
        status: str = None,
        status_detail: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        tags: List[GetServiceResponseBodyTags] = None,
        tenant_type: str = None,
        test_status: str = None,
        trial_duration: int = None,
        trial_type: str = None,
        update_time: str = None,
        upgrade_metadata: str = None,
        version: str = None,
        version_name: str = None,
    ):
        self.alarm_metadata = alarm_metadata
        self.approval_type = approval_type
        self.commodity_code = commodity_code
        self.commodity_entities = commodity_entities
        self.commodity_specifications = commodity_specifications
        self.create_time = create_time
        self.default_license_days = default_license_days
        self.deploy_metadata = deploy_metadata
        self.deploy_type = deploy_type
        self.duration = duration
        self.is_support_operated = is_support_operated
        self.license_metadata = license_metadata
        self.log_metadata = log_metadata
        self.operation_metadata = operation_metadata
        self.pay_from_type = pay_from_type
        self.pay_type = pay_type
        self.permission = permission
        self.policy_names = policy_names
        self.progress = progress
        self.publish_time = publish_time
        self.registration_id = registration_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.service_doc_url = service_doc_url
        self.service_id = service_id
        self.service_infos = service_infos
        self.service_product_url = service_product_url
        self.service_type = service_type
        self.share_type = share_type
        self.source_service_id = source_service_id
        self.source_service_version = source_service_version
        self.source_supplier_name = source_supplier_name
        self.statistic = statistic
        self.status = status
        self.status_detail = status_detail
        self.supplier_name = supplier_name
        self.supplier_url = supplier_url
        self.tags = tags
        self.tenant_type = tenant_type
        self.test_status = test_status
        self.trial_duration = trial_duration
        self.trial_type = trial_type
        self.update_time = update_time
        self.upgrade_metadata = upgrade_metadata
        self.version = version
        self.version_name = version_name

    def validate(self):
        if self.commodity_entities:
            for k in self.commodity_entities:
                if k:
                    k.validate()
        if self.commodity_specifications:
            for k in self.commodity_specifications:
                if k:
                    k.validate()
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()
        if self.statistic:
            self.statistic.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_metadata is not None:
            result['AlarmMetadata'] = self.alarm_metadata
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        result['CommodityEntities'] = []
        if self.commodity_entities is not None:
            for k in self.commodity_entities:
                result['CommodityEntities'].append(k.to_map() if k else None)
        result['CommoditySpecifications'] = []
        if self.commodity_specifications is not None:
            for k in self.commodity_specifications:
                result['CommoditySpecifications'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_license_days is not None:
            result['DefaultLicenseDays'] = self.default_license_days
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
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
        if self.pay_from_type is not None:
            result['PayFromType'] = self.pay_from_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_doc_url is not None:
            result['ServiceDocUrl'] = self.service_doc_url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_product_url is not None:
            result['ServiceProductUrl'] = self.service_product_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.share_type is not None:
            result['ShareType'] = self.share_type
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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMetadata') is not None:
            self.alarm_metadata = m.get('AlarmMetadata')
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        self.commodity_entities = []
        if m.get('CommodityEntities') is not None:
            for k in m.get('CommodityEntities'):
                temp_model = GetServiceResponseBodyCommodityEntities()
                self.commodity_entities.append(temp_model.from_map(k))
        self.commodity_specifications = []
        if m.get('CommoditySpecifications') is not None:
            for k in m.get('CommoditySpecifications'):
                temp_model = GetServiceResponseBodyCommoditySpecifications()
                self.commodity_specifications.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultLicenseDays') is not None:
            self.default_license_days = m.get('DefaultLicenseDays')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
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
        if m.get('PayFromType') is not None:
            self.pay_from_type = m.get('PayFromType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceDocUrl') is not None:
            self.service_doc_url = m.get('ServiceDocUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceResponseBodyServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceProductUrl') is not None:
            self.service_product_url = m.get('ServiceProductUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SourceServiceId') is not None:
            self.source_service_id = m.get('SourceServiceId')
        if m.get('SourceServiceVersion') is not None:
            self.source_service_version = m.get('SourceServiceVersion')
        if m.get('SourceSupplierName') is not None:
            self.source_supplier_name = m.get('SourceSupplierName')
        if m.get('Statistic') is not None:
            temp_model = GetServiceResponseBodyStatistic()
            self.statistic = temp_model.from_map(m['Statistic'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetServiceResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
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
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceEstimateCostRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        template_name: str = None,
    ):
        self.client_token = client_token
        self.parameters = parameters
        self.region_id = region_id
        self.service_id = service_id
        self.service_instance_id = service_instance_id
        self.service_version = service_version
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceEstimateCostShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        template_name: str = None,
    ):
        self.client_token = client_token
        self.parameters_shrink = parameters_shrink
        self.region_id = region_id
        self.service_id = service_id
        self.service_instance_id = service_instance_id
        self.service_version = service_version
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceEstimateCostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class GetServiceEstimateCostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceEstimateCostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetServiceEstimateCostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        self.region_id = region_id
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs(TeaModel):
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
        self.connect_bandwidth = connect_bandwidth
        self.domain_name = domain_name
        self.endpoint_ips = endpoint_ips
        self.ingress_endpoint_status = ingress_endpoint_status
        self.network_service_status = network_service_status
        self.security_groups = security_groups
        self.v_switches = v_switches
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections(TeaModel):
    def __init__(
        self,
        connection_configs: List[GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs] = None,
        endpoint_id: str = None,
        endpoint_service_id: str = None,
        private_zone_name: str = None,
    ):
        self.connection_configs = connection_configs
        self.endpoint_id = endpoint_id
        self.endpoint_service_id = endpoint_service_id
        self.private_zone_name = private_zone_name

    def validate(self):
        if self.connection_configs:
            for k in self.connection_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionConfigs'] = []
        if self.connection_configs is not None:
            for k in self.connection_configs:
                result['ConnectionConfigs'].append(k.to_map() if k else None)
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
            for k in m.get('ConnectionConfigs'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs()
                self.connection_configs.append(temp_model.from_map(k))
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointServiceId') is not None:
            self.endpoint_service_id = m.get('EndpointServiceId')
        if m.get('PrivateZoneName') is not None:
            self.private_zone_name = m.get('PrivateZoneName')
        return self


class GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        endpoint_service_id: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.endpoint_service_id = endpoint_service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceInstanceResponseBodyNetworkConfig(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        endpoint_service_id: str = None,
        private_vpc_connections: List[GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections] = None,
        reverse_private_vpc_connections: List[GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections] = None,
    ):
        self.endpoint_id = endpoint_id
        self.endpoint_service_id = endpoint_service_id
        self.private_vpc_connections = private_vpc_connections
        self.reverse_private_vpc_connections = reverse_private_vpc_connections

    def validate(self):
        if self.private_vpc_connections:
            for k in self.private_vpc_connections:
                if k:
                    k.validate()
        if self.reverse_private_vpc_connections:
            for k in self.reverse_private_vpc_connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_service_id is not None:
            result['EndpointServiceId'] = self.endpoint_service_id
        result['PrivateVpcConnections'] = []
        if self.private_vpc_connections is not None:
            for k in self.private_vpc_connections:
                result['PrivateVpcConnections'].append(k.to_map() if k else None)
        result['ReversePrivateVpcConnections'] = []
        if self.reverse_private_vpc_connections is not None:
            for k in self.reverse_private_vpc_connections:
                result['ReversePrivateVpcConnections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointServiceId') is not None:
            self.endpoint_service_id = m.get('EndpointServiceId')
        self.private_vpc_connections = []
        if m.get('PrivateVpcConnections') is not None:
            for k in m.get('PrivateVpcConnections'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections()
                self.private_vpc_connections.append(temp_model.from_map(k))
        self.reverse_private_vpc_connections = []
        if m.get('ReversePrivateVpcConnections') is not None:
            for k in m.get('ReversePrivateVpcConnections'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections()
                self.reverse_private_vpc_connections.append(temp_model.from_map(k))
        return self


class GetServiceInstanceResponseBodyServiceServiceInfos(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.image = image
        self.locale = locale
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceInstanceResponseBodyService(TeaModel):
    def __init__(
        self,
        deploy_metadata: str = None,
        deploy_type: str = None,
        publish_time: str = None,
        service_doc_url: str = None,
        service_id: str = None,
        service_infos: List[GetServiceInstanceResponseBodyServiceServiceInfos] = None,
        service_product_url: str = None,
        service_type: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        upgradable_service_versions: List[str] = None,
        version: str = None,
        version_name: str = None,
    ):
        self.deploy_metadata = deploy_metadata
        self.deploy_type = deploy_type
        self.publish_time = publish_time
        self.service_doc_url = service_doc_url
        self.service_id = service_id
        self.service_infos = service_infos
        self.service_product_url = service_product_url
        self.service_type = service_type
        self.status = status
        self.supplier_name = supplier_name
        self.supplier_url = supplier_url
        self.upgradable_service_versions = upgradable_service_versions
        self.version = version
        self.version_name = version_name

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
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
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceInstanceResponseBodyServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
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
        if m.get('UpgradableServiceVersions') is not None:
            self.upgradable_service_versions = m.get('UpgradableServiceVersions')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetServiceInstanceResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        biz_status: str = None,
        create_time: str = None,
        enable_instance_ops: bool = None,
        enable_user_prometheus: str = None,
        end_time: str = None,
        is_operated: bool = None,
        license_metadata: str = None,
        name: str = None,
        network_config: GetServiceInstanceResponseBodyNetworkConfig = None,
        operated_service_instance_id: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        outputs: str = None,
        parameters: str = None,
        pay_type: str = None,
        predefined_parameter_name: str = None,
        progress: int = None,
        rd_account_login_url: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resources: str = None,
        service: GetServiceInstanceResponseBodyService = None,
        service_instance_id: str = None,
        service_type: str = None,
        source: str = None,
        status: str = None,
        status_detail: str = None,
        supplier_uid: int = None,
        tags: List[GetServiceInstanceResponseBodyTags] = None,
        template_name: str = None,
        update_time: str = None,
        user_id: int = None,
    ):
        self.biz_status = biz_status
        self.create_time = create_time
        self.enable_instance_ops = enable_instance_ops
        self.enable_user_prometheus = enable_user_prometheus
        self.end_time = end_time
        self.is_operated = is_operated
        self.license_metadata = license_metadata
        self.name = name
        self.network_config = network_config
        self.operated_service_instance_id = operated_service_instance_id
        self.operation_end_time = operation_end_time
        self.operation_start_time = operation_start_time
        self.outputs = outputs
        self.parameters = parameters
        self.pay_type = pay_type
        self.predefined_parameter_name = predefined_parameter_name
        self.progress = progress
        self.rd_account_login_url = rd_account_login_url
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.resources = resources
        self.service = service
        self.service_instance_id = service_instance_id
        self.service_type = service_type
        self.source = source
        self.status = status
        self.status_detail = status_detail
        self.supplier_uid = supplier_uid
        self.tags = tags
        self.template_name = template_name
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.network_config:
            self.network_config.validate()
        if self.service:
            self.service.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')
        if m.get('LicenseMetadata') is not None:
            self.license_metadata = m.get('LicenseMetadata')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkConfig') is not None:
            temp_model = GetServiceInstanceResponseBodyNetworkConfig()
            self.network_config = temp_model.from_map(m['NetworkConfig'])
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
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
            temp_model = GetServiceInstanceResponseBodyService()
            self.service = temp_model.from_map(m['Service'])
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
            for k in m.get('Tags'):
                temp_model = GetServiceInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadCredentialsRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GetUploadCredentialsResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        expire_date: str = None,
        key: str = None,
        region_id: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.bucket_name = bucket_name
        self.expire_date = expire_date
        self.key = key
        self.region_id = region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.key is not None:
            result['Key'] = self.key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetUploadCredentialsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetUploadCredentialsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = GetUploadCredentialsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUploadCredentialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUploadCredentialsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUploadCredentialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactVersionsRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        max_result: int = None,
        next_token: str = None,
    ):
        self.artifact_id = artifact_id
        self.max_result = max_result
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListArtifactVersionsResponseBodyArtifacts(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property: str = None,
        artifact_type: str = None,
        artifact_version: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_delivery: Dict[str, str] = None,
        progress: str = None,
        result_file: str = None,
        security_audit_result: str = None,
        status: str = None,
        support_region_ids: str = None,
        version_name: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_property = artifact_property
        self.artifact_type = artifact_type
        self.artifact_version = artifact_version
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.image_delivery = image_delivery
        self.progress = progress
        self.result_file = result_file
        self.security_audit_result = security_audit_result
        self.status = status
        self.support_region_ids = support_region_ids
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_delivery is not None:
            result['ImageDelivery'] = self.image_delivery
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.result_file is not None:
            result['ResultFile'] = self.result_file
        if self.security_audit_result is not None:
            result['SecurityAuditResult'] = self.security_audit_result
        if self.status is not None:
            result['Status'] = self.status
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageDelivery') is not None:
            self.image_delivery = m.get('ImageDelivery')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ResultFile') is not None:
            self.result_file = m.get('ResultFile')
        if m.get('SecurityAuditResult') is not None:
            self.security_audit_result = m.get('SecurityAuditResult')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ListArtifactVersionsResponseBody(TeaModel):
    def __init__(
        self,
        artifacts: List[ListArtifactVersionsResponseBodyArtifacts] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.artifacts = artifacts
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.artifacts:
            for k in self.artifacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Artifacts'] = []
        if self.artifacts is not None:
            for k in self.artifacts:
                result['Artifacts'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.artifacts = []
        if m.get('Artifacts') is not None:
            for k in m.get('Artifacts'):
                temp_model = ListArtifactVersionsResponseBodyArtifacts()
                self.artifacts.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListArtifactVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListArtifactVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListArtifactVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactsRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        self.name = name
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListArtifactsRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListArtifactsRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListArtifactsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListArtifactsResponseBodyArtifacts(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_type: str = None,
        description: str = None,
        gmt_modified: str = None,
        max_version: str = None,
        name: str = None,
        status: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_type = artifact_type
        self.description = description
        self.gmt_modified = gmt_modified
        self.max_version = max_version
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListArtifactsResponseBody(TeaModel):
    def __init__(
        self,
        artifacts: List[ListArtifactsResponseBodyArtifacts] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.artifacts = artifacts
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.artifacts:
            for k in self.artifacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Artifacts'] = []
        if self.artifacts is not None:
            for k in self.artifacts:
                result['Artifacts'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.artifacts = []
        if m.get('Artifacts') is not None:
            for k in m.get('Artifacts'):
                temp_model = ListArtifactsResponseBodyArtifacts()
                self.artifacts.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListArtifactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListArtifactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListArtifactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListServiceInstancesRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListServiceInstancesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        show_deleted: bool = None,
        tag: List[ListServiceInstancesRequestTag] = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.show_deleted = show_deleted
        self.tag = tag

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.show_deleted is not None:
            result['ShowDeleted'] = self.show_deleted
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShowDeleted') is not None:
            self.show_deleted = m.get('ShowDeleted')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServiceInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.image = image
        self.locale = locale
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListServiceInstancesResponseBodyServiceInstancesService(TeaModel):
    def __init__(
        self,
        deploy_metadata: str = None,
        deploy_type: str = None,
        enable_private_vpc_connection: bool = None,
        publish_time: str = None,
        service_id: str = None,
        service_infos: List[ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos] = None,
        service_type: str = None,
        source_supplier_name: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        version: str = None,
        version_name: str = None,
    ):
        self.deploy_metadata = deploy_metadata
        self.deploy_type = deploy_type
        self.enable_private_vpc_connection = enable_private_vpc_connection
        self.publish_time = publish_time
        self.service_id = service_id
        self.service_infos = service_infos
        self.service_type = service_type
        self.source_supplier_name = source_supplier_name
        self.status = status
        self.supplier_name = supplier_name
        self.supplier_url = supplier_url
        self.version = version
        self.version_name = version_name

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.enable_private_vpc_connection is not None:
            result['EnablePrivateVpcConnection'] = self.enable_private_vpc_connection
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source_supplier_name is not None:
            result['SourceSupplierName'] = self.source_supplier_name
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
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('EnablePrivateVpcConnection') is not None:
            self.enable_private_vpc_connection = m.get('EnablePrivateVpcConnection')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SourceSupplierName') is not None:
            self.source_supplier_name = m.get('SourceSupplierName')
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


class ListServiceInstancesResponseBodyServiceInstancesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListServiceInstancesResponseBodyServiceInstances(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        enable_instance_ops: bool = None,
        end_time: str = None,
        is_operated: bool = None,
        name: str = None,
        operated_service_instance_id: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        parameters: str = None,
        pay_type: str = None,
        progress: int = None,
        resource_group_id: str = None,
        service: ListServiceInstancesResponseBodyServiceInstancesService = None,
        service_instance_id: str = None,
        service_type: str = None,
        source: str = None,
        status: str = None,
        status_detail: str = None,
        tags: List[ListServiceInstancesResponseBodyServiceInstancesTags] = None,
        template_name: str = None,
        update_time: str = None,
        user_id: int = None,
    ):
        self.create_time = create_time
        self.enable_instance_ops = enable_instance_ops
        self.end_time = end_time
        self.is_operated = is_operated
        self.name = name
        self.operated_service_instance_id = operated_service_instance_id
        self.operation_end_time = operation_end_time
        self.operation_start_time = operation_start_time
        self.parameters = parameters
        self.pay_type = pay_type
        self.progress = progress
        self.resource_group_id = resource_group_id
        self.service = service
        self.service_instance_id = service_instance_id
        self.service_type = service_type
        self.source = source
        self.status = status
        self.status_detail = status_detail
        self.tags = tags
        self.template_name = template_name
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.service:
            self.service.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_operated is not None:
            result['IsOperated'] = self.is_operated
        if self.name is not None:
            result['Name'] = self.name
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Service') is not None:
            temp_model = ListServiceInstancesResponseBodyServiceInstancesService()
            self.service = temp_model.from_map(m['Service'])
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListServiceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_instances: List[ListServiceInstancesResponseBodyServiceInstances] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.service_instances = service_instances
        self.total_count = total_count

    def validate(self):
        if self.service_instances:
            for k in self.service_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceInstances'] = []
        if self.service_instances is not None:
            for k in self.service_instances:
                result['ServiceInstances'].append(k.to_map() if k else None)
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
            for k in m.get('ServiceInstances'):
                temp_model = ListServiceInstancesResponseBodyServiceInstances()
                self.service_instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceUsagesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceUsagesRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListServiceUsagesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceUsagesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListServiceUsagesResponseBodyServiceUsagesUserInformation(TeaModel):
    def __init__(
        self,
        company: str = None,
        country: str = None,
        email_address: str = None,
        industry: str = None,
        name: str = None,
        source: str = None,
        telephone: str = None,
        title: str = None,
    ):
        self.company = company
        self.country = country
        self.email_address = email_address
        self.industry = industry
        self.name = name
        self.source = source
        self.telephone = telephone
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company is not None:
            result['Company'] = self.company
        if self.country is not None:
            result['Country'] = self.country
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Company') is not None:
            self.company = m.get('Company')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListServiceUsagesResponseBodyServiceUsages(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_time: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
        supplier_name: str = None,
        update_time: str = None,
        user_ali_uid: int = None,
        user_information: ListServiceUsagesResponseBodyServiceUsagesUserInformation = None,
    ):
        self.comments = comments
        self.create_time = create_time
        self.service_id = service_id
        self.service_name = service_name
        self.status = status
        self.supplier_name = supplier_name
        self.update_time = update_time
        self.user_ali_uid = user_ali_uid
        self.user_information = user_information

    def validate(self):
        if self.user_information:
            self.user_information.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid
        if self.user_information is not None:
            result['UserInformation'] = self.user_information.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')
        if m.get('UserInformation') is not None:
            temp_model = ListServiceUsagesResponseBodyServiceUsagesUserInformation()
            self.user_information = temp_model.from_map(m['UserInformation'])
        return self


class ListServiceUsagesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_usages: List[ListServiceUsagesResponseBodyServiceUsages] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.service_usages = service_usages
        self.total_count = total_count

    def validate(self):
        if self.service_usages:
            for k in self.service_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceUsages'] = []
        if self.service_usages is not None:
            for k in self.service_usages:
                result['ServiceUsages'].append(k.to_map() if k else None)
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
        self.service_usages = []
        if m.get('ServiceUsages') is not None:
            for k in m.get('ServiceUsages'):
                temp_model = ListServiceUsagesResponseBodyServiceUsages()
                self.service_usages.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceUsagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceUsagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceUsagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServicesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        all_versions: bool = None,
        filter: List[ListServicesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[ListServicesRequestTag] = None,
    ):
        self.all_versions = all_versions
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_versions is not None:
            result['AllVersions'] = self.all_versions
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllVersions') is not None:
            self.all_versions = m.get('AllVersions')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServicesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServicesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListServicesResponseBodyServicesServiceInfos(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.image = image
        self.locale = locale
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListServicesResponseBodyServicesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        approval_type: str = None,
        artifact_id: str = None,
        artifact_version: str = None,
        commodity_code: str = None,
        create_time: str = None,
        default_version: bool = None,
        deploy_type: str = None,
        latest_resell_source_service_version: str = None,
        publish_time: str = None,
        relation_type: str = None,
        resell_service_id: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_infos: List[ListServicesResponseBodyServicesServiceInfos] = None,
        service_type: str = None,
        share_type: str = None,
        source_image: str = None,
        source_service_id: str = None,
        source_service_version: str = None,
        source_supplier_name: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        tags: List[ListServicesResponseBodyServicesTags] = None,
        tenant_type: str = None,
        trial_type: str = None,
        update_time: str = None,
        version: str = None,
        version_name: str = None,
    ):
        self.approval_type = approval_type
        self.artifact_id = artifact_id
        self.artifact_version = artifact_version
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.default_version = default_version
        self.deploy_type = deploy_type
        self.latest_resell_source_service_version = latest_resell_source_service_version
        self.publish_time = publish_time
        self.relation_type = relation_type
        self.resell_service_id = resell_service_id
        self.resource_group_id = resource_group_id
        self.service_id = service_id
        self.service_infos = service_infos
        self.service_type = service_type
        self.share_type = share_type
        self.source_image = source_image
        self.source_service_id = source_service_id
        self.source_service_version = source_service_version
        self.source_supplier_name = source_supplier_name
        self.status = status
        self.supplier_name = supplier_name
        self.supplier_url = supplier_url
        self.tags = tags
        self.tenant_type = tenant_type
        self.trial_type = trial_type
        self.update_time = update_time
        self.version = version
        self.version_name = version_name

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.latest_resell_source_service_version is not None:
            result['LatestResellSourceServiceVersion'] = self.latest_resell_source_service_version
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type
        if self.resell_service_id is not None:
            result['ResellServiceId'] = self.resell_service_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('LatestResellSourceServiceVersion') is not None:
            self.latest_resell_source_service_version = m.get('LatestResellSourceServiceVersion')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')
        if m.get('ResellServiceId') is not None:
            self.resell_service_id = m.get('ResellServiceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServicesResponseBodyServicesServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
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
            for k in m.get('Tags'):
                temp_model = ListServicesResponseBodyServicesTags()
                self.tags.append(temp_model.from_map(k))
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
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        services: List[ListServicesResponseBodyServices] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.services = services
        self.total_count = total_count

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
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
            for k in m.get('Services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyServiceInstanceResourcesRequest(TeaModel):
    def __init__(
        self,
        resources: str = None,
        service_instance_id: str = None,
        service_instance_resources_action: str = None,
    ):
        self.resources = resources
        self.service_instance_id = service_instance_id
        self.service_instance_resources_action = service_instance_resources_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_instance_resources_action is not None:
            result['ServiceInstanceResourcesAction'] = self.service_instance_resources_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceInstanceResourcesAction') is not None:
            self.service_instance_resources_action = m.get('ServiceInstanceResourcesAction')
        return self


class ModifyServiceInstanceResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyServiceInstanceResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyServiceInstanceResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyServiceInstanceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseArtifactRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
    ):
        self.artifact_id = artifact_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        return self


class ReleaseArtifactResponseBody(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property: str = None,
        artifact_type: str = None,
        artifact_version: str = None,
        description: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        status: str = None,
        version_name: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_property = artifact_property
        self.artifact_type = artifact_type
        self.artifact_version = artifact_version
        self.description = description
        self.gmt_modified = gmt_modified
        self.request_id = request_id
        self.status = status
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ReleaseArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseArtifactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateArtifactRequestArtifactProperty(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_version: str = None,
        file_script_metadata: str = None,
        image_id: str = None,
        region_id: str = None,
        script_metadata: str = None,
        url: str = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_version = commodity_version
        self.file_script_metadata = file_script_metadata
        self.image_id = image_id
        self.region_id = region_id
        self.script_metadata = script_metadata
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_version is not None:
            result['CommodityVersion'] = self.commodity_version
        if self.file_script_metadata is not None:
            result['FileScriptMetadata'] = self.file_script_metadata
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.script_metadata is not None:
            result['ScriptMetadata'] = self.script_metadata
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityVersion') is not None:
            self.commodity_version = m.get('CommodityVersion')
        if m.get('FileScriptMetadata') is not None:
            self.file_script_metadata = m.get('FileScriptMetadata')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScriptMetadata') is not None:
            self.script_metadata = m.get('ScriptMetadata')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateArtifactRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property: UpdateArtifactRequestArtifactProperty = None,
        description: str = None,
        support_region_ids: List[str] = None,
        version_name: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_property = artifact_property
        self.description = description
        self.support_region_ids = support_region_ids
        self.version_name = version_name

    def validate(self):
        if self.artifact_property:
            self.artifact_property.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            temp_model = UpdateArtifactRequestArtifactProperty()
            self.artifact_property = temp_model.from_map(m['ArtifactProperty'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateArtifactShrinkRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property_shrink: str = None,
        description: str = None,
        support_region_ids: List[str] = None,
        version_name: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_property_shrink = artifact_property_shrink
        self.description = description
        self.support_region_ids = support_region_ids
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property_shrink is not None:
            result['ArtifactProperty'] = self.artifact_property_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property_shrink = m.get('ArtifactProperty')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateArtifactResponseBody(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property: str = None,
        artifact_type: str = None,
        artifact_version: str = None,
        description: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        status: str = None,
        support_region_ids: str = None,
        version_name: str = None,
    ):
        self.artifact_id = artifact_id
        self.artifact_property = artifact_property
        self.artifact_type = artifact_type
        self.artifact_version = artifact_version
        self.description = description
        self.gmt_modified = gmt_modified
        self.request_id = request_id
        self.status = status
        self.support_region_ids = support_region_ids
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateArtifactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceRequestServiceInfo(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.image = image
        self.locale = locale
        self.long_description_url = long_description_url
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        client_token: str = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        duration: int = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        policy_names: str = None,
        region_id: str = None,
        service_id: str = None,
        service_info: List[UpdateServiceRequestServiceInfo] = None,
        service_type: str = None,
        service_version: str = None,
        tenant_type: str = None,
        trial_duration: int = None,
        upgrade_metadata: str = None,
        version_name: str = None,
    ):
        self.alarm_metadata = alarm_metadata
        self.client_token = client_token
        self.deploy_metadata = deploy_metadata
        self.deploy_type = deploy_type
        self.duration = duration
        self.is_support_operated = is_support_operated
        self.license_metadata = license_metadata
        self.log_metadata = log_metadata
        self.operation_metadata = operation_metadata
        self.policy_names = policy_names
        self.region_id = region_id
        self.service_id = service_id
        self.service_info = service_info
        self.service_type = service_type
        self.service_version = service_version
        self.tenant_type = tenant_type
        self.trial_duration = trial_duration
        self.upgrade_metadata = upgrade_metadata
        self.version_name = version_name

    def validate(self):
        if self.service_info:
            for k in self.service_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_metadata is not None:
            result['AlarmMetadata'] = self.alarm_metadata
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
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
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k in self.service_info:
                result['ServiceInfo'].append(k.to_map() if k else None)
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
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
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k in m.get('ServiceInfo'):
                temp_model = UpdateServiceRequestServiceInfo()
                self.service_info.append(temp_model.from_map(k))
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')
        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')
        if m.get('UpgradeMetadata') is not None:
            self.upgrade_metadata = m.get('UpgradeMetadata')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


