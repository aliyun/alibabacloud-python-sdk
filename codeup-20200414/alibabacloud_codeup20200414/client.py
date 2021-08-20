# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_codeup20200414 import models as codeup_20200414_models
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
        self._endpoint = self.get_endpoint('codeup', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def delete_repository_member(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.DeleteRepositoryMemberRequest,
    ) -> codeup_20200414_models.DeleteRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_member_with_options(project_id, user_id, request, headers, runtime)

    async def delete_repository_member_async(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.DeleteRepositoryMemberRequest,
    ) -> codeup_20200414_models.DeleteRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_member_with_options_async(project_id, user_id, request, headers, runtime)

    def delete_repository_member_with_options(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.DeleteRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberResponse(),
            self.do_roarequest('DeleteRepositoryMember', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/members/{user_id}', 'json', req, runtime)
        )

    async def delete_repository_member_with_options_async(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.DeleteRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberResponse(),
            await self.do_roarequest_async('DeleteRepositoryMember', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/members/{user_id}', 'json', req, runtime)
        )

    def create_repository_protected_branch(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateRepositoryProtectedBranchRequest,
    ) -> codeup_20200414_models.CreateRepositoryProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_protected_branch_with_options(project_id, request, headers, runtime)

    async def create_repository_protected_branch_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateRepositoryProtectedBranchRequest,
    ) -> codeup_20200414_models.CreateRepositoryProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repository_protected_branch_with_options_async(project_id, request, headers, runtime)

    def create_repository_protected_branch_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateRepositoryProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateRepositoryProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryProtectedBranchResponse(),
            self.do_roarequest('CreateRepositoryProtectedBranch', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/projects/{project_id}/repository/protect_branches', 'json', req, runtime)
        )

    async def create_repository_protected_branch_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateRepositoryProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateRepositoryProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryProtectedBranchResponse(),
            await self.do_roarequest_async('CreateRepositoryProtectedBranch', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/projects/{project_id}/repository/protect_branches', 'json', req, runtime)
        )

    def create_merge_request(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateMergeRequestRequest,
    ) -> codeup_20200414_models.CreateMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_merge_request_with_options(project_id, request, headers, runtime)

    async def create_merge_request_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateMergeRequestRequest,
    ) -> codeup_20200414_models.CreateMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_merge_request_with_options_async(project_id, request, headers, runtime)

    def create_merge_request_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestResponse(),
            self.do_roarequest('CreateMergeRequest', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/projects/{project_id}/merge_requests', 'json', req, runtime)
        )

    async def create_merge_request_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestResponse(),
            await self.do_roarequest_async('CreateMergeRequest', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/projects/{project_id}/merge_requests', 'json', req, runtime)
        )

    def delete_repository(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryRequest,
    ) -> codeup_20200414_models.DeleteRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_with_options(project_id, request, headers, runtime)

    async def delete_repository_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryRequest,
    ) -> codeup_20200414_models.DeleteRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_with_options_async(project_id, request, headers, runtime)

    def delete_repository_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryResponse(),
            self.do_roarequest('DeleteRepository', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/remove', 'json', req, runtime)
        )

    async def delete_repository_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryResponse(),
            await self.do_roarequest_async('DeleteRepository', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/remove', 'json', req, runtime)
        )

    def get_repository_tag(
        self,
        project_id: str,
        tag_name: str,
        request: codeup_20200414_models.GetRepositoryTagRequest,
    ) -> codeup_20200414_models.GetRepositoryTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_tag_with_options(project_id, tag_name, request, headers, runtime)

    async def get_repository_tag_async(
        self,
        project_id: str,
        tag_name: str,
        request: codeup_20200414_models.GetRepositoryTagRequest,
    ) -> codeup_20200414_models.GetRepositoryTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_tag_with_options_async(project_id, tag_name, request, headers, runtime)

    def get_repository_tag_with_options(
        self,
        project_id: str,
        tag_name: str,
        request: codeup_20200414_models.GetRepositoryTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetRepositoryTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagResponse(),
            self.do_roarequest('GetRepositoryTag', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/tags/{tag_name}', 'json', req, runtime)
        )

    async def get_repository_tag_with_options_async(
        self,
        project_id: str,
        tag_name: str,
        request: codeup_20200414_models.GetRepositoryTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetRepositoryTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagResponse(),
            await self.do_roarequest_async('GetRepositoryTag', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/tags/{tag_name}', 'json', req, runtime)
        )

    def update_merge_request(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.UpdateMergeRequestRequest,
    ) -> codeup_20200414_models.UpdateMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_merge_request_with_options(project_id, merge_request_id, request, headers, runtime)

    async def update_merge_request_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.UpdateMergeRequestRequest,
    ) -> codeup_20200414_models.UpdateMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_merge_request_with_options_async(project_id, merge_request_id, request, headers, runtime)

    def update_merge_request_with_options(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.UpdateMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestResponse(),
            self.do_roarequest('UpdateMergeRequest', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/merge_request/{merge_request_id}', 'json', req, runtime)
        )

    async def update_merge_request_with_options_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.UpdateMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestResponse(),
            await self.do_roarequest_async('UpdateMergeRequest', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/merge_request/{merge_request_id}', 'json', req, runtime)
        )

    def update_repository(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateRepositoryRequest,
    ) -> codeup_20200414_models.UpdateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_with_options(project_id, request, headers, runtime)

    async def update_repository_async(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateRepositoryRequest,
    ) -> codeup_20200414_models.UpdateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_repository_with_options_async(project_id, request, headers, runtime)

    def update_repository_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryResponse(),
            self.do_roarequest('UpdateRepository', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}', 'json', req, runtime)
        )

    async def update_repository_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryResponse(),
            await self.do_roarequest_async('UpdateRepository', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}', 'json', req, runtime)
        )

    def update_merge_request_comment(
        self,
        project_id: str,
        merge_request_id: str,
        note_id: str,
        request: codeup_20200414_models.UpdateMergeRequestCommentRequest,
    ) -> codeup_20200414_models.UpdateMergeRequestCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_merge_request_comment_with_options(project_id, merge_request_id, note_id, request, headers, runtime)

    async def update_merge_request_comment_async(
        self,
        project_id: str,
        merge_request_id: str,
        note_id: str,
        request: codeup_20200414_models.UpdateMergeRequestCommentRequest,
    ) -> codeup_20200414_models.UpdateMergeRequestCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_merge_request_comment_with_options_async(project_id, merge_request_id, note_id, request, headers, runtime)

    def update_merge_request_comment_with_options(
        self,
        project_id: str,
        merge_request_id: str,
        note_id: str,
        request: codeup_20200414_models.UpdateMergeRequestCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateMergeRequestCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestCommentResponse(),
            self.do_roarequest('UpdateMergeRequestComment', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/merge_requests/{merge_request_id}/notes/{note_id}', 'json', req, runtime)
        )

    async def update_merge_request_comment_with_options_async(
        self,
        project_id: str,
        merge_request_id: str,
        note_id: str,
        request: codeup_20200414_models.UpdateMergeRequestCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateMergeRequestCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestCommentResponse(),
            await self.do_roarequest_async('UpdateMergeRequestComment', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/merge_requests/{merge_request_id}/notes/{note_id}', 'json', req, runtime)
        )

    def delete_branch(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteBranchRequest,
    ) -> codeup_20200414_models.DeleteBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_branch_with_options(project_id, request, headers, runtime)

    async def delete_branch_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteBranchRequest,
    ) -> codeup_20200414_models.DeleteBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_branch_with_options_async(project_id, request, headers, runtime)

    def delete_branch_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteBranchResponse(),
            self.do_roarequest('DeleteBranch', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/repository/branches/delete', 'json', req, runtime)
        )

    async def delete_branch_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteBranchResponse(),
            await self.do_roarequest_async('DeleteBranch', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/repository/branches/delete', 'json', req, runtime)
        )

    def list_repository_commit_diff(
        self,
        project_id: str,
        sha: str,
        request: codeup_20200414_models.ListRepositoryCommitDiffRequest,
    ) -> codeup_20200414_models.ListRepositoryCommitDiffResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commit_diff_with_options(project_id, sha, request, headers, runtime)

    async def list_repository_commit_diff_async(
        self,
        project_id: str,
        sha: str,
        request: codeup_20200414_models.ListRepositoryCommitDiffRequest,
    ) -> codeup_20200414_models.ListRepositoryCommitDiffResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_commit_diff_with_options_async(project_id, sha, request, headers, runtime)

    def list_repository_commit_diff_with_options(
        self,
        project_id: str,
        sha: str,
        request: codeup_20200414_models.ListRepositoryCommitDiffRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryCommitDiffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.context_line):
            query['ContextLine'] = request.context_line
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitDiffResponse(),
            self.do_roarequest('ListRepositoryCommitDiff', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/commits/{sha}/diff', 'json', req, runtime)
        )

    async def list_repository_commit_diff_with_options_async(
        self,
        project_id: str,
        sha: str,
        request: codeup_20200414_models.ListRepositoryCommitDiffRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryCommitDiffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.context_line):
            query['ContextLine'] = request.context_line
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitDiffResponse(),
            await self.do_roarequest_async('ListRepositoryCommitDiff', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/commits/{sha}/diff', 'json', req, runtime)
        )

    def get_repository_info(
        self,
        request: codeup_20200414_models.GetRepositoryInfoRequest,
    ) -> codeup_20200414_models.GetRepositoryInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_info_with_options(request, headers, runtime)

    async def get_repository_info_async(
        self,
        request: codeup_20200414_models.GetRepositoryInfoRequest,
    ) -> codeup_20200414_models.GetRepositoryInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_info_with_options_async(request, headers, runtime)

    def get_repository_info_with_options(
        self,
        request: codeup_20200414_models.GetRepositoryInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetRepositoryInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.identity):
            query['Identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryInfoResponse(),
            self.do_roarequest('GetRepositoryInfo', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/info', 'json', req, runtime)
        )

    async def get_repository_info_with_options_async(
        self,
        request: codeup_20200414_models.GetRepositoryInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetRepositoryInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.identity):
            query['Identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryInfoResponse(),
            await self.do_roarequest_async('GetRepositoryInfo', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/info', 'json', req, runtime)
        )

    def accept_merge_request(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.AcceptMergeRequestRequest,
    ) -> codeup_20200414_models.AcceptMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.accept_merge_request_with_options(project_id, merge_request_id, request, headers, runtime)

    async def accept_merge_request_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.AcceptMergeRequestRequest,
    ) -> codeup_20200414_models.AcceptMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.accept_merge_request_with_options_async(project_id, merge_request_id, request, headers, runtime)

    def accept_merge_request_with_options(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.AcceptMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.AcceptMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.AcceptMergeRequestResponse(),
            self.do_roarequest('AcceptMergeRequest', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/merge_request/{merge_request_id}/accept', 'json', req, runtime)
        )

    async def accept_merge_request_with_options_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.AcceptMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.AcceptMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.AcceptMergeRequestResponse(),
            await self.do_roarequest_async('AcceptMergeRequest', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/merge_request/{merge_request_id}/accept', 'json', req, runtime)
        )

    def delete_file(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteFileRequest,
    ) -> codeup_20200414_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(project_id, request, headers, runtime)

    async def delete_file_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteFileRequest,
    ) -> codeup_20200414_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_file_with_options_async(project_id, request, headers, runtime)

    def delete_file_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.commit_message):
            query['CommitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteFileResponse(),
            self.do_roarequest('DeleteFile', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/repository/files', 'json', req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.commit_message):
            query['CommitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteFileResponse(),
            await self.do_roarequest_async('DeleteFile', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/repository/files', 'json', req, runtime)
        )

    def delete_repository_protected_branch(
        self,
        project_id: str,
        protected_branch_id: str,
        request: codeup_20200414_models.DeleteRepositoryProtectedBranchRequest,
    ) -> codeup_20200414_models.DeleteRepositoryProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_protected_branch_with_options(project_id, protected_branch_id, request, headers, runtime)

    async def delete_repository_protected_branch_async(
        self,
        project_id: str,
        protected_branch_id: str,
        request: codeup_20200414_models.DeleteRepositoryProtectedBranchRequest,
    ) -> codeup_20200414_models.DeleteRepositoryProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_protected_branch_with_options_async(project_id, protected_branch_id, request, headers, runtime)

    def delete_repository_protected_branch_with_options(
        self,
        project_id: str,
        protected_branch_id: str,
        request: codeup_20200414_models.DeleteRepositoryProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryProtectedBranchResponse(),
            self.do_roarequest('DeleteRepositoryProtectedBranch', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v4/projects/{project_id}/repository/protect_branches/{protected_branch_id}', 'json', req, runtime)
        )

    async def delete_repository_protected_branch_with_options_async(
        self,
        project_id: str,
        protected_branch_id: str,
        request: codeup_20200414_models.DeleteRepositoryProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryProtectedBranchResponse(),
            await self.do_roarequest_async('DeleteRepositoryProtectedBranch', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v4/projects/{project_id}/repository/protect_branches/{protected_branch_id}', 'json', req, runtime)
        )

    def delete_repository_tag_v2(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryTagV2Request,
    ) -> codeup_20200414_models.DeleteRepositoryTagV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_tag_v2with_options(project_id, request, headers, runtime)

    async def delete_repository_tag_v2_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryTagV2Request,
    ) -> codeup_20200414_models.DeleteRepositoryTagV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_tag_v2with_options_async(project_id, request, headers, runtime)

    def delete_repository_tag_v2with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryTagV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryTagV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagV2Response(),
            self.do_roarequest('DeleteRepositoryTagV2', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/repository/tag/delete', 'json', req, runtime)
        )

    async def delete_repository_tag_v2with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryTagV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryTagV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagV2Response(),
            await self.do_roarequest_async('DeleteRepositoryTagV2', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/repository/tag/delete', 'json', req, runtime)
        )

    def get_file_last_commit(
        self,
        project_id: str,
        request: codeup_20200414_models.GetFileLastCommitRequest,
    ) -> codeup_20200414_models.GetFileLastCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_last_commit_with_options(project_id, request, headers, runtime)

    async def get_file_last_commit_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetFileLastCommitRequest,
    ) -> codeup_20200414_models.GetFileLastCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_last_commit_with_options_async(project_id, request, headers, runtime)

    def get_file_last_commit_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.GetFileLastCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetFileLastCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['Sha'] = request.sha
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileLastCommitResponse(),
            self.do_roarequest('GetFileLastCommit', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/files/last_commit', 'json', req, runtime)
        )

    async def get_file_last_commit_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetFileLastCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetFileLastCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['Sha'] = request.sha
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileLastCommitResponse(),
            await self.do_roarequest_async('GetFileLastCommit', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/files/last_commit', 'json', req, runtime)
        )

    def update_file(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateFileRequest,
    ) -> codeup_20200414_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_file_with_options(project_id, request, headers, runtime)

    async def update_file_async(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateFileRequest,
    ) -> codeup_20200414_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_file_with_options_async(project_id, request, headers, runtime)

    def update_file_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateFileResponse(),
            self.do_roarequest('UpdateFile', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v4/projects/{project_id}/repository/files', 'json', req, runtime)
        )

    async def update_file_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateFileResponse(),
            await self.do_roarequest_async('UpdateFile', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v4/projects/{project_id}/repository/files', 'json', req, runtime)
        )

    def update_repository_member(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.UpdateRepositoryMemberRequest,
    ) -> codeup_20200414_models.UpdateRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_member_with_options(project_id, user_id, request, headers, runtime)

    async def update_repository_member_async(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.UpdateRepositoryMemberRequest,
    ) -> codeup_20200414_models.UpdateRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_repository_member_with_options_async(project_id, user_id, request, headers, runtime)

    def update_repository_member_with_options(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.UpdateRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryMemberResponse(),
            self.do_roarequest('UpdateRepositoryMember', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/members/{user_id}', 'json', req, runtime)
        )

    async def update_repository_member_with_options_async(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.UpdateRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryMemberResponse(),
            await self.do_roarequest_async('UpdateRepositoryMember', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/members/{user_id}', 'json', req, runtime)
        )

    def add_repository_member(
        self,
        project_id: str,
        request: codeup_20200414_models.AddRepositoryMemberRequest,
    ) -> codeup_20200414_models.AddRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_repository_member_with_options(project_id, request, headers, runtime)

    async def add_repository_member_async(
        self,
        project_id: str,
        request: codeup_20200414_models.AddRepositoryMemberRequest,
    ) -> codeup_20200414_models.AddRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_repository_member_with_options_async(project_id, request, headers, runtime)

    def add_repository_member_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.AddRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.AddRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddRepositoryMemberResponse(),
            self.do_roarequest('AddRepositoryMember', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/projects/{project_id}/members', 'json', req, runtime)
        )

    async def add_repository_member_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.AddRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.AddRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddRepositoryMemberResponse(),
            await self.do_roarequest_async('AddRepositoryMember', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/projects/{project_id}/members', 'json', req, runtime)
        )

    def create_ssh_key(
        self,
        request: codeup_20200414_models.CreateSshKeyRequest,
    ) -> codeup_20200414_models.CreateSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ssh_key_with_options(request, headers, runtime)

    async def create_ssh_key_async(
        self,
        request: codeup_20200414_models.CreateSshKeyRequest,
    ) -> codeup_20200414_models.CreateSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ssh_key_with_options_async(request, headers, runtime)

    def create_ssh_key_with_options(
        self,
        request: codeup_20200414_models.CreateSshKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateSshKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateSshKeyResponse(),
            self.do_roarequest('CreateSshKey', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/user/keys', 'json', req, runtime)
        )

    async def create_ssh_key_with_options_async(
        self,
        request: codeup_20200414_models.CreateSshKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateSshKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateSshKeyResponse(),
            await self.do_roarequest_async('CreateSshKey', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/user/keys', 'json', req, runtime)
        )

    def list_repository_tags(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryTagsRequest,
    ) -> codeup_20200414_models.ListRepositoryTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_tags_with_options(project_id, request, headers, runtime)

    async def list_repository_tags_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryTagsRequest,
    ) -> codeup_20200414_models.ListRepositoryTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_tags_with_options_async(project_id, request, headers, runtime)

    def list_repository_tags_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTagsResponse(),
            self.do_roarequest('ListRepositoryTags', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/tags', 'json', req, runtime)
        )

    async def list_repository_tags_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTagsResponse(),
            await self.do_roarequest_async('ListRepositoryTags', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/tags', 'json', req, runtime)
        )

    def add_webhook(
        self,
        project_id: str,
        request: codeup_20200414_models.AddWebhookRequest,
    ) -> codeup_20200414_models.AddWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_webhook_with_options(project_id, request, headers, runtime)

    async def add_webhook_async(
        self,
        project_id: str,
        request: codeup_20200414_models.AddWebhookRequest,
    ) -> codeup_20200414_models.AddWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_webhook_with_options_async(project_id, request, headers, runtime)

    def add_webhook_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.AddWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.AddWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddWebhookResponse(),
            self.do_roarequest('AddWebhook', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/hooks', 'json', req, runtime)
        )

    async def add_webhook_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.AddWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.AddWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddWebhookResponse(),
            await self.do_roarequest_async('AddWebhook', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/hooks', 'json', req, runtime)
        )

    def enable_repository_deploy_key(
        self,
        project_id: str,
        key_id: str,
        request: codeup_20200414_models.EnableRepositoryDeployKeyRequest,
    ) -> codeup_20200414_models.EnableRepositoryDeployKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_repository_deploy_key_with_options(project_id, key_id, request, headers, runtime)

    async def enable_repository_deploy_key_async(
        self,
        project_id: str,
        key_id: str,
        request: codeup_20200414_models.EnableRepositoryDeployKeyRequest,
    ) -> codeup_20200414_models.EnableRepositoryDeployKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_repository_deploy_key_with_options_async(project_id, key_id, request, headers, runtime)

    def enable_repository_deploy_key_with_options(
        self,
        project_id: str,
        key_id: str,
        request: codeup_20200414_models.EnableRepositoryDeployKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.EnableRepositoryDeployKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.EnableRepositoryDeployKeyResponse(),
            self.do_roarequest('EnableRepositoryDeployKey', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/keys/{key_id}/enable', 'json', req, runtime)
        )

    async def enable_repository_deploy_key_with_options_async(
        self,
        project_id: str,
        key_id: str,
        request: codeup_20200414_models.EnableRepositoryDeployKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.EnableRepositoryDeployKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.EnableRepositoryDeployKeyResponse(),
            await self.do_roarequest_async('EnableRepositoryDeployKey', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/keys/{key_id}/enable', 'json', req, runtime)
        )

    def get_user_info(
        self,
        request: codeup_20200414_models.GetUserInfoRequest,
    ) -> codeup_20200414_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_info_with_options(request, headers, runtime)

    async def get_user_info_async(
        self,
        request: codeup_20200414_models.GetUserInfoRequest,
    ) -> codeup_20200414_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_info_with_options_async(request, headers, runtime)

    def get_user_info_with_options(
        self,
        request: codeup_20200414_models.GetUserInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetUserInfoResponse(),
            self.do_roarequest('GetUserInfo', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/user/current', 'json', req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        request: codeup_20200414_models.GetUserInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetUserInfoResponse(),
            await self.do_roarequest_async('GetUserInfo', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/user/current', 'json', req, runtime)
        )

    def list_repository_tree(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryTreeRequest,
    ) -> codeup_20200414_models.ListRepositoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_tree_with_options(project_id, request, headers, runtime)

    async def list_repository_tree_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryTreeRequest,
    ) -> codeup_20200414_models.ListRepositoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_tree_with_options_async(project_id, request, headers, runtime)

    def list_repository_tree_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTreeResponse(),
            self.do_roarequest('ListRepositoryTree', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/tree', 'json', req, runtime)
        )

    async def list_repository_tree_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTreeResponse(),
            await self.do_roarequest_async('ListRepositoryTree', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/tree', 'json', req, runtime)
        )

    def delete_repository_group(
        self,
        group_id: str,
        request: codeup_20200414_models.DeleteRepositoryGroupRequest,
    ) -> codeup_20200414_models.DeleteRepositoryGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_group_with_options(group_id, request, headers, runtime)

    async def delete_repository_group_async(
        self,
        group_id: str,
        request: codeup_20200414_models.DeleteRepositoryGroupRequest,
    ) -> codeup_20200414_models.DeleteRepositoryGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_group_with_options_async(group_id, request, headers, runtime)

    def delete_repository_group_with_options(
        self,
        group_id: str,
        request: codeup_20200414_models.DeleteRepositoryGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryGroupResponse(),
            self.do_roarequest('DeleteRepositoryGroup', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/groups/{group_id}/remove', 'json', req, runtime)
        )

    async def delete_repository_group_with_options_async(
        self,
        group_id: str,
        request: codeup_20200414_models.DeleteRepositoryGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryGroupResponse(),
            await self.do_roarequest_async('DeleteRepositoryGroup', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/groups/{group_id}/remove', 'json', req, runtime)
        )

    def delete_repository_webhook(
        self,
        project_id: str,
        webhook_id: str,
        request: codeup_20200414_models.DeleteRepositoryWebhookRequest,
    ) -> codeup_20200414_models.DeleteRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_webhook_with_options(project_id, webhook_id, request, headers, runtime)

    async def delete_repository_webhook_async(
        self,
        project_id: str,
        webhook_id: str,
        request: codeup_20200414_models.DeleteRepositoryWebhookRequest,
    ) -> codeup_20200414_models.DeleteRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_webhook_with_options_async(project_id, webhook_id, request, headers, runtime)

    def delete_repository_webhook_with_options(
        self,
        project_id: str,
        webhook_id: str,
        request: codeup_20200414_models.DeleteRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryWebhookResponse(),
            self.do_roarequest('DeleteRepositoryWebhook', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/hooks/{webhook_id}', 'json', req, runtime)
        )

    async def delete_repository_webhook_with_options_async(
        self,
        project_id: str,
        webhook_id: str,
        request: codeup_20200414_models.DeleteRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryWebhookResponse(),
            await self.do_roarequest_async('DeleteRepositoryWebhook', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/hooks/{webhook_id}', 'json', req, runtime)
        )

    def list_repository_member(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryMemberRequest,
    ) -> codeup_20200414_models.ListRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_member_with_options(project_id, request, headers, runtime)

    async def list_repository_member_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryMemberRequest,
    ) -> codeup_20200414_models.ListRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_member_with_options_async(project_id, request, headers, runtime)

    def list_repository_member_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberResponse(),
            self.do_roarequest('ListRepositoryMember', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/members', 'json', req, runtime)
        )

    async def list_repository_member_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberResponse(),
            await self.do_roarequest_async('ListRepositoryMember', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/members', 'json', req, runtime)
        )

    def create_tag(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateTagRequest,
    ) -> codeup_20200414_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tag_with_options(project_id, request, headers, runtime)

    async def create_tag_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateTagRequest,
    ) -> codeup_20200414_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_tag_with_options_async(project_id, request, headers, runtime)

    def create_tag_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateTagResponse(),
            self.do_roarequest('CreateTag', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/repository/tags', 'json', req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateTagResponse(),
            await self.do_roarequest_async('CreateTag', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/repository/tags', 'json', req, runtime)
        )

    def get_repository_commit(
        self,
        project_id: str,
        sha: str,
        request: codeup_20200414_models.GetRepositoryCommitRequest,
    ) -> codeup_20200414_models.GetRepositoryCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_commit_with_options(project_id, sha, request, headers, runtime)

    async def get_repository_commit_async(
        self,
        project_id: str,
        sha: str,
        request: codeup_20200414_models.GetRepositoryCommitRequest,
    ) -> codeup_20200414_models.GetRepositoryCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_commit_with_options_async(project_id, sha, request, headers, runtime)

    def get_repository_commit_with_options(
        self,
        project_id: str,
        sha: str,
        request: codeup_20200414_models.GetRepositoryCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetRepositoryCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryCommitResponse(),
            self.do_roarequest('GetRepositoryCommit', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/commits/{sha}', 'json', req, runtime)
        )

    async def get_repository_commit_with_options_async(
        self,
        project_id: str,
        sha: str,
        request: codeup_20200414_models.GetRepositoryCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetRepositoryCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryCommitResponse(),
            await self.do_roarequest_async('GetRepositoryCommit', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/commits/{sha}', 'json', req, runtime)
        )

    def add_group_member(
        self,
        group_id: str,
        request: codeup_20200414_models.AddGroupMemberRequest,
    ) -> codeup_20200414_models.AddGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_group_member_with_options(group_id, request, headers, runtime)

    async def add_group_member_async(
        self,
        group_id: str,
        request: codeup_20200414_models.AddGroupMemberRequest,
    ) -> codeup_20200414_models.AddGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_group_member_with_options_async(group_id, request, headers, runtime)

    def add_group_member_with_options(
        self,
        group_id: str,
        request: codeup_20200414_models.AddGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.AddGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddGroupMemberResponse(),
            self.do_roarequest('AddGroupMember', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/groups/{group_id}/members', 'json', req, runtime)
        )

    async def add_group_member_with_options_async(
        self,
        group_id: str,
        request: codeup_20200414_models.AddGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.AddGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddGroupMemberResponse(),
            await self.do_roarequest_async('AddGroupMember', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/groups/{group_id}/members', 'json', req, runtime)
        )

    def get_branch_info(
        self,
        project_id: str,
        request: codeup_20200414_models.GetBranchInfoRequest,
    ) -> codeup_20200414_models.GetBranchInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_branch_info_with_options(project_id, request, headers, runtime)

    async def get_branch_info_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetBranchInfoRequest,
    ) -> codeup_20200414_models.GetBranchInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_branch_info_with_options_async(project_id, request, headers, runtime)

    def get_branch_info_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.GetBranchInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetBranchInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetBranchInfoResponse(),
            self.do_roarequest('GetBranchInfo', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/branches/detail', 'json', req, runtime)
        )

    async def get_branch_info_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetBranchInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetBranchInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetBranchInfoResponse(),
            await self.do_roarequest_async('GetBranchInfo', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/branches/detail', 'json', req, runtime)
        )

    def list_merge_request_comments(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.ListMergeRequestCommentsRequest,
    ) -> codeup_20200414_models.ListMergeRequestCommentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_merge_request_comments_with_options(project_id, merge_request_id, request, headers, runtime)

    async def list_merge_request_comments_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.ListMergeRequestCommentsRequest,
    ) -> codeup_20200414_models.ListMergeRequestCommentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_merge_request_comments_with_options_async(project_id, merge_request_id, request, headers, runtime)

    def list_merge_request_comments_with_options(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.ListMergeRequestCommentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListMergeRequestCommentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.from_commit):
            query['FromCommit'] = request.from_commit
        if not UtilClient.is_unset(request.to_commit):
            query['ToCommit'] = request.to_commit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestCommentsResponse(),
            self.do_roarequest('ListMergeRequestComments', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/merge_request/{merge_request_id}/comments', 'json', req, runtime)
        )

    async def list_merge_request_comments_with_options_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.ListMergeRequestCommentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListMergeRequestCommentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.from_commit):
            query['FromCommit'] = request.from_commit
        if not UtilClient.is_unset(request.to_commit):
            query['ToCommit'] = request.to_commit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestCommentsResponse(),
            await self.do_roarequest_async('ListMergeRequestComments', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/merge_request/{merge_request_id}/comments', 'json', req, runtime)
        )

    def create_repository_group(
        self,
        request: codeup_20200414_models.CreateRepositoryGroupRequest,
    ) -> codeup_20200414_models.CreateRepositoryGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_group_with_options(request, headers, runtime)

    async def create_repository_group_async(
        self,
        request: codeup_20200414_models.CreateRepositoryGroupRequest,
    ) -> codeup_20200414_models.CreateRepositoryGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repository_group_with_options_async(request, headers, runtime)

    def create_repository_group_with_options(
        self,
        request: codeup_20200414_models.CreateRepositoryGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateRepositoryGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryGroupResponse(),
            self.do_roarequest('CreateRepositoryGroup', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/groups', 'json', req, runtime)
        )

    async def create_repository_group_with_options_async(
        self,
        request: codeup_20200414_models.CreateRepositoryGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateRepositoryGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryGroupResponse(),
            await self.do_roarequest_async('CreateRepositoryGroup', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/groups', 'json', req, runtime)
        )

    def get_merge_request_detail(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.GetMergeRequestDetailRequest,
    ) -> codeup_20200414_models.GetMergeRequestDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_merge_request_detail_with_options(project_id, merge_request_id, request, headers, runtime)

    async def get_merge_request_detail_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.GetMergeRequestDetailRequest,
    ) -> codeup_20200414_models.GetMergeRequestDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_merge_request_detail_with_options_async(project_id, merge_request_id, request, headers, runtime)

    def get_merge_request_detail_with_options(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.GetMergeRequestDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetMergeRequestDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestDetailResponse(),
            self.do_roarequest('GetMergeRequestDetail', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/merge_request/{merge_request_id}', 'json', req, runtime)
        )

    async def get_merge_request_detail_with_options_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.GetMergeRequestDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetMergeRequestDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestDetailResponse(),
            await self.do_roarequest_async('GetMergeRequestDetail', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/merge_request/{merge_request_id}', 'json', req, runtime)
        )

    def list_groups(
        self,
        request: codeup_20200414_models.ListGroupsRequest,
    ) -> codeup_20200414_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_groups_with_options(request, headers, runtime)

    async def list_groups_async(
        self,
        request: codeup_20200414_models.ListGroupsRequest,
    ) -> codeup_20200414_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_groups_with_options_async(request, headers, runtime)

    def list_groups_with_options(
        self,
        request: codeup_20200414_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.include_personal):
            query['IncludePersonal'] = request.include_personal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupsResponse(),
            self.do_roarequest('ListGroups', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/groups/all', 'json', req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: codeup_20200414_models.ListGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.include_personal):
            query['IncludePersonal'] = request.include_personal
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupsResponse(),
            await self.do_roarequest_async('ListGroups', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/groups/all', 'json', req, runtime)
        )

    def list_repository_protected_branch(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryProtectedBranchRequest,
    ) -> codeup_20200414_models.ListRepositoryProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_protected_branch_with_options(project_id, request, headers, runtime)

    async def list_repository_protected_branch_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryProtectedBranchRequest,
    ) -> codeup_20200414_models.ListRepositoryProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_protected_branch_with_options_async(project_id, request, headers, runtime)

    def list_repository_protected_branch_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryProtectedBranchResponse(),
            self.do_roarequest('ListRepositoryProtectedBranch', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/protect_branches', 'json', req, runtime)
        )

    async def list_repository_protected_branch_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryProtectedBranchResponse(),
            await self.do_roarequest_async('ListRepositoryProtectedBranch', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/protect_branches', 'json', req, runtime)
        )

    def list_organizations(
        self,
        request: codeup_20200414_models.ListOrganizationsRequest,
    ) -> codeup_20200414_models.ListOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organizations_with_options(request, headers, runtime)

    async def list_organizations_async(
        self,
        request: codeup_20200414_models.ListOrganizationsRequest,
    ) -> codeup_20200414_models.ListOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_organizations_with_options_async(request, headers, runtime)

    def list_organizations_with_options(
        self,
        request: codeup_20200414_models.ListOrganizationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListOrganizationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.access_level):
            query['AccessLevel'] = request.access_level
        if not UtilClient.is_unset(request.min_access_level):
            query['MinAccessLevel'] = request.min_access_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationsResponse(),
            self.do_roarequest('ListOrganizations', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/organization', 'json', req, runtime)
        )

    async def list_organizations_with_options_async(
        self,
        request: codeup_20200414_models.ListOrganizationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListOrganizationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.access_level):
            query['AccessLevel'] = request.access_level
        if not UtilClient.is_unset(request.min_access_level):
            query['MinAccessLevel'] = request.min_access_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationsResponse(),
            await self.do_roarequest_async('ListOrganizations', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/organization', 'json', req, runtime)
        )

    def get_project_member(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.GetProjectMemberRequest,
    ) -> codeup_20200414_models.GetProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_member_with_options(project_id, user_id, request, headers, runtime)

    async def get_project_member_async(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.GetProjectMemberRequest,
    ) -> codeup_20200414_models.GetProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_member_with_options_async(project_id, user_id, request, headers, runtime)

    def get_project_member_with_options(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.GetProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetProjectMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetProjectMemberResponse(),
            self.do_roarequest('GetProjectMember', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/members/{user_id}', 'json', req, runtime)
        )

    async def get_project_member_with_options_async(
        self,
        project_id: str,
        user_id: str,
        request: codeup_20200414_models.GetProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetProjectMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetProjectMemberResponse(),
            await self.do_roarequest_async('GetProjectMember', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/members/{user_id}', 'json', req, runtime)
        )

    def create_file(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateFileRequest,
    ) -> codeup_20200414_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_with_options(project_id, request, headers, runtime)

    async def create_file_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateFileRequest,
    ) -> codeup_20200414_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_file_with_options_async(project_id, request, headers, runtime)

    def create_file_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateFileResponse(),
            self.do_roarequest('CreateFile', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/repository/files', 'json', req, runtime)
        )

    async def create_file_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateFileResponse(),
            await self.do_roarequest_async('CreateFile', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/repository/files', 'json', req, runtime)
        )

    def list_repository_commits(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryCommitsRequest,
    ) -> codeup_20200414_models.ListRepositoryCommitsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commits_with_options(project_id, request, headers, runtime)

    async def list_repository_commits_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryCommitsRequest,
    ) -> codeup_20200414_models.ListRepositoryCommitsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_commits_with_options_async(project_id, request, headers, runtime)

    def list_repository_commits_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryCommitsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryCommitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitsResponse(),
            self.do_roarequest('ListRepositoryCommits', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/commits', 'json', req, runtime)
        )

    async def list_repository_commits_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryCommitsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryCommitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitsResponse(),
            await self.do_roarequest_async('ListRepositoryCommits', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/commits', 'json', req, runtime)
        )

    def get_merge_request_approve_status(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.GetMergeRequestApproveStatusRequest,
    ) -> codeup_20200414_models.GetMergeRequestApproveStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_merge_request_approve_status_with_options(project_id, merge_request_id, request, headers, runtime)

    async def get_merge_request_approve_status_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.GetMergeRequestApproveStatusRequest,
    ) -> codeup_20200414_models.GetMergeRequestApproveStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_merge_request_approve_status_with_options_async(project_id, merge_request_id, request, headers, runtime)

    def get_merge_request_approve_status_with_options(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.GetMergeRequestApproveStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetMergeRequestApproveStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestApproveStatusResponse(),
            self.do_roarequest('GetMergeRequestApproveStatus', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/merge_request/{merge_request_id}/approve_status', 'json', req, runtime)
        )

    async def get_merge_request_approve_status_with_options_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.GetMergeRequestApproveStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetMergeRequestApproveStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestApproveStatusResponse(),
            await self.do_roarequest_async('GetMergeRequestApproveStatus', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/merge_request/{merge_request_id}/approve_status', 'json', req, runtime)
        )

    def list_repositories(
        self,
        request: codeup_20200414_models.ListRepositoriesRequest,
    ) -> codeup_20200414_models.ListRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repositories_with_options(request, headers, runtime)

    async def list_repositories_async(
        self,
        request: codeup_20200414_models.ListRepositoriesRequest,
    ) -> codeup_20200414_models.ListRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repositories_with_options_async(request, headers, runtime)

    def list_repositories_with_options(
        self,
        request: codeup_20200414_models.ListRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.archive):
            query['Archive'] = request.archive
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoriesResponse(),
            self.do_roarequest('ListRepositories', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/all', 'json', req, runtime)
        )

    async def list_repositories_with_options_async(
        self,
        request: codeup_20200414_models.ListRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.archive):
            query['Archive'] = request.archive
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoriesResponse(),
            await self.do_roarequest_async('ListRepositories', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/all', 'json', req, runtime)
        )

    def update_merge_request_setting(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateMergeRequestSettingRequest,
    ) -> codeup_20200414_models.UpdateMergeRequestSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_merge_request_setting_with_options(project_id, request, headers, runtime)

    async def update_merge_request_setting_async(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateMergeRequestSettingRequest,
    ) -> codeup_20200414_models.UpdateMergeRequestSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_merge_request_setting_with_options_async(project_id, request, headers, runtime)

    def update_merge_request_setting_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateMergeRequestSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateMergeRequestSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestSettingResponse(),
            self.do_roarequest('UpdateMergeRequestSetting', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v4/projects/{project_id}/settings/merge_requests', 'json', req, runtime)
        )

    async def update_merge_request_setting_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.UpdateMergeRequestSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateMergeRequestSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestSettingResponse(),
            await self.do_roarequest_async('UpdateMergeRequestSetting', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v4/projects/{project_id}/settings/merge_requests', 'json', req, runtime)
        )

    def list_group_member(
        self,
        group_id: str,
        request: codeup_20200414_models.ListGroupMemberRequest,
    ) -> codeup_20200414_models.ListGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_member_with_options(group_id, request, headers, runtime)

    async def list_group_member_async(
        self,
        group_id: str,
        request: codeup_20200414_models.ListGroupMemberRequest,
    ) -> codeup_20200414_models.ListGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_group_member_with_options_async(group_id, request, headers, runtime)

    def list_group_member_with_options(
        self,
        group_id: str,
        request: codeup_20200414_models.ListGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupMemberResponse(),
            self.do_roarequest('ListGroupMember', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/groups/{group_id}/members', 'json', req, runtime)
        )

    async def list_group_member_with_options_async(
        self,
        group_id: str,
        request: codeup_20200414_models.ListGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupMemberResponse(),
            await self.do_roarequest_async('ListGroupMember', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/groups/{group_id}/members', 'json', req, runtime)
        )

    def update_group_member(
        self,
        group_id: str,
        user_id: str,
        request: codeup_20200414_models.UpdateGroupMemberRequest,
    ) -> codeup_20200414_models.UpdateGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_member_with_options(group_id, user_id, request, headers, runtime)

    async def update_group_member_async(
        self,
        group_id: str,
        user_id: str,
        request: codeup_20200414_models.UpdateGroupMemberRequest,
    ) -> codeup_20200414_models.UpdateGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_group_member_with_options_async(group_id, user_id, request, headers, runtime)

    def update_group_member_with_options(
        self,
        group_id: str,
        user_id: str,
        request: codeup_20200414_models.UpdateGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateGroupMemberResponse(),
            self.do_roarequest('UpdateGroupMember', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/groups/{group_id}/members/{user_id}', 'json', req, runtime)
        )

    async def update_group_member_with_options_async(
        self,
        group_id: str,
        user_id: str,
        request: codeup_20200414_models.UpdateGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UpdateGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateGroupMemberResponse(),
            await self.do_roarequest_async('UpdateGroupMember', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/groups/{group_id}/members/{user_id}', 'json', req, runtime)
        )

    def create_merge_request_comment(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.CreateMergeRequestCommentRequest,
    ) -> codeup_20200414_models.CreateMergeRequestCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_merge_request_comment_with_options(project_id, merge_request_id, request, headers, runtime)

    async def create_merge_request_comment_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.CreateMergeRequestCommentRequest,
    ) -> codeup_20200414_models.CreateMergeRequestCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_merge_request_comment_with_options_async(project_id, merge_request_id, request, headers, runtime)

    def create_merge_request_comment_with_options(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.CreateMergeRequestCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateMergeRequestCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestCommentResponse(),
            self.do_roarequest('CreateMergeRequestComment', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/projects/{project_id}/merge_request/{merge_request_id}/comments', 'json', req, runtime)
        )

    async def create_merge_request_comment_with_options_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.CreateMergeRequestCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateMergeRequestCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestCommentResponse(),
            await self.do_roarequest_async('CreateMergeRequestComment', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v4/projects/{project_id}/merge_request/{merge_request_id}/comments', 'json', req, runtime)
        )

    def create_repository_deploy_key(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateRepositoryDeployKeyRequest,
    ) -> codeup_20200414_models.CreateRepositoryDeployKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_deploy_key_with_options(project_id, request, headers, runtime)

    async def create_repository_deploy_key_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateRepositoryDeployKeyRequest,
    ) -> codeup_20200414_models.CreateRepositoryDeployKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repository_deploy_key_with_options_async(project_id, request, headers, runtime)

    def create_repository_deploy_key_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateRepositoryDeployKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateRepositoryDeployKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryDeployKeyResponse(),
            self.do_roarequest('CreateRepositoryDeployKey', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/keys', 'json', req, runtime)
        )

    async def create_repository_deploy_key_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateRepositoryDeployKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateRepositoryDeployKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryDeployKeyResponse(),
            await self.do_roarequest_async('CreateRepositoryDeployKey', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/keys', 'json', req, runtime)
        )

    def delete_repository_tag(
        self,
        project_id: str,
        tag_name: str,
        request: codeup_20200414_models.DeleteRepositoryTagRequest,
    ) -> codeup_20200414_models.DeleteRepositoryTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_tag_with_options(project_id, tag_name, request, headers, runtime)

    async def delete_repository_tag_async(
        self,
        project_id: str,
        tag_name: str,
        request: codeup_20200414_models.DeleteRepositoryTagRequest,
    ) -> codeup_20200414_models.DeleteRepositoryTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_tag_with_options_async(project_id, tag_name, request, headers, runtime)

    def delete_repository_tag_with_options(
        self,
        project_id: str,
        tag_name: str,
        request: codeup_20200414_models.DeleteRepositoryTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagResponse(),
            self.do_roarequest('DeleteRepositoryTag', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/repository/tags/{tag_name}', 'json', req, runtime)
        )

    async def delete_repository_tag_with_options_async(
        self,
        project_id: str,
        tag_name: str,
        request: codeup_20200414_models.DeleteRepositoryTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagResponse(),
            await self.do_roarequest_async('DeleteRepositoryTag', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/projects/{project_id}/repository/tags/{tag_name}', 'json', req, runtime)
        )

    def create_repository(
        self,
        request: codeup_20200414_models.CreateRepositoryRequest,
    ) -> codeup_20200414_models.CreateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_with_options(request, headers, runtime)

    async def create_repository_async(
        self,
        request: codeup_20200414_models.CreateRepositoryRequest,
    ) -> codeup_20200414_models.CreateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repository_with_options_async(request, headers, runtime)

    def create_repository_with_options(
        self,
        request: codeup_20200414_models.CreateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.sync):
            query['Sync'] = request.sync
        if not UtilClient.is_unset(request.create_parent_path):
            query['CreateParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryResponse(),
            self.do_roarequest('CreateRepository', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects', 'json', req, runtime)
        )

    async def create_repository_with_options_async(
        self,
        request: codeup_20200414_models.CreateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.sync):
            query['Sync'] = request.sync
        if not UtilClient.is_unset(request.create_parent_path):
            query['CreateParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryResponse(),
            await self.do_roarequest_async('CreateRepository', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects', 'json', req, runtime)
        )

    def get_code_completion(
        self,
        service_name: str,
        request: codeup_20200414_models.GetCodeCompletionRequest,
    ) -> codeup_20200414_models.GetCodeCompletionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_code_completion_with_options(service_name, request, headers, runtime)

    async def get_code_completion_async(
        self,
        service_name: str,
        request: codeup_20200414_models.GetCodeCompletionRequest,
    ) -> codeup_20200414_models.GetCodeCompletionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_code_completion_with_options_async(service_name, request, headers, runtime)

    def get_code_completion_with_options(
        self,
        service_name: str,
        request: codeup_20200414_models.GetCodeCompletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetCodeCompletionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_keys):
            query['FetchKeys'] = request.fetch_keys
        if not UtilClient.is_unset(request.is_encrypted):
            query['IsEncrypted'] = request.is_encrypted
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeCompletionResponse(),
            self.do_roarequest('GetCodeCompletion', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v2/service/invoke/{service_name}', 'json', req, runtime)
        )

    async def get_code_completion_with_options_async(
        self,
        service_name: str,
        request: codeup_20200414_models.GetCodeCompletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetCodeCompletionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_keys):
            query['FetchKeys'] = request.fetch_keys
        if not UtilClient.is_unset(request.is_encrypted):
            query['IsEncrypted'] = request.is_encrypted
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeCompletionResponse(),
            await self.do_roarequest_async('GetCodeCompletion', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v2/service/invoke/{service_name}', 'json', req, runtime)
        )

    def list_merge_requests(
        self,
        request: codeup_20200414_models.ListMergeRequestsRequest,
    ) -> codeup_20200414_models.ListMergeRequestsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_merge_requests_with_options(request, headers, runtime)

    async def list_merge_requests_async(
        self,
        request: codeup_20200414_models.ListMergeRequestsRequest,
    ) -> codeup_20200414_models.ListMergeRequestsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_merge_requests_with_options_async(request, headers, runtime)

    def list_merge_requests_with_options(
        self,
        request: codeup_20200414_models.ListMergeRequestsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListMergeRequestsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.project_id_list):
            query['ProjectIdList'] = request.project_id_list
        if not UtilClient.is_unset(request.author_codeup_id_list):
            query['AuthorCodeupIdList'] = request.author_codeup_id_list
        if not UtilClient.is_unset(request.author_id_list):
            query['AuthorIdList'] = request.author_id_list
        if not UtilClient.is_unset(request.assignee_codeup_id_list):
            query['AssigneeCodeupIdList'] = request.assignee_codeup_id_list
        if not UtilClient.is_unset(request.assignee_id_list):
            query['AssigneeIdList'] = request.assignee_id_list
        if not UtilClient.is_unset(request.subscriber_codeup_id_list):
            query['SubscriberCodeupIdList'] = request.subscriber_codeup_id_list
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.after_date):
            query['AfterDate'] = request.after_date
        if not UtilClient.is_unset(request.before_date):
            query['BeforeDate'] = request.before_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestsResponse(),
            self.do_roarequest('ListMergeRequests', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/merge_requests/advanced_search', 'json', req, runtime)
        )

    async def list_merge_requests_with_options_async(
        self,
        request: codeup_20200414_models.ListMergeRequestsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListMergeRequestsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.project_id_list):
            query['ProjectIdList'] = request.project_id_list
        if not UtilClient.is_unset(request.author_codeup_id_list):
            query['AuthorCodeupIdList'] = request.author_codeup_id_list
        if not UtilClient.is_unset(request.author_id_list):
            query['AuthorIdList'] = request.author_id_list
        if not UtilClient.is_unset(request.assignee_codeup_id_list):
            query['AssigneeCodeupIdList'] = request.assignee_codeup_id_list
        if not UtilClient.is_unset(request.assignee_id_list):
            query['AssigneeIdList'] = request.assignee_id_list
        if not UtilClient.is_unset(request.subscriber_codeup_id_list):
            query['SubscriberCodeupIdList'] = request.subscriber_codeup_id_list
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.after_date):
            query['AfterDate'] = request.after_date
        if not UtilClient.is_unset(request.before_date):
            query['BeforeDate'] = request.before_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestsResponse(),
            await self.do_roarequest_async('ListMergeRequests', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/merge_requests/advanced_search', 'json', req, runtime)
        )

    def list_organization_security_scores(
        self,
        request: codeup_20200414_models.ListOrganizationSecurityScoresRequest,
    ) -> codeup_20200414_models.ListOrganizationSecurityScoresResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organization_security_scores_with_options(request, headers, runtime)

    async def list_organization_security_scores_async(
        self,
        request: codeup_20200414_models.ListOrganizationSecurityScoresRequest,
    ) -> codeup_20200414_models.ListOrganizationSecurityScoresResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_organization_security_scores_with_options_async(request, headers, runtime)

    def list_organization_security_scores_with_options(
        self,
        request: codeup_20200414_models.ListOrganizationSecurityScoresRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListOrganizationSecurityScoresResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationSecurityScoresResponse(),
            self.do_roarequest('ListOrganizationSecurityScores', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/organization/security/scores', 'json', req, runtime)
        )

    async def list_organization_security_scores_with_options_async(
        self,
        request: codeup_20200414_models.ListOrganizationSecurityScoresRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListOrganizationSecurityScoresResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationSecurityScoresResponse(),
            await self.do_roarequest_async('ListOrganizationSecurityScores', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/organization/security/scores', 'json', req, runtime)
        )

    def get_file_blobs(
        self,
        project_id: str,
        request: codeup_20200414_models.GetFileBlobsRequest,
    ) -> codeup_20200414_models.GetFileBlobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_blobs_with_options(project_id, request, headers, runtime)

    async def get_file_blobs_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetFileBlobsRequest,
    ) -> codeup_20200414_models.GetFileBlobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_blobs_with_options_async(project_id, request, headers, runtime)

    def get_file_blobs_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.GetFileBlobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetFileBlobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.ref):
            query['Ref'] = request.ref
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileBlobsResponse(),
            self.do_roarequest('GetFileBlobs', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/blobs', 'json', req, runtime)
        )

    async def get_file_blobs_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetFileBlobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetFileBlobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.ref):
            query['Ref'] = request.ref
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileBlobsResponse(),
            await self.do_roarequest_async('GetFileBlobs', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/repository/blobs', 'json', req, runtime)
        )

    def merge_merge_request(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.MergeMergeRequestRequest,
    ) -> codeup_20200414_models.MergeMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.merge_merge_request_with_options(project_id, merge_request_id, request, headers, runtime)

    async def merge_merge_request_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.MergeMergeRequestRequest,
    ) -> codeup_20200414_models.MergeMergeRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.merge_merge_request_with_options_async(project_id, merge_request_id, request, headers, runtime)

    def merge_merge_request_with_options(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.MergeMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.MergeMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.MergeMergeRequestResponse(),
            self.do_roarequest('MergeMergeRequest', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/merge_request/{merge_request_id}/merge', 'json', req, runtime)
        )

    async def merge_merge_request_with_options_async(
        self,
        project_id: str,
        merge_request_id: str,
        request: codeup_20200414_models.MergeMergeRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.MergeMergeRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.MergeMergeRequestResponse(),
            await self.do_roarequest_async('MergeMergeRequest', '2020-04-14', 'HTTPS', 'PUT', 'AK', f'/api/v3/projects/{project_id}/merge_request/{merge_request_id}/merge', 'json', req, runtime)
        )

    def delete_group_member(
        self,
        group_id: str,
        user_id: str,
        request: codeup_20200414_models.DeleteGroupMemberRequest,
    ) -> codeup_20200414_models.DeleteGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_member_with_options(group_id, user_id, request, headers, runtime)

    async def delete_group_member_async(
        self,
        group_id: str,
        user_id: str,
        request: codeup_20200414_models.DeleteGroupMemberRequest,
    ) -> codeup_20200414_models.DeleteGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_group_member_with_options_async(group_id, user_id, request, headers, runtime)

    def delete_group_member_with_options(
        self,
        group_id: str,
        user_id: str,
        request: codeup_20200414_models.DeleteGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteGroupMemberResponse(),
            self.do_roarequest('DeleteGroupMember', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/groups/{group_id}/members/{user_id}', 'json', req, runtime)
        )

    async def delete_group_member_with_options_async(
        self,
        group_id: str,
        user_id: str,
        request: codeup_20200414_models.DeleteGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteGroupMemberResponse(),
            await self.do_roarequest_async('DeleteGroupMember', '2020-04-14', 'HTTPS', 'DELETE', 'AK', f'/api/v3/groups/{group_id}/members/{user_id}', 'json', req, runtime)
        )

    def list_repository_member_with_inherited(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryMemberWithInheritedRequest,
    ) -> codeup_20200414_models.ListRepositoryMemberWithInheritedResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_member_with_inherited_with_options(project_id, request, headers, runtime)

    async def list_repository_member_with_inherited_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryMemberWithInheritedRequest,
    ) -> codeup_20200414_models.ListRepositoryMemberWithInheritedResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_member_with_inherited_with_options_async(project_id, request, headers, runtime)

    def list_repository_member_with_inherited_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryMemberWithInheritedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryMemberWithInheritedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberWithInheritedResponse(),
            self.do_roarequest('ListRepositoryMemberWithInherited', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/all_members', 'json', req, runtime)
        )

    async def list_repository_member_with_inherited_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryMemberWithInheritedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryMemberWithInheritedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberWithInheritedResponse(),
            await self.do_roarequest_async('ListRepositoryMemberWithInherited', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/all_members', 'json', req, runtime)
        )

    def get_group_detail(
        self,
        request: codeup_20200414_models.GetGroupDetailRequest,
    ) -> codeup_20200414_models.GetGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_detail_with_options(request, headers, runtime)

    async def get_group_detail_async(
        self,
        request: codeup_20200414_models.GetGroupDetailRequest,
    ) -> codeup_20200414_models.GetGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_group_detail_with_options_async(request, headers, runtime)

    def get_group_detail_with_options(
        self,
        request: codeup_20200414_models.GetGroupDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetGroupDetailResponse(),
            self.do_roarequest('GetGroupDetail', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/groups/detail', 'json', req, runtime)
        )

    async def get_group_detail_with_options_async(
        self,
        request: codeup_20200414_models.GetGroupDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetGroupDetailResponse(),
            await self.do_roarequest_async('GetGroupDetail', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/groups/detail', 'json', req, runtime)
        )

    def get_codeup_organization(
        self,
        organization_identity: str,
        request: codeup_20200414_models.GetCodeupOrganizationRequest,
    ) -> codeup_20200414_models.GetCodeupOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_codeup_organization_with_options(organization_identity, request, headers, runtime)

    async def get_codeup_organization_async(
        self,
        organization_identity: str,
        request: codeup_20200414_models.GetCodeupOrganizationRequest,
    ) -> codeup_20200414_models.GetCodeupOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_codeup_organization_with_options_async(organization_identity, request, headers, runtime)

    def get_codeup_organization_with_options(
        self,
        organization_identity: str,
        request: codeup_20200414_models.GetCodeupOrganizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetCodeupOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeupOrganizationResponse(),
            self.do_roarequest('GetCodeupOrganization', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/organization/{organization_identity}', 'json', req, runtime)
        )

    async def get_codeup_organization_with_options_async(
        self,
        organization_identity: str,
        request: codeup_20200414_models.GetCodeupOrganizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetCodeupOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeupOrganizationResponse(),
            await self.do_roarequest_async('GetCodeupOrganization', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/organization/{organization_identity}', 'json', req, runtime)
        )

    def get_organization_security_center_status(
        self,
        request: codeup_20200414_models.GetOrganizationSecurityCenterStatusRequest,
    ) -> codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_organization_security_center_status_with_options(request, headers, runtime)

    async def get_organization_security_center_status_async(
        self,
        request: codeup_20200414_models.GetOrganizationSecurityCenterStatusRequest,
    ) -> codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_organization_security_center_status_with_options_async(request, headers, runtime)

    def get_organization_security_center_status_with_options(
        self,
        request: codeup_20200414_models.GetOrganizationSecurityCenterStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse(),
            self.do_roarequest('GetOrganizationSecurityCenterStatus', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/organization/security/status', 'json', req, runtime)
        )

    async def get_organization_security_center_status_with_options_async(
        self,
        request: codeup_20200414_models.GetOrganizationSecurityCenterStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse(),
            await self.do_roarequest_async('GetOrganizationSecurityCenterStatus', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/organization/security/status', 'json', req, runtime)
        )

    def list_repository_branches(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryBranchesRequest,
    ) -> codeup_20200414_models.ListRepositoryBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_branches_with_options(project_id, request, headers, runtime)

    async def list_repository_branches_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryBranchesRequest,
    ) -> codeup_20200414_models.ListRepositoryBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_branches_with_options_async(project_id, request, headers, runtime)

    def list_repository_branches_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryBranchesResponse(),
            self.do_roarequest('ListRepositoryBranches', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/branches', 'json', req, runtime)
        )

    async def list_repository_branches_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryBranchesResponse(),
            await self.do_roarequest_async('ListRepositoryBranches', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/branches', 'json', req, runtime)
        )

    def create_branch(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateBranchRequest,
    ) -> codeup_20200414_models.CreateBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_branch_with_options(project_id, request, headers, runtime)

    async def create_branch_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateBranchRequest,
    ) -> codeup_20200414_models.CreateBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_branch_with_options_async(project_id, request, headers, runtime)

    def create_branch_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateBranchResponse(),
            self.do_roarequest('CreateBranch', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/repository/branches', 'json', req, runtime)
        )

    async def create_branch_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.CreateBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.CreateBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateBranchResponse(),
            await self.do_roarequest_async('CreateBranch', '2020-04-14', 'HTTPS', 'POST', 'AK', f'/api/v3/projects/{project_id}/repository/branches', 'json', req, runtime)
        )

    def list_group_repositories(
        self,
        identity: str,
        request: codeup_20200414_models.ListGroupRepositoriesRequest,
    ) -> codeup_20200414_models.ListGroupRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_repositories_with_options(identity, request, headers, runtime)

    async def list_group_repositories_async(
        self,
        identity: str,
        request: codeup_20200414_models.ListGroupRepositoriesRequest,
    ) -> codeup_20200414_models.ListGroupRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_group_repositories_with_options_async(identity, request, headers, runtime)

    def list_group_repositories_with_options(
        self,
        identity: str,
        request: codeup_20200414_models.ListGroupRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListGroupRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupRepositoriesResponse(),
            self.do_roarequest('ListGroupRepositories', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/groups/{identity}/projects', 'json', req, runtime)
        )

    async def list_group_repositories_with_options_async(
        self,
        identity: str,
        request: codeup_20200414_models.ListGroupRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListGroupRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupRepositoriesResponse(),
            await self.do_roarequest_async('ListGroupRepositories', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/groups/{identity}/projects', 'json', req, runtime)
        )

    def get_repository_tag_v2(
        self,
        project_id: str,
        request: codeup_20200414_models.GetRepositoryTagV2Request,
    ) -> codeup_20200414_models.GetRepositoryTagV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_tag_v2with_options(project_id, request, headers, runtime)

    async def get_repository_tag_v2_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetRepositoryTagV2Request,
    ) -> codeup_20200414_models.GetRepositoryTagV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_tag_v2with_options_async(project_id, request, headers, runtime)

    def get_repository_tag_v2with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.GetRepositoryTagV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetRepositoryTagV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagV2Response(),
            self.do_roarequest('GetRepositoryTagV2', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/tag/info', 'json', req, runtime)
        )

    async def get_repository_tag_v2with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetRepositoryTagV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetRepositoryTagV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagV2Response(),
            await self.do_roarequest_async('GetRepositoryTagV2', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/repository/tag/info', 'json', req, runtime)
        )

    def get_merge_request_setting(
        self,
        project_id: str,
        request: codeup_20200414_models.GetMergeRequestSettingRequest,
    ) -> codeup_20200414_models.GetMergeRequestSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_merge_request_setting_with_options(project_id, request, headers, runtime)

    async def get_merge_request_setting_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetMergeRequestSettingRequest,
    ) -> codeup_20200414_models.GetMergeRequestSettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_merge_request_setting_with_options_async(project_id, request, headers, runtime)

    def get_merge_request_setting_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.GetMergeRequestSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetMergeRequestSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestSettingResponse(),
            self.do_roarequest('GetMergeRequestSetting', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/settings/merge_requests', 'json', req, runtime)
        )

    async def get_merge_request_setting_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.GetMergeRequestSettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetMergeRequestSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestSettingResponse(),
            await self.do_roarequest_async('GetMergeRequestSetting', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v4/projects/{project_id}/settings/merge_requests', 'json', req, runtime)
        )

    def list_repository_webhook(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryWebhookRequest,
    ) -> codeup_20200414_models.ListRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_webhook_with_options(project_id, request, headers, runtime)

    async def list_repository_webhook_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryWebhookRequest,
    ) -> codeup_20200414_models.ListRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_webhook_with_options_async(project_id, request, headers, runtime)

    def list_repository_webhook_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryWebhookResponse(),
            self.do_roarequest('ListRepositoryWebhook', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/hooks', 'json', req, runtime)
        )

    async def list_repository_webhook_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.ListRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryWebhookResponse(),
            await self.do_roarequest_async('ListRepositoryWebhook', '2020-04-14', 'HTTPS', 'GET', 'AK', f'/api/v3/projects/{project_id}/hooks', 'json', req, runtime)
        )
