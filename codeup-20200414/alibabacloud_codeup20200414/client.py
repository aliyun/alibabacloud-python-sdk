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
        self._signature_algorithm = 'v2'
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
        params = open_api_models.Params(
            action='AcceptMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/accept',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AcceptMergeRequestResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='AcceptMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/accept',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AcceptMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='AddGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddGroupMemberResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='AddGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='AddRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='AddRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddRepositoryMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='AddWebhook',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/hooks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddWebhookResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='AddWebhook',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/hooks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.AddWebhookResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.ref):
            body['ref'] = request.ref
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateBranchResponse(),
            self.call_api(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.ref):
            body['ref'] = request.ref
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateBranchResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateFile',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateFile',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateFileResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_requests',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_requests',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateMergeRequestComment',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/comments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestCommentResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateMergeRequestComment',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/comments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateMergeRequestCommentResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.create_parent_path):
            query['CreateParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.sync):
            query['Sync'] = request.sync
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gitignore_type):
            body['gitignoreType'] = request.gitignore_type
        if not UtilClient.is_unset(request.import_account):
            body['importAccount'] = request.import_account
        if not UtilClient.is_unset(request.import_demo_project):
            body['importDemoProject'] = request.import_demo_project
        if not UtilClient.is_unset(request.import_repo_type):
            body['importRepoType'] = request.import_repo_type
        if not UtilClient.is_unset(request.import_token):
            body['importToken'] = request.import_token
        if not UtilClient.is_unset(request.import_token_encrypted):
            body['importTokenEncrypted'] = request.import_token_encrypted
        if not UtilClient.is_unset(request.import_url):
            body['importUrl'] = request.import_url
        if not UtilClient.is_unset(request.init_standard_service):
            body['initStandardService'] = request.init_standard_service
        if not UtilClient.is_unset(request.is_crypto_enabled):
            body['isCryptoEnabled'] = request.is_crypto_enabled
        if not UtilClient.is_unset(request.local_import_url):
            body['localImportUrl'] = request.local_import_url
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            body['namespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.readme_type):
            body['readmeType'] = request.readme_type
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.create_parent_path):
            query['CreateParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.sync):
            query['Sync'] = request.sync
        body = {}
        if not UtilClient.is_unset(request.avatar_url):
            body['avatarUrl'] = request.avatar_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gitignore_type):
            body['gitignoreType'] = request.gitignore_type
        if not UtilClient.is_unset(request.import_account):
            body['importAccount'] = request.import_account
        if not UtilClient.is_unset(request.import_demo_project):
            body['importDemoProject'] = request.import_demo_project
        if not UtilClient.is_unset(request.import_repo_type):
            body['importRepoType'] = request.import_repo_type
        if not UtilClient.is_unset(request.import_token):
            body['importToken'] = request.import_token
        if not UtilClient.is_unset(request.import_token_encrypted):
            body['importTokenEncrypted'] = request.import_token_encrypted
        if not UtilClient.is_unset(request.import_url):
            body['importUrl'] = request.import_url
        if not UtilClient.is_unset(request.init_standard_service):
            body['initStandardService'] = request.init_standard_service
        if not UtilClient.is_unset(request.is_crypto_enabled):
            body['isCryptoEnabled'] = request.is_crypto_enabled
        if not UtilClient.is_unset(request.local_import_url):
            body['localImportUrl'] = request.local_import_url
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            body['namespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.readme_type):
            body['readmeType'] = request.readme_type
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateRepositoryDeployKey',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/keys',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryDeployKeyResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateRepositoryDeployKey',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/keys',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryDeployKeyResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateRepositoryGroup',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryGroupResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateRepositoryGroup',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateRepositoryProtectedBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/protect_branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryProtectedBranchResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateRepositoryProtectedBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/protect_branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateRepositoryProtectedBranchResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/user/keys',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateSshKeyResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/user/keys',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateSshKeyResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateTag',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateTag',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/branches/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteBranchResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/branches/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteBranchResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            query['CommitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/files',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.branch_name):
            query['BranchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            query['CommitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/files',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteGroupMemberResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryGroup',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(group_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryGroupResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryGroup',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(group_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

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
        params = open_api_models.Params(
            action='DeleteRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository_member_with_extern_uid(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryMemberWithExternUidRequest,
    ) -> codeup_20200414_models.DeleteRepositoryMemberWithExternUidResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_member_with_extern_uid_with_options(project_id, request, headers, runtime)

    async def delete_repository_member_with_extern_uid_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryMemberWithExternUidRequest,
    ) -> codeup_20200414_models.DeleteRepositoryMemberWithExternUidResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_member_with_extern_uid_with_options_async(project_id, request, headers, runtime)

    def delete_repository_member_with_extern_uid_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryMemberWithExternUidRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryMemberWithExternUidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.extern_user_id):
            query['ExternUserId'] = request.extern_user_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryMemberWithExternUid',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberWithExternUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_member_with_extern_uid_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.DeleteRepositoryMemberWithExternUidRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.DeleteRepositoryMemberWithExternUidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.extern_user_id):
            query['ExternUserId'] = request.extern_user_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryMemberWithExternUid',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryMemberWithExternUidResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryProtectedBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/protect_branches/{OpenApiUtilClient.get_encode_param(protected_branch_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryProtectedBranchResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryProtectedBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/protect_branches/{OpenApiUtilClient.get_encode_param(protected_branch_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryProtectedBranchResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryTag',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tags/{OpenApiUtilClient.get_encode_param(tag_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryTag',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tags/{OpenApiUtilClient.get_encode_param(tag_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryTagV2',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tag/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagV2Response(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryTagV2',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tag/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryTagV2Response(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryWebhook',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/hooks/{OpenApiUtilClient.get_encode_param(webhook_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteRepositoryWebhook',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/hooks/{OpenApiUtilClient.get_encode_param(webhook_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.DeleteRepositoryWebhookResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='EnableRepositoryDeployKey',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/keys/{OpenApiUtilClient.get_encode_param(key_id)}/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.EnableRepositoryDeployKeyResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='EnableRepositoryDeployKey',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/keys/{OpenApiUtilClient.get_encode_param(key_id)}/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.EnableRepositoryDeployKeyResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetBranchInfo',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/branches/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetBranchInfoResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetBranchInfo',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/branches/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetBranchInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetCodeCompletion',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v2/service/invoke/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeCompletionResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetCodeCompletion',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v2/service/invoke/{OpenApiUtilClient.get_encode_param(service_name)}',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeCompletionResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetCodeupOrganization',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization/{OpenApiUtilClient.get_encode_param(organization_identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeupOrganizationResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetCodeupOrganization',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization/{OpenApiUtilClient.get_encode_param(organization_identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetCodeupOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.ref):
            query['Ref'] = request.ref
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileBlobs',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/blobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileBlobsResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.ref):
            query['Ref'] = request.ref
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileBlobs',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/blobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileBlobsResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['Sha'] = request.sha
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileLastCommit',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/files/last_commit',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileLastCommitResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['Sha'] = request.sha
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileLastCommit',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/files/last_commit',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetFileLastCommitResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetGroupDetail',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetGroupDetailResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetGroupDetail',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetMergeRequestApproveStatus',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/approve_status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestApproveStatusResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetMergeRequestApproveStatus',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/approve_status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestApproveStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetMergeRequestDetail',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestDetailResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetMergeRequestDetail',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetMergeRequestSetting',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/settings/merge_requests',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestSettingResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetMergeRequestSetting',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/settings/merge_requests',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetMergeRequestSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_organization_repository_setting(
        self,
        request: codeup_20200414_models.GetOrganizationRepositorySettingRequest,
    ) -> codeup_20200414_models.GetOrganizationRepositorySettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_organization_repository_setting_with_options(request, headers, runtime)

    async def get_organization_repository_setting_async(
        self,
        request: codeup_20200414_models.GetOrganizationRepositorySettingRequest,
    ) -> codeup_20200414_models.GetOrganizationRepositorySettingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_organization_repository_setting_with_options_async(request, headers, runtime)

    def get_organization_repository_setting_with_options(
        self,
        request: codeup_20200414_models.GetOrganizationRepositorySettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetOrganizationRepositorySettingResponse:
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
        params = open_api_models.Params(
            action='GetOrganizationRepositorySetting',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization/settings/repo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationRepositorySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_organization_repository_setting_with_options_async(
        self,
        request: codeup_20200414_models.GetOrganizationRepositorySettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.GetOrganizationRepositorySettingResponse:
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
        params = open_api_models.Params(
            action='GetOrganizationRepositorySetting',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization/settings/repo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationRepositorySettingResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetOrganizationSecurityCenterStatus',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization/security/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetOrganizationSecurityCenterStatus',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization/security/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetOrganizationSecurityCenterStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetProjectMemberResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRepositoryCommit',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/commits/{OpenApiUtilClient.get_encode_param(sha)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryCommitResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRepositoryCommit',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/commits/{OpenApiUtilClient.get_encode_param(sha)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryCommitResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRepositoryInfo',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryInfoResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRepositoryInfo',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRepositoryTag',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tags/{OpenApiUtilClient.get_encode_param(tag_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRepositoryTag',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tags/{OpenApiUtilClient.get_encode_param(tag_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRepositoryTagV2',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tag/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagV2Response(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetRepositoryTagV2',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tag/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetRepositoryTagV2Response(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/user/current',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/user/current',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.GetUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def is_sls_user_authrized_codeup(
        self,
        request: codeup_20200414_models.IsSlsUserAuthrizedCodeupRequest,
    ) -> codeup_20200414_models.IsSlsUserAuthrizedCodeupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.is_sls_user_authrized_codeup_with_options(request, headers, runtime)

    async def is_sls_user_authrized_codeup_async(
        self,
        request: codeup_20200414_models.IsSlsUserAuthrizedCodeupRequest,
    ) -> codeup_20200414_models.IsSlsUserAuthrizedCodeupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.is_sls_user_authrized_codeup_with_options_async(request, headers, runtime)

    def is_sls_user_authrized_codeup_with_options(
        self,
        request: codeup_20200414_models.IsSlsUserAuthrizedCodeupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.IsSlsUserAuthrizedCodeupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_sub_user_id):
            body['aliyunSubUserId'] = request.aliyun_sub_user_id
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsSlsUserAuthrizedCodeup',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/repository/is_codeup_authrized',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.IsSlsUserAuthrizedCodeupResponse(),
            self.call_api(params, req, runtime)
        )

    async def is_sls_user_authrized_codeup_with_options_async(
        self,
        request: codeup_20200414_models.IsSlsUserAuthrizedCodeupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.IsSlsUserAuthrizedCodeupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_sub_user_id):
            body['aliyunSubUserId'] = request.aliyun_sub_user_id
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsSlsUserAuthrizedCodeup',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/repository/is_codeup_authrized',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.IsSlsUserAuthrizedCodeupResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupMemberResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupRepositories',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(identity)}/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupRepositoriesResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.is_member):
            query['IsMember'] = request.is_member
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupRepositories',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(identity)}/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.include_personal):
            query['IncludePersonal'] = request.include_personal
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/all',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.include_personal):
            query['IncludePersonal'] = request.include_personal
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/all',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.from_commit):
            query['FromCommit'] = request.from_commit
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.to_commit):
            query['ToCommit'] = request.to_commit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequestComments',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/comments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestCommentsResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.from_commit):
            query['FromCommit'] = request.from_commit
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.to_commit):
            query['ToCommit'] = request.to_commit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequestComments',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/comments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestCommentsResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.after_date):
            query['AfterDate'] = request.after_date
        if not UtilClient.is_unset(request.assignee_codeup_id_list):
            query['AssigneeCodeupIdList'] = request.assignee_codeup_id_list
        if not UtilClient.is_unset(request.assignee_id_list):
            query['AssigneeIdList'] = request.assignee_id_list
        if not UtilClient.is_unset(request.author_codeup_id_list):
            query['AuthorCodeupIdList'] = request.author_codeup_id_list
        if not UtilClient.is_unset(request.author_id_list):
            query['AuthorIdList'] = request.author_id_list
        if not UtilClient.is_unset(request.before_date):
            query['BeforeDate'] = request.before_date
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id_list):
            query['ProjectIdList'] = request.project_id_list
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.subscriber_codeup_id_list):
            query['SubscriberCodeupIdList'] = request.subscriber_codeup_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequests',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/merge_requests/advanced_search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestsResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.after_date):
            query['AfterDate'] = request.after_date
        if not UtilClient.is_unset(request.assignee_codeup_id_list):
            query['AssigneeCodeupIdList'] = request.assignee_codeup_id_list
        if not UtilClient.is_unset(request.assignee_id_list):
            query['AssigneeIdList'] = request.assignee_id_list
        if not UtilClient.is_unset(request.author_codeup_id_list):
            query['AuthorCodeupIdList'] = request.author_codeup_id_list
        if not UtilClient.is_unset(request.author_id_list):
            query['AuthorIdList'] = request.author_id_list
        if not UtilClient.is_unset(request.before_date):
            query['BeforeDate'] = request.before_date
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id_list):
            query['ProjectIdList'] = request.project_id_list
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.subscriber_codeup_id_list):
            query['SubscriberCodeupIdList'] = request.subscriber_codeup_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMergeRequests',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/merge_requests/advanced_search',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListMergeRequestsResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListOrganizationSecurityScores',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization/security/scores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationSecurityScoresResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListOrganizationSecurityScores',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization/security/scores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationSecurityScoresResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.access_level):
            query['AccessLevel'] = request.access_level
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.min_access_level):
            query['MinAccessLevel'] = request.min_access_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizations',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organizations_with_options_async(
        self,
        request: codeup_20200414_models.ListOrganizationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListOrganizationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level):
            query['AccessLevel'] = request.access_level
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.min_access_level):
            query['MinAccessLevel'] = request.min_access_level
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizations',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/organization',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListOrganizationsResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.archive):
            query['Archive'] = request.archive
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositories',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/all',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoriesResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.archive):
            query['Archive'] = request.archive
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositories',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/all',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryBranches',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryBranchesResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryBranches',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryBranchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_code(
        self,
        request: codeup_20200414_models.ListRepositoryCodeRequest,
    ) -> codeup_20200414_models.ListRepositoryCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_code_with_options(request, headers, runtime)

    async def list_repository_code_async(
        self,
        request: codeup_20200414_models.ListRepositoryCodeRequest,
    ) -> codeup_20200414_models.ListRepositoryCodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_code_with_options_async(request, headers, runtime)

    def list_repository_code_with_options(
        self,
        request: codeup_20200414_models.ListRepositoryCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.is_code_block):
            body['IsCodeBlock'] = request.is_code_block
        if not UtilClient.is_unset(request.key_word):
            body['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repository_path):
            body['RepositoryPath'] = request.repository_path
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRepositoryCode',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/search/v3/code',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_code_with_options_async(
        self,
        request: codeup_20200414_models.ListRepositoryCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.ListRepositoryCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.is_code_block):
            body['IsCodeBlock'] = request.is_code_block
        if not UtilClient.is_unset(request.key_word):
            body['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repository_path):
            body['RepositoryPath'] = request.repository_path
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort):
            body['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRepositoryCode',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/search/v3/code',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCodeResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.context_line):
            query['ContextLine'] = request.context_line
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommitDiff',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/commits/{OpenApiUtilClient.get_encode_param(sha)}/diff',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitDiffResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.context_line):
            query['ContextLine'] = request.context_line
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommitDiff',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/commits/{OpenApiUtilClient.get_encode_param(sha)}/diff',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitDiffResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommits',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/commits',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitsResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommits',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/commits',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryCommitsResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListRepositoryMemberWithInherited',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/all_members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberWithInheritedResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListRepositoryMemberWithInherited',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/all_members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryMemberWithInheritedResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListRepositoryProtectedBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/protect_branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryProtectedBranchResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListRepositoryProtectedBranch',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/protect_branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryProtectedBranchResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTags',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTagsResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.show_signature):
            query['ShowSignature'] = request.show_signature
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTags',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTree',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tree',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTreeResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.ref_name):
            query['RefName'] = request.ref_name
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTree',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/tree',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryTreeResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListRepositoryWebhook',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/hooks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListRepositoryWebhook',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/hooks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.ListRepositoryWebhookResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='MergeMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/merge',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.MergeMergeRequestResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='MergeMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}/merge',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.MergeMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sls_relation(
        self,
        request: codeup_20200414_models.QuerySlsRelationRequest,
    ) -> codeup_20200414_models.QuerySlsRelationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_sls_relation_with_options(request, headers, runtime)

    async def query_sls_relation_async(
        self,
        request: codeup_20200414_models.QuerySlsRelationRequest,
    ) -> codeup_20200414_models.QuerySlsRelationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_sls_relation_with_options_async(request, headers, runtime)

    def query_sls_relation_with_options(
        self,
        request: codeup_20200414_models.QuerySlsRelationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.QuerySlsRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySlsRelation',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/repository/query_sls_relation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.QuerySlsRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sls_relation_with_options_async(
        self,
        request: codeup_20200414_models.QuerySlsRelationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.QuerySlsRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySlsRelation',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/repository/query_sls_relation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.QuerySlsRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def related_sls_log_store(
        self,
        request: codeup_20200414_models.RelatedSlsLogStoreRequest,
    ) -> codeup_20200414_models.RelatedSlsLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.related_sls_log_store_with_options(request, headers, runtime)

    async def related_sls_log_store_async(
        self,
        request: codeup_20200414_models.RelatedSlsLogStoreRequest,
    ) -> codeup_20200414_models.RelatedSlsLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.related_sls_log_store_with_options_async(request, headers, runtime)

    def related_sls_log_store_with_options(
        self,
        request: codeup_20200414_models.RelatedSlsLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.RelatedSlsLogStoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.default_viewer):
            body['defaultViewer'] = request.default_viewer
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RelatedSlsLogStore',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/repository/related_to_sls_log_store',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.RelatedSlsLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def related_sls_log_store_with_options_async(
        self,
        request: codeup_20200414_models.RelatedSlsLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.RelatedSlsLogStoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.default_viewer):
            body['defaultViewer'] = request.default_viewer
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RelatedSlsLogStore',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/repository/related_to_sls_log_store',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.RelatedSlsLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_repository_mirror_sync(
        self,
        project_id: str,
        request: codeup_20200414_models.TriggerRepositoryMirrorSyncRequest,
    ) -> codeup_20200414_models.TriggerRepositoryMirrorSyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_repository_mirror_sync_with_options(project_id, request, headers, runtime)

    async def trigger_repository_mirror_sync_async(
        self,
        project_id: str,
        request: codeup_20200414_models.TriggerRepositoryMirrorSyncRequest,
    ) -> codeup_20200414_models.TriggerRepositoryMirrorSyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.trigger_repository_mirror_sync_with_options_async(project_id, request, headers, runtime)

    def trigger_repository_mirror_sync_with_options(
        self,
        project_id: str,
        request: codeup_20200414_models.TriggerRepositoryMirrorSyncRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.TriggerRepositoryMirrorSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRepositoryMirrorSync',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.TriggerRepositoryMirrorSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_repository_mirror_sync_with_options_async(
        self,
        project_id: str,
        request: codeup_20200414_models.TriggerRepositoryMirrorSyncRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.TriggerRepositoryMirrorSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRepositoryMirrorSync',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.TriggerRepositoryMirrorSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_related_sls_log_store(
        self,
        request: codeup_20200414_models.UnRelatedSlsLogStoreRequest,
    ) -> codeup_20200414_models.UnRelatedSlsLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_related_sls_log_store_with_options(request, headers, runtime)

    async def un_related_sls_log_store_async(
        self,
        request: codeup_20200414_models.UnRelatedSlsLogStoreRequest,
    ) -> codeup_20200414_models.UnRelatedSlsLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_related_sls_log_store_with_options_async(request, headers, runtime)

    def un_related_sls_log_store_with_options(
        self,
        request: codeup_20200414_models.UnRelatedSlsLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UnRelatedSlsLogStoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnRelatedSlsLogStore',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/repository/unrelated_to_sls_log_store',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UnRelatedSlsLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_related_sls_log_store_with_options_async(
        self,
        request: codeup_20200414_models.UnRelatedSlsLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> codeup_20200414_models.UnRelatedSlsLogStoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.aliyun_user_id):
            body['aliyunUserId'] = request.aliyun_user_id
        if not UtilClient.is_unset(request.codeup_project_id):
            body['codeupProjectId'] = request.codeup_project_id
        if not UtilClient.is_unset(request.sls_log_store):
            body['slsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnRelatedSlsLogStore',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/repository/unrelated_to_sls_log_store',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UnRelatedSlsLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateFile',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/files',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateFileResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateFile',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/repository/files',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateFileResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateGroupMemberResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateGroupMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/groups/{OpenApiUtilClient.get_encode_param(group_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateMergeRequest',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_request/{OpenApiUtilClient.get_encode_param(merge_request_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateMergeRequestComment',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(merge_request_id)}/notes/{OpenApiUtilClient.get_encode_param(note_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestCommentResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateMergeRequestComment',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/merge_requests/{OpenApiUtilClient.get_encode_param(merge_request_id)}/notes/{OpenApiUtilClient.get_encode_param(note_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestCommentResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateMergeRequestSetting',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/settings/merge_requests',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestSettingResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateMergeRequestSetting',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v4/projects/{OpenApiUtilClient.get_encode_param(project_id)}/settings/merge_requests',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateMergeRequestSettingResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateRepositoryMember',
            version='2020-04-14',
            protocol='HTTPS',
            pathname=f'/api/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/members/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            codeup_20200414_models.UpdateRepositoryMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )
