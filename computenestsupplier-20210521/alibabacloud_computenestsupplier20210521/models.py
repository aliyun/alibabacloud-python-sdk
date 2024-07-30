# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AddServiceSharedAccountsRequestSharedAccounts(TeaModel):
    def __init__(
        self,
        permission: str = None,
        user_ali_uid: str = None,
    ):
        # The permissions on the service. Valid values:
        # 
        # *   Deployable: Permissions to deploy the service.
        # *   Accessible: Permissions to access the service.
        # 
        # This parameter is required.
        self.permission = permission
        # The Alibaba Cloud account ID of the user.
        # 
        # This parameter is required.
        self.user_ali_uid = user_ali_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')
        return self


class AddServiceSharedAccountsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_id: str = None,
        shared_accounts: List[AddServiceSharedAccountsRequestSharedAccounts] = None,
        type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The shared account and permissions of the service.
        # 
        # This parameter is required.
        self.shared_accounts = shared_accounts
        # The share type of the service. Default value: SharedAccount. Valid values:
        # 
        # *   SharedAccount: The service is shared by multiple accounts.
        # *   Reseller: The service is distributed.
        self.type = type

    def validate(self):
        if self.shared_accounts:
            for k in self.shared_accounts:
                if k:
                    k.validate()

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
        result['SharedAccounts'] = []
        if self.shared_accounts is not None:
            for k in self.shared_accounts:
                result['SharedAccounts'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.shared_accounts = []
        if m.get('SharedAccounts') is not None:
            for k in m.get('SharedAccounts'):
                temp_model = AddServiceSharedAccountsRequestSharedAccounts()
                self.shared_accounts.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddServiceSharedAccountsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class AddServiceSharedAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddServiceSharedAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddServiceSharedAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveServiceUsageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        comments: str = None,
        region_id: str = None,
        service_id: str = None,
        type: int = None,
        user_ali_uid: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # Approval comments.
        self.comments = comments
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # ServiceSharedAccountType，
        self.type = type
        # User ali uid.
        # 
        # This parameter is required.
        self.user_ali_uid = user_ali_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.type is not None:
            result['Type'] = self.type
        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')
        return self


class ApproveServiceUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ApproveServiceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApproveServiceUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ApproveServiceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinueDeployServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        parameters: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   true: performs a dry run for the request, but does not create a service instance.
        # *   false: performs a dry run for the request, and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # The configuration parameters of the service instance.
        self.parameters = parameters
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
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
        # The parameters that can be modified. The operation that is performed to modify the parameters does not cause a validation error.
        # 
        # >  This parameter is returned only if DryRun is set to true.
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        # The parameters that can be modified under specific conditions. The new values of the parameters determine whether the operation that is performed to modify the parameters causes a validation error.
        # 
        # >  This parameter is returned only if DryRun is set to true.
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        # The parameters that cannot be modified. The operation that is performed to modify the parameters causes a validation error.
        # 
        # >  This parameter is returned only if DryRun is set to true.
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
        # The dry run result.
        self.dry_run_result = dry_run_result
        # The request ID.
        self.request_id = request_id
        # The ID of the service instance.
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
        # The commodity code of the service in Alibaba Cloud Marketplace.
        # 
        # >  This parameter is available only if the deployment package is an image.
        self.commodity_code = commodity_code
        # The commodity version of the service in Alibaba Cloud Marketplace.
        # 
        # >  This parameter is available only if the deployment package is an image.
        self.commodity_version = commodity_version
        # The script metadata.
        self.file_script_metadata = file_script_metadata
        # The image ID.
        # 
        # >  This parameter is available only if the deployment package is an image.
        self.image_id = image_id
        # The region ID.
        # 
        # >  This parameter is available only if the deployment package is an image.
        self.region_id = region_id
        # The ID of the image repository.
        # 
        # >  This parameter is available only if the deployment package is a container image or of the Helm chart type.
        self.repo_id = repo_id
        # The name of the image repository.
        # 
        # >  This parameter is available only if the deployment package is a container image or of the Helm chart type.
        self.repo_name = repo_name
        # The script content.
        # 
        # >  This parameter is available only if the deployment package is a script.
        self.script_metadata = script_metadata
        # The version tag of the image repository.
        # 
        # >  This parameter is available only if the deployment package is a container image or of the Helm chart type.
        self.tag = tag
        # The object URL of the deployment package.
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


class CreateArtifactRequestTag(TeaModel):
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


class CreateArtifactRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property: CreateArtifactRequestArtifactProperty = None,
        artifact_type: str = None,
        description: str = None,
        name: str = None,
        resource_group_id: str = None,
        support_region_ids: List[str] = None,
        tag: List[CreateArtifactRequestTag] = None,
        version_name: str = None,
    ):
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The properties of the deployment object.
        self.artifact_property = artifact_property
        # The type of the deployment package. Valid values:
        # 
        # *   EcsImage: Elastic Compute Service (ECS) image.
        # *   AcrImage: container image.
        # *   File: Object Storage Service (OSS) object.
        # *   Script: script.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # The description of the deployment package.
        self.description = description
        # The name of the deployment package.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The supported regions.
        self.support_region_ids = support_region_ids
        # The custom tags.
        self.tag = tag
        # The version name of the deployment package.
        # 
        # This parameter is required.
        self.version_name = version_name

    def validate(self):
        if self.artifact_property:
            self.artifact_property.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateArtifactRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateArtifactShrinkRequestTag(TeaModel):
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


class CreateArtifactShrinkRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property_shrink: str = None,
        artifact_type: str = None,
        description: str = None,
        name: str = None,
        resource_group_id: str = None,
        support_region_ids: List[str] = None,
        tag: List[CreateArtifactShrinkRequestTag] = None,
        version_name: str = None,
    ):
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The properties of the deployment object.
        self.artifact_property_shrink = artifact_property_shrink
        # The type of the deployment package. Valid values:
        # 
        # *   EcsImage: Elastic Compute Service (ECS) image.
        # *   AcrImage: container image.
        # *   File: Object Storage Service (OSS) object.
        # *   Script: script.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # The description of the deployment package.
        self.description = description
        # The name of the deployment package.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The supported regions.
        self.support_region_ids = support_region_ids
        # The custom tags.
        self.tag = tag
        # The version name of the deployment package.
        # 
        # This parameter is required.
        self.version_name = version_name

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateArtifactShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
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
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The properties of the deployment object.
        self.artifact_property = artifact_property
        # The type of the deployment package.
        self.artifact_type = artifact_type
        # The version of the deployment package.
        self.artifact_version = artifact_version
        # The description of the deployment package.
        self.description = description
        # The time when the deployment package was modified.
        self.gmt_modified = gmt_modified
        # The latest version of the deployment package.
        self.max_version = max_version
        # The name of the deployment package.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The status of the deployment package. Valid values:
        self.status = status
        # The ID of the region that supports the deployment package.
        self.support_region_ids = support_region_ids
        # The name of the deployment package.
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


class CreateServiceRequestServiceInfoAgreements(TeaModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        # Protocol name.
        self.name = name
        # Protocol url.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateServiceRequestServiceInfo(TeaModel):
    def __init__(
        self,
        agreements: List[CreateServiceRequestServiceInfoAgreements] = None,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
    ):
        # Protocol document information about the service.
        self.agreements = agreements
        # The URL of the service icon.
        self.image = image
        # The language of the service. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        # 
        # This parameter is required.
        self.locale = locale
        # The URL of the detailed description of the service.
        self.long_description_url = long_description_url
        # The service name.
        # 
        # This parameter is required.
        self.name = name
        # The description of the service.
        self.short_description = short_description

    def validate(self):
        if self.agreements:
            for k in self.agreements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Agreements'] = []
        if self.agreements is not None:
            for k in self.agreements:
                result['Agreements'].append(k.to_map() if k else None)
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
        self.agreements = []
        if m.get('Agreements') is not None:
            for k in m.get('Agreements'):
                temp_model = CreateServiceRequestServiceInfoAgreements()
                self.agreements.append(temp_model.from_map(k))
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
        # The tag key.
        self.key = key
        # The tag value.
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
        build_parameters: str = None,
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
        resellable: bool = None,
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
        # The alert configurations of the service.
        # 
        # >  This parameter takes effect only when you specify an alert policy for **PolicyNames**.
        self.alarm_metadata = alarm_metadata
        # The approval type of the service usage application. Valid values:
        # 
        # *   Manual: The application is manually approved.
        # *   AutoPass: The application is automatically approved.
        self.approval_type = approval_type
        # The parameters for building the service
        self.build_parameters = build_parameters
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # The storage configurations of the service. The format in which the deployment information of a service is stored varies based on the deployment type of the service. In this case, the deployment information is stored in the JSON string format.
        self.deploy_metadata = deploy_metadata
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        # *   ack: The service is deployed by using Container Service for Kubernetes (ACK).
        # *   spi: The service is deployed by calling a service provider interface (SPI).
        # *   operation: The service is deployed by using a hosted O\\&M service.
        # 
        # This parameter is required.
        self.deploy_type = deploy_type
        # The duration for which hosted O\\&M is implemented. Unit: seconds.
        self.duration = duration
        # Specifies whether to enable the hosted O\\&M feature for the service. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is required if you set **ServiceType** to **private**.
        self.is_support_operated = is_support_operated
        # The license metadata.
        self.license_metadata = license_metadata
        # The logging configurations.
        self.log_metadata = log_metadata
        # The hosted O\\&M configurations.
        self.operation_metadata = operation_metadata
        # The policy name. The name can be up to 128 characters in length. Separate multiple names with commas (,). Only hosted O\\&M policies are supported.
        self.policy_names = policy_names
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Whether resell is supported.
        self.resellable = resellable
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The service ID.
        self.service_id = service_id
        # The service details.
        self.service_info = service_info
        # The service type. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        # *   poc: The service is a trial service.
        self.service_type = service_type
        # The permission type of the deployment URL. Valid values:
        # 
        # *   Public: All users can go to the URL to create a service instance or a trial service instance.
        # *   Restricted: Only users in the whitelist can go to the URL to create a service instance or a trial service instance.
        # *   OnlyFormalRestricted: Only users in the whitelist can go to the URL to create a service instance.
        # *   OnlyTrailRestricted: Only users in the whitelist can go to the URL to create a trial service instance.
        # *   Hidden: Users not in the whitelist cannot see the service details page when they go to the URL and cannot request deployment permissions.
        self.share_type = share_type
        # The source service ID for resell。
        self.source_service_id = source_service_id
        # The source service version for resell。
        self.source_service_version = source_service_version
        # The custom tags.
        self.tag = tag
        # The type of the tenant. Valid values:
        # 
        # *   SingleTenant
        # *   MultiTenant
        self.tenant_type = tenant_type
        # The trial duration. Unit: day. The maximum trial duration cannot exceed 30 days.
        self.trial_duration = trial_duration
        # The metadata about the upgrade.
        self.upgrade_metadata = upgrade_metadata
        # The version name.
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
        if self.build_parameters is not None:
            result['BuildParameters'] = self.build_parameters
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
        if self.resellable is not None:
            result['Resellable'] = self.resellable
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
        if m.get('BuildParameters') is not None:
            self.build_parameters = m.get('BuildParameters')
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
        if m.get('Resellable') is not None:
            self.resellable = m.get('Resellable')
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
        # The request ID.
        self.request_id = request_id
        # The service ID.
        self.service_id = service_id
        # The status of the service.
        self.status = status
        # The service version.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        end_time: str = None,
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   true: performs a dry run for the request, but does not create a service instance.
        # *   false: performs a dry run for the request, and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # The time when the service instance was released.
        # 
        # >  This parameter is available only for the service instances that are managed by service providers.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.end_time = end_time
        # The name of the service instance. The value must meet the following requirements:
        # 
        # *   The name cannot exceed 64 characters in length.
        # *   It can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or a letter.
        self.name = name
        # The parameters that are specified for service instance deployment.
        # 
        # >  If you want to specify the region in which the service instance is deployed, you must specify the information in Parameters.
        self.parameters = parameters
        # The region ID. Valid values:
        # 
        # *   cn-hangzhou: China (Hangzhou)
        # *   ap-southeast-1: Singapore
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        self.service_version = service_version
        # The name of the package specification.
        self.specification_name = specification_name
        # The custom tags.
        self.tag = tag
        # The template name. You must specify a template name if the service supports multiple templates.
        self.template_name = template_name
        # The user ID.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
        # The tag key.
        self.key = key
        # The tag value.
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
        end_time: str = None,
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   true: performs a dry run for the request, but does not create a service instance.
        # *   false: performs a dry run for the request, and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # The time when the service instance was released.
        # 
        # >  This parameter is available only for the service instances that are managed by service providers.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.end_time = end_time
        # The name of the service instance. The value must meet the following requirements:
        # 
        # *   The name cannot exceed 64 characters in length.
        # *   It can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or a letter.
        self.name = name
        # The parameters that are specified for service instance deployment.
        # 
        # >  If you want to specify the region in which the service instance is deployed, you must specify the information in Parameters.
        self.parameters_shrink = parameters_shrink
        # The region ID. Valid values:
        # 
        # *   cn-hangzhou: China (Hangzhou)
        # *   ap-southeast-1: Singapore
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        self.service_version = service_version
        # The name of the package specification.
        self.specification_name = specification_name
        # The custom tags.
        self.tag = tag
        # The template name. You must specify a template name if the service supports multiple templates.
        self.template_name = template_name
        # The user ID.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
        # The request ID.
        self.request_id = request_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The status of the service instance. Valid values:
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


class CreateServiceUsageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CreateServiceUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class CreateServiceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateServiceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteArtifactRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_version: str = None,
    ):
        # The ID of the artifact.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # The version of the artifact.
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
        # The request ID.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        # 
        # This parameter is required.
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
        # The request ID.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the service instances.
        # 
        # This parameter is required.
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
        # The request ID.
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


class DeployServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
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


class DeployServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeployServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeployServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_name: str = None,
        artifact_version: str = None,
    ):
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The name of the deployment package.
        self.artifact_name = artifact_name
        # The version of the deployment package.
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


class GetArtifactResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the deployment package.
        self.key = key
        # The tag value of the deployment package.
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
        resource_group_id: str = None,
        status: str = None,
        support_region_ids: str = None,
        tags: List[GetArtifactResponseBodyTags] = None,
        version_name: str = None,
    ):
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The properties of the deployment package.
        self.artifact_property = artifact_property
        # The type of the deployment package.
        self.artifact_type = artifact_type
        # The version of the deployment package.
        self.artifact_version = artifact_version
        # The description of the deployment package.
        self.description = description
        # The time when the deployment package was modified.
        self.gmt_modified = gmt_modified
        # The latest version of the deployment package.
        self.max_version = max_version
        # The name of the deployment package.
        self.name = name
        # The distribution progress of the deployment package.
        self.progress = progress
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the deployment package. Valid values:
        self.status = status
        # The ID of the region that supports the deployment package.
        self.support_region_ids = support_region_ids
        # The tags of the deployment package.
        self.tags = tags
        # The version name of the deployment package.
        self.version_name = version_name

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetArtifactResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
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
        # The type of the deployment package. Valid values:
        # 
        # *   File: Object Storage Service (OSS) object.
        # *   AcrImage: container image.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # The region ID.
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
        # The path.
        self.path = path
        # The region ID.
        self.region_id = region_id
        # The repository name.
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
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The AccessKey secret.
        self.access_key_secret = access_key_secret
        # The password.
        self.password = password
        # The Security Token Service (STS) token.
        self.security_token = security_token
        # The username.
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
        # The information about the resources that can be uploaded.
        self.available_resources = available_resources
        # The credentials.
        self.credentials = credentials
        # The time when the credentials expired.
        self.expire_date = expire_date
        # The request ID.
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
        # Specifies whether to filter information based on Alibaba Cloud account IDs.
        self.filter_ali_uid = filter_ali_uid
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        self.service_version = service_version
        # The share type of the service. Default value: SharedAccount. Valid values:
        # 
        # *   SharedAccount: The service is shared by multiple accounts.
        # *   Resell: The service is distributed.
        self.shared_account_type = shared_account_type
        # The information that you want to query.
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


class GetServiceResponseBodyCommodityCssMetadataComponentsMappings(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyCommodityCssMetadataMeteringEntityExtraInfos(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyCommodityCssMetadataMeteringEntityMappings(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyCommodityCssMetadata(TeaModel):
    def __init__(
        self,
        components_mappings: List[GetServiceResponseBodyCommodityCssMetadataComponentsMappings] = None,
        metering_entity_extra_infos: List[GetServiceResponseBodyCommodityCssMetadataMeteringEntityExtraInfos] = None,
        metering_entity_mappings: List[GetServiceResponseBodyCommodityCssMetadataMeteringEntityMappings] = None,
    ):
        # The mapping information about the billing items.
        self.components_mappings = components_mappings
        # Metering item configuration information.
        self.metering_entity_extra_infos = metering_entity_extra_infos
        # The binding relationship between package and measurement dimension.
        self.metering_entity_mappings = metering_entity_mappings

    def validate(self):
        if self.components_mappings:
            for k in self.components_mappings:
                if k:
                    k.validate()
        if self.metering_entity_extra_infos:
            for k in self.metering_entity_extra_infos:
                if k:
                    k.validate()
        if self.metering_entity_mappings:
            for k in self.metering_entity_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentsMappings'] = []
        if self.components_mappings is not None:
            for k in self.components_mappings:
                result['ComponentsMappings'].append(k.to_map() if k else None)
        result['MeteringEntityExtraInfos'] = []
        if self.metering_entity_extra_infos is not None:
            for k in self.metering_entity_extra_infos:
                result['MeteringEntityExtraInfos'].append(k.to_map() if k else None)
        result['MeteringEntityMappings'] = []
        if self.metering_entity_mappings is not None:
            for k in self.metering_entity_mappings:
                result['MeteringEntityMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components_mappings = []
        if m.get('ComponentsMappings') is not None:
            for k in m.get('ComponentsMappings'):
                temp_model = GetServiceResponseBodyCommodityCssMetadataComponentsMappings()
                self.components_mappings.append(temp_model.from_map(k))
        self.metering_entity_extra_infos = []
        if m.get('MeteringEntityExtraInfos') is not None:
            for k in m.get('MeteringEntityExtraInfos'):
                temp_model = GetServiceResponseBodyCommodityCssMetadataMeteringEntityExtraInfos()
                self.metering_entity_extra_infos.append(temp_model.from_map(k))
        self.metering_entity_mappings = []
        if m.get('MeteringEntityMappings') is not None:
            for k in m.get('MeteringEntityMappings'):
                temp_model = GetServiceResponseBodyCommodityCssMetadataMeteringEntityMappings()
                self.metering_entity_mappings.append(temp_model.from_map(k))
        return self


class GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityExtraInfos(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityMappings(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyCommodityMarketplaceMetadata(TeaModel):
    def __init__(
        self,
        metering_entity_extra_infos: List[GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityExtraInfos] = None,
        metering_entity_mappings: List[GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityMappings] = None,
        specification_mappings: List[GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings] = None,
    ):
        # The configurations of the billable items.
        self.metering_entity_extra_infos = metering_entity_extra_infos
        # The billable items that are associated with the package.
        self.metering_entity_mappings = metering_entity_mappings
        # The mappings between the service specifications and the template or package.
        self.specification_mappings = specification_mappings

    def validate(self):
        if self.metering_entity_extra_infos:
            for k in self.metering_entity_extra_infos:
                if k:
                    k.validate()
        if self.metering_entity_mappings:
            for k in self.metering_entity_mappings:
                if k:
                    k.validate()
        if self.specification_mappings:
            for k in self.specification_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MeteringEntityExtraInfos'] = []
        if self.metering_entity_extra_infos is not None:
            for k in self.metering_entity_extra_infos:
                result['MeteringEntityExtraInfos'].append(k.to_map() if k else None)
        result['MeteringEntityMappings'] = []
        if self.metering_entity_mappings is not None:
            for k in self.metering_entity_mappings:
                result['MeteringEntityMappings'].append(k.to_map() if k else None)
        result['SpecificationMappings'] = []
        if self.specification_mappings is not None:
            for k in self.specification_mappings:
                result['SpecificationMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metering_entity_extra_infos = []
        if m.get('MeteringEntityExtraInfos') is not None:
            for k in m.get('MeteringEntityExtraInfos'):
                temp_model = GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityExtraInfos()
                self.metering_entity_extra_infos.append(temp_model.from_map(k))
        self.metering_entity_mappings = []
        if m.get('MeteringEntityMappings') is not None:
            for k in m.get('MeteringEntityMappings'):
                temp_model = GetServiceResponseBodyCommodityMarketplaceMetadataMeteringEntityMappings()
                self.metering_entity_mappings.append(temp_model.from_map(k))
        self.specification_mappings = []
        if m.get('SpecificationMappings') is not None:
            for k in m.get('SpecificationMappings'):
                temp_model = GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings()
                self.specification_mappings.append(temp_model.from_map(k))
        return self


class GetServiceResponseBodyCommodityMeteringEntities(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyCommoditySpecifications(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyCommodity(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        components: List[str] = None,
        css_metadata: GetServiceResponseBodyCommodityCssMetadata = None,
        marketplace_metadata: GetServiceResponseBodyCommodityMarketplaceMetadata = None,
        metering_entities: List[GetServiceResponseBodyCommodityMeteringEntities] = None,
        saas_boost_metadata: str = None,
        specifications: List[GetServiceResponseBodyCommoditySpecifications] = None,
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
            for k in self.metering_entities:
                if k:
                    k.validate()
        if self.specifications:
            for k in self.specifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.metering_entities:
                result['MeteringEntities'].append(k.to_map() if k else None)
        if self.saas_boost_metadata is not None:
            result['SaasBoostMetadata'] = self.saas_boost_metadata
        result['Specifications'] = []
        if self.specifications is not None:
            for k in self.specifications:
                result['Specifications'].append(k.to_map() if k else None)
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
            temp_model = GetServiceResponseBodyCommodityCssMetadata()
            self.css_metadata = temp_model.from_map(m['CssMetadata'])
        if m.get('MarketplaceMetadata') is not None:
            temp_model = GetServiceResponseBodyCommodityMarketplaceMetadata()
            self.marketplace_metadata = temp_model.from_map(m['MarketplaceMetadata'])
        self.metering_entities = []
        if m.get('MeteringEntities') is not None:
            for k in m.get('MeteringEntities'):
                temp_model = GetServiceResponseBodyCommodityMeteringEntities()
                self.metering_entities.append(temp_model.from_map(k))
        if m.get('SaasBoostMetadata') is not None:
            self.saas_boost_metadata = m.get('SaasBoostMetadata')
        self.specifications = []
        if m.get('Specifications') is not None:
            for k in m.get('Specifications'):
                temp_model = GetServiceResponseBodyCommoditySpecifications()
                self.specifications.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetServiceResponseBodyServiceInfosAgreements(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetServiceResponseBodyServiceInfos(TeaModel):
    def __init__(
        self,
        agreements: List[GetServiceResponseBodyServiceInfosAgreements] = None,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
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

    def validate(self):
        if self.agreements:
            for k in self.agreements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Agreements'] = []
        if self.agreements is not None:
            for k in self.agreements:
                result['Agreements'].append(k.to_map() if k else None)
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
        self.agreements = []
        if m.get('Agreements') is not None:
            for k in m.get('Agreements'):
                temp_model = GetServiceResponseBodyServiceInfosAgreements()
                self.agreements.append(temp_model.from_map(k))
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
        # The tag key.
        self.key = key
        # The tag value.
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
        build_info: str = None,
        categories: str = None,
        commodity: GetServiceResponseBodyCommodity = None,
        commodity_code: str = None,
        create_time: str = None,
        cross_region_connection_status: str = None,
        default_license_days: int = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        duration: int = None,
        entity_source: Dict[str, str] = None,
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
        resellable: bool = None,
        resource_group_id: str = None,
        service_audit_document_url: str = None,
        service_discoverable: str = None,
        service_doc_url: str = None,
        service_id: str = None,
        service_infos: List[GetServiceResponseBodyServiceInfos] = None,
        service_product_url: str = None,
        service_type: str = None,
        share_type: str = None,
        share_type_status: str = None,
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
        # The category of the service.
        self.categories = categories
        # The commodity details.
        self.commodity = commodity
        # The commodity code of the service in Alibaba Cloud Marketplace.
        self.commodity_code = commodity_code
        # The time when the service was created.
        self.create_time = create_time
        # The binding configurations of the commodity module.
        self.cross_region_connection_status = cross_region_connection_status
        # The validity period of the default license. Unit: day. Valid values: 1 to 1000.
        self.default_license_days = default_license_days
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
        # The billing method of the service. Valid values:
        # 
        # *   Permanent: Once you purchase the service, you can use it permanently.
        # *   Subscription: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a subscription basis.
        # *   PayAsYouGo: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a pay-as-you-go basis.
        # *   CustomFixTime: You are charged for the service based on a custom duration fixed by the service provider.
        self.pay_type = pay_type
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
        # The URL of the service audit file.
        self.service_audit_document_url = service_audit_document_url
        # Indicates whether the service is visible. Valid values:
        # 
        # *   INVISIBLE
        # *   DISCOVERABLE
        self.service_discoverable = service_discoverable
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
        if self.cross_region_connection_status is not None:
            result['CrossRegionConnectionStatus'] = self.cross_region_connection_status
        if self.default_license_days is not None:
            result['DefaultLicenseDays'] = self.default_license_days
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
        if self.resellable is not None:
            result['Resellable'] = self.resellable
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_audit_document_url is not None:
            result['ServiceAuditDocumentUrl'] = self.service_audit_document_url
        if self.service_discoverable is not None:
            result['ServiceDiscoverable'] = self.service_discoverable
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
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Commodity') is not None:
            temp_model = GetServiceResponseBodyCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossRegionConnectionStatus') is not None:
            self.cross_region_connection_status = m.get('CrossRegionConnectionStatus')
        if m.get('DefaultLicenseDays') is not None:
            self.default_license_days = m.get('DefaultLicenseDays')
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
        if m.get('Resellable') is not None:
            self.resellable = m.get('Resellable')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceAuditDocumentUrl') is not None:
            self.service_audit_document_url = m.get('ServiceAuditDocumentUrl')
        if m.get('ServiceDiscoverable') is not None:
            self.service_discoverable = m.get('ServiceDiscoverable')
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
        if m.get('ShareTypeStatus') is not None:
            self.share_type_status = m.get('ShareTypeStatus')
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
        if m.get('VirtualInternetService') is not None:
            self.virtual_internet_service = m.get('VirtualInternetService')
        if m.get('VirtualInternetServiceId') is not None:
            self.virtual_internet_service_id = m.get('VirtualInternetServiceId')
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


class GetServiceEstimateCostRequestCommodity(TeaModel):
    def __init__(
        self,
        pay_period: int = None,
        pay_period_unit: str = None,
    ):
        # The subscription duration.
        self.pay_period = pay_period
        # The unit of the subscription duration. Valid values:
        # 
        # *   Year
        # *   Month
        # *   Day
        self.pay_period_unit = pay_period_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_period is not None:
            result['PayPeriod'] = self.pay_period
        if self.pay_period_unit is not None:
            result['PayPeriodUnit'] = self.pay_period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayPeriod') is not None:
            self.pay_period = m.get('PayPeriod')
        if m.get('PayPeriodUnit') is not None:
            self.pay_period_unit = m.get('PayPeriodUnit')
        return self


class GetServiceEstimateCostRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: GetServiceEstimateCostRequestCommodity = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        template_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The subscription duration information about the purchase order of Alibaba Cloud Marketplace.
        self.commodity = commodity
        # The parameters that are specified to deploy the service instance.
        self.parameters = parameters
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # The package name.
        self.specification_name = specification_name
        # The template name.
        self.template_name = template_name

    def validate(self):
        if self.commodity:
            self.commodity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
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
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            temp_model = GetServiceEstimateCostRequestCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
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
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceEstimateCostShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity_shrink: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        template_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The subscription duration information about the purchase order of Alibaba Cloud Marketplace.
        self.commodity_shrink = commodity_shrink
        # The parameters that are specified to deploy the service instance.
        self.parameters_shrink = parameters_shrink
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # The package name.
        self.specification_name = specification_name
        # The template name.
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
        if self.commodity_shrink is not None:
            result['Commodity'] = self.commodity_shrink
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
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            self.commodity_shrink = m.get('Commodity')
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
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceEstimateCostResponseBody(TeaModel):
    def __init__(
        self,
        commodity: Dict[str, Any] = None,
        request_id: str = None,
        resources: Dict[str, Any] = None,
    ):
        # The subscription duration information about the purchase order of Alibaba Cloud Marketplace.
        self.commodity = commodity
        # The request ID.
        self.request_id = request_id
        # The list of resources.
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity is not None:
            result['Commodity'] = self.commodity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')
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
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
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
        # The ID of the endpoint for the reverse private connection.
        self.endpoint_id = endpoint_id
        # The ID of the endpoint service for the reverse private connection.
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
        # The service versions that can be updated.
        self.upgradable_service_versions = upgradable_service_versions
        # The service version.
        self.version = version
        # The custom version name defined by the service provider.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        enable_user_prometheus: bool = None,
        end_time: str = None,
        grafana_dash_board_url: str = None,
        is_operated: bool = None,
        license_metadata: str = None,
        name: str = None,
        network_config: GetServiceInstanceResponseBodyNetworkConfig = None,
        operated_service_instance_id: str = None,
        operation_end_time: str = None,
        operation_extra_info: str = None,
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
        if self.grafana_dash_board_url is not None:
            result['GrafanaDashBoardUrl'] = self.grafana_dash_board_url
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
        if m.get('GrafanaDashBoardUrl') is not None:
            self.grafana_dash_board_url = m.get('GrafanaDashBoardUrl')
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


class GetServiceTemplateParameterConstraintsRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The parameter name.
        self.parameter_key = parameter_key
        # The parameter value.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetServiceTemplateParameterConstraintsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        deploy_region_id: str = None,
        enable_private_vpc_connection: bool = None,
        parameters: List[GetServiceTemplateParameterConstraintsRequestParameters] = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        template_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # The ID of the region in which the service instance is deployed.
        # 
        # This parameter is required.
        self.deploy_region_id = deploy_region_id
        # Specifies whether to enable the private connection feature. Valid values:
        # 
        # *   true
        # *   false
        self.enable_private_vpc_connection = enable_private_vpc_connection
        # The parameters in the template.
        self.parameters = parameters
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # The template name.
        # 
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.enable_private_vpc_connection is not None:
            result['EnablePrivateVpcConnection'] = self.enable_private_vpc_connection
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
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
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('EnablePrivateVpcConnection') is not None:
            self.enable_private_vpc_connection = m.get('EnablePrivateVpcConnection')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetServiceTemplateParameterConstraintsRequestParameters()
                self.parameters.append(temp_model.from_map(k))
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


class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints(TeaModel):
    def __init__(
        self,
        allowed_values: List[str] = None,
        property_name: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The valid values of the parameter.
        self.allowed_values = allowed_values
        # The property name.
        self.property_name = property_name
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints(TeaModel):
    def __init__(
        self,
        allowed_values: List[str] = None,
        association_parameter_names: List[str] = None,
        behavior: str = None,
        behavior_reason: str = None,
        original_constraints: List[GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints] = None,
        parameter_key: str = None,
        type: str = None,
    ):
        # The valid values of the parameter.
        self.allowed_values = allowed_values
        # The names of the associated parameters.
        self.association_parameter_names = association_parameter_names
        # The behavior of the parameter. Valid values:
        # 
        # *   NoLimit: The value of this parameter is not limited.
        # *   NotSupport: The value of this parameter cannot be queried.
        # *   QueryError: The query failed.
        # 
        # >  If AllowedValues is not returned, Behavior and BehaviorReason are returned.
        self.behavior = behavior
        # The reason why the behavior of the parameter is returned.
        self.behavior_reason = behavior_reason
        # The original constraint information.
        self.original_constraints = original_constraints
        # The name of the parameter.
        self.parameter_key = parameter_key
        # The type of the parameter.
        self.type = type

    def validate(self):
        if self.original_constraints:
            for k in self.original_constraints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        if self.association_parameter_names is not None:
            result['AssociationParameterNames'] = self.association_parameter_names
        if self.behavior is not None:
            result['Behavior'] = self.behavior
        if self.behavior_reason is not None:
            result['BehaviorReason'] = self.behavior_reason
        result['OriginalConstraints'] = []
        if self.original_constraints is not None:
            for k in self.original_constraints:
                result['OriginalConstraints'].append(k.to_map() if k else None)
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        if m.get('AssociationParameterNames') is not None:
            self.association_parameter_names = m.get('AssociationParameterNames')
        if m.get('Behavior') is not None:
            self.behavior = m.get('Behavior')
        if m.get('BehaviorReason') is not None:
            self.behavior_reason = m.get('BehaviorReason')
        self.original_constraints = []
        if m.get('OriginalConstraints') is not None:
            for k in m.get('OriginalConstraints'):
                temp_model = GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints()
                self.original_constraints.append(temp_model.from_map(k))
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetServiceTemplateParameterConstraintsResponseBody(TeaModel):
    def __init__(
        self,
        family_constraints: List[str] = None,
        parameter_constraints: List[GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints] = None,
        request_id: str = None,
    ):
        # The constraint families.
        self.family_constraints = family_constraints
        # The parameters in the template.
        self.parameter_constraints = parameter_constraints
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parameter_constraints:
            for k in self.parameter_constraints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.family_constraints is not None:
            result['FamilyConstraints'] = self.family_constraints
        result['ParameterConstraints'] = []
        if self.parameter_constraints is not None:
            for k in self.parameter_constraints:
                result['ParameterConstraints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FamilyConstraints') is not None:
            self.family_constraints = m.get('FamilyConstraints')
        self.parameter_constraints = []
        if m.get('ParameterConstraints') is not None:
            for k in m.get('ParameterConstraints'):
                temp_model = GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints()
                self.parameter_constraints.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetServiceTemplateParameterConstraintsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceTemplateParameterConstraintsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetServiceTemplateParameterConstraintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadCredentialsRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        visibility: str = None,
    ):
        # The file name to upload.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Specifies whether the file is publicly accessible. Valid values: **public** or **private**. The default value is **private**.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
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
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The AccessKey secret.
        self.access_key_secret = access_key_secret
        # The bucket name.
        self.bucket_name = bucket_name
        # The time when the AccessKey pair expires.
        self.expire_date = expire_date
        # The name of the key.
        self.key = key
        # The region ID.
        self.region_id = region_id
        # The security token.
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
        # The response code.
        self.code = code
        # The response parameters.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. A value of true indicates the request was successful. A value of false indicates the request failed.
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


class ListAcrImageRepositoriesRequest(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        max_results: int = None,
        next_token: str = None,
        repo_name: str = None,
    ):
        # The type of the artifact. Default value: AcrImage. Valid values:
        # 
        # *   HelmChart: Helm chart image.
        # *   AcrImage: container image.
        self.artifact_type = artifact_type
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The name of the image repository.
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class ListAcrImageRepositoriesResponseBodyRepositories(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modified_time: str = None,
        repo_id: str = None,
        repo_name: str = None,
    ):
        # The time when the image was created.
        self.create_time = create_time
        # The time when the image was modified.
        self.modified_time = modified_time
        # The image repo ID.
        self.repo_id = repo_id
        # The image repo name.
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class ListAcrImageRepositoriesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        repositories: List[ListAcrImageRepositoriesResponseBodyRepositories] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The images.
        self.repositories = repositories
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.repositories:
            for k in self.repositories:
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
        result['Repositories'] = []
        if self.repositories is not None:
            for k in self.repositories:
                result['Repositories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.repositories = []
        if m.get('Repositories') is not None:
            for k in m.get('Repositories'):
                temp_model = ListAcrImageRepositoriesResponseBodyRepositories()
                self.repositories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAcrImageRepositoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAcrImageRepositoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAcrImageRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAcrImageTagsRequest(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        max_results: int = None,
        next_token: str = None,
        repo_id: str = None,
    ):
        # The type of the deployment package. Default value: AcrImage. Valid values:
        # 
        # *   HelmChart: Helm chart image.
        # *   AcrImage: container image.
        self.artifact_type = artifact_type
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The image ID.
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListAcrImageTagsResponseBodyImages(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        image_size: str = None,
        modified_time: str = None,
        tag: str = None,
    ):
        # The time when the image was created.
        self.create_time = create_time
        # The image size. Unit: bytes.
        self.image_size = image_size
        # The time when the image was modified.
        self.modified_time = modified_time
        # The image version.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListAcrImageTagsResponseBody(TeaModel):
    def __init__(
        self,
        images: List[ListAcrImageTagsResponseBodyImages] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of images.
        self.images = images
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
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
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListAcrImageTagsResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAcrImageTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAcrImageTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAcrImageTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactVersionsRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the deployment package.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
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
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The properties of the deployment package.
        self.artifact_property = artifact_property
        # The type of the deployment package.
        self.artifact_type = artifact_type
        # The version of the deployment package.
        self.artifact_version = artifact_version
        # The time when the certificate was created.
        self.gmt_create = gmt_create
        # The time when the deployment package was modified.
        self.gmt_modified = gmt_modified
        # The distribution result of the image.
        self.image_delivery = image_delivery
        # The distribution progress of the deployment package.
        self.progress = progress
        # The result file of the security scan.
        self.result_file = result_file
        # The result of the security scan. Valid values:
        # 
        # *   Normal: No risks exist on the deployment package.
        # *   AtRisk: Risks exist on the deployment package.
        # *   Processing: The deployment package is being scanned.
        self.security_audit_result = security_audit_result
        # The status of the deployment package. Valid values:
        # 
        # *   Created: The deployment package is created.
        # *   Scanning: The deployment package is being scanned.
        # *   ScanFailed: The deployment package failed to be scanned.
        # *   Delivering: The deployment package is being distributed.
        # *   Available: The deployment package is available.
        # *   Deleted: The deployment package is deleted.
        self.status = status
        # The ID of the region that supports the deployment package.
        self.support_region_ids = support_region_ids
        # The version name of the deployment package.
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
        # The version information about the deployment package.
        self.artifacts = artifacts
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        # The parameter name of the filter. You can specify one or more filters. Valid values:
        # 
        # *   *Name*: The name of the deployment package. Fuzzy match is used.
        # *   ArtifactId: The ID of the deployment package.
        # *   ArtifactType: The type of the deployment package.
        self.name = name
        # The parameter values of the filter.
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


class ListArtifactsRequestTag(TeaModel):
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


class ListArtifactsRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListArtifactsRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        tag: List[ListArtifactsRequestTag] = None,
    ):
        # The filter.
        self.filter = filter
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
                temp_model = ListArtifactsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListArtifactsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListArtifactsResponseBodyArtifactsTags(TeaModel):
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


class ListArtifactsResponseBodyArtifacts(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_type: str = None,
        description: str = None,
        gmt_modified: str = None,
        max_version: str = None,
        name: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[ListArtifactsResponseBodyArtifactsTags] = None,
    ):
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The type of the deployment package.
        self.artifact_type = artifact_type
        # The description of the deployment package.
        self.description = description
        # The time when the deployment package was modified.
        self.gmt_modified = gmt_modified
        # The latest version of the deployment package.
        self.max_version = max_version
        # The name of the deployment package.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the deployment package. Valid values:
        # 
        # *   Created: The deployment package is created.
        # *   Scanning: The deployment package is being scanned.
        # *   ScanFailed: The deployment package failed to be scanned.
        # *   Delivering: The deployment package is being distributed.
        # *   Available: The deployment package is available.
        # *   Deleted: The deployment package is deleted.
        self.status = status
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListArtifactsResponseBodyArtifactsTags()
                self.tags.append(temp_model.from_map(k))
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
        # The information about deployment packages.
        self.artifacts = artifacts
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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


class ListServiceCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        request_id: str = None,
    ):
        # The category list of the service.
        self.categories = categories
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListServiceCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceCategoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListServiceCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The parameter name of the filter. You can specify one or more filters. Valid values:
        # 
        # *   Name: The service name. If you want to perform a fuzzy match, specify the service name in the *xxx* format. For example, if the service name is My Service, you can set the filter value to *My* or *Service*.
        # *   ServiceInstanceId: The ID of the service instance.
        # *   ServiceId: The service ID.
        # *   UserId: The user ID.
        # *   Version: The service version.
        # *   Status: The status of the service instance.
        # *   DeployType: The deployment type of the service.
        # *   ServiceType: The service type.
        # *   OperationStartTimeBefore: The time before the hosted O\\&M starts.
        # *   OperationStartTimeAfter: The time after the hosted O\\&M starts.
        # *   OperationEndTimeBefore: The time before the hosted O\\&M ends.
        # *   OperationEndTimeAfter: The time after the hosted O\\&M ends.
        # *   OperatedServiceInstanceId: The ID of the hosted O\\&M instance that belongs to a private service.
        # *   OperationServiceInstanceId: The ID of the hosted O\\&M service instance that belongs to a hosted O\\&M service.
        # *   EnableInstanceOps: Whether the hosted O\\&M feature is enabled for service instances.
        self.name = name
        # The parameter values of the filter.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        # The filter.
        self.filter = filter
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to display the information that the service instance is deleted. Valid values:
        # 
        # *   true
        # *   false
        self.show_deleted = show_deleted
        # The custom tags.
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
        # Indicates whether the private connection feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.enable_private_vpc_connection = enable_private_vpc_connection
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
        # *   poc: The service is a trial service.
        self.service_type = service_type
        # The name of the distribution source service provider.
        self.source_supplier_name = source_supplier_name
        # The status of the service.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        biz_status: str = None,
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
        # The time when the service instance expires.
        self.end_time = end_time
        # Indicates whether the hosted O\\&M feature is enabled for the service instance. Valid values:
        # 
        # *   true
        # *   false
        self.is_operated = is_operated
        # The name of the service instance.
        self.name = name
        # The ID of the service instance that is used to implement hosted O\\&M.
        self.operated_service_instance_id = operated_service_instance_id
        # The end of the time range during which hosted O\\&M is implemented.
        self.operation_end_time = operation_end_time
        # The beginning of the time range during which hosted O\\&M is implemented.
        self.operation_start_time = operation_start_time
        # The parameters of the service instance.
        self.parameters = parameters
        # The billing method of the service. Valid values:
        # 
        # *   Permanent: Once you purchase the service, you can use it permanently.
        # *   Subscription: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a subscription basis.
        # *   PayAsYouGo: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a pay-as-you-go basis.
        # *   CustomFixTime: You are charged for the service based on a custom duration fixed by the service provider.
        self.pay_type = pay_type
        # The deployment progress of the service instance. Unit: percentage.
        self.progress = progress
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The information about the service.
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
        # The source from which the service instance is created.
        self.source = source
        # The status of the service instance. Valid values:
        # 
        # *   Created
        # *   Deploying
        # *   DeployedFailed
        # *   Deployed
        # *   Upgrading
        # *   Deleting
        # *   Deleted
        self.status = status
        # The description of the deployment of the service instance.
        self.status_detail = status_detail
        # The custom tags.
        self.tags = tags
        # The template name.
        self.template_name = template_name
        # The time when the service instance was updated.
        self.update_time = update_time
        # The Alibaba Cloud account ID of the user.
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
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
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
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
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
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about service instances.
        self.service_instances = service_instances
        # The total number of entries returned.
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


class ListServiceSharedAccountsRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The parameter name of the filter. You can specify one or more parameter names to query services. Valid values:
        # 
        # *   Name: the name of the service.
        self.name = name
        # The parameter value N of the filter. Valid values of N: 1 to 10.
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


class ListServiceSharedAccountsRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListServiceSharedAccountsRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        permission: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        # The filters.
        self.filter = filter
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The permissions on the service. Valid values:
        # 
        # *   Deployable: Permissions to deploy the service.
        # *   Accessible: Permissions to access the service.
        self.permission = permission
        # The region ID where the service instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        self.service_id = service_id

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
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceSharedAccountsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ListServiceSharedAccountsResponseBodyShareAccount(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        logo: str = None,
        name: str = None,
        permission: str = None,
        service_id: str = None,
        update_time: str = None,
        user_ali_uid: str = None,
    ):
        # The time when the service was created.
        self.create_time = create_time
        # Service logo.
        self.logo = logo
        # The name of the service instance. The value must meet the following requirements:
        # 
        # *   The name cannot exceed 64 characters in length.
        # *   It can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or a letter.
        self.name = name
        # The permissions on the service. Valid values:
        # 
        # *   Deployable: Permissions to deploy the service.
        # *   Accessible: Permissions to access the service.
        self.permission = permission
        # The service ID.
        self.service_id = service_id
        # The time when the service was updated.
        self.update_time = update_time
        self.user_ali_uid = user_ali_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.name is not None:
            result['Name'] = self.name
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')
        return self


class ListServiceSharedAccountsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        share_account: List[ListServiceSharedAccountsResponseBodyShareAccount] = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        self.share_account = share_account
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.share_account:
            for k in self.share_account:
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
        result['ShareAccount'] = []
        if self.share_account is not None:
            for k in self.share_account:
                result['ShareAccount'].append(k.to_map() if k else None)
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
        self.share_account = []
        if m.get('ShareAccount') is not None:
            for k in m.get('ShareAccount'):
                temp_model = ListServiceSharedAccountsResponseBodyShareAccount()
                self.share_account.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceSharedAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceSharedAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListServiceSharedAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceUsagesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The parameter name of the filter. You can specify one or more filters. Valid values:
        # 
        # *   ServiceId: the ID of the service.
        # *   ServiceName: the service name.
        # *   Status: the state of the service.
        # *   SupplierName: the name of the service provider.
        self.name = name
        # The parameter value N of the filter. Valid values of N: 1 to 10.
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
        supplier_role: str = None,
    ):
        # The filter.
        self.filter = filter
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The role of the service provider.
        self.supplier_role = supplier_role

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
        if self.supplier_role is not None:
            result['SupplierRole'] = self.supplier_role
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
        if m.get('SupplierRole') is not None:
            self.supplier_role = m.get('SupplierRole')
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
        user_information: Dict[str, str] = None,
    ):
        # The comment on the approval.
        self.comments = comments
        # The time when the application was created.
        self.create_time = create_time
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The status of the service application. Valid values:
        # 
        # *   Submitted: The application is submitted or is to be approved.
        # *   Approved: The application is approved.
        # *   Rejected: The application is rejected.
        # *   Canceled: The application is canceled.
        self.status = status
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The time when the application was updated.
        self.update_time = update_time
        # The ID of the Alibaba Cloud account.
        self.user_ali_uid = user_ali_uid
        # The user information.
        self.user_information = user_information

    def validate(self):
        pass

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
            result['UserInformation'] = self.user_information
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
            self.user_information = m.get('UserInformation')
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
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The service applications.
        self.service_usages = service_usages
        # The total number of entries returned.
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
        # The parameter name of the filter. You can specify one or more parameter names to query services. Valid values:
        # 
        # *   ServiceId: the ID of the service.
        # *   Name: the name of the service.
        # *   Status: the state of the service.
        # *   SupplierName: the name of the service provider.
        self.name = name
        # The parameter values of the filter.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        # Specifies whether to return all versions of a service. Default value: false, which specifies that only the default version of a service is returned.
        self.all_versions = all_versions
        # The filters.
        self.filter = filter
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The custom tags.
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


class ListServicesResponseBodyServicesCommodity(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListServicesResponseBodyServicesServiceInfos(TeaModel):
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
        # The tag key.
        self.key = key
        # The tag value.
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
        build_info: str = None,
        categories: str = None,
        commodity: ListServicesResponseBodyServicesCommodity = None,
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
        # *\
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
            temp_model = ListServicesResponseBodyServicesCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
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
        if m.get('VirtualInternetService') is not None:
            self.virtual_internet_service = m.get('VirtualInternetService')
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
        # The imported resources.
        self.resources = resources
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id
        # The type of operation performed on the service instance resource. Valid values:
        # 
        # *   Import: The resource is imported.
        # *   UnImport: The resource import is canceled.
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
        # The request ID.
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


class PushMeteringDataRequest(TeaModel):
    def __init__(
        self,
        metering: str = None,
        service_instance_id: str = None,
    ):
        # The metering data. Parameters in the example value:
        # 
        # *   InstanceId: the ID of an instance in Alibaba Cloud Marketplace. Parameter type: STRING.
        # 
        # *   StartTime: the time when the metering operation started. Set the parameter to a UNIX timestamp. Unit: seconds. Parameter type: LONG.
        # 
        # *   EndTime: the time when the metering operation ended. Set the parameter to a UNIX timestamp. Unit: seconds. Parameter type: LONG.
        # 
        # *   Entities: the metering entities. Parameter type: LIST.
        # 
        #     *   Key: the name of the metering item. Parameter type: STRING.
        # 
        #         *   Frequency: the number of times the instance was used.
        #         *   Period: the usage duration of the instance. Unit: seconds.
        # 
        #     Note: The metering unit is second, whereas the billing unit is hour. Therefore, when bills are generated, seconds are converted to hours. For example, the usage metered from 19:00 to 20:00 is 1800 seconds and the price is USD 1 per hour. In this case, the hourly bill for 19:00 to 20:00 is calculated by using the following formula: 1800/3600 x 1 = 0.5. If the result is a decimal, only the first two decimal places are retained.
        # 
        #           - Storage: The used storage space. Unit: bytes.   
        #            Note: The metering unit is byte, whereas the billing unit is MB. Therefore, when bills are generated, bytes are converted to megabytes. For example, the usage metered from 19:00 to 20:00 is 524,288 bytes and the price is USD 1 per MB. In this case, the hourly bill for 19:00 to 20:00 is calculated by using the following formula: 524288/1024/1024 x 1 = 0.5. If the result is a decimal, only the first two decimal places are retained.  - NetworkOut: the upstream traffic consumed. Unit: bit.  
        #            Note: The metering unit is bit, whereas the billing unit is Mbit. Therefore, when bills are generated, bits are converted to megabits. For example, the usage metered from 19:00 to 20:00 is 524,288 bits and the price is USD 1 per Mbit. In this case, the hourly bill for 19:00 to 20:00 is calculated by using the following formula: 524288/1024/1024 x 1 = 0.5. If the result is a decimal, only the first two decimal places are retained.  - NetworkIn: the downstream traffic consumed. Unit: bit.  
        #            Note: The metering unit is bit, whereas the billing unit is Mbit. Therefore, when bills are generated, bits are converted to megabits. For example, the usage metered from 19:00 to 20:00 is 524,288 bits and the price is USD 1 per Mbit. In this case, the hourly bill for 19:00 to 20:00 is calculated by using the following formula: 524288/1024/1024 x 1 = 0.5. If the result is a decimal, only the first two decimal places are retained.  - Character: the number of characters.
        #           - DailyActiveUser: the number of daily active users (DAU).
        #           - PeriodMin: the usage duration of the instance. Unit: minutes.  - VirtualCpu: the number of virtual CPU cores.
        # 
        #     *   Value: the value of the metering item. The value is equal to or greater than 0. Parameter type: INTEGER.
        # 
        # **Note**:
        # 
        # *   If bills are generated for the commodity in real time, the difference between the values of StartTime and EndTime is not limited. However, the time specified by EndTime must be later than that specified by StartTime.
        # *   If bills are generated for the commodity by billing cycle, such as by hour, by day, or by month, the difference between the values of StartTime and EndTime must be greater than 5 minutes.
        # *   In a request for pushing multiple metering data records, the values of InstanceId must indicate instances of the same commodity. You cannot push metering data of instances of multiple commodities at a time.
        # 
        # This parameter is required.
        self.metering = metering
        # The service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering is not None:
            result['Metering'] = self.metering
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metering') is not None:
            self.metering = m.get('Metering')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class PushMeteringDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class PushMeteringDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushMeteringDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PushMeteringDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class RegisterServiceResponseBody(TeaModel):
    def __init__(
        self,
        registration_id: str = None,
        request_id: str = None,
    ):
        # The registration ID.
        self.registration_id = registration_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RegisterServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectServiceUsageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        comments: str = None,
        service_id: str = None,
        type: int = None,
        user_ali_uid: int = None,
    ):
        self.client_token = client_token
        self.comments = comments
        # This parameter is required.
        self.service_id = service_id
        self.type = type
        # This parameter is required.
        self.user_ali_uid = user_ali_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.type is not None:
            result['Type'] = self.type
        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')
        return self


class RejectServiceUsageResponseBody(TeaModel):
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


class RejectServiceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RejectServiceUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RejectServiceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseArtifactRequest(TeaModel):
    def __init__(
        self,
        artifact_id: str = None,
    ):
        # The ID of the artifact.
        # 
        # This parameter is required.
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
        # The ID of the artifact.
        self.artifact_id = artifact_id
        # The content of the artifact.
        self.artifact_property = artifact_property
        # The type of the artifact.
        self.artifact_type = artifact_type
        # The version of the artifact.
        self.artifact_version = artifact_version
        # The description of the artifact.
        self.description = description
        # The time when the artifact was modified.
        self.gmt_modified = gmt_modified
        # The request ID.
        self.request_id = request_id
        # The state of the artifact. Valid values:
        # 
        # *   Created: The artifact is created.
        # *   Scanning: The artifact is being scanned.
        # *   ScanFailed: The artifact failed to be scanned.
        # *   Delivering: The artifact is being distributed.
        # *   Available: The artifact is available.
        # *   Deleted: The artifact is deleted.
        self.status = status
        # The version name of the artifact.
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


class RemoveServiceSharedAccountsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_id: str = None,
        type: str = None,
        user_ali_uids: List[int] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The share type of the service. Default value: SharedAccount. Valid values:
        # 
        # *   SharedAccount: The service is shared by multiple accounts.
        # *   Reseller: The service is distributed.
        self.type = type
        # This parameter is required.
        self.user_ali_uids = user_ali_uids

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
        if self.type is not None:
            result['Type'] = self.type
        if self.user_ali_uids is not None:
            result['UserAliUids'] = self.user_ali_uids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserAliUids') is not None:
            self.user_ali_uids = m.get('UserAliUids')
        return self


class RemoveServiceSharedAccountsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RemoveServiceSharedAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveServiceSharedAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveServiceSharedAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID where the service instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
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


class RestartServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RestartServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RestartServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID where the service instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
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


class StartServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StartServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = StartServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # The region id where the service instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
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


class StopServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StopServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = StopServiceInstanceResponseBody()
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
        # The commodity code of the service in Alibaba Cloud Marketplace.
        # 
        # >  This parameter is available only if the deployment package is an image.
        self.commodity_code = commodity_code
        # The commodity version of the service in Alibaba Cloud Marketplace.
        # 
        # >  This parameter is available only if the deployment package is an image.
        self.commodity_version = commodity_version
        # The metadata of the Object Storage Service (OSS) object.
        # 
        # >  This parameter is available only if the deployment package is an OSS object.
        self.file_script_metadata = file_script_metadata
        # The image ID.
        # 
        # >  This parameter is available only if the deployment package is an image.
        self.image_id = image_id
        # The region ID.
        # 
        # >  This parameter is available only if the deployment package is an image.
        self.region_id = region_id
        # The script content of the deployment package.
        # 
        # >  This parameter is available only if the deployment package is a script.
        self.script_metadata = script_metadata
        # The URL of the deployment package object.
        # 
        # 
        # > Note This parameter is available only if the deployment package is an file.
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
        # The ID of the deployment package.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # The properties of the deployment package.
        # 
        # This parameter is required.
        self.artifact_property = artifact_property
        # The description of the deployment package.
        self.description = description
        # The IDs of the regions that support the deployment package.
        self.support_region_ids = support_region_ids
        # The version name of the deployment package.
        # 
        # This parameter is required.
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
        # The ID of the deployment package.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # The properties of the deployment package.
        # 
        # This parameter is required.
        self.artifact_property_shrink = artifact_property_shrink
        # The description of the deployment package.
        self.description = description
        # The IDs of the regions that support the deployment package.
        self.support_region_ids = support_region_ids
        # The version name of the deployment package.
        # 
        # This parameter is required.
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
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The properties of the deployment package.
        self.artifact_property = artifact_property
        # The type of the deployment package.
        self.artifact_type = artifact_type
        # The version of the deployment package.
        self.artifact_version = artifact_version
        # The description of the deployment package.
        self.description = description
        # The time when the deployment package was modified.
        self.gmt_modified = gmt_modified
        # The request ID.
        self.request_id = request_id
        # The status of the deployment package. Valid values:
        # 
        # *   Created: The deployment package is created.
        # *   Scanning: The deployment package is being scanned.
        # *   ScanFailed: The deployment package failed to be scanned.
        # *   Delivering: The deployment package is being distributed.
        # *   Available: The deployment package is available.
        # *   Deleted: The deployment package is deleted.
        self.status = status
        # The ID of the region that supports the deployment package.
        self.support_region_ids = support_region_ids
        # The name of the deployment package.
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


class UpdateServiceRequestCommodityComponentsMappings(TeaModel):
    def __init__(
        self,
        mappings: str = None,
        template_name: str = None,
    ):
        # This parameter is not publicly accessible.
        self.mappings = mappings
        # This parameter is not publicly accessible.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateServiceRequestCommodityMeteringEntityExtraInfos(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        metric_name: str = None,
        promql: str = None,
        type: str = None,
    ):
        # The ID of the entity.
        self.entity_id = entity_id
        # Metric Name, filled in when Type is ComputeNestBill or ComputeNestPrometheus
        self.metric_name = metric_name
        # Custom prometheus query
        self.promql = promql
        # Type, value：
        # 
        # * **Custom**\
        # * **ComputeNestBill**\
        # * **ComputeNestPrometheus**\
        # * **ComputeNestTime**\
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateServiceRequestCommodityMeteringEntityMappings(TeaModel):
    def __init__(
        self,
        entity_ids: List[str] = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateServiceRequestCommoditySpecificationMappings(TeaModel):
    def __init__(
        self,
        specification_code: str = None,
        specification_name: str = None,
        template_name: str = None,
    ):
        # Specification code.
        self.specification_code = specification_code
        # The package name.
        self.specification_name = specification_name
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateServiceRequestCommodity(TeaModel):
    def __init__(
        self,
        components_mappings: List[UpdateServiceRequestCommodityComponentsMappings] = None,
        metering_entity_extra_infos: List[UpdateServiceRequestCommodityMeteringEntityExtraInfos] = None,
        metering_entity_mappings: List[UpdateServiceRequestCommodityMeteringEntityMappings] = None,
        saas_boost_config: str = None,
        specification_mappings: List[UpdateServiceRequestCommoditySpecificationMappings] = None,
    ):
        # This parameter is not publicly accessible.
        self.components_mappings = components_mappings
        # Metering Item Configuration Information (Cloud Marketplace - Pay-As-You-Go Use)
        self.metering_entity_extra_infos = metering_entity_extra_infos
        # Product Specifications and Template/specification mapping Relationships (Cloud Marketplace - Pay-As-You-Go Use)
        self.metering_entity_mappings = metering_entity_mappings
        # Saas boost config information
        self.saas_boost_config = saas_boost_config
        # Product Specifications and Template/specification mapping Relationships (Cloud Marketplace - Subscription/Permanent Use)
        self.specification_mappings = specification_mappings

    def validate(self):
        if self.components_mappings:
            for k in self.components_mappings:
                if k:
                    k.validate()
        if self.metering_entity_extra_infos:
            for k in self.metering_entity_extra_infos:
                if k:
                    k.validate()
        if self.metering_entity_mappings:
            for k in self.metering_entity_mappings:
                if k:
                    k.validate()
        if self.specification_mappings:
            for k in self.specification_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentsMappings'] = []
        if self.components_mappings is not None:
            for k in self.components_mappings:
                result['ComponentsMappings'].append(k.to_map() if k else None)
        result['MeteringEntityExtraInfos'] = []
        if self.metering_entity_extra_infos is not None:
            for k in self.metering_entity_extra_infos:
                result['MeteringEntityExtraInfos'].append(k.to_map() if k else None)
        result['MeteringEntityMappings'] = []
        if self.metering_entity_mappings is not None:
            for k in self.metering_entity_mappings:
                result['MeteringEntityMappings'].append(k.to_map() if k else None)
        if self.saas_boost_config is not None:
            result['SaasBoostConfig'] = self.saas_boost_config
        result['SpecificationMappings'] = []
        if self.specification_mappings is not None:
            for k in self.specification_mappings:
                result['SpecificationMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components_mappings = []
        if m.get('ComponentsMappings') is not None:
            for k in m.get('ComponentsMappings'):
                temp_model = UpdateServiceRequestCommodityComponentsMappings()
                self.components_mappings.append(temp_model.from_map(k))
        self.metering_entity_extra_infos = []
        if m.get('MeteringEntityExtraInfos') is not None:
            for k in m.get('MeteringEntityExtraInfos'):
                temp_model = UpdateServiceRequestCommodityMeteringEntityExtraInfos()
                self.metering_entity_extra_infos.append(temp_model.from_map(k))
        self.metering_entity_mappings = []
        if m.get('MeteringEntityMappings') is not None:
            for k in m.get('MeteringEntityMappings'):
                temp_model = UpdateServiceRequestCommodityMeteringEntityMappings()
                self.metering_entity_mappings.append(temp_model.from_map(k))
        if m.get('SaasBoostConfig') is not None:
            self.saas_boost_config = m.get('SaasBoostConfig')
        self.specification_mappings = []
        if m.get('SpecificationMappings') is not None:
            for k in m.get('SpecificationMappings'):
                temp_model = UpdateServiceRequestCommoditySpecificationMappings()
                self.specification_mappings.append(temp_model.from_map(k))
        return self


class UpdateServiceRequestServiceInfoAgreements(TeaModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        # Protocol name.
        self.name = name
        # Protocol url.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateServiceRequestServiceInfo(TeaModel):
    def __init__(
        self,
        agreements: List[UpdateServiceRequestServiceInfoAgreements] = None,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
    ):
        # Protocol document information about the service.
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

    def validate(self):
        if self.agreements:
            for k in self.agreements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Agreements'] = []
        if self.agreements is not None:
            for k in self.agreements:
                result['Agreements'].append(k.to_map() if k else None)
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
        self.agreements = []
        if m.get('Agreements') is not None:
            for k in m.get('Agreements'):
                temp_model = UpdateServiceRequestServiceInfoAgreements()
                self.agreements.append(temp_model.from_map(k))
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


class UpdateServiceRequestUpdateOption(TeaModel):
    def __init__(
        self,
        update_artifact: bool = None,
        update_from: str = None,
    ):
        self.update_artifact = update_artifact
        # The options for update the service. Valid values:
        # - CODE
        # - PARAMETERS
        self.update_from = update_from

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_artifact is not None:
            result['UpdateArtifact'] = self.update_artifact
        if self.update_from is not None:
            result['UpdateFrom'] = self.update_from
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateArtifact') is not None:
            self.update_artifact = m.get('UpdateArtifact')
        if m.get('UpdateFrom') is not None:
            self.update_from = m.get('UpdateFrom')
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        approval_type: str = None,
        client_token: str = None,
        commodity: UpdateServiceRequestCommodity = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        duration: int = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        policy_names: str = None,
        region_id: str = None,
        resellable: bool = None,
        service_id: str = None,
        service_info: List[UpdateServiceRequestServiceInfo] = None,
        service_type: str = None,
        service_version: str = None,
        share_type: str = None,
        tenant_type: str = None,
        trial_duration: int = None,
        update_option: UpdateServiceRequestUpdateOption = None,
        upgrade_metadata: str = None,
        version_name: str = None,
    ):
        # The alert configurations of the service.
        # 
        # >  This parameter takes effect only when you specify an alert policy for **PolicyNames**.
        self.alarm_metadata = alarm_metadata
        # The approval type of the service usage application. Valid values:
        # 
        # - Manual: The application is manually approved.
        # - AutoPass: The application is automatically approved.
        self.approval_type = approval_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Bind Commodity Information
        self.commodity = commodity
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
        # Specifies whether to enable the hosted O\\&M feature for the service. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is required if you set **ServiceType** to **private**.
        self.is_support_operated = is_support_operated
        # The license metadata.
        self.license_metadata = license_metadata
        # The logging configurations.
        self.log_metadata = log_metadata
        # The hosted O\\&M configurations.
        self.operation_metadata = operation_metadata
        # The policy name. The name can be up to 128 characters in length. Separate multiple names with commas (,). Only hosted O\\&M policies are supported.
        self.policy_names = policy_names
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to support distribution. Valid values:
        # 
        # *   false
        # *   true
        self.resellable = resellable
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service details.
        self.service_info = service_info
        # The service type. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        # *   poc: The service is a trial service.
        self.service_type = service_type
        # The service version.
        self.service_version = service_version
        # The permission type of the deployment URL. Valid values:
        # 
        # - Public: All users can go to the URL to create a service instance or a trial service instance.
        # - Restricted: Only users in the whitelist can go to the URL to create a service instance or a trial service instance.
        # - OnlyFormalRestricted: Only users in the whitelist can go to the URL to create a service instance.
        # - OnlyTrailRestricted: Only users in the whitelist can go to the URL to create a trial service instance.
        # - Hidden: Users not in the whitelist cannot see the service details page when they go to the URL and cannot request deployment permissions.
        self.share_type = share_type
        # The type of the tenant. Valid values:
        # 
        # *   SingleTenant
        # *   MultiTenant
        self.tenant_type = tenant_type
        # The trial duration. Unit: day. The maximum trial duration cannot exceed 30 days.
        self.trial_duration = trial_duration
        # The options for update the service.
        self.update_option = update_option
        # The metadata about the upgrade.
        self.upgrade_metadata = upgrade_metadata
        # The version name.
        self.version_name = version_name

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.service_info:
            for k in self.service_info:
                if k:
                    k.validate()
        if self.update_option:
            self.update_option.validate()

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
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
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
        if self.resellable is not None:
            result['Resellable'] = self.resellable
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
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tenant_type is not None:
            result['TenantType'] = self.tenant_type
        if self.trial_duration is not None:
            result['TrialDuration'] = self.trial_duration
        if self.update_option is not None:
            result['UpdateOption'] = self.update_option.to_map()
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
        if m.get('Commodity') is not None:
            temp_model = UpdateServiceRequestCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
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
        if m.get('Resellable') is not None:
            self.resellable = m.get('Resellable')
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
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')
        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')
        if m.get('UpdateOption') is not None:
            temp_model = UpdateServiceRequestUpdateOption()
            self.update_option = temp_model.from_map(m['UpdateOption'])
        if m.get('UpgradeMetadata') is not None:
            self.upgrade_metadata = m.get('UpgradeMetadata')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateServiceShrinkRequestServiceInfoAgreements(TeaModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        # Protocol name.
        self.name = name
        # Protocol url.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateServiceShrinkRequestServiceInfo(TeaModel):
    def __init__(
        self,
        agreements: List[UpdateServiceShrinkRequestServiceInfoAgreements] = None,
        image: str = None,
        locale: str = None,
        long_description_url: str = None,
        name: str = None,
        short_description: str = None,
    ):
        # Protocol document information about the service.
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

    def validate(self):
        if self.agreements:
            for k in self.agreements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Agreements'] = []
        if self.agreements is not None:
            for k in self.agreements:
                result['Agreements'].append(k.to_map() if k else None)
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
        self.agreements = []
        if m.get('Agreements') is not None:
            for k in m.get('Agreements'):
                temp_model = UpdateServiceShrinkRequestServiceInfoAgreements()
                self.agreements.append(temp_model.from_map(k))
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


class UpdateServiceShrinkRequest(TeaModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        approval_type: str = None,
        client_token: str = None,
        commodity_shrink: str = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        duration: int = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        policy_names: str = None,
        region_id: str = None,
        resellable: bool = None,
        service_id: str = None,
        service_info: List[UpdateServiceShrinkRequestServiceInfo] = None,
        service_type: str = None,
        service_version: str = None,
        share_type: str = None,
        tenant_type: str = None,
        trial_duration: int = None,
        update_option_shrink: str = None,
        upgrade_metadata: str = None,
        version_name: str = None,
    ):
        # The alert configurations of the service.
        # 
        # >  This parameter takes effect only when you specify an alert policy for **PolicyNames**.
        self.alarm_metadata = alarm_metadata
        # The approval type of the service usage application. Valid values:
        # 
        # - Manual: The application is manually approved.
        # - AutoPass: The application is automatically approved.
        self.approval_type = approval_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Bind Commodity Information
        self.commodity_shrink = commodity_shrink
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
        # Specifies whether to enable the hosted O\\&M feature for the service. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is required if you set **ServiceType** to **private**.
        self.is_support_operated = is_support_operated
        # The license metadata.
        self.license_metadata = license_metadata
        # The logging configurations.
        self.log_metadata = log_metadata
        # The hosted O\\&M configurations.
        self.operation_metadata = operation_metadata
        # The policy name. The name can be up to 128 characters in length. Separate multiple names with commas (,). Only hosted O\\&M policies are supported.
        self.policy_names = policy_names
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to support distribution. Valid values:
        # 
        # *   false
        # *   true
        self.resellable = resellable
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service details.
        self.service_info = service_info
        # The service type. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        # *   poc: The service is a trial service.
        self.service_type = service_type
        # The service version.
        self.service_version = service_version
        # The permission type of the deployment URL. Valid values:
        # 
        # - Public: All users can go to the URL to create a service instance or a trial service instance.
        # - Restricted: Only users in the whitelist can go to the URL to create a service instance or a trial service instance.
        # - OnlyFormalRestricted: Only users in the whitelist can go to the URL to create a service instance.
        # - OnlyTrailRestricted: Only users in the whitelist can go to the URL to create a trial service instance.
        # - Hidden: Users not in the whitelist cannot see the service details page when they go to the URL and cannot request deployment permissions.
        self.share_type = share_type
        # The type of the tenant. Valid values:
        # 
        # *   SingleTenant
        # *   MultiTenant
        self.tenant_type = tenant_type
        # The trial duration. Unit: day. The maximum trial duration cannot exceed 30 days.
        self.trial_duration = trial_duration
        # The options for update the service.
        self.update_option_shrink = update_option_shrink
        # The metadata about the upgrade.
        self.upgrade_metadata = upgrade_metadata
        # The version name.
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
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_shrink is not None:
            result['Commodity'] = self.commodity_shrink
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
        if self.resellable is not None:
            result['Resellable'] = self.resellable
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            self.commodity_shrink = m.get('Commodity')
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
        if m.get('Resellable') is not None:
            self.resellable = m.get('Resellable')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k in m.get('ServiceInfo'):
                temp_model = UpdateServiceShrinkRequestServiceInfo()
                self.service_info.append(temp_model.from_map(k))
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


class UpdateServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateServiceInstanceAttributeRequestLicenseData(TeaModel):
    def __init__(
        self,
        custom_data: str = None,
    ):
        # The Custom Data
        self.custom_data = custom_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_data is not None:
            result['CustomData'] = self.custom_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomData') is not None:
            self.custom_data = m.get('CustomData')
        return self


class UpdateServiceInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        license_data: UpdateServiceInstanceAttributeRequestLicenseData = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The time when the service instance expires.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.end_time = end_time
        # The License Data
        self.license_data = license_data
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.license_data:
            self.license_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.license_data is not None:
            result['LicenseData'] = self.license_data.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LicenseData') is not None:
            temp_model = UpdateServiceInstanceAttributeRequestLicenseData()
            self.license_data = temp_model.from_map(m['LicenseData'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class UpdateServiceInstanceAttributeShrinkRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        license_data_shrink: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The time when the service instance expires.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.end_time = end_time
        # The License Data
        self.license_data_shrink = license_data_shrink
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.license_data_shrink is not None:
            result['LicenseData'] = self.license_data_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LicenseData') is not None:
            self.license_data_shrink = m.get('LicenseData')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class UpdateServiceInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateServiceInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateServiceInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        enable_user_prometheus: bool = None,
        operation_name: str = None,
        parameters: Dict[str, Any] = None,
        predefined_parameters_name: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to enable Prometheus on the customer side. Valid values:
        # 
        # *   true
        # *   false
        self.enable_user_prometheus = enable_user_prometheus
        # The name of the configuration update operation.
        self.operation_name = operation_name
        # The configuration parameters of the service instance.
        self.parameters = parameters
        # The name of the specification package.
        self.predefined_parameters_name = predefined_parameters_name
        # The service instance ID.
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
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.predefined_parameters_name is not None:
            result['PredefinedParametersName'] = self.predefined_parameters_name
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PredefinedParametersName') is not None:
            self.predefined_parameters_name = m.get('PredefinedParametersName')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class UpdateServiceInstanceSpecShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        enable_user_prometheus: bool = None,
        operation_name: str = None,
        parameters_shrink: str = None,
        predefined_parameters_name: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to enable Prometheus on the customer side. Valid values:
        # 
        # *   true
        # *   false
        self.enable_user_prometheus = enable_user_prometheus
        # The name of the configuration update operation.
        self.operation_name = operation_name
        # The configuration parameters of the service instance.
        self.parameters_shrink = parameters_shrink
        # The name of the specification package.
        self.predefined_parameters_name = predefined_parameters_name
        # The service instance ID.
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
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.predefined_parameters_name is not None:
            result['PredefinedParametersName'] = self.predefined_parameters_name
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('PredefinedParametersName') is not None:
            self.predefined_parameters_name = m.get('PredefinedParametersName')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class UpdateServiceInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceInstanceSpecResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateServiceInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   true: performs a dry run for the request, but does not create a service instance.
        # *   false: performs a dry run for the request, and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # The configuration parameters of the service instance.
        self.parameters = parameters
        # The region ID.
        self.region_id = region_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The service version.
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
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
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class UpgradeServiceInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   true: performs a dry run for the request, but does not create a service instance.
        # *   false: performs a dry run for the request, and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # The configuration parameters of the service instance.
        self.parameters_shrink = parameters_shrink
        # The region ID.
        self.region_id = region_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The service version.
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class UpgradeServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_instance_id: str = None,
        status: str = None,
        upgrade_required_parameters: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
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
        # The parameters required for the upgrade.
        self.upgrade_required_parameters = upgrade_required_parameters

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
        if self.upgrade_required_parameters is not None:
            result['UpgradeRequiredParameters'] = self.upgrade_required_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpgradeRequiredParameters') is not None:
            self.upgrade_required_parameters = m.get('UpgradeRequiredParameters')
        return self


class UpgradeServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpgradeServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


