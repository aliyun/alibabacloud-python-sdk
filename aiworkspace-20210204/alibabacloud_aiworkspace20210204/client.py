# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiworkspace20210204 import models as aiwork_space_20210204_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aiworkspace', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_dataworks_event_with_options(
        self,
        request: aiwork_space_20210204_models.AcceptDataworksEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.AcceptDataworksEventResponse:
        """
        @summary Receives and processes system event messages sent by DataWorks.
        
        @description This operation can be called only by the internal system and cannot be called by external users.
        
        @param request: AcceptDataworksEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptDataworksEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AcceptDataworksEvent',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/action/acceptdataworksevent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.AcceptDataworksEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_dataworks_event_with_options_async(
        self,
        request: aiwork_space_20210204_models.AcceptDataworksEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.AcceptDataworksEventResponse:
        """
        @summary Receives and processes system event messages sent by DataWorks.
        
        @description This operation can be called only by the internal system and cannot be called by external users.
        
        @param request: AcceptDataworksEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptDataworksEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AcceptDataworksEvent',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/action/acceptdataworksevent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.AcceptDataworksEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_dataworks_event(
        self,
        request: aiwork_space_20210204_models.AcceptDataworksEventRequest,
    ) -> aiwork_space_20210204_models.AcceptDataworksEventResponse:
        """
        @summary Receives and processes system event messages sent by DataWorks.
        
        @description This operation can be called only by the internal system and cannot be called by external users.
        
        @param request: AcceptDataworksEventRequest
        @return: AcceptDataworksEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.accept_dataworks_event_with_options(request, headers, runtime)

    async def accept_dataworks_event_async(
        self,
        request: aiwork_space_20210204_models.AcceptDataworksEventRequest,
    ) -> aiwork_space_20210204_models.AcceptDataworksEventResponse:
        """
        @summary Receives and processes system event messages sent by DataWorks.
        
        @description This operation can be called only by the internal system and cannot be called by external users.
        
        @param request: AcceptDataworksEventRequest
        @return: AcceptDataworksEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.accept_dataworks_event_with_options_async(request, headers, runtime)

    def add_image_with_options(
        self,
        request: aiwork_space_20210204_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.AddImageResponse:
        """
        @summary Adds a custom image to a workspace.
        
        @param request: AddImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_uri):
            body['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.AddImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_with_options_async(
        self,
        request: aiwork_space_20210204_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.AddImageResponse:
        """
        @summary Adds a custom image to a workspace.
        
        @param request: AddImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_uri):
            body['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.AddImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image(
        self,
        request: aiwork_space_20210204_models.AddImageRequest,
    ) -> aiwork_space_20210204_models.AddImageResponse:
        """
        @summary Adds a custom image to a workspace.
        
        @param request: AddImageRequest
        @return: AddImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_image_with_options(request, headers, runtime)

    async def add_image_async(
        self,
        request: aiwork_space_20210204_models.AddImageRequest,
    ) -> aiwork_space_20210204_models.AddImageResponse:
        """
        @summary Adds a custom image to a workspace.
        
        @param request: AddImageRequest
        @return: AddImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_image_with_options_async(request, headers, runtime)

    def add_image_labels_with_options(
        self,
        image_id: str,
        request: aiwork_space_20210204_models.AddImageLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.AddImageLabelsResponse:
        """
        @summary Adds tags to an image.
        
        @param request: AddImageLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImageLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.AddImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_labels_with_options_async(
        self,
        image_id: str,
        request: aiwork_space_20210204_models.AddImageLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.AddImageLabelsResponse:
        """
        @summary Adds tags to an image.
        
        @param request: AddImageLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImageLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.AddImageLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image_labels(
        self,
        image_id: str,
        request: aiwork_space_20210204_models.AddImageLabelsRequest,
    ) -> aiwork_space_20210204_models.AddImageLabelsResponse:
        """
        @summary Adds tags to an image.
        
        @param request: AddImageLabelsRequest
        @return: AddImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_image_labels_with_options(image_id, request, headers, runtime)

    async def add_image_labels_async(
        self,
        image_id: str,
        request: aiwork_space_20210204_models.AddImageLabelsRequest,
    ) -> aiwork_space_20210204_models.AddImageLabelsResponse:
        """
        @summary Adds tags to an image.
        
        @param request: AddImageLabelsRequest
        @return: AddImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_image_labels_with_options_async(image_id, request, headers, runtime)

    def add_member_role_with_options(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.AddMemberRoleResponse:
        """
        @summary Adds a role to a member in a workspace. After you add a role to a member, the member is granted the permissions of the role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMemberRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AddMemberRole',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members/{OpenApiUtilClient.get_encode_param(member_id)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.AddMemberRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_member_role_with_options_async(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.AddMemberRoleResponse:
        """
        @summary Adds a role to a member in a workspace. After you add a role to a member, the member is granted the permissions of the role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMemberRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AddMemberRole',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members/{OpenApiUtilClient.get_encode_param(member_id)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.AddMemberRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_member_role(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
    ) -> aiwork_space_20210204_models.AddMemberRoleResponse:
        """
        @summary Adds a role to a member in a workspace. After you add a role to a member, the member is granted the permissions of the role.
        
        @return: AddMemberRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_member_role_with_options(workspace_id, member_id, role_name, headers, runtime)

    async def add_member_role_async(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
    ) -> aiwork_space_20210204_models.AddMemberRoleResponse:
        """
        @summary Adds a role to a member in a workspace. After you add a role to a member, the member is granted the permissions of the role.
        
        @return: AddMemberRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_member_role_with_options_async(workspace_id, member_id, role_name, headers, runtime)

    def change_resource_group_with_options(
        self,
        request: aiwork_space_20210204_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a resource belongs based on the ID.
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/resourcegroups/action/changeresourcegroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: aiwork_space_20210204_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a resource belongs based on the ID.
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/resourcegroups/action/changeresourcegroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: aiwork_space_20210204_models.ChangeResourceGroupRequest,
    ) -> aiwork_space_20210204_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a resource belongs based on the ID.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: aiwork_space_20210204_models.ChangeResourceGroupRequest,
    ) -> aiwork_space_20210204_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a resource belongs based on the ID.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_code_source_with_options(
        self,
        request: aiwork_space_20210204_models.CreateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateCodeSourceResponse:
        """
        @summary Creates a code build in Platform for AI (PAI). You can configure Git branches and commit IDs. After the code build is created, you can reference the code build in a Deep Learning Containers (DLC) job.
        
        @param request: CreateCodeSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCodeSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.code_commit):
            body['CodeCommit'] = request.code_commit
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not UtilClient.is_unset(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_code_source_with_options_async(
        self,
        request: aiwork_space_20210204_models.CreateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateCodeSourceResponse:
        """
        @summary Creates a code build in Platform for AI (PAI). You can configure Git branches and commit IDs. After the code build is created, you can reference the code build in a Deep Learning Containers (DLC) job.
        
        @param request: CreateCodeSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCodeSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.code_commit):
            body['CodeCommit'] = request.code_commit
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not UtilClient.is_unset(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_code_source(
        self,
        request: aiwork_space_20210204_models.CreateCodeSourceRequest,
    ) -> aiwork_space_20210204_models.CreateCodeSourceResponse:
        """
        @summary Creates a code build in Platform for AI (PAI). You can configure Git branches and commit IDs. After the code build is created, you can reference the code build in a Deep Learning Containers (DLC) job.
        
        @param request: CreateCodeSourceRequest
        @return: CreateCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_code_source_with_options(request, headers, runtime)

    async def create_code_source_async(
        self,
        request: aiwork_space_20210204_models.CreateCodeSourceRequest,
    ) -> aiwork_space_20210204_models.CreateCodeSourceResponse:
        """
        @summary Creates a code build in Platform for AI (PAI). You can configure Git branches and commit IDs. After the code build is created, you can reference the code build in a Deep Learning Containers (DLC) job.
        
        @param request: CreateCodeSourceRequest
        @return: CreateCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_code_source_with_options_async(request, headers, runtime)

    def create_dataset_with_options(
        self,
        request: aiwork_space_20210204_models.CreateDatasetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetResponse:
        """
        @summary Creates a dataset.
        
        @param request: CreateDatasetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.data_count):
            body['DataCount'] = request.data_count
        if not UtilClient.is_unset(request.data_size):
            body['DataSize'] = request.data_size
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.import_info):
            body['ImportInfo'] = request.import_info
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.mount_access_read_write_role_id_list):
            body['MountAccessReadWriteRoleIdList'] = request.mount_access_read_write_role_id_list
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.property):
            body['Property'] = request.property
        if not UtilClient.is_unset(request.provider):
            body['Provider'] = request.provider
        if not UtilClient.is_unset(request.provider_type):
            body['ProviderType'] = request.provider_type
        if not UtilClient.is_unset(request.source_dataset_id):
            body['SourceDatasetId'] = request.source_dataset_id
        if not UtilClient.is_unset(request.source_dataset_version):
            body['SourceDatasetVersion'] = request.source_dataset_version
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.version_description):
            body['VersionDescription'] = request.version_description
        if not UtilClient.is_unset(request.version_labels):
            body['VersionLabels'] = request.version_labels
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        request: aiwork_space_20210204_models.CreateDatasetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetResponse:
        """
        @summary Creates a dataset.
        
        @param request: CreateDatasetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.data_count):
            body['DataCount'] = request.data_count
        if not UtilClient.is_unset(request.data_size):
            body['DataSize'] = request.data_size
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.import_info):
            body['ImportInfo'] = request.import_info
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.mount_access_read_write_role_id_list):
            body['MountAccessReadWriteRoleIdList'] = request.mount_access_read_write_role_id_list
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.property):
            body['Property'] = request.property
        if not UtilClient.is_unset(request.provider):
            body['Provider'] = request.provider
        if not UtilClient.is_unset(request.provider_type):
            body['ProviderType'] = request.provider_type
        if not UtilClient.is_unset(request.source_dataset_id):
            body['SourceDatasetId'] = request.source_dataset_id
        if not UtilClient.is_unset(request.source_dataset_version):
            body['SourceDatasetVersion'] = request.source_dataset_version
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.version_description):
            body['VersionDescription'] = request.version_description
        if not UtilClient.is_unset(request.version_labels):
            body['VersionLabels'] = request.version_labels
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: aiwork_space_20210204_models.CreateDatasetRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetResponse:
        """
        @summary Creates a dataset.
        
        @param request: CreateDatasetRequest
        @return: CreateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dataset_with_options(request, headers, runtime)

    async def create_dataset_async(
        self,
        request: aiwork_space_20210204_models.CreateDatasetRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetResponse:
        """
        @summary Creates a dataset.
        
        @param request: CreateDatasetRequest
        @return: CreateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dataset_with_options_async(request, headers, runtime)

    def create_dataset_file_metas_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetFileMetasResponse:
        """
        @summary Creates the metadata records of multiple files in a dataset at a time.
        
        @param request: CreateDatasetFileMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetFileMetasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_file_metas):
            body['DatasetFileMetas'] = request.dataset_file_metas
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetFileMetas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetFileMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_file_metas_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetFileMetasResponse:
        """
        @summary Creates the metadata records of multiple files in a dataset at a time.
        
        @param request: CreateDatasetFileMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetFileMetasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_file_metas):
            body['DatasetFileMetas'] = request.dataset_file_metas
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetFileMetas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetFileMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_file_metas(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetFileMetasRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetFileMetasResponse:
        """
        @summary Creates the metadata records of multiple files in a dataset at a time.
        
        @param request: CreateDatasetFileMetasRequest
        @return: CreateDatasetFileMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dataset_file_metas_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_file_metas_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetFileMetasRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetFileMetasResponse:
        """
        @summary Creates the metadata records of multiple files in a dataset at a time.
        
        @param request: CreateDatasetFileMetasRequest
        @return: CreateDatasetFileMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dataset_file_metas_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_job_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetJobResponse:
        """
        @summary Creates a dataset job.
        
        @param request: CreateDatasetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.job_action):
            body['JobAction'] = request.job_action
        if not UtilClient.is_unset(request.job_mode):
            body['JobMode'] = request.job_mode
        if not UtilClient.is_unset(request.job_spec):
            body['JobSpec'] = request.job_spec
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_job_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetJobResponse:
        """
        @summary Creates a dataset job.
        
        @param request: CreateDatasetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.job_action):
            body['JobAction'] = request.job_action
        if not UtilClient.is_unset(request.job_mode):
            body['JobMode'] = request.job_mode
        if not UtilClient.is_unset(request.job_spec):
            body['JobSpec'] = request.job_spec
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_job(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetJobRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetJobResponse:
        """
        @summary Creates a dataset job.
        
        @param request: CreateDatasetJobRequest
        @return: CreateDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dataset_job_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_job_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetJobRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetJobResponse:
        """
        @summary Creates a dataset job.
        
        @param request: CreateDatasetJobRequest
        @return: CreateDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dataset_job_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_job_config_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetJobConfigResponse:
        """
        @summary Creates a job configuration for a dataset.
        
        @param request: CreateDatasetJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetJobConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.config_type):
            body['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetJobConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_job_config_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetJobConfigResponse:
        """
        @summary Creates a job configuration for a dataset.
        
        @param request: CreateDatasetJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetJobConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.config_type):
            body['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetJobConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_job_config(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetJobConfigRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetJobConfigResponse:
        """
        @summary Creates a job configuration for a dataset.
        
        @param request: CreateDatasetJobConfigRequest
        @return: CreateDatasetJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dataset_job_config_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_job_config_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetJobConfigRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetJobConfigResponse:
        """
        @summary Creates a job configuration for a dataset.
        
        @param request: CreateDatasetJobConfigRequest
        @return: CreateDatasetJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dataset_job_config_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_labels_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetLabelsResponse:
        """
        @summary Creates tags for a dataset.
        
        @description Before you call this operation, take note of the following items:
        The tag key and value are not empty strings and cannot exceed 128 characters in length.
        The tag key cannot start with any of the following strings: "aliyun", "acs", "http://", and "https://".
        
        @param request: CreateDatasetLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_labels_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetLabelsResponse:
        """
        @summary Creates tags for a dataset.
        
        @description Before you call this operation, take note of the following items:
        The tag key and value are not empty strings and cannot exceed 128 characters in length.
        The tag key cannot start with any of the following strings: "aliyun", "acs", "http://", and "https://".
        
        @param request: CreateDatasetLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_labels(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetLabelsRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetLabelsResponse:
        """
        @summary Creates tags for a dataset.
        
        @description Before you call this operation, take note of the following items:
        The tag key and value are not empty strings and cannot exceed 128 characters in length.
        The tag key cannot start with any of the following strings: "aliyun", "acs", "http://", and "https://".
        
        @param request: CreateDatasetLabelsRequest
        @return: CreateDatasetLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dataset_labels_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_labels_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetLabelsRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetLabelsResponse:
        """
        @summary Creates tags for a dataset.
        
        @description Before you call this operation, take note of the following items:
        The tag key and value are not empty strings and cannot exceed 128 characters in length.
        The tag key cannot start with any of the following strings: "aliyun", "acs", "http://", and "https://".
        
        @param request: CreateDatasetLabelsRequest
        @return: CreateDatasetLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dataset_labels_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_version_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetVersionResponse:
        """
        @summary Creates a dataset version.
        
        @param request: CreateDatasetVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_count):
            body['DataCount'] = request.data_count
        if not UtilClient.is_unset(request.data_size):
            body['DataSize'] = request.data_size
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.import_info):
            body['ImportInfo'] = request.import_info
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.property):
            body['Property'] = request.property
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_version_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetVersionResponse:
        """
        @summary Creates a dataset version.
        
        @param request: CreateDatasetVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_count):
            body['DataCount'] = request.data_count
        if not UtilClient.is_unset(request.data_size):
            body['DataSize'] = request.data_size
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.import_info):
            body['ImportInfo'] = request.import_info
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.property):
            body['Property'] = request.property
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_version(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetVersionRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetVersionResponse:
        """
        @summary Creates a dataset version.
        
        @param request: CreateDatasetVersionRequest
        @return: CreateDatasetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dataset_version_with_options(dataset_id, request, headers, runtime)

    async def create_dataset_version_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.CreateDatasetVersionRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetVersionResponse:
        """
        @summary Creates a dataset version.
        
        @param request: CreateDatasetVersionRequest
        @return: CreateDatasetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dataset_version_with_options_async(dataset_id, request, headers, runtime)

    def create_dataset_version_labels_with_options(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.CreateDatasetVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetVersionLabelsResponse:
        """
        @summary Creates tags for a dataset version.
        
        @param request: CreateDatasetVersionLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetVersionLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetVersionLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/labels',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetVersionLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_version_labels_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.CreateDatasetVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateDatasetVersionLabelsResponse:
        """
        @summary Creates tags for a dataset version.
        
        @param request: CreateDatasetVersionLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetVersionLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasetVersionLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/labels',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateDatasetVersionLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_version_labels(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.CreateDatasetVersionLabelsRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetVersionLabelsResponse:
        """
        @summary Creates tags for a dataset version.
        
        @param request: CreateDatasetVersionLabelsRequest
        @return: CreateDatasetVersionLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dataset_version_labels_with_options(dataset_id, version_name, request, headers, runtime)

    async def create_dataset_version_labels_async(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.CreateDatasetVersionLabelsRequest,
    ) -> aiwork_space_20210204_models.CreateDatasetVersionLabelsResponse:
        """
        @summary Creates tags for a dataset version.
        
        @param request: CreateDatasetVersionLabelsRequest
        @return: CreateDatasetVersionLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dataset_version_labels_with_options_async(dataset_id, version_name, request, headers, runtime)

    def create_experiment_with_options(
        self,
        request: aiwork_space_20210204_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateExperimentResponse:
        """
        @summary Creates an experiment.
        
        @param request: CreateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.artifact_uri):
            body['ArtifactUri'] = request.artifact_uri
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_with_options_async(
        self,
        request: aiwork_space_20210204_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateExperimentResponse:
        """
        @summary Creates an experiment.
        
        @param request: CreateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.artifact_uri):
            body['ArtifactUri'] = request.artifact_uri
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment(
        self,
        request: aiwork_space_20210204_models.CreateExperimentRequest,
    ) -> aiwork_space_20210204_models.CreateExperimentResponse:
        """
        @summary Creates an experiment.
        
        @param request: CreateExperimentRequest
        @return: CreateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    async def create_experiment_async(
        self,
        request: aiwork_space_20210204_models.CreateExperimentRequest,
    ) -> aiwork_space_20210204_models.CreateExperimentResponse:
        """
        @summary Creates an experiment.
        
        @param request: CreateExperimentRequest
        @return: CreateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_with_options_async(request, headers, runtime)

    def create_member_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.CreateMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateMemberResponse:
        """
        @summary Adds a user to a workspace as a member. You can add multiple users as members.
        
        @param request: CreateMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['Members'] = request.members
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMember',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_member_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.CreateMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateMemberResponse:
        """
        @summary Adds a user to a workspace as a member. You can add multiple users as members.
        
        @param request: CreateMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['Members'] = request.members
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMember',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_member(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.CreateMemberRequest,
    ) -> aiwork_space_20210204_models.CreateMemberResponse:
        """
        @summary Adds a user to a workspace as a member. You can add multiple users as members.
        
        @param request: CreateMemberRequest
        @return: CreateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_member_with_options(workspace_id, request, headers, runtime)

    async def create_member_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.CreateMemberRequest,
    ) -> aiwork_space_20210204_models.CreateMemberResponse:
        """
        @summary Adds a user to a workspace as a member. You can add multiple users as members.
        
        @param request: CreateMemberRequest
        @return: CreateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_member_with_options_async(workspace_id, request, headers, runtime)

    def create_model_with_options(
        self,
        request: aiwork_space_20210204_models.CreateModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateModelResponse:
        """
        @summary Creates a model. A model is a collection of model versions. When you create a model, you must specify the model name and description.
        
        @param request: CreateModelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.model_description):
            body['ModelDescription'] = request.model_description
        if not UtilClient.is_unset(request.model_doc):
            body['ModelDoc'] = request.model_doc
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.order_number):
            body['OrderNumber'] = request.order_number
        if not UtilClient.is_unset(request.origin):
            body['Origin'] = request.origin
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        request: aiwork_space_20210204_models.CreateModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateModelResponse:
        """
        @summary Creates a model. A model is a collection of model versions. When you create a model, you must specify the model name and description.
        
        @param request: CreateModelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.model_description):
            body['ModelDescription'] = request.model_description
        if not UtilClient.is_unset(request.model_doc):
            body['ModelDoc'] = request.model_doc
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.order_number):
            body['OrderNumber'] = request.order_number
        if not UtilClient.is_unset(request.origin):
            body['Origin'] = request.origin
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model(
        self,
        request: aiwork_space_20210204_models.CreateModelRequest,
    ) -> aiwork_space_20210204_models.CreateModelResponse:
        """
        @summary Creates a model. A model is a collection of model versions. When you create a model, you must specify the model name and description.
        
        @param request: CreateModelRequest
        @return: CreateModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_with_options(request, headers, runtime)

    async def create_model_async(
        self,
        request: aiwork_space_20210204_models.CreateModelRequest,
    ) -> aiwork_space_20210204_models.CreateModelResponse:
        """
        @summary Creates a model. A model is a collection of model versions. When you create a model, you must specify the model name and description.
        
        @param request: CreateModelRequest
        @return: CreateModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_with_options_async(request, headers, runtime)

    def create_model_labels_with_options(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.CreateModelLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateModelLabelsResponse:
        """
        @summary Creates a tag for a model.
        
        @param request: CreateModelLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateModelLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_labels_with_options_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.CreateModelLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateModelLabelsResponse:
        """
        @summary Creates a tag for a model.
        
        @param request: CreateModelLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateModelLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_labels(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.CreateModelLabelsRequest,
    ) -> aiwork_space_20210204_models.CreateModelLabelsResponse:
        """
        @summary Creates a tag for a model.
        
        @param request: CreateModelLabelsRequest
        @return: CreateModelLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_labels_with_options(model_id, request, headers, runtime)

    async def create_model_labels_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.CreateModelLabelsRequest,
    ) -> aiwork_space_20210204_models.CreateModelLabelsResponse:
        """
        @summary Creates a tag for a model.
        
        @param request: CreateModelLabelsRequest
        @return: CreateModelLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_labels_with_options_async(model_id, request, headers, runtime)

    def create_model_version_with_options(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.CreateModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateModelVersionResponse:
        """
        @summary Creates a new version for the specified model.
        
        @param request: CreateModelVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.approval_status):
            body['ApprovalStatus'] = request.approval_status
        if not UtilClient.is_unset(request.compression_spec):
            body['CompressionSpec'] = request.compression_spec
        if not UtilClient.is_unset(request.evaluation_spec):
            body['EvaluationSpec'] = request.evaluation_spec
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.framework_type):
            body['FrameworkType'] = request.framework_type
        if not UtilClient.is_unset(request.inference_spec):
            body['InferenceSpec'] = request.inference_spec
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.training_spec):
            body['TrainingSpec'] = request.training_spec
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.version_description):
            body['VersionDescription'] = request.version_description
        if not UtilClient.is_unset(request.version_name):
            body['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_version_with_options_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.CreateModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateModelVersionResponse:
        """
        @summary Creates a new version for the specified model.
        
        @param request: CreateModelVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.approval_status):
            body['ApprovalStatus'] = request.approval_status
        if not UtilClient.is_unset(request.compression_spec):
            body['CompressionSpec'] = request.compression_spec
        if not UtilClient.is_unset(request.evaluation_spec):
            body['EvaluationSpec'] = request.evaluation_spec
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.format_type):
            body['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.framework_type):
            body['FrameworkType'] = request.framework_type
        if not UtilClient.is_unset(request.inference_spec):
            body['InferenceSpec'] = request.inference_spec
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.training_spec):
            body['TrainingSpec'] = request.training_spec
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.version_description):
            body['VersionDescription'] = request.version_description
        if not UtilClient.is_unset(request.version_name):
            body['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_version(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.CreateModelVersionRequest,
    ) -> aiwork_space_20210204_models.CreateModelVersionResponse:
        """
        @summary Creates a new version for the specified model.
        
        @param request: CreateModelVersionRequest
        @return: CreateModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_version_with_options(model_id, request, headers, runtime)

    async def create_model_version_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.CreateModelVersionRequest,
    ) -> aiwork_space_20210204_models.CreateModelVersionResponse:
        """
        @summary Creates a new version for the specified model.
        
        @param request: CreateModelVersionRequest
        @return: CreateModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_version_with_options_async(model_id, request, headers, runtime)

    def create_model_version_labels_with_options(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.CreateModelVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateModelVersionLabelsResponse:
        """
        @summary Creates a tag for a model version.
        
        @param request: CreateModelVersionLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelVersionLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelVersionLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateModelVersionLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_version_labels_with_options_async(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.CreateModelVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateModelVersionLabelsResponse:
        """
        @summary Creates a tag for a model version.
        
        @param request: CreateModelVersionLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelVersionLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelVersionLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateModelVersionLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_version_labels(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.CreateModelVersionLabelsRequest,
    ) -> aiwork_space_20210204_models.CreateModelVersionLabelsResponse:
        """
        @summary Creates a tag for a model version.
        
        @param request: CreateModelVersionLabelsRequest
        @return: CreateModelVersionLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_version_labels_with_options(model_id, version_name, request, headers, runtime)

    async def create_model_version_labels_async(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.CreateModelVersionLabelsRequest,
    ) -> aiwork_space_20210204_models.CreateModelVersionLabelsResponse:
        """
        @summary Creates a tag for a model version.
        
        @param request: CreateModelVersionLabelsRequest
        @return: CreateModelVersionLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_version_labels_with_options_async(model_id, version_name, request, headers, runtime)

    def create_product_orders_with_options(
        self,
        request: aiwork_space_20210204_models.CreateProductOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateProductOrdersResponse:
        """
        @summary Creates a pay-as-you-go order for DataWorks, OSS, PAI, or MaxCompute.
        
        @param request: CreateProductOrdersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductOrdersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.products):
            body['Products'] = request.products
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductOrders',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/productorders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateProductOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_orders_with_options_async(
        self,
        request: aiwork_space_20210204_models.CreateProductOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateProductOrdersResponse:
        """
        @summary Creates a pay-as-you-go order for DataWorks, OSS, PAI, or MaxCompute.
        
        @param request: CreateProductOrdersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductOrdersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.products):
            body['Products'] = request.products
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductOrders',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/productorders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateProductOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_orders(
        self,
        request: aiwork_space_20210204_models.CreateProductOrdersRequest,
    ) -> aiwork_space_20210204_models.CreateProductOrdersResponse:
        """
        @summary Creates a pay-as-you-go order for DataWorks, OSS, PAI, or MaxCompute.
        
        @param request: CreateProductOrdersRequest
        @return: CreateProductOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_product_orders_with_options(request, headers, runtime)

    async def create_product_orders_async(
        self,
        request: aiwork_space_20210204_models.CreateProductOrdersRequest,
    ) -> aiwork_space_20210204_models.CreateProductOrdersResponse:
        """
        @summary Creates a pay-as-you-go order for DataWorks, OSS, PAI, or MaxCompute.
        
        @param request: CreateProductOrdersRequest
        @return: CreateProductOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_product_orders_with_options_async(request, headers, runtime)

    def create_run_with_options(
        self,
        request: aiwork_space_20210204_models.CreateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateRunResponse:
        """
        @summary Creates a run. A run is an experiment that can be associated with a specific workload or simply a code execution.
        
        @param request: CreateRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRunResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRun',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_run_with_options_async(
        self,
        request: aiwork_space_20210204_models.CreateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateRunResponse:
        """
        @summary Creates a run. A run is an experiment that can be associated with a specific workload or simply a code execution.
        
        @param request: CreateRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRunResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRun',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_run(
        self,
        request: aiwork_space_20210204_models.CreateRunRequest,
    ) -> aiwork_space_20210204_models.CreateRunResponse:
        """
        @summary Creates a run. A run is an experiment that can be associated with a specific workload or simply a code execution.
        
        @param request: CreateRunRequest
        @return: CreateRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_run_with_options(request, headers, runtime)

    async def create_run_async(
        self,
        request: aiwork_space_20210204_models.CreateRunRequest,
    ) -> aiwork_space_20210204_models.CreateRunResponse:
        """
        @summary Creates a run. A run is an experiment that can be associated with a specific workload or simply a code execution.
        
        @param request: CreateRunRequest
        @return: CreateRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_run_with_options_async(request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: aiwork_space_20210204_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateWorkspaceResponse:
        """
        @summary Creates a workspace.
        
        @param request: CreateWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.env_types):
            body['EnvTypes'] = request.env_types
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.workspace_name):
            body['WorkspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: aiwork_space_20210204_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateWorkspaceResponse:
        """
        @summary Creates a workspace.
        
        @param request: CreateWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.env_types):
            body['EnvTypes'] = request.env_types
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.workspace_name):
            body['WorkspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: aiwork_space_20210204_models.CreateWorkspaceRequest,
    ) -> aiwork_space_20210204_models.CreateWorkspaceResponse:
        """
        @summary Creates a workspace.
        
        @param request: CreateWorkspaceRequest
        @return: CreateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: aiwork_space_20210204_models.CreateWorkspaceRequest,
    ) -> aiwork_space_20210204_models.CreateWorkspaceResponse:
        """
        @summary Creates a workspace.
        
        @param request: CreateWorkspaceRequest
        @return: CreateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def create_workspace_resource_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.CreateWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateWorkspaceResourceResponse:
        """
        @summary Associates resources with a workspace.
        
        @param request: CreateWorkspaceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkspaceResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.option):
            body['Option'] = request.option
        if not UtilClient.is_unset(request.resources):
            body['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspaceResource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateWorkspaceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_resource_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.CreateWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.CreateWorkspaceResourceResponse:
        """
        @summary Associates resources with a workspace.
        
        @param request: CreateWorkspaceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkspaceResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.option):
            body['Option'] = request.option
        if not UtilClient.is_unset(request.resources):
            body['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspaceResource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.CreateWorkspaceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace_resource(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.CreateWorkspaceResourceRequest,
    ) -> aiwork_space_20210204_models.CreateWorkspaceResourceResponse:
        """
        @summary Associates resources with a workspace.
        
        @param request: CreateWorkspaceResourceRequest
        @return: CreateWorkspaceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_resource_with_options(workspace_id, request, headers, runtime)

    async def create_workspace_resource_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.CreateWorkspaceResourceRequest,
    ) -> aiwork_space_20210204_models.CreateWorkspaceResourceResponse:
        """
        @summary Associates resources with a workspace.
        
        @param request: CreateWorkspaceResourceRequest
        @return: CreateWorkspaceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workspace_resource_with_options_async(workspace_id, request, headers, runtime)

    def delete_code_source_with_options(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteCodeSourceResponse:
        """
        @summary Deletes a code source based on the provided ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCodeSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{OpenApiUtilClient.get_encode_param(code_source_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteCodeSourceResponse:
        """
        @summary Deletes a code source based on the provided ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCodeSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{OpenApiUtilClient.get_encode_param(code_source_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_code_source(
        self,
        code_source_id: str,
    ) -> aiwork_space_20210204_models.DeleteCodeSourceResponse:
        """
        @summary Deletes a code source based on the provided ID.
        
        @return: DeleteCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_code_source_with_options(code_source_id, headers, runtime)

    async def delete_code_source_async(
        self,
        code_source_id: str,
    ) -> aiwork_space_20210204_models.DeleteCodeSourceResponse:
        """
        @summary Deletes a code source based on the provided ID.
        
        @return: DeleteCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_code_source_with_options_async(code_source_id, headers, runtime)

    def delete_config_with_options(
        self,
        workspace_id: str,
        config_key: str,
        request: aiwork_space_20210204_models.DeleteConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteConfigResponse:
        """
        @summary Deletes workspace configurations.
        
        @param request: DeleteConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/configs/{OpenApiUtilClient.get_encode_param(config_key)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_with_options_async(
        self,
        workspace_id: str,
        config_key: str,
        request: aiwork_space_20210204_models.DeleteConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteConfigResponse:
        """
        @summary Deletes workspace configurations.
        
        @param request: DeleteConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/configs/{OpenApiUtilClient.get_encode_param(config_key)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config(
        self,
        workspace_id: str,
        config_key: str,
        request: aiwork_space_20210204_models.DeleteConfigRequest,
    ) -> aiwork_space_20210204_models.DeleteConfigResponse:
        """
        @summary Deletes workspace configurations.
        
        @param request: DeleteConfigRequest
        @return: DeleteConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_with_options(workspace_id, config_key, request, headers, runtime)

    async def delete_config_async(
        self,
        workspace_id: str,
        config_key: str,
        request: aiwork_space_20210204_models.DeleteConfigRequest,
    ) -> aiwork_space_20210204_models.DeleteConfigResponse:
        """
        @summary Deletes workspace configurations.
        
        @param request: DeleteConfigRequest
        @return: DeleteConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_config_with_options_async(workspace_id, config_key, request, headers, runtime)

    def delete_dataset_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetResponse:
        """
        @summary Deletes a dataset.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetResponse:
        """
        @summary Deletes a dataset.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        dataset_id: str,
    ) -> aiwork_space_20210204_models.DeleteDatasetResponse:
        """
        @summary Deletes a dataset.
        
        @return: DeleteDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dataset_with_options(dataset_id, headers, runtime)

    async def delete_dataset_async(
        self,
        dataset_id: str,
    ) -> aiwork_space_20210204_models.DeleteDatasetResponse:
        """
        @summary Deletes a dataset.
        
        @return: DeleteDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_dataset_with_options_async(dataset_id, headers, runtime)

    def delete_dataset_file_metas_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetFileMetasResponse:
        """
        @summary Deletes the metadata records of multiple files in a dataset at a time.
        
        @param request: DeleteDatasetFileMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetFileMetasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_file_meta_ids):
            query['DatasetFileMetaIds'] = request.dataset_file_meta_ids
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatasetFileMetas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetFileMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_file_metas_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetFileMetasResponse:
        """
        @summary Deletes the metadata records of multiple files in a dataset at a time.
        
        @param request: DeleteDatasetFileMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetFileMetasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_file_meta_ids):
            query['DatasetFileMetaIds'] = request.dataset_file_meta_ids
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatasetFileMetas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetFileMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_file_metas(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetFileMetasRequest,
    ) -> aiwork_space_20210204_models.DeleteDatasetFileMetasResponse:
        """
        @summary Deletes the metadata records of multiple files in a dataset at a time.
        
        @param request: DeleteDatasetFileMetasRequest
        @return: DeleteDatasetFileMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dataset_file_metas_with_options(dataset_id, request, headers, runtime)

    async def delete_dataset_file_metas_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetFileMetasRequest,
    ) -> aiwork_space_20210204_models.DeleteDatasetFileMetasResponse:
        """
        @summary Deletes the metadata records of multiple files in a dataset at a time.
        
        @param request: DeleteDatasetFileMetasRequest
        @return: DeleteDatasetFileMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_dataset_file_metas_with_options_async(dataset_id, request, headers, runtime)

    def delete_dataset_job_with_options(
        self,
        dataset_id: str,
        dataset_job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetJobResponse:
        """
        @summary Deletes a dataset job.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs/{OpenApiUtilClient.get_encode_param(dataset_job_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_job_with_options_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetJobResponse:
        """
        @summary Deletes a dataset job.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs/{OpenApiUtilClient.get_encode_param(dataset_job_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_job(
        self,
        dataset_id: str,
        dataset_job_id: str,
    ) -> aiwork_space_20210204_models.DeleteDatasetJobResponse:
        """
        @summary Deletes a dataset job.
        
        @return: DeleteDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dataset_job_with_options(dataset_id, dataset_job_id, headers, runtime)

    async def delete_dataset_job_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
    ) -> aiwork_space_20210204_models.DeleteDatasetJobResponse:
        """
        @summary Deletes a dataset job.
        
        @return: DeleteDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_dataset_job_with_options_async(dataset_id, dataset_job_id, headers, runtime)

    def delete_dataset_job_config_with_options(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetJobConfigResponse:
        """
        @summary Deletes a job configuration for a dataset.
        
        @param request: DeleteDatasetJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetJobConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatasetJobConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs/{OpenApiUtilClient.get_encode_param(dataset_job_config_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_job_config_with_options_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetJobConfigResponse:
        """
        @summary Deletes a job configuration for a dataset.
        
        @param request: DeleteDatasetJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetJobConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatasetJobConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs/{OpenApiUtilClient.get_encode_param(dataset_job_config_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_job_config(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetJobConfigRequest,
    ) -> aiwork_space_20210204_models.DeleteDatasetJobConfigResponse:
        """
        @summary Deletes a job configuration for a dataset.
        
        @param request: DeleteDatasetJobConfigRequest
        @return: DeleteDatasetJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dataset_job_config_with_options(dataset_id, dataset_job_config_id, request, headers, runtime)

    async def delete_dataset_job_config_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetJobConfigRequest,
    ) -> aiwork_space_20210204_models.DeleteDatasetJobConfigResponse:
        """
        @summary Deletes a job configuration for a dataset.
        
        @param request: DeleteDatasetJobConfigRequest
        @return: DeleteDatasetJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_dataset_job_config_with_options_async(dataset_id, dataset_job_config_id, request, headers, runtime)

    def delete_dataset_labels_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetLabelsResponse:
        """
        @summary Deletes a dataset tag.
        
        @param request: DeleteDatasetLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatasetLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_labels_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetLabelsResponse:
        """
        @summary Deletes a dataset tag.
        
        @param request: DeleteDatasetLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatasetLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_labels(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetLabelsRequest,
    ) -> aiwork_space_20210204_models.DeleteDatasetLabelsResponse:
        """
        @summary Deletes a dataset tag.
        
        @param request: DeleteDatasetLabelsRequest
        @return: DeleteDatasetLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dataset_labels_with_options(dataset_id, request, headers, runtime)

    async def delete_dataset_labels_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.DeleteDatasetLabelsRequest,
    ) -> aiwork_space_20210204_models.DeleteDatasetLabelsResponse:
        """
        @summary Deletes a dataset tag.
        
        @param request: DeleteDatasetLabelsRequest
        @return: DeleteDatasetLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_dataset_labels_with_options_async(dataset_id, request, headers, runtime)

    def delete_dataset_version_with_options(
        self,
        dataset_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetVersionResponse:
        """
        @summary Deletes the information about a specified version of a dataset. Version v1 cannot be deleted by using this operation. When you call the DeleteDataset operation to delete a dataset, it can be deleted at the same time.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDatasetVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_version_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetVersionResponse:
        """
        @summary Deletes the information about a specified version of a dataset. Version v1 cannot be deleted by using this operation. When you call the DeleteDataset operation to delete a dataset, it can be deleted at the same time.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDatasetVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_version(
        self,
        dataset_id: str,
        version_name: str,
    ) -> aiwork_space_20210204_models.DeleteDatasetVersionResponse:
        """
        @summary Deletes the information about a specified version of a dataset. Version v1 cannot be deleted by using this operation. When you call the DeleteDataset operation to delete a dataset, it can be deleted at the same time.
        
        @return: DeleteDatasetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dataset_version_with_options(dataset_id, version_name, headers, runtime)

    async def delete_dataset_version_async(
        self,
        dataset_id: str,
        version_name: str,
    ) -> aiwork_space_20210204_models.DeleteDatasetVersionResponse:
        """
        @summary Deletes the information about a specified version of a dataset. Version v1 cannot be deleted by using this operation. When you call the DeleteDataset operation to delete a dataset, it can be deleted at the same time.
        
        @return: DeleteDatasetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_dataset_version_with_options_async(dataset_id, version_name, headers, runtime)

    def delete_dataset_version_labels_with_options(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.DeleteDatasetVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetVersionLabelsResponse:
        """
        @summary Deletes tags for a dataset version.
        
        @param request: DeleteDatasetVersionLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetVersionLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keys):
            query['Keys'] = request.keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatasetVersionLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetVersionLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_version_labels_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.DeleteDatasetVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteDatasetVersionLabelsResponse:
        """
        @summary Deletes tags for a dataset version.
        
        @param request: DeleteDatasetVersionLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetVersionLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keys):
            query['Keys'] = request.keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatasetVersionLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteDatasetVersionLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_version_labels(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.DeleteDatasetVersionLabelsRequest,
    ) -> aiwork_space_20210204_models.DeleteDatasetVersionLabelsResponse:
        """
        @summary Deletes tags for a dataset version.
        
        @param request: DeleteDatasetVersionLabelsRequest
        @return: DeleteDatasetVersionLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dataset_version_labels_with_options(dataset_id, version_name, request, headers, runtime)

    async def delete_dataset_version_labels_async(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.DeleteDatasetVersionLabelsRequest,
    ) -> aiwork_space_20210204_models.DeleteDatasetVersionLabelsResponse:
        """
        @summary Deletes tags for a dataset version.
        
        @param request: DeleteDatasetVersionLabelsRequest
        @return: DeleteDatasetVersionLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_dataset_version_labels_with_options_async(dataset_id, version_name, request, headers, runtime)

    def delete_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteExperimentResponse:
        """
        @summary Deletes an experiment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteExperimentResponse:
        """
        @summary Deletes an experiment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment(
        self,
        experiment_id: str,
    ) -> aiwork_space_20210204_models.DeleteExperimentResponse:
        """
        @summary Deletes an experiment.
        
        @return: DeleteExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(experiment_id, headers, runtime)

    async def delete_experiment_async(
        self,
        experiment_id: str,
    ) -> aiwork_space_20210204_models.DeleteExperimentResponse:
        """
        @summary Deletes an experiment.
        
        @return: DeleteExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_with_options_async(experiment_id, headers, runtime)

    def delete_experiment_label_with_options(
        self,
        experiment_id: str,
        key: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteExperimentLabelResponse:
        """
        @summary Deletes an experiment tag.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentLabelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperimentLabel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/labels/{OpenApiUtilClient.get_encode_param(key)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteExperimentLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_label_with_options_async(
        self,
        experiment_id: str,
        key: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteExperimentLabelResponse:
        """
        @summary Deletes an experiment tag.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentLabelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperimentLabel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/labels/{OpenApiUtilClient.get_encode_param(key)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteExperimentLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment_label(
        self,
        experiment_id: str,
        key: str,
    ) -> aiwork_space_20210204_models.DeleteExperimentLabelResponse:
        """
        @summary Deletes an experiment tag.
        
        @return: DeleteExperimentLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_label_with_options(experiment_id, key, headers, runtime)

    async def delete_experiment_label_async(
        self,
        experiment_id: str,
        key: str,
    ) -> aiwork_space_20210204_models.DeleteExperimentLabelResponse:
        """
        @summary Deletes an experiment tag.
        
        @return: DeleteExperimentLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_label_with_options_async(experiment_id, key, headers, runtime)

    def delete_members_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.DeleteMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteMembersResponse:
        """
        @summary Deletes a member from a workspace.
        
        @param request: DeleteMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_ids):
            query['MemberIds'] = request.member_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMembers',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_members_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.DeleteMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteMembersResponse:
        """
        @summary Deletes a member from a workspace.
        
        @param request: DeleteMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_ids):
            query['MemberIds'] = request.member_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMembers',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_members(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.DeleteMembersRequest,
    ) -> aiwork_space_20210204_models.DeleteMembersResponse:
        """
        @summary Deletes a member from a workspace.
        
        @param request: DeleteMembersRequest
        @return: DeleteMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_members_with_options(workspace_id, request, headers, runtime)

    async def delete_members_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.DeleteMembersRequest,
    ) -> aiwork_space_20210204_models.DeleteMembersResponse:
        """
        @summary Deletes a member from a workspace.
        
        @param request: DeleteMembersRequest
        @return: DeleteMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_members_with_options_async(workspace_id, request, headers, runtime)

    def delete_model_with_options(
        self,
        model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteModelResponse:
        """
        @summary Deletes a model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteModelResponse:
        """
        @summary Deletes a model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model(
        self,
        model_id: str,
    ) -> aiwork_space_20210204_models.DeleteModelResponse:
        """
        @summary Deletes a model.
        
        @return: DeleteModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_with_options(model_id, headers, runtime)

    async def delete_model_async(
        self,
        model_id: str,
    ) -> aiwork_space_20210204_models.DeleteModelResponse:
        """
        @summary Deletes a model.
        
        @return: DeleteModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_with_options_async(model_id, headers, runtime)

    def delete_model_labels_with_options(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.DeleteModelLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteModelLabelsResponse:
        """
        @summary Deletes the labels of a model.
        
        @param request: DeleteModelLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModelLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteModelLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_labels_with_options_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.DeleteModelLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteModelLabelsResponse:
        """
        @summary Deletes the labels of a model.
        
        @param request: DeleteModelLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModelLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteModelLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_labels(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.DeleteModelLabelsRequest,
    ) -> aiwork_space_20210204_models.DeleteModelLabelsResponse:
        """
        @summary Deletes the labels of a model.
        
        @param request: DeleteModelLabelsRequest
        @return: DeleteModelLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_labels_with_options(model_id, request, headers, runtime)

    async def delete_model_labels_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.DeleteModelLabelsRequest,
    ) -> aiwork_space_20210204_models.DeleteModelLabelsResponse:
        """
        @summary Deletes the labels of a model.
        
        @param request: DeleteModelLabelsRequest
        @return: DeleteModelLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_labels_with_options_async(model_id, request, headers, runtime)

    def delete_model_version_with_options(
        self,
        model_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteModelVersionResponse:
        """
        @summary Deletes a model version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_version_with_options_async(
        self,
        model_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteModelVersionResponse:
        """
        @summary Deletes a model version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_version(
        self,
        model_id: str,
        version_name: str,
    ) -> aiwork_space_20210204_models.DeleteModelVersionResponse:
        """
        @summary Deletes a model version.
        
        @return: DeleteModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_version_with_options(model_id, version_name, headers, runtime)

    async def delete_model_version_async(
        self,
        model_id: str,
        version_name: str,
    ) -> aiwork_space_20210204_models.DeleteModelVersionResponse:
        """
        @summary Deletes a model version.
        
        @return: DeleteModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_version_with_options_async(model_id, version_name, headers, runtime)

    def delete_model_version_labels_with_options(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.DeleteModelVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteModelVersionLabelsResponse:
        """
        @summary Delete a model version tag.
        
        @param request: DeleteModelVersionLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelVersionLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModelVersionLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteModelVersionLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_version_labels_with_options_async(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.DeleteModelVersionLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteModelVersionLabelsResponse:
        """
        @summary Delete a model version tag.
        
        @param request: DeleteModelVersionLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelVersionLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModelVersionLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteModelVersionLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_version_labels(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.DeleteModelVersionLabelsRequest,
    ) -> aiwork_space_20210204_models.DeleteModelVersionLabelsResponse:
        """
        @summary Delete a model version tag.
        
        @param request: DeleteModelVersionLabelsRequest
        @return: DeleteModelVersionLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_version_labels_with_options(model_id, version_name, request, headers, runtime)

    async def delete_model_version_labels_async(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.DeleteModelVersionLabelsRequest,
    ) -> aiwork_space_20210204_models.DeleteModelVersionLabelsResponse:
        """
        @summary Delete a model version tag.
        
        @param request: DeleteModelVersionLabelsRequest
        @return: DeleteModelVersionLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_version_labels_with_options_async(model_id, version_name, request, headers, runtime)

    def delete_run_with_options(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteRunResponse:
        """
        @summary Deletes a run.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRunResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRun',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_run_with_options_async(
        self,
        run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteRunResponse:
        """
        @summary Deletes a run.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRunResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRun',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_run(
        self,
        run_id: str,
    ) -> aiwork_space_20210204_models.DeleteRunResponse:
        """
        @summary Deletes a run.
        
        @return: DeleteRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_run_with_options(run_id, headers, runtime)

    async def delete_run_async(
        self,
        run_id: str,
    ) -> aiwork_space_20210204_models.DeleteRunResponse:
        """
        @summary Deletes a run.
        
        @return: DeleteRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_run_with_options_async(run_id, headers, runtime)

    def delete_run_label_with_options(
        self,
        run_id: str,
        key: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteRunLabelResponse:
        """
        @summary Deletes a tag that is added to a run.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRunLabelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRunLabel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}/labels/{OpenApiUtilClient.get_encode_param(key)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteRunLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_run_label_with_options_async(
        self,
        run_id: str,
        key: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteRunLabelResponse:
        """
        @summary Deletes a tag that is added to a run.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRunLabelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRunLabel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}/labels/{OpenApiUtilClient.get_encode_param(key)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteRunLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_run_label(
        self,
        run_id: str,
        key: str,
    ) -> aiwork_space_20210204_models.DeleteRunLabelResponse:
        """
        @summary Deletes a tag that is added to a run.
        
        @return: DeleteRunLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_run_label_with_options(run_id, key, headers, runtime)

    async def delete_run_label_async(
        self,
        run_id: str,
        key: str,
    ) -> aiwork_space_20210204_models.DeleteRunLabelResponse:
        """
        @summary Deletes a tag that is added to a run.
        
        @return: DeleteRunLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_run_label_with_options_async(run_id, key, headers, runtime)

    def delete_user_config_with_options(
        self,
        category_name: str,
        request: aiwork_space_20210204_models.DeleteUserConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteUserConfigResponse:
        """
        @summary Deletes user configurations.
        
        @param request: DeleteUserConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/userconfigs/{OpenApiUtilClient.get_encode_param(category_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_config_with_options_async(
        self,
        category_name: str,
        request: aiwork_space_20210204_models.DeleteUserConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteUserConfigResponse:
        """
        @summary Deletes user configurations.
        
        @param request: DeleteUserConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/userconfigs/{OpenApiUtilClient.get_encode_param(category_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_config(
        self,
        category_name: str,
        request: aiwork_space_20210204_models.DeleteUserConfigRequest,
    ) -> aiwork_space_20210204_models.DeleteUserConfigResponse:
        """
        @summary Deletes user configurations.
        
        @param request: DeleteUserConfigRequest
        @return: DeleteUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_config_with_options(category_name, request, headers, runtime)

    async def delete_user_config_async(
        self,
        category_name: str,
        request: aiwork_space_20210204_models.DeleteUserConfigRequest,
    ) -> aiwork_space_20210204_models.DeleteUserConfigResponse:
        """
        @summary Deletes user configurations.
        
        @param request: DeleteUserConfigRequest
        @return: DeleteUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_user_config_with_options_async(category_name, request, headers, runtime)

    def delete_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteWorkspaceResponse:
        """
        @summary Deletes a workspace. After you delete a workspace, the associated resources are not automatically released. You must manually release the resources.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteWorkspaceResponse:
        """
        @summary Deletes a workspace. After you delete a workspace, the associated resources are not automatically released. You must manually release the resources.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        workspace_id: str,
    ) -> aiwork_space_20210204_models.DeleteWorkspaceResponse:
        """
        @summary Deletes a workspace. After you delete a workspace, the associated resources are not automatically released. You must manually release the resources.
        
        @return: DeleteWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workspace_with_options(workspace_id, headers, runtime)

    async def delete_workspace_async(
        self,
        workspace_id: str,
    ) -> aiwork_space_20210204_models.DeleteWorkspaceResponse:
        """
        @summary Deletes a workspace. After you delete a workspace, the associated resources are not automatically released. You must manually release the resources.
        
        @return: DeleteWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_id, headers, runtime)

    def delete_workspace_resource_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.DeleteWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteWorkspaceResourceResponse:
        """
        @summary Deletes a resource from a workspace. The resource is not deleted at the underlying layer.
        
        @param request: DeleteWorkspaceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkspaceResource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/resources',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteWorkspaceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_resource_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.DeleteWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.DeleteWorkspaceResourceResponse:
        """
        @summary Deletes a resource from a workspace. The resource is not deleted at the underlying layer.
        
        @param request: DeleteWorkspaceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkspaceResource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/resources',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.DeleteWorkspaceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace_resource(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.DeleteWorkspaceResourceRequest,
    ) -> aiwork_space_20210204_models.DeleteWorkspaceResourceResponse:
        """
        @summary Deletes a resource from a workspace. The resource is not deleted at the underlying layer.
        
        @param request: DeleteWorkspaceResourceRequest
        @return: DeleteWorkspaceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workspace_resource_with_options(workspace_id, request, headers, runtime)

    async def delete_workspace_resource_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.DeleteWorkspaceResourceRequest,
    ) -> aiwork_space_20210204_models.DeleteWorkspaceResourceResponse:
        """
        @summary Deletes a resource from a workspace. The resource is not deleted at the underlying layer.
        
        @param request: DeleteWorkspaceResourceRequest
        @return: DeleteWorkspaceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workspace_resource_with_options_async(workspace_id, request, headers, runtime)

    def get_code_source_with_options(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetCodeSourceResponse:
        """
        @summary Obtains the details of a code source.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCodeSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{OpenApiUtilClient.get_encode_param(code_source_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetCodeSourceResponse:
        """
        @summary Obtains the details of a code source.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCodeSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{OpenApiUtilClient.get_encode_param(code_source_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_code_source(
        self,
        code_source_id: str,
    ) -> aiwork_space_20210204_models.GetCodeSourceResponse:
        """
        @summary Obtains the details of a code source.
        
        @return: GetCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_code_source_with_options(code_source_id, headers, runtime)

    async def get_code_source_async(
        self,
        code_source_id: str,
    ) -> aiwork_space_20210204_models.GetCodeSourceResponse:
        """
        @summary Obtains the details of a code source.
        
        @return: GetCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_code_source_with_options_async(code_source_id, headers, runtime)

    def get_config_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetConfigResponse:
        """
        @summary Obtains a workspace configuration item.
        
        @param request: GetConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetConfigResponse:
        """
        @summary Obtains a workspace configuration item.
        
        @param request: GetConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetConfigRequest,
    ) -> aiwork_space_20210204_models.GetConfigResponse:
        """
        @summary Obtains a workspace configuration item.
        
        @param request: GetConfigRequest
        @return: GetConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_config_with_options(workspace_id, request, headers, runtime)

    async def get_config_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetConfigRequest,
    ) -> aiwork_space_20210204_models.GetConfigResponse:
        """
        @summary Obtains a workspace configuration item.
        
        @param request: GetConfigRequest
        @return: GetConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_config_with_options_async(workspace_id, request, headers, runtime)

    def get_dataset_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetResponse:
        """
        @summary Obtains a dataset.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetResponse:
        """
        @summary Obtains a dataset.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        dataset_id: str,
    ) -> aiwork_space_20210204_models.GetDatasetResponse:
        """
        @summary Obtains a dataset.
        
        @return: GetDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dataset_with_options(dataset_id, headers, runtime)

    async def get_dataset_async(
        self,
        dataset_id: str,
    ) -> aiwork_space_20210204_models.GetDatasetResponse:
        """
        @summary Obtains a dataset.
        
        @return: GetDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dataset_with_options_async(dataset_id, headers, runtime)

    def get_dataset_file_meta_with_options(
        self,
        dataset_id: str,
        dataset_file_meta_id: str,
        request: aiwork_space_20210204_models.GetDatasetFileMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetFileMetaResponse:
        """
        @summary Queries the metadata records of specific files in a dataset.
        
        @param request: GetDatasetFileMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetFileMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatasetFileMeta',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas/{OpenApiUtilClient.get_encode_param(dataset_file_meta_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_file_meta_with_options_async(
        self,
        dataset_id: str,
        dataset_file_meta_id: str,
        request: aiwork_space_20210204_models.GetDatasetFileMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetFileMetaResponse:
        """
        @summary Queries the metadata records of specific files in a dataset.
        
        @param request: GetDatasetFileMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetFileMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatasetFileMeta',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas/{OpenApiUtilClient.get_encode_param(dataset_file_meta_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_file_meta(
        self,
        dataset_id: str,
        dataset_file_meta_id: str,
        request: aiwork_space_20210204_models.GetDatasetFileMetaRequest,
    ) -> aiwork_space_20210204_models.GetDatasetFileMetaResponse:
        """
        @summary Queries the metadata records of specific files in a dataset.
        
        @param request: GetDatasetFileMetaRequest
        @return: GetDatasetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dataset_file_meta_with_options(dataset_id, dataset_file_meta_id, request, headers, runtime)

    async def get_dataset_file_meta_async(
        self,
        dataset_id: str,
        dataset_file_meta_id: str,
        request: aiwork_space_20210204_models.GetDatasetFileMetaRequest,
    ) -> aiwork_space_20210204_models.GetDatasetFileMetaResponse:
        """
        @summary Queries the metadata records of specific files in a dataset.
        
        @param request: GetDatasetFileMetaRequest
        @return: GetDatasetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dataset_file_meta_with_options_async(dataset_id, dataset_file_meta_id, request, headers, runtime)

    def get_dataset_file_metas_statistics_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.GetDatasetFileMetasStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetFileMetasStatisticsResponse:
        """
        @summary Obtains metadata statistics of a dataset.
        
        @param request: GetDatasetFileMetasStatisticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetFileMetasStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregate_by):
            query['AggregateBy'] = request.aggregate_by
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatasetFileMetasStatistics',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetFileMetasStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_file_metas_statistics_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.GetDatasetFileMetasStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetFileMetasStatisticsResponse:
        """
        @summary Obtains metadata statistics of a dataset.
        
        @param request: GetDatasetFileMetasStatisticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetFileMetasStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregate_by):
            query['AggregateBy'] = request.aggregate_by
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatasetFileMetasStatistics',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetFileMetasStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_file_metas_statistics(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.GetDatasetFileMetasStatisticsRequest,
    ) -> aiwork_space_20210204_models.GetDatasetFileMetasStatisticsResponse:
        """
        @summary Obtains metadata statistics of a dataset.
        
        @param request: GetDatasetFileMetasStatisticsRequest
        @return: GetDatasetFileMetasStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dataset_file_metas_statistics_with_options(dataset_id, request, headers, runtime)

    async def get_dataset_file_metas_statistics_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.GetDatasetFileMetasStatisticsRequest,
    ) -> aiwork_space_20210204_models.GetDatasetFileMetasStatisticsResponse:
        """
        @summary Obtains metadata statistics of a dataset.
        
        @param request: GetDatasetFileMetasStatisticsRequest
        @return: GetDatasetFileMetasStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dataset_file_metas_statistics_with_options_async(dataset_id, request, headers, runtime)

    def get_dataset_job_with_options(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.GetDatasetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetJobResponse:
        """
        @summary Obtains a dataset job.
        
        @param request: GetDatasetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs/{OpenApiUtilClient.get_encode_param(dataset_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_job_with_options_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.GetDatasetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetJobResponse:
        """
        @summary Obtains a dataset job.
        
        @param request: GetDatasetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs/{OpenApiUtilClient.get_encode_param(dataset_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_job(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.GetDatasetJobRequest,
    ) -> aiwork_space_20210204_models.GetDatasetJobResponse:
        """
        @summary Obtains a dataset job.
        
        @param request: GetDatasetJobRequest
        @return: GetDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dataset_job_with_options(dataset_id, dataset_job_id, request, headers, runtime)

    async def get_dataset_job_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.GetDatasetJobRequest,
    ) -> aiwork_space_20210204_models.GetDatasetJobResponse:
        """
        @summary Obtains a dataset job.
        
        @param request: GetDatasetJobRequest
        @return: GetDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dataset_job_with_options_async(dataset_id, dataset_job_id, request, headers, runtime)

    def get_dataset_job_config_with_options(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.GetDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetJobConfigResponse:
        """
        @summary Obtains a job configuration for a dataset.
        
        @param request: GetDatasetJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetJobConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatasetJobConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs/{OpenApiUtilClient.get_encode_param(dataset_job_config_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_job_config_with_options_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.GetDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetJobConfigResponse:
        """
        @summary Obtains a job configuration for a dataset.
        
        @param request: GetDatasetJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetJobConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatasetJobConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs/{OpenApiUtilClient.get_encode_param(dataset_job_config_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_job_config(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.GetDatasetJobConfigRequest,
    ) -> aiwork_space_20210204_models.GetDatasetJobConfigResponse:
        """
        @summary Obtains a job configuration for a dataset.
        
        @param request: GetDatasetJobConfigRequest
        @return: GetDatasetJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dataset_job_config_with_options(dataset_id, dataset_job_config_id, request, headers, runtime)

    async def get_dataset_job_config_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.GetDatasetJobConfigRequest,
    ) -> aiwork_space_20210204_models.GetDatasetJobConfigResponse:
        """
        @summary Obtains a job configuration for a dataset.
        
        @param request: GetDatasetJobConfigRequest
        @return: GetDatasetJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dataset_job_config_with_options_async(dataset_id, dataset_job_config_id, request, headers, runtime)

    def get_dataset_version_with_options(
        self,
        dataset_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetVersionResponse:
        """
        @summary Obtains the information about a specified version of a dataset.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasetVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_version_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDatasetVersionResponse:
        """
        @summary Obtains the information about a specified version of a dataset.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasetVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_version(
        self,
        dataset_id: str,
        version_name: str,
    ) -> aiwork_space_20210204_models.GetDatasetVersionResponse:
        """
        @summary Obtains the information about a specified version of a dataset.
        
        @return: GetDatasetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dataset_version_with_options(dataset_id, version_name, headers, runtime)

    async def get_dataset_version_async(
        self,
        dataset_id: str,
        version_name: str,
    ) -> aiwork_space_20210204_models.GetDatasetVersionResponse:
        """
        @summary Obtains the information about a specified version of a dataset.
        
        @return: GetDatasetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dataset_version_with_options_async(dataset_id, version_name, headers, runtime)

    def get_default_workspace_with_options(
        self,
        request: aiwork_space_20210204_models.GetDefaultWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDefaultWorkspaceResponse:
        """
        @summary Queries information about the default workspace.
        
        @param request: GetDefaultWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDefaultWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDefaultWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/defaultWorkspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDefaultWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_workspace_with_options_async(
        self,
        request: aiwork_space_20210204_models.GetDefaultWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetDefaultWorkspaceResponse:
        """
        @summary Queries information about the default workspace.
        
        @param request: GetDefaultWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDefaultWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDefaultWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/defaultWorkspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetDefaultWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_workspace(
        self,
        request: aiwork_space_20210204_models.GetDefaultWorkspaceRequest,
    ) -> aiwork_space_20210204_models.GetDefaultWorkspaceResponse:
        """
        @summary Queries information about the default workspace.
        
        @param request: GetDefaultWorkspaceRequest
        @return: GetDefaultWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_default_workspace_with_options(request, headers, runtime)

    async def get_default_workspace_async(
        self,
        request: aiwork_space_20210204_models.GetDefaultWorkspaceRequest,
    ) -> aiwork_space_20210204_models.GetDefaultWorkspaceResponse:
        """
        @summary Queries information about the default workspace.
        
        @param request: GetDefaultWorkspaceRequest
        @return: GetDefaultWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_default_workspace_with_options_async(request, headers, runtime)

    def get_experiment_with_options(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetExperimentResponse:
        """
        @summary Obtains an experiment.
        
        @param request: GetExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_with_options_async(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetExperimentResponse:
        """
        @summary Obtains an experiment.
        
        @param request: GetExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.GetExperimentRequest,
    ) -> aiwork_space_20210204_models.GetExperimentResponse:
        """
        @summary Obtains an experiment.
        
        @param request: GetExperimentRequest
        @return: GetExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(experiment_id, request, headers, runtime)

    async def get_experiment_async(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.GetExperimentRequest,
    ) -> aiwork_space_20210204_models.GetExperimentResponse:
        """
        @summary Obtains an experiment.
        
        @param request: GetExperimentRequest
        @return: GetExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_with_options_async(experiment_id, request, headers, runtime)

    def get_image_with_options(
        self,
        image_id: str,
        request: aiwork_space_20210204_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetImageResponse:
        """
        @summary Obtains the information about an image.
        
        @param request: GetImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        image_id: str,
        request: aiwork_space_20210204_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetImageResponse:
        """
        @summary Obtains the information about an image.
        
        @param request: GetImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        image_id: str,
        request: aiwork_space_20210204_models.GetImageRequest,
    ) -> aiwork_space_20210204_models.GetImageResponse:
        """
        @summary Obtains the information about an image.
        
        @param request: GetImageRequest
        @return: GetImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_with_options(image_id, request, headers, runtime)

    async def get_image_async(
        self,
        image_id: str,
        request: aiwork_space_20210204_models.GetImageRequest,
    ) -> aiwork_space_20210204_models.GetImageResponse:
        """
        @summary Obtains the information about an image.
        
        @param request: GetImageRequest
        @return: GetImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_image_with_options_async(image_id, request, headers, runtime)

    def get_member_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetMemberResponse:
        """
        @summary Obtains a member in a workspace.
        
        @param request: GetMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMember',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/member',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_member_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetMemberResponse:
        """
        @summary Obtains a member in a workspace.
        
        @param request: GetMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMember',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/member',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_member(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetMemberRequest,
    ) -> aiwork_space_20210204_models.GetMemberResponse:
        """
        @summary Obtains a member in a workspace.
        
        @param request: GetMemberRequest
        @return: GetMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_member_with_options(workspace_id, request, headers, runtime)

    async def get_member_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetMemberRequest,
    ) -> aiwork_space_20210204_models.GetMemberResponse:
        """
        @summary Obtains a member in a workspace.
        
        @param request: GetMemberRequest
        @return: GetMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_member_with_options_async(workspace_id, request, headers, runtime)

    def get_model_with_options(
        self,
        model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetModelResponse:
        """
        @summary Obtains the details of a specified model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_with_options_async(
        self,
        model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetModelResponse:
        """
        @summary Obtains the details of a specified model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model(
        self,
        model_id: str,
    ) -> aiwork_space_20210204_models.GetModelResponse:
        """
        @summary Obtains the details of a specified model.
        
        @return: GetModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_with_options(model_id, headers, runtime)

    async def get_model_async(
        self,
        model_id: str,
    ) -> aiwork_space_20210204_models.GetModelResponse:
        """
        @summary Obtains the details of a specified model.
        
        @return: GetModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_with_options_async(model_id, headers, runtime)

    def get_model_version_with_options(
        self,
        model_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetModelVersionResponse:
        """
        @summary Queries a model version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_version_with_options_async(
        self,
        model_id: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetModelVersionResponse:
        """
        @summary Queries a model version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_version(
        self,
        model_id: str,
        version_name: str,
    ) -> aiwork_space_20210204_models.GetModelVersionResponse:
        """
        @summary Queries a model version.
        
        @return: GetModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_version_with_options(model_id, version_name, headers, runtime)

    async def get_model_version_async(
        self,
        model_id: str,
        version_name: str,
    ) -> aiwork_space_20210204_models.GetModelVersionResponse:
        """
        @summary Queries a model version.
        
        @return: GetModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_version_with_options_async(model_id, version_name, headers, runtime)

    def get_permission_with_options(
        self,
        workspace_id: str,
        permission_code: str,
        tmp_req: aiwork_space_20210204_models.GetPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetPermissionResponse:
        """
        @summary Obtains permissions on a workspace.
        
        @param tmp_req: GetPermissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPermissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiwork_space_20210204_models.GetPermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPermission',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/permissions/{OpenApiUtilClient.get_encode_param(permission_code)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_permission_with_options_async(
        self,
        workspace_id: str,
        permission_code: str,
        tmp_req: aiwork_space_20210204_models.GetPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetPermissionResponse:
        """
        @summary Obtains permissions on a workspace.
        
        @param tmp_req: GetPermissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPermissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiwork_space_20210204_models.GetPermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPermission',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/permissions/{OpenApiUtilClient.get_encode_param(permission_code)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_permission(
        self,
        workspace_id: str,
        permission_code: str,
        request: aiwork_space_20210204_models.GetPermissionRequest,
    ) -> aiwork_space_20210204_models.GetPermissionResponse:
        """
        @summary Obtains permissions on a workspace.
        
        @param request: GetPermissionRequest
        @return: GetPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_permission_with_options(workspace_id, permission_code, request, headers, runtime)

    async def get_permission_async(
        self,
        workspace_id: str,
        permission_code: str,
        request: aiwork_space_20210204_models.GetPermissionRequest,
    ) -> aiwork_space_20210204_models.GetPermissionResponse:
        """
        @summary Obtains permissions on a workspace.
        
        @param request: GetPermissionRequest
        @return: GetPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_permission_with_options_async(workspace_id, permission_code, request, headers, runtime)

    def get_run_with_options(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetRunResponse:
        """
        @summary Queries the run information.
        
        @param request: GetRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRun',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_run_with_options_async(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetRunResponse:
        """
        @summary Queries the run information.
        
        @param request: GetRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRun',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_run(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.GetRunRequest,
    ) -> aiwork_space_20210204_models.GetRunResponse:
        """
        @summary Queries the run information.
        
        @param request: GetRunRequest
        @return: GetRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_run_with_options(run_id, request, headers, runtime)

    async def get_run_async(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.GetRunRequest,
    ) -> aiwork_space_20210204_models.GetRunResponse:
        """
        @summary Queries the run information.
        
        @param request: GetRunRequest
        @return: GetRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_run_with_options_async(run_id, request, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetWorkspaceResponse:
        """
        @summary Queries the details about a workspace.
        
        @param request: GetWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.GetWorkspaceResponse:
        """
        @summary Queries the details about a workspace.
        
        @param request: GetWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetWorkspaceRequest,
    ) -> aiwork_space_20210204_models.GetWorkspaceResponse:
        """
        @summary Queries the details about a workspace.
        
        @param request: GetWorkspaceRequest
        @return: GetWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, request, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.GetWorkspaceRequest,
    ) -> aiwork_space_20210204_models.GetWorkspaceResponse:
        """
        @summary Queries the details about a workspace.
        
        @param request: GetWorkspaceRequest
        @return: GetWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_id, request, headers, runtime)

    def list_code_sources_with_options(
        self,
        request: aiwork_space_20210204_models.ListCodeSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListCodeSourcesResponse:
        """
        @summary Lists code sources. Pagination, sorting, and filtering by condition are supported.
        
        @param request: ListCodeSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCodeSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCodeSources',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListCodeSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_code_sources_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListCodeSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListCodeSourcesResponse:
        """
        @summary Lists code sources. Pagination, sorting, and filtering by condition are supported.
        
        @param request: ListCodeSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCodeSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCodeSources',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListCodeSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_code_sources(
        self,
        request: aiwork_space_20210204_models.ListCodeSourcesRequest,
    ) -> aiwork_space_20210204_models.ListCodeSourcesResponse:
        """
        @summary Lists code sources. Pagination, sorting, and filtering by condition are supported.
        
        @param request: ListCodeSourcesRequest
        @return: ListCodeSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_code_sources_with_options(request, headers, runtime)

    async def list_code_sources_async(
        self,
        request: aiwork_space_20210204_models.ListCodeSourcesRequest,
    ) -> aiwork_space_20210204_models.ListCodeSourcesResponse:
        """
        @summary Lists code sources. Pagination, sorting, and filtering by condition are supported.
        
        @param request: ListCodeSourcesRequest
        @return: ListCodeSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_code_sources_with_options_async(request, headers, runtime)

    def list_configs_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListConfigsResponse:
        """
        @summary Obtains a list of workspace configurations.
        
        @param request: ListConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.config_keys):
            query['ConfigKeys'] = request.config_keys
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_configs_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListConfigsResponse:
        """
        @summary Obtains a list of workspace configurations.
        
        @param request: ListConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.config_keys):
            query['ConfigKeys'] = request.config_keys
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_configs(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListConfigsRequest,
    ) -> aiwork_space_20210204_models.ListConfigsResponse:
        """
        @summary Obtains a list of workspace configurations.
        
        @param request: ListConfigsRequest
        @return: ListConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_configs_with_options(workspace_id, request, headers, runtime)

    async def list_configs_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListConfigsRequest,
    ) -> aiwork_space_20210204_models.ListConfigsResponse:
        """
        @summary Obtains a list of workspace configurations.
        
        @param request: ListConfigsRequest
        @return: ListConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_configs_with_options_async(workspace_id, request, headers, runtime)

    def list_dataset_file_metas_with_options(
        self,
        dataset_id: str,
        tmp_req: aiwork_space_20210204_models.ListDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetFileMetasResponse:
        """
        @summary Queries a list of dataset files.
        
        @param tmp_req: ListDatasetFileMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetFileMetasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiwork_space_20210204_models.ListDatasetFileMetasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_file_type_include_any):
            request.query_file_type_include_any_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_file_type_include_any, 'QueryFileTypeIncludeAny', 'simple')
        if not UtilClient.is_unset(tmp_req.query_tags_exclude):
            request.query_tags_exclude_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_tags_exclude, 'QueryTagsExclude', 'simple')
        if not UtilClient.is_unset(tmp_req.query_tags_include_all):
            request.query_tags_include_all_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_tags_include_all, 'QueryTagsIncludeAll', 'simple')
        if not UtilClient.is_unset(tmp_req.query_tags_include_any):
            request.query_tags_include_any_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_tags_include_any, 'QueryTagsIncludeAny', 'simple')
        query = {}
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.end_file_update_time):
            query['EndFileUpdateTime'] = request.end_file_update_time
        if not UtilClient.is_unset(request.end_tag_update_time):
            query['EndTagUpdateTime'] = request.end_tag_update_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_file_dir):
            query['QueryFileDir'] = request.query_file_dir
        if not UtilClient.is_unset(request.query_file_name):
            query['QueryFileName'] = request.query_file_name
        if not UtilClient.is_unset(request.query_file_type_include_any_shrink):
            query['QueryFileTypeIncludeAny'] = request.query_file_type_include_any_shrink
        if not UtilClient.is_unset(request.query_image):
            query['QueryImage'] = request.query_image
        if not UtilClient.is_unset(request.query_tags_exclude_shrink):
            query['QueryTagsExclude'] = request.query_tags_exclude_shrink
        if not UtilClient.is_unset(request.query_tags_include_all_shrink):
            query['QueryTagsIncludeAll'] = request.query_tags_include_all_shrink
        if not UtilClient.is_unset(request.query_tags_include_any_shrink):
            query['QueryTagsIncludeAny'] = request.query_tags_include_any_shrink
        if not UtilClient.is_unset(request.query_text):
            query['QueryText'] = request.query_text
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_file_update_time):
            query['StartFileUpdateTime'] = request.start_file_update_time
        if not UtilClient.is_unset(request.start_tag_update_time):
            query['StartTagUpdateTime'] = request.start_tag_update_time
        if not UtilClient.is_unset(request.thumbnail_mode):
            query['ThumbnailMode'] = request.thumbnail_mode
        if not UtilClient.is_unset(request.top_k):
            query['TopK'] = request.top_k
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasetFileMetas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetFileMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_file_metas_with_options_async(
        self,
        dataset_id: str,
        tmp_req: aiwork_space_20210204_models.ListDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetFileMetasResponse:
        """
        @summary Queries a list of dataset files.
        
        @param tmp_req: ListDatasetFileMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetFileMetasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiwork_space_20210204_models.ListDatasetFileMetasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_file_type_include_any):
            request.query_file_type_include_any_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_file_type_include_any, 'QueryFileTypeIncludeAny', 'simple')
        if not UtilClient.is_unset(tmp_req.query_tags_exclude):
            request.query_tags_exclude_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_tags_exclude, 'QueryTagsExclude', 'simple')
        if not UtilClient.is_unset(tmp_req.query_tags_include_all):
            request.query_tags_include_all_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_tags_include_all, 'QueryTagsIncludeAll', 'simple')
        if not UtilClient.is_unset(tmp_req.query_tags_include_any):
            request.query_tags_include_any_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_tags_include_any, 'QueryTagsIncludeAny', 'simple')
        query = {}
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.end_file_update_time):
            query['EndFileUpdateTime'] = request.end_file_update_time
        if not UtilClient.is_unset(request.end_tag_update_time):
            query['EndTagUpdateTime'] = request.end_tag_update_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_file_dir):
            query['QueryFileDir'] = request.query_file_dir
        if not UtilClient.is_unset(request.query_file_name):
            query['QueryFileName'] = request.query_file_name
        if not UtilClient.is_unset(request.query_file_type_include_any_shrink):
            query['QueryFileTypeIncludeAny'] = request.query_file_type_include_any_shrink
        if not UtilClient.is_unset(request.query_image):
            query['QueryImage'] = request.query_image
        if not UtilClient.is_unset(request.query_tags_exclude_shrink):
            query['QueryTagsExclude'] = request.query_tags_exclude_shrink
        if not UtilClient.is_unset(request.query_tags_include_all_shrink):
            query['QueryTagsIncludeAll'] = request.query_tags_include_all_shrink
        if not UtilClient.is_unset(request.query_tags_include_any_shrink):
            query['QueryTagsIncludeAny'] = request.query_tags_include_any_shrink
        if not UtilClient.is_unset(request.query_text):
            query['QueryText'] = request.query_text
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.score_threshold):
            query['ScoreThreshold'] = request.score_threshold
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_file_update_time):
            query['StartFileUpdateTime'] = request.start_file_update_time
        if not UtilClient.is_unset(request.start_tag_update_time):
            query['StartTagUpdateTime'] = request.start_tag_update_time
        if not UtilClient.is_unset(request.thumbnail_mode):
            query['ThumbnailMode'] = request.thumbnail_mode
        if not UtilClient.is_unset(request.top_k):
            query['TopK'] = request.top_k
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasetFileMetas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetFileMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_file_metas(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetFileMetasRequest,
    ) -> aiwork_space_20210204_models.ListDatasetFileMetasResponse:
        """
        @summary Queries a list of dataset files.
        
        @param request: ListDatasetFileMetasRequest
        @return: ListDatasetFileMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dataset_file_metas_with_options(dataset_id, request, headers, runtime)

    async def list_dataset_file_metas_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetFileMetasRequest,
    ) -> aiwork_space_20210204_models.ListDatasetFileMetasResponse:
        """
        @summary Queries a list of dataset files.
        
        @param request: ListDatasetFileMetasRequest
        @return: ListDatasetFileMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dataset_file_metas_with_options_async(dataset_id, request, headers, runtime)

    def list_dataset_job_configs_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetJobConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetJobConfigsResponse:
        """
        @summary Queries the dataset job configurations at a time.
        
        @param request: ListDatasetJobConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetJobConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_type):
            query['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasetJobConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetJobConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_job_configs_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetJobConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetJobConfigsResponse:
        """
        @summary Queries the dataset job configurations at a time.
        
        @param request: ListDatasetJobConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetJobConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_type):
            query['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasetJobConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetJobConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_job_configs(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetJobConfigsRequest,
    ) -> aiwork_space_20210204_models.ListDatasetJobConfigsResponse:
        """
        @summary Queries the dataset job configurations at a time.
        
        @param request: ListDatasetJobConfigsRequest
        @return: ListDatasetJobConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dataset_job_configs_with_options(dataset_id, request, headers, runtime)

    async def list_dataset_job_configs_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetJobConfigsRequest,
    ) -> aiwork_space_20210204_models.ListDatasetJobConfigsResponse:
        """
        @summary Queries the dataset job configurations at a time.
        
        @param request: ListDatasetJobConfigsRequest
        @return: ListDatasetJobConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dataset_job_configs_with_options_async(dataset_id, request, headers, runtime)

    def list_dataset_jobs_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetJobsResponse:
        """
        @summary Lists jobs in a dataset.
        
        @param request: ListDatasetJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.job_action):
            query['JobAction'] = request.job_action
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasetJobs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_jobs_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetJobsResponse:
        """
        @summary Lists jobs in a dataset.
        
        @param request: ListDatasetJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_version):
            query['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.job_action):
            query['JobAction'] = request.job_action
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasetJobs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_jobs(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetJobsRequest,
    ) -> aiwork_space_20210204_models.ListDatasetJobsResponse:
        """
        @summary Lists jobs in a dataset.
        
        @param request: ListDatasetJobsRequest
        @return: ListDatasetJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dataset_jobs_with_options(dataset_id, request, headers, runtime)

    async def list_dataset_jobs_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetJobsRequest,
    ) -> aiwork_space_20210204_models.ListDatasetJobsResponse:
        """
        @summary Lists jobs in a dataset.
        
        @param request: ListDatasetJobsRequest
        @return: ListDatasetJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dataset_jobs_with_options_async(dataset_id, request, headers, runtime)

    def list_dataset_versions_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetVersionsResponse:
        """
        @summary Lists dataset versions.
        
        @param request: ListDatasetVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not UtilClient.is_unset(request.label_values):
            query['LabelValues'] = request.label_values
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_types):
            query['SourceTypes'] = request.source_types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasetVersions',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_versions_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetVersionsResponse:
        """
        @summary Lists dataset versions.
        
        @param request: ListDatasetVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not UtilClient.is_unset(request.label_values):
            query['LabelValues'] = request.label_values
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_types):
            query['SourceTypes'] = request.source_types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasetVersions',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_versions(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetVersionsRequest,
    ) -> aiwork_space_20210204_models.ListDatasetVersionsResponse:
        """
        @summary Lists dataset versions.
        
        @param request: ListDatasetVersionsRequest
        @return: ListDatasetVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dataset_versions_with_options(dataset_id, request, headers, runtime)

    async def list_dataset_versions_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.ListDatasetVersionsRequest,
    ) -> aiwork_space_20210204_models.ListDatasetVersionsResponse:
        """
        @summary Lists dataset versions.
        
        @param request: ListDatasetVersionsRequest
        @return: ListDatasetVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dataset_versions_with_options_async(dataset_id, request, headers, runtime)

    def list_datasets_with_options(
        self,
        request: aiwork_space_20210204_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetsResponse:
        """
        @summary Lists the datasets in a workspace.
        
        @param request: ListDatasetsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_types):
            query['DataSourceTypes'] = request.data_source_types
        if not UtilClient.is_unset(request.data_types):
            query['DataTypes'] = request.data_types
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_dataset_id):
            query['SourceDatasetId'] = request.source_dataset_id
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_types):
            query['SourceTypes'] = request.source_types
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListDatasetsResponse:
        """
        @summary Lists the datasets in a workspace.
        
        @param request: ListDatasetsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_types):
            query['DataSourceTypes'] = request.data_source_types
        if not UtilClient.is_unset(request.data_types):
            query['DataTypes'] = request.data_types
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_dataset_id):
            query['SourceDatasetId'] = request.source_dataset_id
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_types):
            query['SourceTypes'] = request.source_types
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        request: aiwork_space_20210204_models.ListDatasetsRequest,
    ) -> aiwork_space_20210204_models.ListDatasetsResponse:
        """
        @summary Lists the datasets in a workspace.
        
        @param request: ListDatasetsRequest
        @return: ListDatasetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_datasets_with_options(request, headers, runtime)

    async def list_datasets_async(
        self,
        request: aiwork_space_20210204_models.ListDatasetsRequest,
    ) -> aiwork_space_20210204_models.ListDatasetsResponse:
        """
        @summary Lists the datasets in a workspace.
        
        @param request: ListDatasetsRequest
        @return: ListDatasetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_datasets_with_options_async(request, headers, runtime)

    def list_experiment_with_options(
        self,
        tmp_req: aiwork_space_20210204_models.ListExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListExperimentResponse:
        """
        @summary Lists experiments.
        
        @param tmp_req: ListExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiwork_space_20210204_models.ListExperimentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.options, 'Options', 'json')
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.options_shrink):
            query['Options'] = request.options_shrink
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_token):
            query['PageToken'] = request.page_token
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiment_with_options_async(
        self,
        tmp_req: aiwork_space_20210204_models.ListExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListExperimentResponse:
        """
        @summary Lists experiments.
        
        @param tmp_req: ListExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiwork_space_20210204_models.ListExperimentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.options, 'Options', 'json')
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.options_shrink):
            query['Options'] = request.options_shrink
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_token):
            query['PageToken'] = request.page_token
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiment(
        self,
        request: aiwork_space_20210204_models.ListExperimentRequest,
    ) -> aiwork_space_20210204_models.ListExperimentResponse:
        """
        @summary Lists experiments.
        
        @param request: ListExperimentRequest
        @return: ListExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiment_with_options(request, headers, runtime)

    async def list_experiment_async(
        self,
        request: aiwork_space_20210204_models.ListExperimentRequest,
    ) -> aiwork_space_20210204_models.ListExperimentResponse:
        """
        @summary Lists experiments.
        
        @param request: ListExperimentRequest
        @return: ListExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiment_with_options_async(request, headers, runtime)

    def list_image_labels_with_options(
        self,
        request: aiwork_space_20210204_models.ListImageLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListImageLabelsResponse:
        """
        @summary Lists all tags of an image.
        
        @param request: ListImageLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImageLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.label_filter):
            query['LabelFilter'] = request.label_filter
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImageLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/image/labels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_image_labels_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListImageLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListImageLabelsResponse:
        """
        @summary Lists all tags of an image.
        
        @param request: ListImageLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImageLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.label_filter):
            query['LabelFilter'] = request.label_filter
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImageLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/image/labels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListImageLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_image_labels(
        self,
        request: aiwork_space_20210204_models.ListImageLabelsRequest,
    ) -> aiwork_space_20210204_models.ListImageLabelsResponse:
        """
        @summary Lists all tags of an image.
        
        @param request: ListImageLabelsRequest
        @return: ListImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_image_labels_with_options(request, headers, runtime)

    async def list_image_labels_async(
        self,
        request: aiwork_space_20210204_models.ListImageLabelsRequest,
    ) -> aiwork_space_20210204_models.ListImageLabelsResponse:
        """
        @summary Lists all tags of an image.
        
        @param request: ListImageLabelsRequest
        @return: ListImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_image_labels_with_options_async(request, headers, runtime)

    def list_images_with_options(
        self,
        request: aiwork_space_20210204_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListImagesResponse:
        """
        @summary Queries a list of images.
        
        @param request: ListImagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListImagesResponse:
        """
        @summary Queries a list of images.
        
        @param request: ListImagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: aiwork_space_20210204_models.ListImagesRequest,
    ) -> aiwork_space_20210204_models.ListImagesResponse:
        """
        @summary Queries a list of images.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    async def list_images_async(
        self,
        request: aiwork_space_20210204_models.ListImagesRequest,
    ) -> aiwork_space_20210204_models.ListImagesResponse:
        """
        @summary Queries a list of images.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_images_with_options_async(request, headers, runtime)

    def list_members_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListMembersResponse:
        """
        @summary Obtains the members in a workspace.
        
        @param request: ListMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_name):
            query['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.roles):
            query['Roles'] = request.roles
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMembers',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_members_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListMembersResponse:
        """
        @summary Obtains the members in a workspace.
        
        @param request: ListMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_name):
            query['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.roles):
            query['Roles'] = request.roles
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMembers',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_members(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListMembersRequest,
    ) -> aiwork_space_20210204_models.ListMembersResponse:
        """
        @summary Obtains the members in a workspace.
        
        @param request: ListMembersRequest
        @return: ListMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_members_with_options(workspace_id, request, headers, runtime)

    async def list_members_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListMembersRequest,
    ) -> aiwork_space_20210204_models.ListMembersResponse:
        """
        @summary Obtains the members in a workspace.
        
        @param request: ListMembersRequest
        @return: ListMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_members_with_options_async(workspace_id, request, headers, runtime)

    def list_model_versions_with_options(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.ListModelVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListModelVersionsResponse:
        """
        @summary Queries a list of model versions.
        
        @param request: ListModelVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approval_status):
            query['ApprovalStatus'] = request.approval_status
        if not UtilClient.is_unset(request.format_type):
            query['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.framework_type):
            query['FrameworkType'] = request.framework_type
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelVersions',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListModelVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_versions_with_options_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.ListModelVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListModelVersionsResponse:
        """
        @summary Queries a list of model versions.
        
        @param request: ListModelVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approval_status):
            query['ApprovalStatus'] = request.approval_status
        if not UtilClient.is_unset(request.format_type):
            query['FormatType'] = request.format_type
        if not UtilClient.is_unset(request.framework_type):
            query['FrameworkType'] = request.framework_type
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelVersions',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListModelVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_versions(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.ListModelVersionsRequest,
    ) -> aiwork_space_20210204_models.ListModelVersionsResponse:
        """
        @summary Queries a list of model versions.
        
        @param request: ListModelVersionsRequest
        @return: ListModelVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_model_versions_with_options(model_id, request, headers, runtime)

    async def list_model_versions_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.ListModelVersionsRequest,
    ) -> aiwork_space_20210204_models.ListModelVersionsResponse:
        """
        @summary Queries a list of model versions.
        
        @param request: ListModelVersionsRequest
        @return: ListModelVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_model_versions_with_options_async(model_id, request, headers, runtime)

    def list_models_with_options(
        self,
        tmp_req: aiwork_space_20210204_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListModelsResponse:
        """
        @summary Queries a list of models.
        
        @param tmp_req: ListModelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiwork_space_20210204_models.ListModelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.collections):
            query['Collections'] = request.collections
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.task):
            query['Task'] = request.task
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_models_with_options_async(
        self,
        tmp_req: aiwork_space_20210204_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListModelsResponse:
        """
        @summary Queries a list of models.
        
        @param tmp_req: ListModelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aiwork_space_20210204_models.ListModelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.collections):
            query['Collections'] = request.collections
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.task):
            query['Task'] = request.task
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_models(
        self,
        request: aiwork_space_20210204_models.ListModelsRequest,
    ) -> aiwork_space_20210204_models.ListModelsResponse:
        """
        @summary Queries a list of models.
        
        @param request: ListModelsRequest
        @return: ListModelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_models_with_options(request, headers, runtime)

    async def list_models_async(
        self,
        request: aiwork_space_20210204_models.ListModelsRequest,
    ) -> aiwork_space_20210204_models.ListModelsResponse:
        """
        @summary Queries a list of models.
        
        @param request: ListModelsRequest
        @return: ListModelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_models_with_options_async(request, headers, runtime)

    def list_permissions_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListPermissionsResponse:
        """
        @summary Lists the permissions that a user has in a workspace.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPermissions',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/permissions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permissions_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListPermissionsResponse:
        """
        @summary Lists the permissions that a user has in a workspace.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPermissions',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/permissions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permissions(
        self,
        workspace_id: str,
    ) -> aiwork_space_20210204_models.ListPermissionsResponse:
        """
        @summary Lists the permissions that a user has in a workspace.
        
        @return: ListPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_permissions_with_options(workspace_id, headers, runtime)

    async def list_permissions_async(
        self,
        workspace_id: str,
    ) -> aiwork_space_20210204_models.ListPermissionsResponse:
        """
        @summary Lists the permissions that a user has in a workspace.
        
        @return: ListPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_permissions_with_options_async(workspace_id, headers, runtime)

    def list_products_with_options(
        self,
        request: aiwork_space_20210204_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListProductsResponse:
        """
        @summary 列举产品
        
        @param request: ListProductsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_codes):
            query['ProductCodes'] = request.product_codes
        if not UtilClient.is_unset(request.service_codes):
            query['ServiceCodes'] = request.service_codes
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListProductsResponse:
        """
        @summary 列举产品
        
        @param request: ListProductsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_codes):
            query['ProductCodes'] = request.product_codes
        if not UtilClient.is_unset(request.service_codes):
            query['ServiceCodes'] = request.service_codes
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        request: aiwork_space_20210204_models.ListProductsRequest,
    ) -> aiwork_space_20210204_models.ListProductsResponse:
        """
        @summary 列举产品
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_products_with_options(request, headers, runtime)

    async def list_products_async(
        self,
        request: aiwork_space_20210204_models.ListProductsRequest,
    ) -> aiwork_space_20210204_models.ListProductsResponse:
        """
        @summary 列举产品
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_products_with_options_async(request, headers, runtime)

    def list_quotas_with_options(
        self,
        request: aiwork_space_20210204_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListQuotasResponse:
        """
        @summary Obtains the list of quotas.
        
        @param request: ListQuotasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListQuotasResponse:
        """
        @summary Obtains the list of quotas.
        
        @param request: ListQuotasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas(
        self,
        request: aiwork_space_20210204_models.ListQuotasRequest,
    ) -> aiwork_space_20210204_models.ListQuotasResponse:
        """
        @summary Obtains the list of quotas.
        
        @param request: ListQuotasRequest
        @return: ListQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    async def list_quotas_async(
        self,
        request: aiwork_space_20210204_models.ListQuotasRequest,
    ) -> aiwork_space_20210204_models.ListQuotasResponse:
        """
        @summary Obtains the list of quotas.
        
        @param request: ListQuotasRequest
        @return: ListQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_quotas_with_options_async(request, headers, runtime)

    def list_resources_with_options(
        self,
        request: aiwork_space_20210204_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListResourcesResponse:
        """
        @summary Queries the resources that are associated with a workspace.
        
        @param request: ListResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_types):
            query['ProductTypes'] = request.product_types
        if not UtilClient.is_unset(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.verbose_fields):
            query['VerboseFields'] = request.verbose_fields
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListResourcesResponse:
        """
        @summary Queries the resources that are associated with a workspace.
        
        @param request: ListResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_types):
            query['ProductTypes'] = request.product_types
        if not UtilClient.is_unset(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.verbose_fields):
            query['VerboseFields'] = request.verbose_fields
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: aiwork_space_20210204_models.ListResourcesRequest,
    ) -> aiwork_space_20210204_models.ListResourcesResponse:
        """
        @summary Queries the resources that are associated with a workspace.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    async def list_resources_async(
        self,
        request: aiwork_space_20210204_models.ListResourcesRequest,
    ) -> aiwork_space_20210204_models.ListResourcesResponse:
        """
        @summary Queries the resources that are associated with a workspace.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(request, headers, runtime)

    def list_run_metrics_with_options(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.ListRunMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListRunMetricsResponse:
        """
        @summary Lists the metrics for a run.
        
        @param request: ListRunMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRunMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['PageToken'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRunMetrics',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListRunMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_run_metrics_with_options_async(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.ListRunMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListRunMetricsResponse:
        """
        @summary Lists the metrics for a run.
        
        @param request: ListRunMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRunMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['PageToken'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRunMetrics',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListRunMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_run_metrics(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.ListRunMetricsRequest,
    ) -> aiwork_space_20210204_models.ListRunMetricsResponse:
        """
        @summary Lists the metrics for a run.
        
        @param request: ListRunMetricsRequest
        @return: ListRunMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_run_metrics_with_options(run_id, request, headers, runtime)

    async def list_run_metrics_async(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.ListRunMetricsRequest,
    ) -> aiwork_space_20210204_models.ListRunMetricsResponse:
        """
        @summary Lists the metrics for a run.
        
        @param request: ListRunMetricsRequest
        @return: ListRunMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_run_metrics_with_options_async(run_id, request, headers, runtime)

    def list_runs_with_options(
        self,
        request: aiwork_space_20210204_models.ListRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListRunsResponse:
        """
        @summary Queries a list of runs.
        
        @param request: ListRunsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRunsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.gmt_create_time):
            query['GmtCreateTime'] = request.gmt_create_time
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_token):
            query['PageToken'] = request.page_token
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuns',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_runs_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListRunsResponse:
        """
        @summary Queries a list of runs.
        
        @param request: ListRunsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRunsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.gmt_create_time):
            query['GmtCreateTime'] = request.gmt_create_time
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_token):
            query['PageToken'] = request.page_token
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuns',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_runs(
        self,
        request: aiwork_space_20210204_models.ListRunsRequest,
    ) -> aiwork_space_20210204_models.ListRunsResponse:
        """
        @summary Queries a list of runs.
        
        @param request: ListRunsRequest
        @return: ListRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_runs_with_options(request, headers, runtime)

    async def list_runs_async(
        self,
        request: aiwork_space_20210204_models.ListRunsRequest,
    ) -> aiwork_space_20210204_models.ListRunsResponse:
        """
        @summary Queries a list of runs.
        
        @param request: ListRunsRequest
        @return: ListRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_runs_with_options_async(request, headers, runtime)

    def list_user_configs_with_options(
        self,
        request: aiwork_space_20210204_models.ListUserConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListUserConfigsResponse:
        """
        @summary Queries user information.
        
        @param request: ListUserConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_names):
            query['CategoryNames'] = request.category_names
        if not UtilClient.is_unset(request.config_keys):
            query['ConfigKeys'] = request.config_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/userconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_configs_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListUserConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListUserConfigsResponse:
        """
        @summary Queries user information.
        
        @param request: ListUserConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_names):
            query['CategoryNames'] = request.category_names
        if not UtilClient.is_unset(request.config_keys):
            query['ConfigKeys'] = request.config_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/userconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_configs(
        self,
        request: aiwork_space_20210204_models.ListUserConfigsRequest,
    ) -> aiwork_space_20210204_models.ListUserConfigsResponse:
        """
        @summary Queries user information.
        
        @param request: ListUserConfigsRequest
        @return: ListUserConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_configs_with_options(request, headers, runtime)

    async def list_user_configs_async(
        self,
        request: aiwork_space_20210204_models.ListUserConfigsRequest,
    ) -> aiwork_space_20210204_models.ListUserConfigsResponse:
        """
        @summary Queries user information.
        
        @param request: ListUserConfigsRequest
        @return: ListUserConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_configs_with_options_async(request, headers, runtime)

    def list_workspace_users_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListWorkspaceUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListWorkspaceUsersResponse:
        """
        @summary Lists the users who do not belong to a workspace. These users can be added to the workspace as members.
        
        @param request: ListWorkspaceUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceUsers',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListWorkspaceUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_users_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListWorkspaceUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListWorkspaceUsersResponse:
        """
        @summary Lists the users who do not belong to a workspace. These users can be added to the workspace as members.
        
        @param request: ListWorkspaceUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceUsers',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListWorkspaceUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_users(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListWorkspaceUsersRequest,
    ) -> aiwork_space_20210204_models.ListWorkspaceUsersResponse:
        """
        @summary Lists the users who do not belong to a workspace. These users can be added to the workspace as members.
        
        @param request: ListWorkspaceUsersRequest
        @return: ListWorkspaceUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspace_users_with_options(workspace_id, request, headers, runtime)

    async def list_workspace_users_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.ListWorkspaceUsersRequest,
    ) -> aiwork_space_20210204_models.ListWorkspaceUsersResponse:
        """
        @summary Lists the users who do not belong to a workspace. These users can be added to the workspace as members.
        
        @param request: ListWorkspaceUsersRequest
        @return: ListWorkspaceUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspace_users_with_options_async(workspace_id, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        request: aiwork_space_20210204_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListWorkspacesResponse:
        """
        @summary Lists all workspaces in a region.
        
        @description You can use the option parameter to specify query options, so as to obtain different information about the workspaces.
        
        @param request: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not UtilClient.is_unset(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        request: aiwork_space_20210204_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.ListWorkspacesResponse:
        """
        @summary Lists all workspaces in a region.
        
        @description You can use the option parameter to specify query options, so as to obtain different information about the workspaces.
        
        @param request: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not UtilClient.is_unset(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: aiwork_space_20210204_models.ListWorkspacesRequest,
    ) -> aiwork_space_20210204_models.ListWorkspacesResponse:
        """
        @summary Lists all workspaces in a region.
        
        @description You can use the option parameter to specify query options, so as to obtain different information about the workspaces.
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: aiwork_space_20210204_models.ListWorkspacesRequest,
    ) -> aiwork_space_20210204_models.ListWorkspacesResponse:
        """
        @summary Lists all workspaces in a region.
        
        @description You can use the option parameter to specify query options, so as to obtain different information about the workspaces.
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def log_run_metrics_with_options(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.LogRunMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.LogRunMetricsResponse:
        """
        @summary Logs multiple metrics for a run at a time.
        
        @param request: LogRunMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LogRunMetricsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LogRunMetrics',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}/metrics/action/log',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.LogRunMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_run_metrics_with_options_async(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.LogRunMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.LogRunMetricsResponse:
        """
        @summary Logs multiple metrics for a run at a time.
        
        @param request: LogRunMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LogRunMetricsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LogRunMetrics',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}/metrics/action/log',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.LogRunMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_run_metrics(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.LogRunMetricsRequest,
    ) -> aiwork_space_20210204_models.LogRunMetricsResponse:
        """
        @summary Logs multiple metrics for a run at a time.
        
        @param request: LogRunMetricsRequest
        @return: LogRunMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_run_metrics_with_options(run_id, request, headers, runtime)

    async def log_run_metrics_async(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.LogRunMetricsRequest,
    ) -> aiwork_space_20210204_models.LogRunMetricsResponse:
        """
        @summary Logs multiple metrics for a run at a time.
        
        @param request: LogRunMetricsRequest
        @return: LogRunMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_run_metrics_with_options_async(run_id, request, headers, runtime)

    def publish_code_source_with_options(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.PublishCodeSourceResponse:
        """
        @summary Publishes a private code source to a workspace to make the code source publicly accessible.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishCodeSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{OpenApiUtilClient.get_encode_param(code_source_id)}/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.PublishCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.PublishCodeSourceResponse:
        """
        @summary Publishes a private code source to a workspace to make the code source publicly accessible.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishCodeSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{OpenApiUtilClient.get_encode_param(code_source_id)}/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.PublishCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_code_source(
        self,
        code_source_id: str,
    ) -> aiwork_space_20210204_models.PublishCodeSourceResponse:
        """
        @summary Publishes a private code source to a workspace to make the code source publicly accessible.
        
        @return: PublishCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_code_source_with_options(code_source_id, headers, runtime)

    async def publish_code_source_async(
        self,
        code_source_id: str,
    ) -> aiwork_space_20210204_models.PublishCodeSourceResponse:
        """
        @summary Publishes a private code source to a workspace to make the code source publicly accessible.
        
        @return: PublishCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_code_source_with_options_async(code_source_id, headers, runtime)

    def publish_dataset_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.PublishDatasetResponse:
        """
        @summary Publishes a private dataset in a workspace.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishDatasetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.PublishDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_dataset_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.PublishDatasetResponse:
        """
        @summary Publishes a private dataset in a workspace.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishDatasetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.PublishDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_dataset(
        self,
        dataset_id: str,
    ) -> aiwork_space_20210204_models.PublishDatasetResponse:
        """
        @summary Publishes a private dataset in a workspace.
        
        @return: PublishDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_dataset_with_options(dataset_id, headers, runtime)

    async def publish_dataset_async(
        self,
        dataset_id: str,
    ) -> aiwork_space_20210204_models.PublishDatasetResponse:
        """
        @summary Publishes a private dataset in a workspace.
        
        @return: PublishDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_dataset_with_options_async(dataset_id, headers, runtime)

    def publish_image_with_options(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.PublishImageResponse:
        """
        @summary Publishes an image. After the image is published, the visibility of the image is changed from PRIVATE to PUBLIC.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishImageResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishImage',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.PublishImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_image_with_options_async(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.PublishImageResponse:
        """
        @summary Publishes an image. After the image is published, the visibility of the image is changed from PRIVATE to PUBLIC.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishImageResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishImage',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.PublishImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_image(
        self,
        image_id: str,
    ) -> aiwork_space_20210204_models.PublishImageResponse:
        """
        @summary Publishes an image. After the image is published, the visibility of the image is changed from PRIVATE to PUBLIC.
        
        @return: PublishImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_image_with_options(image_id, headers, runtime)

    async def publish_image_async(
        self,
        image_id: str,
    ) -> aiwork_space_20210204_models.PublishImageResponse:
        """
        @summary Publishes an image. After the image is published, the visibility of the image is changed from PRIVATE to PUBLIC.
        
        @return: PublishImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_image_with_options_async(image_id, headers, runtime)

    def remove_image_with_options(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.RemoveImageResponse:
        """
        @summary Removes an image.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveImage',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.RemoveImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_image_with_options_async(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.RemoveImageResponse:
        """
        @summary Removes an image.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveImage',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.RemoveImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_image(
        self,
        image_id: str,
    ) -> aiwork_space_20210204_models.RemoveImageResponse:
        """
        @summary Removes an image.
        
        @return: RemoveImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_image_with_options(image_id, headers, runtime)

    async def remove_image_async(
        self,
        image_id: str,
    ) -> aiwork_space_20210204_models.RemoveImageResponse:
        """
        @summary Removes an image.
        
        @return: RemoveImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_image_with_options_async(image_id, headers, runtime)

    def remove_image_labels_with_options(
        self,
        image_id: str,
        label_key: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.RemoveImageLabelsResponse:
        """
        @summary Removes an image tag.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageLabelsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveImageLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}/labels/{OpenApiUtilClient.get_encode_param(label_key)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.RemoveImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_image_labels_with_options_async(
        self,
        image_id: str,
        label_key: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.RemoveImageLabelsResponse:
        """
        @summary Removes an image tag.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageLabelsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveImageLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/images/{OpenApiUtilClient.get_encode_param(image_id)}/labels/{OpenApiUtilClient.get_encode_param(label_key)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.RemoveImageLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_image_labels(
        self,
        image_id: str,
        label_key: str,
    ) -> aiwork_space_20210204_models.RemoveImageLabelsResponse:
        """
        @summary Removes an image tag.
        
        @return: RemoveImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_image_labels_with_options(image_id, label_key, headers, runtime)

    async def remove_image_labels_async(
        self,
        image_id: str,
        label_key: str,
    ) -> aiwork_space_20210204_models.RemoveImageLabelsResponse:
        """
        @summary Removes an image tag.
        
        @return: RemoveImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_image_labels_with_options_async(image_id, label_key, headers, runtime)

    def remove_member_role_with_options(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.RemoveMemberRoleResponse:
        """
        @summary Removes a member role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveMemberRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveMemberRole',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members/{OpenApiUtilClient.get_encode_param(member_id)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.RemoveMemberRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_member_role_with_options_async(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.RemoveMemberRoleResponse:
        """
        @summary Removes a member role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveMemberRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveMemberRole',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/members/{OpenApiUtilClient.get_encode_param(member_id)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.RemoveMemberRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_member_role(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
    ) -> aiwork_space_20210204_models.RemoveMemberRoleResponse:
        """
        @summary Removes a member role.
        
        @return: RemoveMemberRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_member_role_with_options(workspace_id, member_id, role_name, headers, runtime)

    async def remove_member_role_async(
        self,
        workspace_id: str,
        member_id: str,
        role_name: str,
    ) -> aiwork_space_20210204_models.RemoveMemberRoleResponse:
        """
        @summary Removes a member role.
        
        @return: RemoveMemberRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_member_role_with_options_async(workspace_id, member_id, role_name, headers, runtime)

    def set_experiment_labels_with_options(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.SetExperimentLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.SetExperimentLabelsResponse:
        """
        @summary Updates a experiment tag.
        
        @param request: SetExperimentLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetExperimentLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetExperimentLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.SetExperimentLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_experiment_labels_with_options_async(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.SetExperimentLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.SetExperimentLabelsResponse:
        """
        @summary Updates a experiment tag.
        
        @param request: SetExperimentLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetExperimentLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetExperimentLabels',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.SetExperimentLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_experiment_labels(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.SetExperimentLabelsRequest,
    ) -> aiwork_space_20210204_models.SetExperimentLabelsResponse:
        """
        @summary Updates a experiment tag.
        
        @param request: SetExperimentLabelsRequest
        @return: SetExperimentLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_experiment_labels_with_options(experiment_id, request, headers, runtime)

    async def set_experiment_labels_async(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.SetExperimentLabelsRequest,
    ) -> aiwork_space_20210204_models.SetExperimentLabelsResponse:
        """
        @summary Updates a experiment tag.
        
        @param request: SetExperimentLabelsRequest
        @return: SetExperimentLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_experiment_labels_with_options_async(experiment_id, request, headers, runtime)

    def set_user_configs_with_options(
        self,
        request: aiwork_space_20210204_models.SetUserConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.SetUserConfigsResponse:
        """
        @summary Updates the user configurations.
        
        @param request: SetUserConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserConfigsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.configs):
            body['Configs'] = request.configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/userconfigs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.SetUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_configs_with_options_async(
        self,
        request: aiwork_space_20210204_models.SetUserConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.SetUserConfigsResponse:
        """
        @summary Updates the user configurations.
        
        @param request: SetUserConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserConfigsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.configs):
            body['Configs'] = request.configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/userconfigs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.SetUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_configs(
        self,
        request: aiwork_space_20210204_models.SetUserConfigsRequest,
    ) -> aiwork_space_20210204_models.SetUserConfigsResponse:
        """
        @summary Updates the user configurations.
        
        @param request: SetUserConfigsRequest
        @return: SetUserConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_user_configs_with_options(request, headers, runtime)

    async def set_user_configs_async(
        self,
        request: aiwork_space_20210204_models.SetUserConfigsRequest,
    ) -> aiwork_space_20210204_models.SetUserConfigsResponse:
        """
        @summary Updates the user configurations.
        
        @param request: SetUserConfigsRequest
        @return: SetUserConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_user_configs_with_options_async(request, headers, runtime)

    def stop_dataset_job_with_options(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.StopDatasetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.StopDatasetJobResponse:
        """
        @summary Stops a dataset job.
        
        @param request: StopDatasetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDatasetJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs/{OpenApiUtilClient.get_encode_param(dataset_job_id)}/action/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.StopDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dataset_job_with_options_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.StopDatasetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.StopDatasetJobResponse:
        """
        @summary Stops a dataset job.
        
        @param request: StopDatasetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDatasetJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs/{OpenApiUtilClient.get_encode_param(dataset_job_id)}/action/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.StopDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dataset_job(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.StopDatasetJobRequest,
    ) -> aiwork_space_20210204_models.StopDatasetJobResponse:
        """
        @summary Stops a dataset job.
        
        @param request: StopDatasetJobRequest
        @return: StopDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_dataset_job_with_options(dataset_id, dataset_job_id, request, headers, runtime)

    async def stop_dataset_job_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.StopDatasetJobRequest,
    ) -> aiwork_space_20210204_models.StopDatasetJobResponse:
        """
        @summary Stops a dataset job.
        
        @param request: StopDatasetJobRequest
        @return: StopDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_dataset_job_with_options_async(dataset_id, dataset_job_id, request, headers, runtime)

    def update_code_source_with_options(
        self,
        code_source_id: str,
        request: aiwork_space_20210204_models.UpdateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateCodeSourceResponse:
        """
        @summary Updates a code build.
        
        @param request: UpdateCodeSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCodeSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.code_commit):
            body['CodeCommit'] = request.code_commit
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not UtilClient.is_unset(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{OpenApiUtilClient.get_encode_param(code_source_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_code_source_with_options_async(
        self,
        code_source_id: str,
        request: aiwork_space_20210204_models.UpdateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateCodeSourceResponse:
        """
        @summary Updates a code build.
        
        @param request: UpdateCodeSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCodeSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.code_commit):
            body['CodeCommit'] = request.code_commit
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not UtilClient.is_unset(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCodeSource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{OpenApiUtilClient.get_encode_param(code_source_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_code_source(
        self,
        code_source_id: str,
        request: aiwork_space_20210204_models.UpdateCodeSourceRequest,
    ) -> aiwork_space_20210204_models.UpdateCodeSourceResponse:
        """
        @summary Updates a code build.
        
        @param request: UpdateCodeSourceRequest
        @return: UpdateCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_code_source_with_options(code_source_id, request, headers, runtime)

    async def update_code_source_async(
        self,
        code_source_id: str,
        request: aiwork_space_20210204_models.UpdateCodeSourceRequest,
    ) -> aiwork_space_20210204_models.UpdateCodeSourceResponse:
        """
        @summary Updates a code build.
        
        @param request: UpdateCodeSourceRequest
        @return: UpdateCodeSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_code_source_with_options_async(code_source_id, request, headers, runtime)

    def update_config_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateConfigResponse:
        """
        @summary Updates or adds a workspace configuration item.
        
        @param request: UpdateConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_name):
            body['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.config_key):
            body['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.config_value):
            body['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateConfigResponse:
        """
        @summary Updates or adds a workspace configuration item.
        
        @param request: UpdateConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_name):
            body['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.config_key):
            body['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.config_value):
            body['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateConfigRequest,
    ) -> aiwork_space_20210204_models.UpdateConfigResponse:
        """
        @summary Updates or adds a workspace configuration item.
        
        @param request: UpdateConfigRequest
        @return: UpdateConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_config_with_options(workspace_id, request, headers, runtime)

    async def update_config_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateConfigRequest,
    ) -> aiwork_space_20210204_models.UpdateConfigResponse:
        """
        @summary Updates or adds a workspace configuration item.
        
        @param request: UpdateConfigRequest
        @return: UpdateConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_config_with_options_async(workspace_id, request, headers, runtime)

    def update_configs_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateConfigsResponse:
        """
        @summary Updates or adds workspace configurations in batches.
        
        @param request: UpdateConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.configs):
            body['Configs'] = request.configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/configs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_configs_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateConfigsResponse:
        """
        @summary Updates or adds workspace configurations in batches.
        
        @param request: UpdateConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.configs):
            body['Configs'] = request.configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigs',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/configs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_configs(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateConfigsRequest,
    ) -> aiwork_space_20210204_models.UpdateConfigsResponse:
        """
        @summary Updates or adds workspace configurations in batches.
        
        @param request: UpdateConfigsRequest
        @return: UpdateConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_configs_with_options(workspace_id, request, headers, runtime)

    async def update_configs_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateConfigsRequest,
    ) -> aiwork_space_20210204_models.UpdateConfigsResponse:
        """
        @summary Updates or adds workspace configurations in batches.
        
        @param request: UpdateConfigsRequest
        @return: UpdateConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_configs_with_options_async(workspace_id, request, headers, runtime)

    def update_dataset_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetResponse:
        """
        @summary Updates the name, description, and other information about a dataset.
        
        @param request: UpdateDatasetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.mount_access_read_write_role_id_list):
            body['MountAccessReadWriteRoleIdList'] = request.mount_access_read_write_role_id_list
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetResponse:
        """
        @summary Updates the name, description, and other information about a dataset.
        
        @param request: UpdateDatasetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.mount_access_read_write_role_id_list):
            body['MountAccessReadWriteRoleIdList'] = request.mount_access_read_write_role_id_list
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetResponse:
        """
        @summary Updates the name, description, and other information about a dataset.
        
        @param request: UpdateDatasetRequest
        @return: UpdateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dataset_with_options(dataset_id, request, headers, runtime)

    async def update_dataset_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetResponse:
        """
        @summary Updates the name, description, and other information about a dataset.
        
        @param request: UpdateDatasetRequest
        @return: UpdateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_dataset_with_options_async(dataset_id, request, headers, runtime)

    def update_dataset_file_metas_with_options(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetFileMetasResponse:
        """
        @summary Updates the metadata records of multiple files in a dataset at a time.
        
        @param request: UpdateDatasetFileMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetFileMetasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_file_metas):
            body['DatasetFileMetas'] = request.dataset_file_metas
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.tag_job_id):
            body['TagJobId'] = request.tag_job_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetFileMetas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetFileMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_file_metas_with_options_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetFileMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetFileMetasResponse:
        """
        @summary Updates the metadata records of multiple files in a dataset at a time.
        
        @param request: UpdateDatasetFileMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetFileMetasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_file_metas):
            body['DatasetFileMetas'] = request.dataset_file_metas
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.tag_job_id):
            body['TagJobId'] = request.tag_job_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetFileMetas',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetfilemetas',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetFileMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_file_metas(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetFileMetasRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetFileMetasResponse:
        """
        @summary Updates the metadata records of multiple files in a dataset at a time.
        
        @param request: UpdateDatasetFileMetasRequest
        @return: UpdateDatasetFileMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dataset_file_metas_with_options(dataset_id, request, headers, runtime)

    async def update_dataset_file_metas_async(
        self,
        dataset_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetFileMetasRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetFileMetasResponse:
        """
        @summary Updates the metadata records of multiple files in a dataset at a time.
        
        @param request: UpdateDatasetFileMetasRequest
        @return: UpdateDatasetFileMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_dataset_file_metas_with_options_async(dataset_id, request, headers, runtime)

    def update_dataset_job_with_options(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetJobResponse:
        """
        @summary Updates a dataset job.
        
        @param request: UpdateDatasetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs/{OpenApiUtilClient.get_encode_param(dataset_job_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_job_with_options_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetJobResponse:
        """
        @summary Updates a dataset job.
        
        @param request: UpdateDatasetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_version):
            body['DatasetVersion'] = request.dataset_version
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetJob',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobs/{OpenApiUtilClient.get_encode_param(dataset_job_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_job(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetJobRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetJobResponse:
        """
        @summary Updates a dataset job.
        
        @param request: UpdateDatasetJobRequest
        @return: UpdateDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dataset_job_with_options(dataset_id, dataset_job_id, request, headers, runtime)

    async def update_dataset_job_async(
        self,
        dataset_id: str,
        dataset_job_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetJobRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetJobResponse:
        """
        @summary Updates a dataset job.
        
        @param request: UpdateDatasetJobRequest
        @return: UpdateDatasetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_dataset_job_with_options_async(dataset_id, dataset_job_id, request, headers, runtime)

    def update_dataset_job_config_with_options(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetJobConfigResponse:
        """
        @summary Updates a job configuration for a dataset.
        
        @param request: UpdateDatasetJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetJobConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.config_type):
            body['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetJobConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs/{OpenApiUtilClient.get_encode_param(dataset_job_config_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_job_config_with_options_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetJobConfigResponse:
        """
        @summary Updates a job configuration for a dataset.
        
        @param request: UpdateDatasetJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetJobConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.config_type):
            body['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetJobConfig',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/datasetjobconfigs/{OpenApiUtilClient.get_encode_param(dataset_job_config_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_job_config(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetJobConfigRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetJobConfigResponse:
        """
        @summary Updates a job configuration for a dataset.
        
        @param request: UpdateDatasetJobConfigRequest
        @return: UpdateDatasetJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dataset_job_config_with_options(dataset_id, dataset_job_config_id, request, headers, runtime)

    async def update_dataset_job_config_async(
        self,
        dataset_id: str,
        dataset_job_config_id: str,
        request: aiwork_space_20210204_models.UpdateDatasetJobConfigRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetJobConfigResponse:
        """
        @summary Updates a job configuration for a dataset.
        
        @param request: UpdateDatasetJobConfigRequest
        @return: UpdateDatasetJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_dataset_job_config_with_options_async(dataset_id, dataset_job_config_id, request, headers, runtime)

    def update_dataset_version_with_options(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.UpdateDatasetVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetVersionResponse:
        """
        @summary Updates the information about a specified version of a dataset.
        
        @param request: UpdateDatasetVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_count):
            body['DataCount'] = request.data_count
        if not UtilClient.is_unset(request.data_size):
            body['DataSize'] = request.data_size
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_version_with_options_async(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.UpdateDatasetVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDatasetVersionResponse:
        """
        @summary Updates the information about a specified version of a dataset.
        
        @param request: UpdateDatasetVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_count):
            body['DataCount'] = request.data_count
        if not UtilClient.is_unset(request.data_size):
            body['DataSize'] = request.data_size
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasetVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/datasets/{OpenApiUtilClient.get_encode_param(dataset_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDatasetVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_version(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.UpdateDatasetVersionRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetVersionResponse:
        """
        @summary Updates the information about a specified version of a dataset.
        
        @param request: UpdateDatasetVersionRequest
        @return: UpdateDatasetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dataset_version_with_options(dataset_id, version_name, request, headers, runtime)

    async def update_dataset_version_async(
        self,
        dataset_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.UpdateDatasetVersionRequest,
    ) -> aiwork_space_20210204_models.UpdateDatasetVersionResponse:
        """
        @summary Updates the information about a specified version of a dataset.
        
        @param request: UpdateDatasetVersionRequest
        @return: UpdateDatasetVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_dataset_version_with_options_async(dataset_id, version_name, request, headers, runtime)

    def update_default_workspace_with_options(
        self,
        request: aiwork_space_20210204_models.UpdateDefaultWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDefaultWorkspaceResponse:
        """
        @summary Specifies a workspace as the default workspace.
        
        @param request: UpdateDefaultWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDefaultWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDefaultWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/defaultWorkspaces',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDefaultWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_default_workspace_with_options_async(
        self,
        request: aiwork_space_20210204_models.UpdateDefaultWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateDefaultWorkspaceResponse:
        """
        @summary Specifies a workspace as the default workspace.
        
        @param request: UpdateDefaultWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDefaultWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDefaultWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/defaultWorkspaces',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateDefaultWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_default_workspace(
        self,
        request: aiwork_space_20210204_models.UpdateDefaultWorkspaceRequest,
    ) -> aiwork_space_20210204_models.UpdateDefaultWorkspaceResponse:
        """
        @summary Specifies a workspace as the default workspace.
        
        @param request: UpdateDefaultWorkspaceRequest
        @return: UpdateDefaultWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_default_workspace_with_options(request, headers, runtime)

    async def update_default_workspace_async(
        self,
        request: aiwork_space_20210204_models.UpdateDefaultWorkspaceRequest,
    ) -> aiwork_space_20210204_models.UpdateDefaultWorkspaceResponse:
        """
        @summary Specifies a workspace as the default workspace.
        
        @param request: UpdateDefaultWorkspaceRequest
        @return: UpdateDefaultWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_default_workspace_with_options_async(request, headers, runtime)

    def update_experiment_with_options(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateExperimentResponse:
        """
        @summary Updates an experiment.
        
        @param request: UpdateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_with_options_async(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateExperimentResponse:
        """
        @summary Updates an experiment.
        
        @param request: UpdateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperiment',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.UpdateExperimentRequest,
    ) -> aiwork_space_20210204_models.UpdateExperimentResponse:
        """
        @summary Updates an experiment.
        
        @param request: UpdateExperimentRequest
        @return: UpdateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_with_options(experiment_id, request, headers, runtime)

    async def update_experiment_async(
        self,
        experiment_id: str,
        request: aiwork_space_20210204_models.UpdateExperimentRequest,
    ) -> aiwork_space_20210204_models.UpdateExperimentResponse:
        """
        @summary Updates an experiment.
        
        @param request: UpdateExperimentRequest
        @return: UpdateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_with_options_async(experiment_id, request, headers, runtime)

    def update_model_with_options(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.UpdateModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateModelResponse:
        """
        @summary Updates the basic configuration information about a model.
        
        @param request: UpdateModelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.model_description):
            body['ModelDescription'] = request.model_description
        if not UtilClient.is_unset(request.model_doc):
            body['ModelDoc'] = request.model_doc
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.order_number):
            body['OrderNumber'] = request.order_number
        if not UtilClient.is_unset(request.origin):
            body['Origin'] = request.origin
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_with_options_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.UpdateModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateModelResponse:
        """
        @summary Updates the basic configuration information about a model.
        
        @param request: UpdateModelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.model_description):
            body['ModelDescription'] = request.model_description
        if not UtilClient.is_unset(request.model_doc):
            body['ModelDoc'] = request.model_doc
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.order_number):
            body['OrderNumber'] = request.order_number
        if not UtilClient.is_unset(request.origin):
            body['Origin'] = request.origin
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModel',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.UpdateModelRequest,
    ) -> aiwork_space_20210204_models.UpdateModelResponse:
        """
        @summary Updates the basic configuration information about a model.
        
        @param request: UpdateModelRequest
        @return: UpdateModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_with_options(model_id, request, headers, runtime)

    async def update_model_async(
        self,
        model_id: str,
        request: aiwork_space_20210204_models.UpdateModelRequest,
    ) -> aiwork_space_20210204_models.UpdateModelResponse:
        """
        @summary Updates the basic configuration information about a model.
        
        @param request: UpdateModelRequest
        @return: UpdateModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_model_with_options_async(model_id, request, headers, runtime)

    def update_model_version_with_options(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.UpdateModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateModelVersionResponse:
        """
        @summary Updates a model version.
        
        @param request: UpdateModelVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.approval_status):
            body['ApprovalStatus'] = request.approval_status
        if not UtilClient.is_unset(request.compression_spec):
            body['CompressionSpec'] = request.compression_spec
        if not UtilClient.is_unset(request.evaluation_spec):
            body['EvaluationSpec'] = request.evaluation_spec
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.inference_spec):
            body['InferenceSpec'] = request.inference_spec
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.training_spec):
            body['TrainingSpec'] = request.training_spec
        if not UtilClient.is_unset(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_version_with_options_async(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.UpdateModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateModelVersionResponse:
        """
        @summary Updates a model version.
        
        @param request: UpdateModelVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.approval_status):
            body['ApprovalStatus'] = request.approval_status
        if not UtilClient.is_unset(request.compression_spec):
            body['CompressionSpec'] = request.compression_spec
        if not UtilClient.is_unset(request.evaluation_spec):
            body['EvaluationSpec'] = request.evaluation_spec
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.inference_spec):
            body['InferenceSpec'] = request.inference_spec
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.training_spec):
            body['TrainingSpec'] = request.training_spec
        if not UtilClient.is_unset(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelVersion',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/models/{OpenApiUtilClient.get_encode_param(model_id)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_version(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.UpdateModelVersionRequest,
    ) -> aiwork_space_20210204_models.UpdateModelVersionResponse:
        """
        @summary Updates a model version.
        
        @param request: UpdateModelVersionRequest
        @return: UpdateModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_version_with_options(model_id, version_name, request, headers, runtime)

    async def update_model_version_async(
        self,
        model_id: str,
        version_name: str,
        request: aiwork_space_20210204_models.UpdateModelVersionRequest,
    ) -> aiwork_space_20210204_models.UpdateModelVersionResponse:
        """
        @summary Updates a model version.
        
        @param request: UpdateModelVersionRequest
        @return: UpdateModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_model_version_with_options_async(model_id, version_name, request, headers, runtime)

    def update_run_with_options(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.UpdateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateRunResponse:
        """
        @summary Updates the run information.
        
        @param request: UpdateRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRunResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRun',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_run_with_options_async(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.UpdateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateRunResponse:
        """
        @summary Updates the run information.
        
        @param request: UpdateRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRunResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRun',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/runs/{OpenApiUtilClient.get_encode_param(run_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_run(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.UpdateRunRequest,
    ) -> aiwork_space_20210204_models.UpdateRunResponse:
        """
        @summary Updates the run information.
        
        @param request: UpdateRunRequest
        @return: UpdateRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_run_with_options(run_id, request, headers, runtime)

    async def update_run_async(
        self,
        run_id: str,
        request: aiwork_space_20210204_models.UpdateRunRequest,
    ) -> aiwork_space_20210204_models.UpdateRunResponse:
        """
        @summary Updates the run information.
        
        @param request: UpdateRunRequest
        @return: UpdateRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_run_with_options_async(run_id, request, headers, runtime)

    def update_workspace_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateWorkspaceResponse:
        """
        @summary Updates the name and description of a workspace.
        
        @param request: UpdateWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateWorkspaceResponse:
        """
        @summary Updates the name and description of a workspace.
        
        @param request: UpdateWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspace',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateWorkspaceRequest,
    ) -> aiwork_space_20210204_models.UpdateWorkspaceResponse:
        """
        @summary Updates the name and description of a workspace.
        
        @param request: UpdateWorkspaceRequest
        @return: UpdateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_workspace_with_options(workspace_id, request, headers, runtime)

    async def update_workspace_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateWorkspaceRequest,
    ) -> aiwork_space_20210204_models.UpdateWorkspaceResponse:
        """
        @summary Updates the name and description of a workspace.
        
        @param request: UpdateWorkspaceRequest
        @return: UpdateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_workspace_with_options_async(workspace_id, request, headers, runtime)

    def update_workspace_resource_with_options(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateWorkspaceResourceResponse:
        """
        @summary Updates the resources of a workspace.
        
        @param request: UpdateWorkspaceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.is_default):
            body['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceResource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/resources',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateWorkspaceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_resource_with_options_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateWorkspaceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiwork_space_20210204_models.UpdateWorkspaceResourceResponse:
        """
        @summary Updates the resources of a workspace.
        
        @param request: UpdateWorkspaceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.is_default):
            body['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceResource',
            version='2021-02-04',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/resources',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiwork_space_20210204_models.UpdateWorkspaceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace_resource(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateWorkspaceResourceRequest,
    ) -> aiwork_space_20210204_models.UpdateWorkspaceResourceResponse:
        """
        @summary Updates the resources of a workspace.
        
        @param request: UpdateWorkspaceResourceRequest
        @return: UpdateWorkspaceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_workspace_resource_with_options(workspace_id, request, headers, runtime)

    async def update_workspace_resource_async(
        self,
        workspace_id: str,
        request: aiwork_space_20210204_models.UpdateWorkspaceResourceRequest,
    ) -> aiwork_space_20210204_models.UpdateWorkspaceResourceResponse:
        """
        @summary Updates the resources of a workspace.
        
        @param request: UpdateWorkspaceResourceRequest
        @return: UpdateWorkspaceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_workspace_resource_with_options_async(workspace_id, request, headers, runtime)
