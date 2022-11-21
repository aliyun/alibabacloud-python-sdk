# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_devops20210625 import models as devops_20210625_models
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
        self._endpoint = self.get_endpoint('devops', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_repository_member(
        self,
        repository_id: str,
        request: devops_20210625_models.AddRepositoryMemberRequest,
    ) -> devops_20210625_models.AddRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_repository_member_with_options(repository_id, request, headers, runtime)

    async def add_repository_member_async(
        self,
        repository_id: str,
        request: devops_20210625_models.AddRepositoryMemberRequest,
    ) -> devops_20210625_models.AddRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_repository_member_with_options_async(repository_id, request, headers, runtime)

    def add_repository_member_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.AddRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.aliyun_pks):
            body['aliyunPks'] = request.aliyun_pks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_repository_member_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.AddRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.aliyun_pks):
            body['aliyunPks'] = request.aliyun_pks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddRepositoryMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_webhook(
        self,
        repository_id: str,
        request: devops_20210625_models.AddWebhookRequest,
    ) -> devops_20210625_models.AddWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_webhook_with_options(repository_id, request, headers, runtime)

    async def add_webhook_async(
        self,
        repository_id: str,
        request: devops_20210625_models.AddWebhookRequest,
    ) -> devops_20210625_models.AddWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_webhook_with_options_async(repository_id, request, headers, runtime)

    def add_webhook_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.AddWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_ssl_verification):
            body['enableSslVerification'] = request.enable_ssl_verification
        if not UtilClient.is_unset(request.merge_requests_events):
            body['mergeRequestsEvents'] = request.merge_requests_events
        if not UtilClient.is_unset(request.note_events):
            body['noteEvents'] = request.note_events
        if not UtilClient.is_unset(request.push_events):
            body['pushEvents'] = request.push_events
        if not UtilClient.is_unset(request.secret_token):
            body['secretToken'] = request.secret_token
        if not UtilClient.is_unset(request.tag_push_events):
            body['tagPushEvents'] = request.tag_push_events
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/webhooks/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_webhook_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.AddWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.AddWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.enable_ssl_verification):
            body['enableSslVerification'] = request.enable_ssl_verification
        if not UtilClient.is_unset(request.merge_requests_events):
            body['mergeRequestsEvents'] = request.merge_requests_events
        if not UtilClient.is_unset(request.note_events):
            body['noteEvents'] = request.note_events
        if not UtilClient.is_unset(request.push_events):
            body['pushEvents'] = request.push_events
        if not UtilClient.is_unset(request.secret_token):
            body['secretToken'] = request.secret_token
        if not UtilClient.is_unset(request.tag_push_events):
            body['tagPushEvents'] = request.tag_push_events
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/webhooks/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.AddWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_branch(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateBranchRequest,
    ) -> devops_20210625_models.CreateBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_branch_with_options(repository_id, request, headers, runtime)

    async def create_branch_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateBranchRequest,
    ) -> devops_20210625_models.CreateBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_branch_with_options_async(repository_id, request, headers, runtime)

    def create_branch_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
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
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_branch_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
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
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateFileRequest,
    ) -> devops_20210625_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_with_options(repository_id, request, headers, runtime)

    async def create_file_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateFileRequest,
    ) -> devops_20210625_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_file_with_options_async(repository_id, request, headers, runtime)

    def create_file_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_tag(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_flow_tag_with_options(organization_id, request, headers, runtime)

    async def create_flow_tag_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_flow_tag_with_options_async(organization_id, request, headers, runtime)

    def create_flow_tag_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_tag_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_tag_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_flow_tag_group_with_options(organization_id, request, headers, runtime)

    async def create_flow_tag_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_flow_tag_group_with_options_async(organization_id, request, headers, runtime)

    def create_flow_tag_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_host_group_with_options(organization_id, request, headers, runtime)

    async def create_host_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_host_group_with_options_async(organization_id, request, headers, runtime)

    def create_host_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateHostGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oauth_token(
        self,
        request: devops_20210625_models.CreateOAuthTokenRequest,
    ) -> devops_20210625_models.CreateOAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oauth_token_with_options(request, headers, runtime)

    async def create_oauth_token_async(
        self,
        request: devops_20210625_models.CreateOAuthTokenRequest,
    ) -> devops_20210625_models.CreateOAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_oauth_token_with_options_async(request, headers, runtime)

    def create_oauth_token_with_options(
        self,
        request: devops_20210625_models.CreateOAuthTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateOAuthTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['clientSecret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grantType'] = request.grant_type
        if not UtilClient.is_unset(request.login):
            body['login'] = request.login
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOAuthToken',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/login/oauth/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateOAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oauth_token_with_options_async(
        self,
        request: devops_20210625_models.CreateOAuthTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateOAuthTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['clientId'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['clientSecret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grantType'] = request.grant_type
        if not UtilClient.is_unset(request.login):
            body['login'] = request.login
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOAuthToken',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/login/oauth/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateOAuthTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineRequest,
    ) -> devops_20210625_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_with_options(organization_id, request, headers, runtime)

    async def create_pipeline_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineRequest,
    ) -> devops_20210625_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_with_options_async(organization_id, request, headers, runtime)

    def create_pipeline_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.basic_info):
            body['basicInfo'] = request.basic_info
        if not UtilClient.is_unset(request.pipeline_yaml):
            body['pipelineYaml'] = request.pipeline_yaml
        if not UtilClient.is_unset(request.settings):
            body['settings'] = request.settings
        if not UtilClient.is_unset(request.trigger_info):
            body['triggerInfo'] = request.trigger_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.basic_info):
            body['basicInfo'] = request.basic_info
        if not UtilClient.is_unset(request.pipeline_yaml):
            body['pipelineYaml'] = request.pipeline_yaml
        if not UtilClient.is_unset(request.settings):
            body['settings'] = request.settings
        if not UtilClient.is_unset(request.trigger_info):
            body['triggerInfo'] = request.trigger_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineGroupRequest,
    ) -> devops_20210625_models.CreatePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_group_with_options(organization_id, request, headers, runtime)

    async def create_pipeline_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineGroupRequest,
    ) -> devops_20210625_models.CreatePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_group_with_options_async(organization_id, request, headers, runtime)

    def create_pipeline_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreatePipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreatePipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreatePipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateProjectRequest,
    ) -> devops_20210625_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(organization_id, request, headers, runtime)

    async def create_project_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateProjectRequest,
    ) -> devops_20210625_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(organization_id, request, headers, runtime)

    def create_project_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_code):
            body['customCode'] = request.custom_code
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.template_identifier):
            body['templateIdentifier'] = request.template_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/createProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_code):
            body['customCode'] = request.custom_code
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.template_identifier):
            body['templateIdentifier'] = request.template_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/createProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_protectd_branch(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateProtectdBranchRequest,
    ) -> devops_20210625_models.CreateProtectdBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_protectd_branch_with_options(repository_id, request, headers, runtime)

    async def create_protectd_branch_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateProtectdBranchRequest,
    ) -> devops_20210625_models.CreateProtectdBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_protectd_branch_with_options_async(repository_id, request, headers, runtime)

    def create_protectd_branch_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateProtectdBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProtectdBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProtectdBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProtectdBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_protectd_branch_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.CreateProtectdBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateProtectdBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProtectdBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateProtectdBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repository(
        self,
        request: devops_20210625_models.CreateRepositoryRequest,
    ) -> devops_20210625_models.CreateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_with_options(request, headers, runtime)

    async def create_repository_async(
        self,
        request: devops_20210625_models.CreateRepositoryRequest,
    ) -> devops_20210625_models.CreateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repository_with_options_async(request, headers, runtime)

    def create_repository_with_options(
        self,
        request: devops_20210625_models.CreateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.create_parent_path):
            query['createParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sync):
            query['sync'] = request.sync
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
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repository_with_options_async(
        self,
        request: devops_20210625_models.CreateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.create_parent_path):
            query['createParentPath'] = request.create_parent_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sync):
            query['sync'] = request.sync
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
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_member(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_member_with_options(organization_id, resource_type, resource_id, request, headers, runtime)

    async def create_resource_member_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_member_with_options_async(organization_id, resource_type, resource_id, request, headers, runtime)

    def create_resource_member_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_member_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        request: devops_20210625_models.CreateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateResourceMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateResourceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sprint(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateSprintRequest,
    ) -> devops_20210625_models.CreateSprintResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sprint_with_options(organization_id, request, headers, runtime)

    async def create_sprint_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateSprintRequest,
    ) -> devops_20210625_models.CreateSprintResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sprint_with_options_async(organization_id, request, headers, runtime)

    def create_sprint_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateSprintRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSprintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.staff_ids):
            body['staffIds'] = request.staff_ids
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSprint',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSprintResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sprint_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateSprintRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSprintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.staff_ids):
            body['staffIds'] = request.staff_ids
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSprint',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSprintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ssh_key(
        self,
        organization_id: str,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ssh_key_with_options(organization_id, headers, runtime)

    async def create_ssh_key_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ssh_key_with_options_async(organization_id, headers, runtime)

    def create_ssh_key_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sshKey',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ssh_key_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateSshKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sshKey',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSshKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_variable_group(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_variable_group_with_options(organization_id, request, headers, runtime)

    async def create_variable_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_variable_group_with_options_async(organization_id, request, headers, runtime)

    def create_variable_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_variable_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateVariableGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workitem(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRequest,
    ) -> devops_20210625_models.CreateWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_with_options(organization_id, request, headers, runtime)

    async def create_workitem_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRequest,
    ) -> devops_20210625_models.CreateWorkitemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workitem_with_options_async(organization_id, request, headers, runtime)

    def create_workitem_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.description_format):
            body['descriptionFormat'] = request.description_format
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.parent):
            body['parent'] = request.parent
        if not UtilClient.is_unset(request.participant):
            body['participant'] = request.participant
        if not UtilClient.is_unset(request.space):
            body['space'] = request.space
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            body['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.sprint):
            body['sprint'] = request.sprint
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tracker):
            body['tracker'] = request.tracker
        if not UtilClient.is_unset(request.verifier):
            body['verifier'] = request.verifier
        if not UtilClient.is_unset(request.workitem_type):
            body['workitemType'] = request.workitem_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workitem_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assigned_to):
            body['assignedTo'] = request.assigned_to
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.description_format):
            body['descriptionFormat'] = request.description_format
        if not UtilClient.is_unset(request.field_value_list):
            body['fieldValueList'] = request.field_value_list
        if not UtilClient.is_unset(request.parent):
            body['parent'] = request.parent
        if not UtilClient.is_unset(request.participant):
            body['participant'] = request.participant
        if not UtilClient.is_unset(request.space):
            body['space'] = request.space
        if not UtilClient.is_unset(request.space_identifier):
            body['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            body['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.sprint):
            body['sprint'] = request.sprint
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.tracker):
            body['tracker'] = request.tracker
        if not UtilClient.is_unset(request.verifier):
            body['verifier'] = request.verifier
        if not UtilClient.is_unset(request.workitem_type):
            body['workitemType'] = request.workitem_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workitem_comment(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemCommentRequest,
    ) -> devops_20210625_models.CreateWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_comment_with_options(organization_id, request, headers, runtime)

    async def create_workitem_comment_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemCommentRequest,
    ) -> devops_20210625_models.CreateWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workitem_comment_with_options_async(organization_id, request, headers, runtime)

    def create_workitem_comment_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/comment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workitem_comment_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/comment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workitem_estimate(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemEstimateRequest,
    ) -> devops_20210625_models.CreateWorkitemEstimateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_estimate_with_options(organization_id, request, headers, runtime)

    async def create_workitem_estimate_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemEstimateRequest,
    ) -> devops_20210625_models.CreateWorkitemEstimateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workitem_estimate_with_options_async(organization_id, request, headers, runtime)

    def create_workitem_estimate_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemEstimateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemEstimateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.spent_time):
            body['spentTime'] = request.spent_time
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemEstimate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/estimate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemEstimateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workitem_estimate_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemEstimateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemEstimateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.spent_time):
            body['spentTime'] = request.spent_time
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemEstimate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/estimate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemEstimateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workitem_record(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRecordRequest,
    ) -> devops_20210625_models.CreateWorkitemRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workitem_record_with_options(organization_id, request, headers, runtime)

    async def create_workitem_record_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRecordRequest,
    ) -> devops_20210625_models.CreateWorkitemRecordResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workitem_record_with_options_async(organization_id, request, headers, runtime)

    def create_workitem_record_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_time):
            body['actualTime'] = request.actual_time
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gmt_end):
            body['gmtEnd'] = request.gmt_end
        if not UtilClient.is_unset(request.gmt_start):
            body['gmtStart'] = request.gmt_start
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemRecord',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/record',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workitem_record_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.CreateWorkitemRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkitemRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.actual_time):
            body['actualTime'] = request.actual_time
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gmt_end):
            body['gmtEnd'] = request.gmt_end
        if not UtilClient.is_unset(request.gmt_start):
            body['gmtStart'] = request.gmt_start
        if not UtilClient.is_unset(request.record_user_identifier):
            body['recordUserIdentifier'] = request.record_user_identifier
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkitemRecord',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/record',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkitemRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.code_version):
            body['codeVersion'] = request.code_version
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.request_from):
            body['requestFrom'] = request.request_from
        if not UtilClient.is_unset(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not UtilClient.is_unset(request.reuse):
            body['reuse'] = request.reuse
        if not UtilClient.is_unset(request.workspace_template):
            body['workspaceTemplate'] = request.workspace_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: devops_20210625_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.code_version):
            body['codeVersion'] = request.code_version
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.request_from):
            body['requestFrom'] = request.request_from
        if not UtilClient.is_unset(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not UtilClient.is_unset(request.reuse):
            body['reuse'] = request.reuse
        if not UtilClient.is_unset(request.workspace_template):
            body['workspaceTemplate'] = request.workspace_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_branch(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteBranchRequest,
    ) -> devops_20210625_models.DeleteBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_branch_with_options(repository_id, request, headers, runtime)

    async def delete_branch_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteBranchRequest,
    ) -> devops_20210625_models.DeleteBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_branch_with_options_async(repository_id, request, headers, runtime)

    def delete_branch_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_branch_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteFileRequest,
    ) -> devops_20210625_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(repository_id, request, headers, runtime)

    async def delete_file_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteFileRequest,
    ) -> devops_20210625_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_file_with_options_async(repository_id, request, headers, runtime)

    def delete_file_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            query['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            query['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_tag(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_flow_tag_with_options(organization_id, id, headers, runtime)

    async def delete_flow_tag_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_flow_tag_with_options_async(organization_id, id, headers, runtime)

    def delete_flow_tag_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_tag_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_tag_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_flow_tag_group_with_options(organization_id, id, headers, runtime)

    async def delete_flow_tag_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_flow_tag_group_with_options_async(organization_id, id, headers, runtime)

    def delete_flow_tag_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteFlowTagGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_host_group_with_options(organization_id, id, headers, runtime)

    async def delete_host_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_host_group_with_options_async(organization_id, id, headers, runtime)

    def delete_host_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteHostGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    async def delete_pipeline_async(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_with_options_async(organization_id, pipeline_id, headers, runtime)

    def delete_pipeline_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline_group(
        self,
        organization_id: str,
        group_id: str,
    ) -> devops_20210625_models.DeletePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_group_with_options(organization_id, group_id, headers, runtime)

    async def delete_pipeline_group_async(
        self,
        organization_id: str,
        group_id: str,
    ) -> devops_20210625_models.DeletePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_group_with_options_async(organization_id, group_id, headers, runtime)

    def delete_pipeline_group_with_options(
        self,
        organization_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_group_with_options_async(
        self,
        organization_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeletePipelineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteProjectRequest,
    ) -> devops_20210625_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(organization_id, request, headers, runtime)

    async def delete_project_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteProjectRequest,
    ) -> devops_20210625_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(organization_id, request, headers, runtime)

    def delete_project_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_protected_branch(
        self,
        repository_id: str,
        protected_branch_id: str,
        request: devops_20210625_models.DeleteProtectedBranchRequest,
    ) -> devops_20210625_models.DeleteProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_protected_branch_with_options(repository_id, protected_branch_id, request, headers, runtime)

    async def delete_protected_branch_async(
        self,
        repository_id: str,
        protected_branch_id: str,
        request: devops_20210625_models.DeleteProtectedBranchRequest,
    ) -> devops_20210625_models.DeleteProtectedBranchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_protected_branch_with_options_async(repository_id, protected_branch_id, request, headers, runtime)

    def delete_protected_branch_with_options(
        self,
        repository_id: str,
        protected_branch_id: str,
        request: devops_20210625_models.DeleteProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtectedBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches/{OpenApiUtilClient.get_encode_param(protected_branch_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProtectedBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_protected_branch_with_options_async(
        self,
        repository_id: str,
        protected_branch_id: str,
        request: devops_20210625_models.DeleteProtectedBranchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteProtectedBranchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtectedBranch',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches/{OpenApiUtilClient.get_encode_param(protected_branch_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteProtectedBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteRepositoryRequest,
    ) -> devops_20210625_models.DeleteRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_with_options(repository_id, request, headers, runtime)

    async def delete_repository_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteRepositoryRequest,
    ) -> devops_20210625_models.DeleteRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_with_options_async(repository_id, request, headers, runtime)

    def delete_repository_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.DeleteRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.reason):
            body['reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository_webhook(
        self,
        repository_id: str,
        hook_id: str,
        request: devops_20210625_models.DeleteRepositoryWebhookRequest,
    ) -> devops_20210625_models.DeleteRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_webhook_with_options(repository_id, hook_id, request, headers, runtime)

    async def delete_repository_webhook_async(
        self,
        repository_id: str,
        hook_id: str,
        request: devops_20210625_models.DeleteRepositoryWebhookRequest,
    ) -> devops_20210625_models.DeleteRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_webhook_with_options_async(repository_id, hook_id, request, headers, runtime)

    def delete_repository_webhook_with_options(
        self,
        repository_id: str,
        hook_id: str,
        request: devops_20210625_models.DeleteRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/hooks/{OpenApiUtilClient.get_encode_param(hook_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_webhook_with_options_async(
        self,
        repository_id: str,
        hook_id: str,
        request: devops_20210625_models.DeleteRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/hooks/{OpenApiUtilClient.get_encode_param(hook_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteRepositoryWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_member(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_member_with_options(organization_id, resource_type, resource_id, account_id, headers, runtime)

    async def delete_resource_member_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_member_with_options_async(organization_id, resource_type, resource_id, account_id, headers, runtime)

    def delete_resource_member_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_member_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteResourceMemberResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteResourceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_variable_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_variable_group_with_options(organization_id, id, headers, runtime)

    async def delete_variable_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_variable_group_with_options_async(organization_id, id, headers, runtime)

    def delete_variable_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_variable_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteVariableGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workitem_all_comment(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemAllCommentRequest,
    ) -> devops_20210625_models.DeleteWorkitemAllCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workitem_all_comment_with_options(organization_id, request, headers, runtime)

    async def delete_workitem_all_comment_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemAllCommentRequest,
    ) -> devops_20210625_models.DeleteWorkitemAllCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workitem_all_comment_with_options_async(organization_id, request, headers, runtime)

    def delete_workitem_all_comment_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemAllCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemAllCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemAllComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/deleteAllComment',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemAllCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workitem_all_comment_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemAllCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemAllCommentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemAllComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/deleteAllComment',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemAllCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workitem_comment(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemCommentRequest,
    ) -> devops_20210625_models.DeleteWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workitem_comment_with_options(organization_id, request, headers, runtime)

    async def delete_workitem_comment_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemCommentRequest,
    ) -> devops_20210625_models.DeleteWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workitem_comment_with_options_async(organization_id, request, headers, runtime)

    def delete_workitem_comment_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/deleteComent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workitem_comment_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.DeleteWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.DeleteWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/deleteComent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteWorkitemCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def frozen_workspace(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.frozen_workspace_with_options(workspace_id, headers, runtime)

    async def frozen_workspace_async(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.frozen_workspace_with_options_async(workspace_id, headers, runtime)

    def frozen_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FrozenWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/frozen',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.FrozenWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def frozen_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.FrozenWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FrozenWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/frozen',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.FrozenWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_branch_info(
        self,
        repository_id: str,
        request: devops_20210625_models.GetBranchInfoRequest,
    ) -> devops_20210625_models.GetBranchInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_branch_info_with_options(repository_id, request, headers, runtime)

    async def get_branch_info_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetBranchInfoRequest,
    ) -> devops_20210625_models.GetBranchInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_branch_info_with_options_async(repository_id, request, headers, runtime)

    def get_branch_info_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.GetBranchInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetBranchInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBranchInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetBranchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_branch_info_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetBranchInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetBranchInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.branch_name):
            query['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBranchInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetBranchInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_codeup_organization(
        self,
        identity: str,
        request: devops_20210625_models.GetCodeupOrganizationRequest,
    ) -> devops_20210625_models.GetCodeupOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_codeup_organization_with_options(identity, request, headers, runtime)

    async def get_codeup_organization_async(
        self,
        identity: str,
        request: devops_20210625_models.GetCodeupOrganizationRequest,
    ) -> devops_20210625_models.GetCodeupOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_codeup_organization_with_options_async(identity, request, headers, runtime)

    def get_codeup_organization_with_options(
        self,
        identity: str,
        request: devops_20210625_models.GetCodeupOrganizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCodeupOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCodeupOrganization',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/organization/{OpenApiUtilClient.get_encode_param(identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCodeupOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_codeup_organization_with_options_async(
        self,
        identity: str,
        request: devops_20210625_models.GetCodeupOrganizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCodeupOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCodeupOrganization',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/organization/{OpenApiUtilClient.get_encode_param(identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCodeupOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_field_option(
        self,
        organization_id: str,
        field_id: str,
        request: devops_20210625_models.GetCustomFieldOptionRequest,
    ) -> devops_20210625_models.GetCustomFieldOptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_custom_field_option_with_options(organization_id, field_id, request, headers, runtime)

    async def get_custom_field_option_async(
        self,
        organization_id: str,
        field_id: str,
        request: devops_20210625_models.GetCustomFieldOptionRequest,
    ) -> devops_20210625_models.GetCustomFieldOptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_custom_field_option_with_options_async(organization_id, field_id, request, headers, runtime)

    def get_custom_field_option_with_options(
        self,
        organization_id: str,
        field_id: str,
        request: devops_20210625_models.GetCustomFieldOptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCustomFieldOptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomFieldOption',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/fields/{OpenApiUtilClient.get_encode_param(field_id)}/getCustomOption',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCustomFieldOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_field_option_with_options_async(
        self,
        organization_id: str,
        field_id: str,
        request: devops_20210625_models.GetCustomFieldOptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetCustomFieldOptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomFieldOption',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/fields/{OpenApiUtilClient.get_encode_param(field_id)}/getCustomOption',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetCustomFieldOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_blobs(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileBlobsRequest,
    ) -> devops_20210625_models.GetFileBlobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_blobs_with_options(repository_id, request, headers, runtime)

    async def get_file_blobs_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileBlobsRequest,
    ) -> devops_20210625_models.GetFileBlobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_blobs_with_options_async(repository_id, request, headers, runtime)

    def get_file_blobs_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileBlobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFileBlobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.ref):
            query['ref'] = request.ref
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileBlobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/blobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileBlobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_blobs_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileBlobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFileBlobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.ref):
            query['ref'] = request.ref
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileBlobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/blobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileBlobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_last_commit(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileLastCommitRequest,
    ) -> devops_20210625_models.GetFileLastCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_last_commit_with_options(repository_id, request, headers, runtime)

    async def get_file_last_commit_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileLastCommitRequest,
    ) -> devops_20210625_models.GetFileLastCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_last_commit_with_options_async(repository_id, request, headers, runtime)

    def get_file_last_commit_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileLastCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFileLastCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['sha'] = request.sha
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileLastCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/lastCommit',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileLastCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_last_commit_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.GetFileLastCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFileLastCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.sha):
            query['sha'] = request.sha
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileLastCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/lastCommit',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFileLastCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_tag_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_flow_tag_group_with_options(organization_id, id, headers, runtime)

    async def get_flow_tag_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_flow_tag_group_with_options_async(organization_id, id, headers, runtime)

    def get_flow_tag_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetFlowTagGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_host_group_with_options(organization_id, id, headers, runtime)

    async def get_host_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_host_group_with_options_async(organization_id, id, headers, runtime)

    def get_host_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetHostGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetHostGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_organization_member(
        self,
        organization_id: str,
        account_id: str,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_organization_member_with_options(organization_id, account_id, headers, runtime)

    async def get_organization_member_async(
        self,
        organization_id: str,
        account_id: str,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_organization_member_with_options_async(organization_id, account_id, headers, runtime)

    def get_organization_member_with_options(
        self,
        organization_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrganizationMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetOrganizationMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_organization_member_with_options_async(
        self,
        organization_id: str,
        account_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetOrganizationMemberResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrganizationMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetOrganizationMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    async def get_pipeline_async(
        self,
        organization_id: str,
        pipeline_id: str,
    ) -> devops_20210625_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_with_options_async(organization_id, pipeline_id, headers, runtime)

    def get_pipeline_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_artifact_url(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineArtifactUrlRequest,
    ) -> devops_20210625_models.GetPipelineArtifactUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_artifact_url_with_options(organization_id, request, headers, runtime)

    async def get_pipeline_artifact_url_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineArtifactUrlRequest,
    ) -> devops_20210625_models.GetPipelineArtifactUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_artifact_url_with_options_async(organization_id, request, headers, runtime)

    def get_pipeline_artifact_url_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineArtifactUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineArtifactUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/getArtifactDownloadUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineArtifactUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_artifact_url_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineArtifactUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineArtifactUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/getArtifactDownloadUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineArtifactUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_emas_artifact_url(
        self,
        organization_id: str,
        emas_job_instance_id: str,
        md_5: str,
        pipeline_id: str,
        pipeline_run_id: str,
        request: devops_20210625_models.GetPipelineEmasArtifactUrlRequest,
    ) -> devops_20210625_models.GetPipelineEmasArtifactUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_emas_artifact_url_with_options(organization_id, emas_job_instance_id, md_5, pipeline_id, pipeline_run_id, request, headers, runtime)

    async def get_pipeline_emas_artifact_url_async(
        self,
        organization_id: str,
        emas_job_instance_id: str,
        md_5: str,
        pipeline_id: str,
        pipeline_run_id: str,
        request: devops_20210625_models.GetPipelineEmasArtifactUrlRequest,
    ) -> devops_20210625_models.GetPipelineEmasArtifactUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_emas_artifact_url_with_options_async(organization_id, emas_job_instance_id, md_5, pipeline_id, pipeline_run_id, request, headers, runtime)

    def get_pipeline_emas_artifact_url_with_options(
        self,
        organization_id: str,
        emas_job_instance_id: str,
        md_5: str,
        pipeline_id: str,
        pipeline_run_id: str,
        request: devops_20210625_models.GetPipelineEmasArtifactUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineEmasArtifactUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_connection_id):
            query['serviceConnectionId'] = request.service_connection_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineEmasArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRun/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/emas/artifact/{OpenApiUtilClient.get_encode_param(emas_job_instance_id)}/{OpenApiUtilClient.get_encode_param(md_5)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineEmasArtifactUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_emas_artifact_url_with_options_async(
        self,
        organization_id: str,
        emas_job_instance_id: str,
        md_5: str,
        pipeline_id: str,
        pipeline_run_id: str,
        request: devops_20210625_models.GetPipelineEmasArtifactUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineEmasArtifactUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_connection_id):
            query['serviceConnectionId'] = request.service_connection_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipelineEmasArtifactUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRun/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/emas/artifact/{OpenApiUtilClient.get_encode_param(emas_job_instance_id)}/{OpenApiUtilClient.get_encode_param(md_5)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineEmasArtifactUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_group(
        self,
        organization_id: str,
        group_id: str,
    ) -> devops_20210625_models.GetPipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_group_with_options(organization_id, group_id, headers, runtime)

    async def get_pipeline_group_async(
        self,
        organization_id: str,
        group_id: str,
    ) -> devops_20210625_models.GetPipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_group_with_options_async(organization_id, group_id, headers, runtime)

    def get_pipeline_group_with_options(
        self,
        organization_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_group_with_options_async(
        self,
        organization_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    async def get_pipeline_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def get_pipeline_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_scan_report_url(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineScanReportUrlRequest,
    ) -> devops_20210625_models.GetPipelineScanReportUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_scan_report_url_with_options(organization_id, request, headers, runtime)

    async def get_pipeline_scan_report_url_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineScanReportUrlRequest,
    ) -> devops_20210625_models.GetPipelineScanReportUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_scan_report_url_with_options_async(organization_id, request, headers, runtime)

    def get_pipeline_scan_report_url_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineScanReportUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineScanReportUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.report_path):
            body['reportPath'] = request.report_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPipelineScanReportUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/getPipelineScanReportUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineScanReportUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_scan_report_url_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.GetPipelineScanReportUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetPipelineScanReportUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.report_path):
            body['reportPath'] = request.report_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPipelineScanReportUrl',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/getPipelineScanReportUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineScanReportUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_info(
        self,
        organization_id: str,
        project_id: str,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_info_with_options(organization_id, project_id, headers, runtime)

    async def get_project_info_async(
        self,
        organization_id: str,
        project_id: str,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_info_with_options_async(organization_id, project_id, headers, runtime)

    def get_project_info_with_options(
        self,
        organization_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_info_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_member(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.GetProjectMemberRequest,
    ) -> devops_20210625_models.GetProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_member_with_options(repository_id, aliyun_pk, request, headers, runtime)

    async def get_project_member_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.GetProjectMemberRequest,
    ) -> devops_20210625_models.GetProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_member_with_options_async(repository_id, aliyun_pk, request, headers, runtime)

    def get_project_member_with_options(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.GetProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/get/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_member_with_options_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.GetProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetProjectMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/get/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repository(
        self,
        request: devops_20210625_models.GetRepositoryRequest,
    ) -> devops_20210625_models.GetRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_with_options(request, headers, runtime)

    async def get_repository_async(
        self,
        request: devops_20210625_models.GetRepositoryRequest,
    ) -> devops_20210625_models.GetRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_with_options_async(request, headers, runtime)

    def get_repository_with_options(
        self,
        request: devops_20210625_models.GetRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.identity):
            query['identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repository_with_options_async(
        self,
        request: devops_20210625_models.GetRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.identity):
            query['identity'] = request.identity
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repository_commit(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.GetRepositoryCommitRequest,
    ) -> devops_20210625_models.GetRepositoryCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_commit_with_options(repository_id, sha, request, headers, runtime)

    async def get_repository_commit_async(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.GetRepositoryCommitRequest,
    ) -> devops_20210625_models.GetRepositoryCommitResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_commit_with_options_async(repository_id, sha, request, headers, runtime)

    def get_repository_commit_with_options(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.GetRepositoryCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/{OpenApiUtilClient.get_encode_param(sha)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryCommitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repository_commit_with_options_async(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.GetRepositoryCommitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetRepositoryCommitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepositoryCommit',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/{OpenApiUtilClient.get_encode_param(sha)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetRepositoryCommitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sprint_info(
        self,
        organization_id: str,
        sprint_id: str,
    ) -> devops_20210625_models.GetSprintInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sprint_info_with_options(organization_id, sprint_id, headers, runtime)

    async def get_sprint_info_async(
        self,
        organization_id: str,
        sprint_id: str,
    ) -> devops_20210625_models.GetSprintInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sprint_info_with_options_async(organization_id, sprint_id, headers, runtime)

    def get_sprint_info_with_options(
        self,
        organization_id: str,
        sprint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetSprintInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSprintInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/{OpenApiUtilClient.get_encode_param(sprint_id)}/getSprintinfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetSprintInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sprint_info_with_options_async(
        self,
        organization_id: str,
        sprint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetSprintInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSprintInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/{OpenApiUtilClient.get_encode_param(sprint_id)}/getSprintinfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetSprintInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vmdeploy_order(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    async def get_vmdeploy_order_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_vmdeploy_order_with_options_async(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def get_vmdeploy_order_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vmdeploy_order_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVMDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_variable_group(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_variable_group_with_options(organization_id, id, headers, runtime)

    async def get_variable_group_async(
        self,
        organization_id: str,
        id: str,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_variable_group_with_options_async(organization_id, id, headers, runtime)

    def get_variable_group_with_options(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_variable_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetVariableGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_item_activity(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkItemActivityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_work_item_activity_with_options(organization_id, workitem_id, headers, runtime)

    async def get_work_item_activity_async(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkItemActivityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_work_item_activity_with_options_async(organization_id, workitem_id, headers, runtime)

    def get_work_item_activity_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemActivityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemActivity',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getActivity',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_item_activity_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemActivityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemActivity',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getActivity',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_item_info(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkItemInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_work_item_info_with_options(organization_id, workitem_id, headers, runtime)

    async def get_work_item_info_async(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkItemInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_work_item_info_with_options_async(organization_id, workitem_id, headers, runtime)

    def get_work_item_info_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_item_info_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkItemInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_item_work_flow_info(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkItemWorkFlowInfoRequest,
    ) -> devops_20210625_models.GetWorkItemWorkFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_work_item_work_flow_info_with_options(organization_id, workitem_id, request, headers, runtime)

    async def get_work_item_work_flow_info_async(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkItemWorkFlowInfoRequest,
    ) -> devops_20210625_models.GetWorkItemWorkFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_work_item_work_flow_info_with_options_async(organization_id, workitem_id, request, headers, runtime)

    def get_work_item_work_flow_info_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkItemWorkFlowInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemWorkFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration_id):
            query['configurationId'] = request.configuration_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkItemWorkFlowInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getWorkflowInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemWorkFlowInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_item_work_flow_info_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkItemWorkFlowInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkItemWorkFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration_id):
            query['configurationId'] = request.configuration_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkItemWorkFlowInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getWorkflowInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkItemWorkFlowInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workitem_comment_list(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkitemCommentListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_comment_list_with_options(organization_id, workitem_id, headers, runtime)

    async def get_workitem_comment_list_async(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.GetWorkitemCommentListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workitem_comment_list_with_options_async(organization_id, workitem_id, headers, runtime)

    def get_workitem_comment_list_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemCommentListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemCommentList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/commentList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemCommentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workitem_comment_list_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemCommentListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemCommentList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/commentList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemCommentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workitem_relations(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkitemRelationsRequest,
    ) -> devops_20210625_models.GetWorkitemRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_relations_with_options(organization_id, workitem_id, request, headers, runtime)

    async def get_workitem_relations_async(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkitemRelationsRequest,
    ) -> devops_20210625_models.GetWorkitemRelationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workitem_relations_with_options_async(organization_id, workitem_id, request, headers, runtime)

    def get_workitem_relations_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkitemRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkitemRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getRelations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workitem_relations_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        request: devops_20210625_models.GetWorkitemRelationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_type):
            query['relationType'] = request.relation_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkitemRelations',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/getRelations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workitem_time_type_list(
        self,
        organization_id: str,
    ) -> devops_20210625_models.GetWorkitemTimeTypeListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workitem_time_type_list_with_options(organization_id, headers, runtime)

    async def get_workitem_time_type_list_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.GetWorkitemTimeTypeListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workitem_time_type_list_with_options_async(organization_id, headers, runtime)

    def get_workitem_time_type_list_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemTimeTypeListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemTimeTypeList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/type/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemTimeTypeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workitem_time_type_list_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkitemTimeTypeListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkitemTimeTypeList',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/type/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkitemTimeTypeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_id, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.GetWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_pipeline_group(
        self,
        organization_id: str,
        request: devops_20210625_models.JoinPipelineGroupRequest,
    ) -> devops_20210625_models.JoinPipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.join_pipeline_group_with_options(organization_id, request, headers, runtime)

    async def join_pipeline_group_async(
        self,
        organization_id: str,
        request: devops_20210625_models.JoinPipelineGroupRequest,
    ) -> devops_20210625_models.JoinPipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.join_pipeline_group_with_options_async(organization_id, request, headers, runtime)

    def join_pipeline_group_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.JoinPipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.JoinPipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/join',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.JoinPipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_pipeline_group_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.JoinPipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.JoinPipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinPipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/join',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.JoinPipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_tag_groups(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_tag_groups_with_options(organization_id, headers, runtime)

    async def list_flow_tag_groups_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_flow_tag_groups_with_options_async(organization_id, headers, runtime)

    def list_flow_tag_groups_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFlowTagGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListFlowTagGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_tag_groups_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListFlowTagGroupsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFlowTagGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListFlowTagGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_groups(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_host_groups_with_options(organization_id, request, headers, runtime)

    async def list_host_groups_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_host_groups_with_options_async(organization_id, request, headers, runtime)

    def list_host_groups_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_groups_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListHostGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListHostGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListHostGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organization_members(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organization_members_with_options(organization_id, request, headers, runtime)

    async def list_organization_members_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_organization_members_with_options_async(organization_id, request, headers, runtime)

    def list_organization_members_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extern_uid):
            query['externUid'] = request.extern_uid
        if not UtilClient.is_unset(request.join_time_from):
            query['joinTimeFrom'] = request.join_time_from
        if not UtilClient.is_unset(request.join_time_to):
            query['joinTimeTo'] = request.join_time_to
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.organization_member_name):
            query['organizationMemberName'] = request.organization_member_name
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organization_members_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListOrganizationMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListOrganizationMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extern_uid):
            query['externUid'] = request.extern_uid
        if not UtilClient.is_unset(request.join_time_from):
            query['joinTimeFrom'] = request.join_time_from
        if not UtilClient.is_unset(request.join_time_to):
            query['joinTimeTo'] = request.join_time_to
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.organization_member_name):
            query['organizationMemberName'] = request.organization_member_name
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_group_pipelines(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.ListPipelineGroupPipelinesRequest,
    ) -> devops_20210625_models.ListPipelineGroupPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_group_pipelines_with_options(organization_id, group_id, request, headers, runtime)

    async def list_pipeline_group_pipelines_async(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.ListPipelineGroupPipelinesRequest,
    ) -> devops_20210625_models.ListPipelineGroupPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_group_pipelines_with_options_async(organization_id, group_id, request, headers, runtime)

    def list_pipeline_group_pipelines_with_options(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.ListPipelineGroupPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineGroupPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.result_status_list):
            query['resultStatusList'] = request.result_status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroupPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_group_pipelines_with_options_async(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.ListPipelineGroupPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineGroupPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.result_status_list):
            query['resultStatusList'] = request.result_status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroupPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_groups(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelineGroupsRequest,
    ) -> devops_20210625_models.ListPipelineGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_groups_with_options(organization_id, request, headers, runtime)

    async def list_pipeline_groups_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelineGroupsRequest,
    ) -> devops_20210625_models.ListPipelineGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_groups_with_options_async(organization_id, request, headers, runtime)

    def list_pipeline_groups_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelineGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_groups_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelineGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_job_historys(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobHistorysRequest,
    ) -> devops_20210625_models.ListPipelineJobHistorysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_job_historys_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def list_pipeline_job_historys_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobHistorysRequest,
    ) -> devops_20210625_models.ListPipelineJobHistorysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_job_historys_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_job_historys_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobHistorysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineJobHistorysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobHistorys',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/job/historys',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobHistorysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_job_historys_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobHistorysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineJobHistorysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.identifier):
            query['identifier'] = request.identifier
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobHistorys',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/job/historys',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobHistorysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_jobs(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobsRequest,
    ) -> devops_20210625_models.ListPipelineJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_jobs_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def list_pipeline_jobs_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobsRequest,
    ) -> devops_20210625_models.ListPipelineJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_jobs_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_jobs_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_jobs_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineJobs',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_runs(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_runs_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def list_pipeline_runs_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_runs_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_runs_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.trigger_mode):
            query['triggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_runs_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.ListPipelineRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelineRunsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.trigger_mode):
            query['triggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipelines(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
    ) -> devops_20210625_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(organization_id, request, headers, runtime)

    async def list_pipelines_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
    ) -> devops_20210625_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipelines_with_options_async(organization_id, request, headers, runtime)

    def list_pipelines_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.execute_account_ids):
            query['executeAccountIds'] = request.execute_account_ids
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.status_list):
            query['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.execute_account_ids):
            query['executeAccountIds'] = request.execute_account_ids
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.status_list):
            query['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_members(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_members_with_options(organization_id, project_id, request, headers, runtime)

    async def list_project_members_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_members_with_options_async(organization_id, project_id, request, headers, runtime)

    def list_project_members_with_options(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/listMembers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_members_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/listMembers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_templates(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectTemplatesRequest,
    ) -> devops_20210625_models.ListProjectTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_templates_with_options(organization_id, request, headers, runtime)

    async def list_project_templates_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectTemplatesRequest,
    ) -> devops_20210625_models.ListProjectTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_templates_with_options_async(organization_id, request, headers, runtime)

    def list_project_templates_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectTemplates',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/listTemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_templates_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectTemplates',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/listTemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_workitem_types(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectWorkitemTypesRequest,
    ) -> devops_20210625_models.ListProjectWorkitemTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_workitem_types_with_options(organization_id, project_id, request, headers, runtime)

    async def list_project_workitem_types_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectWorkitemTypesRequest,
    ) -> devops_20210625_models.ListProjectWorkitemTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_workitem_types_with_options_async(organization_id, project_id, request, headers, runtime)

    def list_project_workitem_types_with_options(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectWorkitemTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectWorkitemTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectWorkitemTypes',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/getWorkitemType',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectWorkitemTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_workitem_types_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.ListProjectWorkitemTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectWorkitemTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjectWorkitemTypes',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/getWorkitemType',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectWorkitemTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectsRequest,
    ) -> devops_20210625_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(organization_id, request, headers, runtime)

    async def list_projects_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectsRequest,
    ) -> devops_20210625_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(organization_id, request, headers, runtime)

    def list_projects_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/listProjects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/listProjects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_protected_branches(
        self,
        repository_id: str,
        request: devops_20210625_models.ListProtectedBranchesRequest,
    ) -> devops_20210625_models.ListProtectedBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_protected_branches_with_options(repository_id, request, headers, runtime)

    async def list_protected_branches_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListProtectedBranchesRequest,
    ) -> devops_20210625_models.ListProtectedBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_protected_branches_with_options_async(repository_id, request, headers, runtime)

    def list_protected_branches_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListProtectedBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProtectedBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProtectedBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_protected_branches_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListProtectedBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListProtectedBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListProtectedBranchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repositories(
        self,
        request: devops_20210625_models.ListRepositoriesRequest,
    ) -> devops_20210625_models.ListRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repositories_with_options(request, headers, runtime)

    async def list_repositories_async(
        self,
        request: devops_20210625_models.ListRepositoriesRequest,
    ) -> devops_20210625_models.ListRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repositories_with_options_async(request, headers, runtime)

    def list_repositories_with_options(
        self,
        request: devops_20210625_models.ListRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.archived):
            query['archived'] = request.archived
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.per_page):
            query['perPage'] = request.per_page
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositories',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repositories_with_options_async(
        self,
        request: devops_20210625_models.ListRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.archived):
            query['archived'] = request.archived
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.per_page):
            query['perPage'] = request.per_page
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositories',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_branches(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryBranchesRequest,
    ) -> devops_20210625_models.ListRepositoryBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_branches_with_options(repository_id, request, headers, runtime)

    async def list_repository_branches_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryBranchesRequest,
    ) -> devops_20210625_models.ListRepositoryBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_branches_with_options_async(repository_id, request, headers, runtime)

    def list_repository_branches_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_branches_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/branches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryBranchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_commit_diff(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.ListRepositoryCommitDiffRequest,
    ) -> devops_20210625_models.ListRepositoryCommitDiffResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commit_diff_with_options(repository_id, sha, request, headers, runtime)

    async def list_repository_commit_diff_async(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.ListRepositoryCommitDiffRequest,
    ) -> devops_20210625_models.ListRepositoryCommitDiffResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_commit_diff_with_options_async(repository_id, sha, request, headers, runtime)

    def list_repository_commit_diff_with_options(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.ListRepositoryCommitDiffRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryCommitDiffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.context_line):
            query['contextLine'] = request.context_line
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommitDiff',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/{OpenApiUtilClient.get_encode_param(sha)}/diff',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitDiffResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_commit_diff_with_options_async(
        self,
        repository_id: str,
        sha: str,
        request: devops_20210625_models.ListRepositoryCommitDiffRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryCommitDiffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.context_line):
            query['contextLine'] = request.context_line
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommitDiff',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits/{OpenApiUtilClient.get_encode_param(sha)}/diff',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitDiffResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_commits(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryCommitsRequest,
    ) -> devops_20210625_models.ListRepositoryCommitsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_commits_with_options(repository_id, request, headers, runtime)

    async def list_repository_commits_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryCommitsRequest,
    ) -> devops_20210625_models.ListRepositoryCommitsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_commits_with_options_async(repository_id, request, headers, runtime)

    def list_repository_commits_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryCommitsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryCommitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.show_comments_count):
            query['showCommentsCount'] = request.show_comments_count
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommits',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_commits_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryCommitsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryCommitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.search):
            query['search'] = request.search
        if not UtilClient.is_unset(request.show_comments_count):
            query['showCommentsCount'] = request.show_comments_count
        if not UtilClient.is_unset(request.show_signature):
            query['showSignature'] = request.show_signature
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryCommits',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/commits',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryCommitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_member_with_inherited(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryMemberWithInheritedRequest,
    ) -> devops_20210625_models.ListRepositoryMemberWithInheritedResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_member_with_inherited_with_options(repository_id, request, headers, runtime)

    async def list_repository_member_with_inherited_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryMemberWithInheritedRequest,
    ) -> devops_20210625_models.ListRepositoryMemberWithInheritedResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_member_with_inherited_with_options_async(repository_id, request, headers, runtime)

    def list_repository_member_with_inherited_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryMemberWithInheritedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryMemberWithInheritedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryMemberWithInherited',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryMemberWithInheritedResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_member_with_inherited_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryMemberWithInheritedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryMemberWithInheritedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryMemberWithInherited',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryMemberWithInheritedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_tree(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTreeRequest,
    ) -> devops_20210625_models.ListRepositoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_tree_with_options(repository_id, request, headers, runtime)

    async def list_repository_tree_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTreeRequest,
    ) -> devops_20210625_models.ListRepositoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_tree_with_options_async(repository_id, request, headers, runtime)

    def list_repository_tree_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTree',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/tree',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_tree_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.ref_name):
            query['refName'] = request.ref_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryTree',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/tree',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository_webhook(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryWebhookRequest,
    ) -> devops_20210625_models.ListRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repository_webhook_with_options(repository_id, request, headers, runtime)

    async def list_repository_webhook_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryWebhookRequest,
    ) -> devops_20210625_models.ListRepositoryWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repository_webhook_with_options_async(repository_id, request, headers, runtime)

    def list_repository_webhook_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/webhooks/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_webhook_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.ListRepositoryWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListRepositoryWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepositoryWebhook',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/webhooks/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListRepositoryWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_members(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_members_with_options(organization_id, resource_type, resource_id, headers, runtime)

    async def list_resource_members_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_members_with_options_async(organization_id, resource_type, resource_id, headers, runtime)

    def list_resource_members_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListResourceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_members_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListResourceMembersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListResourceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_connections(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_connections_with_options(organization_id, request, headers, runtime)

    async def list_service_connections_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_connections_with_options_async(organization_id, request, headers, runtime)

    def list_service_connections_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.serice_connection_type):
            query['sericeConnectionType'] = request.serice_connection_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceConnections',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceConnections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_connections_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListServiceConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListServiceConnectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.serice_connection_type):
            query['sericeConnectionType'] = request.serice_connection_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceConnections',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/serviceConnections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sprints(
        self,
        organization_id: str,
        request: devops_20210625_models.ListSprintsRequest,
    ) -> devops_20210625_models.ListSprintsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sprints_with_options(organization_id, request, headers, runtime)

    async def list_sprints_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListSprintsRequest,
    ) -> devops_20210625_models.ListSprintsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sprints_with_options_async(organization_id, request, headers, runtime)

    def list_sprints_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListSprintsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSprintsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSprints',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSprintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sprints_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListSprintsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListSprintsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSprints',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sprints/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListSprintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_variable_groups(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_variable_groups_with_options(organization_id, request, headers, runtime)

    async def list_variable_groups_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_variable_groups_with_options_async(organization_id, request, headers, runtime)

    def list_variable_groups_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariableGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListVariableGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_variable_groups_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListVariableGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListVariableGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariableGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListVariableGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_work_item_all_fields(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemAllFieldsRequest,
    ) -> devops_20210625_models.ListWorkItemAllFieldsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_work_item_all_fields_with_options(organization_id, request, headers, runtime)

    async def list_work_item_all_fields_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemAllFieldsRequest,
    ) -> devops_20210625_models.ListWorkItemAllFieldsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_work_item_all_fields_with_options_async(organization_id, request, headers, runtime)

    def list_work_item_all_fields_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemAllFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkItemAllFieldsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemAllFields',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/fields/listAll',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemAllFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_work_item_all_fields_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemAllFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkItemAllFieldsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemAllFields',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/fields/listAll',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemAllFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_work_item_work_flow_status(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemWorkFlowStatusRequest,
    ) -> devops_20210625_models.ListWorkItemWorkFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_work_item_work_flow_status_with_options(organization_id, request, headers, runtime)

    async def list_work_item_work_flow_status_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemWorkFlowStatusRequest,
    ) -> devops_20210625_models.ListWorkItemWorkFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_work_item_work_flow_status_with_options_async(organization_id, request, headers, runtime)

    def list_work_item_work_flow_status_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemWorkFlowStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkItemWorkFlowStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_category_identifier):
            query['workitemCategoryIdentifier'] = request.workitem_category_identifier
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemWorkFlowStatus',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/workflow/listWorkflowStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemWorkFlowStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_work_item_work_flow_status_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkItemWorkFlowStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkItemWorkFlowStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        if not UtilClient.is_unset(request.workitem_category_identifier):
            query['workitemCategoryIdentifier'] = request.workitem_category_identifier
        if not UtilClient.is_unset(request.workitem_type_identifier):
            query['workitemTypeIdentifier'] = request.workitem_type_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkItemWorkFlowStatus',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/workflow/listWorkflowStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkItemWorkFlowStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workitem_time(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.ListWorkitemTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workitem_time_with_options(organization_id, workitem_id, headers, runtime)

    async def list_workitem_time_async(
        self,
        organization_id: str,
        workitem_id: str,
    ) -> devops_20210625_models.ListWorkitemTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workitem_time_with_options_async(organization_id, workitem_id, headers, runtime)

    def list_workitem_time_with_options(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemTimeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWorkitemTime',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/time/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workitem_time_with_options_async(
        self,
        organization_id: str,
        workitem_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemTimeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListWorkitemTime',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/{OpenApiUtilClient.get_encode_param(workitem_id)}/time/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workitems(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkitemsRequest,
    ) -> devops_20210625_models.ListWorkitemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workitems_with_options(organization_id, request, headers, runtime)

    async def list_workitems_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkitemsRequest,
    ) -> devops_20210625_models.ListWorkitemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workitems_with_options_async(organization_id, request, headers, runtime)

    def list_workitems_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkitemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.group_condition):
            query['groupCondition'] = request.group_condition
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.search_type):
            query['searchType'] = request.search_type
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkitems',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/listWorkitems',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workitems_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.ListWorkitemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkitemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.extra_conditions):
            query['extraConditions'] = request.extra_conditions
        if not UtilClient.is_unset(request.group_condition):
            query['groupCondition'] = request.group_condition
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['orderBy'] = request.order_by
        if not UtilClient.is_unset(request.search_type):
            query['searchType'] = request.search_type
        if not UtilClient.is_unset(request.space_identifier):
            query['spaceIdentifier'] = request.space_identifier
        if not UtilClient.is_unset(request.space_type):
            query['spaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkitems',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/listWorkitems',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkitemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: devops_20210625_models.ListWorkspacesRequest,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: devops_20210625_models.ListWorkspacesRequest,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def list_workspaces_with_options(
        self,
        tmp_req: devops_20210625_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = devops_20210625_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        if not UtilClient.is_unset(tmp_req.workspace_template_list):
            request.workspace_template_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_template_list, 'workspaceTemplateList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.workspace_template_list_shrink):
            query['workspaceTemplateList'] = request.workspace_template_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        tmp_req: devops_20210625_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ListWorkspacesResponse:
        UtilClient.validate_model(tmp_req)
        request = devops_20210625_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        if not UtilClient.is_unset(tmp_req.workspace_template_list):
            request.workspace_template_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_template_list, 'workspaceTemplateList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.workspace_template_list_shrink):
            query['workspaceTemplateList'] = request.workspace_template_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_pipeline_job_run_with_options(organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime)

    async def log_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_pipeline_job_run_with_options_async(organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime)

    def log_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRun/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/job/{OpenApiUtilClient.get_encode_param(job_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        job_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipeline/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRun/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/job/{OpenApiUtilClient.get_encode_param(job_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_vmdeploy_machine(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    async def log_vmdeploy_machine_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_vmdeploy_machine_with_options_async(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def log_vmdeploy_machine_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_vmdeploy_machine_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.LogVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogVMDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pass_pipeline_validate(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pass_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def pass_pipeline_validate_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pass_pipeline_validate_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def pass_pipeline_validate_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PassPipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pass',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.PassPipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    async def pass_pipeline_validate_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.PassPipelineValidateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PassPipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pass',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.PassPipelineValidateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refuse_pipeline_validate(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refuse_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def refuse_pipeline_validate_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.refuse_pipeline_validate_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def refuse_pipeline_validate_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefusePipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/refuse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RefusePipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    async def refuse_pipeline_validate_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RefusePipelineValidateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefusePipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/refuse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RefusePipelineValidateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_workspace(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_workspace_with_options(workspace_id, headers, runtime)

    async def release_workspace_async(
        self,
        workspace_id: str,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.release_workspace_with_options_async(workspace_id, headers, runtime)

    def release_workspace_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/release',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReleaseWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ReleaseWorkspaceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/api/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/release',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReleaseWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_ssh_key(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_ssh_key_with_options(organization_id, headers, runtime)

    async def reset_ssh_key_async(
        self,
        organization_id: str,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reset_ssh_key_with_options_async(organization_id, headers, runtime)

    def reset_ssh_key_with_options(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sshKey',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResetSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_ssh_key_with_options_async(
        self,
        organization_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResetSshKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/sshKey',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResetSshKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_vmdeploy_order(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    async def resume_vmdeploy_order_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_vmdeploy_order_with_options_async(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def resume_vmdeploy_order_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResumeVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_vmdeploy_order_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.ResumeVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResumeVMDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def retry_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retry_pipeline_job_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def retry_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_vmdeploy_machine(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    async def retry_vmdeploy_machine_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retry_vmdeploy_machine_with_options_async(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def retry_vmdeploy_machine_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/retry',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_vmdeploy_machine_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.RetryVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/retry',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryVMDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def skip_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.skip_pipeline_job_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def skip_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_vmdeploy_machine(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    async def skip_vmdeploy_machine_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.skip_vmdeploy_machine_with_options_async(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def skip_vmdeploy_machine_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_vmdeploy_machine_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        machine_sn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.SkipVMDeployMachineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/machine/{OpenApiUtilClient.get_encode_param(machine_sn)}/skip',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipVMDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_pipeline_run(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_run_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def start_pipeline_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_pipeline_run_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def start_pipeline_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organizations/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StartPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_pipeline_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.StartPipelineRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StartPipelineRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organizations/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StartPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_pipeline_job_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    async def stop_pipeline_job_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_pipeline_job_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def stop_pipeline_job_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_pipeline_job_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineJobRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_pipeline_run(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    async def stop_pipeline_run_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_pipeline_run_with_options_async(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def stop_pipeline_run_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_pipeline_run_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        pipeline_run_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopPipelineRunResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/pipelineRuns/{OpenApiUtilClient.get_encode_param(pipeline_run_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_vmdeploy_order(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    async def stop_vmdeploy_order_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_vmdeploy_order_with_options_async(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def stop_vmdeploy_order_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_vmdeploy_order_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        deploy_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.StopVMDeployOrderResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/deploy/{OpenApiUtilClient.get_encode_param(deploy_order_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopVMDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_repository_mirror_sync(
        self,
        repository_id: str,
        request: devops_20210625_models.TriggerRepositoryMirrorSyncRequest,
    ) -> devops_20210625_models.TriggerRepositoryMirrorSyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_repository_mirror_sync_with_options(repository_id, request, headers, runtime)

    async def trigger_repository_mirror_sync_async(
        self,
        repository_id: str,
        request: devops_20210625_models.TriggerRepositoryMirrorSyncRequest,
    ) -> devops_20210625_models.TriggerRepositoryMirrorSyncResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.trigger_repository_mirror_sync_with_options_async(repository_id, request, headers, runtime)

    def trigger_repository_mirror_sync_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.TriggerRepositoryMirrorSyncRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.TriggerRepositoryMirrorSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.account):
            query['account'] = request.account
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRepositoryMirrorSync',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.TriggerRepositoryMirrorSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_repository_mirror_sync_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.TriggerRepositoryMirrorSyncRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.TriggerRepositoryMirrorSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.account):
            query['account'] = request.account
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRepositoryMirrorSync',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/mirror',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.TriggerRepositoryMirrorSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateFileRequest,
    ) -> devops_20210625_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_file_with_options(repository_id, request, headers, runtime)

    async def update_file_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateFileRequest,
    ) -> devops_20210625_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_file_with_options_async(repository_id, request, headers, runtime)

    def update_file_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.new_path):
            body['newPath'] = request.new_path
        if not UtilClient.is_unset(request.old_path):
            body['oldPath'] = request.old_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.branch_name):
            body['branchName'] = request.branch_name
        if not UtilClient.is_unset(request.commit_message):
            body['commitMessage'] = request.commit_message
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.encoding):
            body['encoding'] = request.encoding
        if not UtilClient.is_unset(request.new_path):
            body['newPath'] = request.new_path
        if not UtilClient.is_unset(request.old_path):
            body['oldPath'] = request.old_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/files/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_tag(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_flow_tag_with_options(organization_id, id, request, headers, runtime)

    async def update_flow_tag_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_flow_tag_with_options_async(organization_id, id, request, headers, runtime)

    def update_flow_tag_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_tag_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.color):
            query['color'] = request.color
        if not UtilClient.is_unset(request.flow_tag_group_id):
            query['flowTagGroupId'] = request.flow_tag_group_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTag',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tags/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_tag_group(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_flow_tag_group_with_options(organization_id, id, request, headers, runtime)

    async def update_flow_tag_group_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_flow_tag_group_with_options_async(organization_id, id, request, headers, runtime)

    def update_flow_tag_group_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_tag_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateFlowTagGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateFlowTagGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowTagGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/flow/tagGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateFlowTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_host_group(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_host_group_with_options(organization_id, id, request, headers, runtime)

    async def update_host_group_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_host_group_with_options_async(organization_id, id, request, headers, runtime)

    def update_host_group_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_host_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateHostGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateHostGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/hostGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdatePipelineRequest,
    ) -> devops_20210625_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_with_options(organization_id, request, headers, runtime)

    async def update_pipeline_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdatePipelineRequest,
    ) -> devops_20210625_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_with_options_async(organization_id, request, headers, runtime)

    def update_pipeline_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.basic_info):
            body['basicInfo'] = request.basic_info
        if not UtilClient.is_unset(request.pipeline_yaml):
            body['pipelineYaml'] = request.pipeline_yaml
        if not UtilClient.is_unset(request.settings):
            body['settings'] = request.settings
        if not UtilClient.is_unset(request.trigger_info):
            body['triggerInfo'] = request.trigger_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.basic_info):
            body['basicInfo'] = request.basic_info
        if not UtilClient.is_unset(request.pipeline_yaml):
            body['pipelineYaml'] = request.pipeline_yaml
        if not UtilClient.is_unset(request.settings):
            body['settings'] = request.settings
        if not UtilClient.is_unset(request.trigger_info):
            body['triggerInfo'] = request.trigger_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_base_info(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_base_info_with_options(organization_id, pipeline_id, request, headers, runtime)

    async def update_pipeline_base_info_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_base_info_with_options_async(organization_id, pipeline_id, request, headers, runtime)

    def update_pipeline_base_info_with_options(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['envId'] = request.env_id
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.tag_list):
            query['tagList'] = request.tag_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineBaseInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/baseInfo',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_base_info_with_options_async(
        self,
        organization_id: str,
        pipeline_id: str,
        request: devops_20210625_models.UpdatePipelineBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineBaseInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['envId'] = request.env_id
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.tag_list):
            query['tagList'] = request.tag_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineBaseInfo',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelines/{OpenApiUtilClient.get_encode_param(pipeline_id)}/baseInfo',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_group(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.UpdatePipelineGroupRequest,
    ) -> devops_20210625_models.UpdatePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_group_with_options(organization_id, group_id, request, headers, runtime)

    async def update_pipeline_group_async(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.UpdatePipelineGroupRequest,
    ) -> devops_20210625_models.UpdatePipelineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_group_with_options_async(organization_id, group_id, request, headers, runtime)

    def update_pipeline_group_with_options(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.UpdatePipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_group_with_options_async(
        self,
        organization_id: str,
        group_id: str,
        request: devops_20210625_models.UpdatePipelineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdatePipelineGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/pipelineGroups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdatePipelineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_member(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.UpdateProjectMemberRequest,
    ) -> devops_20210625_models.UpdateProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_member_with_options(organization_id, project_id, request, headers, runtime)

    async def update_project_member_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.UpdateProjectMemberRequest,
    ) -> devops_20210625_models.UpdateProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_member_with_options_async(organization_id, project_id, request, headers, runtime)

    def update_project_member_with_options(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.UpdateProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProjectMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_identifier):
            body['roleIdentifier'] = request.role_identifier
        if not UtilClient.is_unset(request.target_identifier):
            body['targetIdentifier'] = request.target_identifier
        if not UtilClient.is_unset(request.target_type):
            body['targetType'] = request.target_type
        if not UtilClient.is_unset(request.user_identifier):
            body['userIdentifier'] = request.user_identifier
        if not UtilClient.is_unset(request.user_type):
            body['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/updateMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_member_with_options_async(
        self,
        organization_id: str,
        project_id: str,
        request: devops_20210625_models.UpdateProjectMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProjectMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_identifier):
            body['roleIdentifier'] = request.role_identifier
        if not UtilClient.is_unset(request.target_identifier):
            body['targetIdentifier'] = request.target_identifier
        if not UtilClient.is_unset(request.target_type):
            body['targetType'] = request.target_type
        if not UtilClient.is_unset(request.user_identifier):
            body['userIdentifier'] = request.user_identifier
        if not UtilClient.is_unset(request.user_type):
            body['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/updateMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_protected_branches(
        self,
        repository_id: str,
        id: str,
        request: devops_20210625_models.UpdateProtectedBranchesRequest,
    ) -> devops_20210625_models.UpdateProtectedBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_protected_branches_with_options(repository_id, id, request, headers, runtime)

    async def update_protected_branches_async(
        self,
        repository_id: str,
        id: str,
        request: devops_20210625_models.UpdateProtectedBranchesRequest,
    ) -> devops_20210625_models.UpdateProtectedBranchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_protected_branches_with_options_async(repository_id, id, request, headers, runtime)

    def update_protected_branches_with_options(
        self,
        repository_id: str,
        id: str,
        request: devops_20210625_models.UpdateProtectedBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProtectedBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProtectedBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_protected_branches_with_options_async(
        self,
        repository_id: str,
        id: str,
        request: devops_20210625_models.UpdateProtectedBranchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateProtectedBranchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.allow_merge_roles):
            body['allowMergeRoles'] = request.allow_merge_roles
        if not UtilClient.is_unset(request.allow_merge_user_ids):
            body['allowMergeUserIds'] = request.allow_merge_user_ids
        if not UtilClient.is_unset(request.allow_push_roles):
            body['allowPushRoles'] = request.allow_push_roles
        if not UtilClient.is_unset(request.allow_push_user_ids):
            body['allowPushUserIds'] = request.allow_push_user_ids
        if not UtilClient.is_unset(request.branch):
            body['branch'] = request.branch
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.merge_request_setting):
            body['mergeRequestSetting'] = request.merge_request_setting
        if not UtilClient.is_unset(request.test_setting_dto):
            body['testSettingDTO'] = request.test_setting_dto
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProtectedBranches',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(repository_id)}/protect_branches/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateProtectedBranchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repository(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateRepositoryRequest,
    ) -> devops_20210625_models.UpdateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_with_options(repository_id, request, headers, runtime)

    async def update_repository_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateRepositoryRequest,
    ) -> devops_20210625_models.UpdateRepositoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_repository_with_options_async(repository_id, request, headers, runtime)

    def update_repository_with_options(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.admin_setting_language):
            body['adminSettingLanguage'] = request.admin_setting_language
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.builds_enabled):
            body['buildsEnabled'] = request.builds_enabled
        if not UtilClient.is_unset(request.check_email):
            body['checkEmail'] = request.check_email
        if not UtilClient.is_unset(request.default_branch):
            body['defaultBranch'] = request.default_branch
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.issues_enabled):
            body['issuesEnabled'] = request.issues_enabled
        if not UtilClient.is_unset(request.merge_requests_enabled):
            body['mergeRequestsEnabled'] = request.merge_requests_enabled
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.open_clone_download_control):
            body['openCloneDownloadControl'] = request.open_clone_download_control
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.project_clone_download_method_list):
            body['projectCloneDownloadMethodList'] = request.project_clone_download_method_list
        if not UtilClient.is_unset(request.project_clone_download_role_list):
            body['projectCloneDownloadRoleList'] = request.project_clone_download_role_list
        if not UtilClient.is_unset(request.snippets_enabled):
            body['snippetsEnabled'] = request.snippets_enabled
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        if not UtilClient.is_unset(request.wiki_enabled):
            body['wikiEnabled'] = request.wiki_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repository_with_options_async(
        self,
        repository_id: str,
        request: devops_20210625_models.UpdateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateRepositoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.admin_setting_language):
            body['adminSettingLanguage'] = request.admin_setting_language
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.builds_enabled):
            body['buildsEnabled'] = request.builds_enabled
        if not UtilClient.is_unset(request.check_email):
            body['checkEmail'] = request.check_email
        if not UtilClient.is_unset(request.default_branch):
            body['defaultBranch'] = request.default_branch
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.issues_enabled):
            body['issuesEnabled'] = request.issues_enabled
        if not UtilClient.is_unset(request.merge_requests_enabled):
            body['mergeRequestsEnabled'] = request.merge_requests_enabled
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.open_clone_download_control):
            body['openCloneDownloadControl'] = request.open_clone_download_control
        if not UtilClient.is_unset(request.path):
            body['path'] = request.path
        if not UtilClient.is_unset(request.project_clone_download_method_list):
            body['projectCloneDownloadMethodList'] = request.project_clone_download_method_list
        if not UtilClient.is_unset(request.project_clone_download_role_list):
            body['projectCloneDownloadRoleList'] = request.project_clone_download_role_list
        if not UtilClient.is_unset(request.snippets_enabled):
            body['snippetsEnabled'] = request.snippets_enabled
        if not UtilClient.is_unset(request.visibility_level):
            body['visibilityLevel'] = request.visibility_level
        if not UtilClient.is_unset(request.wiki_enabled):
            body['wikiEnabled'] = request.wiki_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repository_member(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.UpdateRepositoryMemberRequest,
    ) -> devops_20210625_models.UpdateRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repository_member_with_options(repository_id, aliyun_pk, request, headers, runtime)

    async def update_repository_member_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.UpdateRepositoryMemberRequest,
    ) -> devops_20210625_models.UpdateRepositoryMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_repository_member_with_options_async(repository_id, aliyun_pk, request, headers, runtime)

    def update_repository_member_with_options(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.UpdateRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.expire_at):
            body['expireAt'] = request.expire_at
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        if not UtilClient.is_unset(request.related_id):
            body['relatedId'] = request.related_id
        if not UtilClient.is_unset(request.related_infos):
            body['relatedInfos'] = request.related_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repository_member_with_options_async(
        self,
        repository_id: str,
        aliyun_pk: str,
        request: devops_20210625_models.UpdateRepositoryMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateRepositoryMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['accessToken'] = request.access_token
        if not UtilClient.is_unset(request.organization_id):
            query['organizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.access_level):
            body['accessLevel'] = request.access_level
        if not UtilClient.is_unset(request.expire_at):
            body['expireAt'] = request.expire_at
        if not UtilClient.is_unset(request.member_type):
            body['memberType'] = request.member_type
        if not UtilClient.is_unset(request.related_id):
            body['relatedId'] = request.related_id
        if not UtilClient.is_unset(request.related_infos):
            body['relatedInfos'] = request.related_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRepositoryMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/repository/{OpenApiUtilClient.get_encode_param(repository_id)}/members/{OpenApiUtilClient.get_encode_param(aliyun_pk)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateRepositoryMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_member(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_member_with_options(organization_id, resource_type, resource_id, account_id, request, headers, runtime)

    async def update_resource_member_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_member_with_options_async(organization_id, resource_type, resource_id, account_id, request, headers, runtime)

    def update_resource_member_with_options(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_member_with_options_async(
        self,
        organization_id: str,
        resource_type: str,
        resource_id: str,
        account_id: str,
        request: devops_20210625_models.UpdateResourceMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateResourceMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/{OpenApiUtilClient.get_encode_param(resource_type)}/{OpenApiUtilClient.get_encode_param(resource_id)}/members/{OpenApiUtilClient.get_encode_param(account_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateResourceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_variable_group(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_variable_group_with_options(organization_id, id, request, headers, runtime)

    async def update_variable_group_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_variable_group_with_options_async(organization_id, id, request, headers, runtime)

    def update_variable_group_with_options(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_variable_group_with_options_async(
        self,
        organization_id: str,
        id: str,
        request: devops_20210625_models.UpdateVariableGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateVariableGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/variableGroups/{OpenApiUtilClient.get_encode_param(id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateVariableGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_work_item(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkItemRequest,
    ) -> devops_20210625_models.UpdateWorkItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_work_item_with_options(organization_id, request, headers, runtime)

    async def update_work_item_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkItemRequest,
    ) -> devops_20210625_models.UpdateWorkItemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_work_item_with_options_async(organization_id, request, headers, runtime)

    def update_work_item_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_type):
            body['fieldType'] = request.field_type
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.property_key):
            body['propertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_value):
            body['propertyValue'] = request.property_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkItem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_work_item_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkItemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.field_type):
            body['fieldType'] = request.field_type
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.property_key):
            body['propertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_value):
            body['propertyValue'] = request.property_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkItem',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workitem_comment(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemCommentRequest,
    ) -> devops_20210625_models.UpdateWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_workitem_comment_with_options(organization_id, request, headers, runtime)

    async def update_workitem_comment_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemCommentRequest,
    ) -> devops_20210625_models.UpdateWorkitemCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_workitem_comment_with_options_async(organization_id, request, headers, runtime)

    def update_workitem_comment_with_options(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/commentUpdate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkitemCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workitem_comment_with_options_async(
        self,
        organization_id: str,
        request: devops_20210625_models.UpdateWorkitemCommentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devops_20210625_models.UpdateWorkitemCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment_id):
            body['commentId'] = request.comment_id
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.format_type):
            body['formatType'] = request.format_type
        if not UtilClient.is_unset(request.workitem_identifier):
            body['workitemIdentifier'] = request.workitem_identifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkitemComment',
            version='2021-06-25',
            protocol='HTTPS',
            pathname=f'/organization/{OpenApiUtilClient.get_encode_param(organization_id)}/workitems/commentUpdate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateWorkitemCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )
