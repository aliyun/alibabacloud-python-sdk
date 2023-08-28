# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aliding20230426 import models as aliding_20230426_models
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
        self._endpoint = self.get_endpoint('aliding', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_workspace_doc_members_with_options(
        self,
        tmp_req: aliding_20230426_models.AddWorkspaceDocMembersRequest,
        tmp_header: aliding_20230426_models.AddWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.AddWorkspaceDocMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddWorkspaceDocMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddWorkspaceDocMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkspaceDocMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/addWorkspaceDocMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddWorkspaceDocMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_workspace_doc_members_with_options_async(
        self,
        tmp_req: aliding_20230426_models.AddWorkspaceDocMembersRequest,
        tmp_header: aliding_20230426_models.AddWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.AddWorkspaceDocMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddWorkspaceDocMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddWorkspaceDocMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkspaceDocMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/addWorkspaceDocMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddWorkspaceDocMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_workspace_doc_members(
        self,
        request: aliding_20230426_models.AddWorkspaceDocMembersRequest,
    ) -> aliding_20230426_models.AddWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddWorkspaceDocMembersHeaders()
        return self.add_workspace_doc_members_with_options(request, headers, runtime)

    async def add_workspace_doc_members_async(
        self,
        request: aliding_20230426_models.AddWorkspaceDocMembersRequest,
    ) -> aliding_20230426_models.AddWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddWorkspaceDocMembersHeaders()
        return await self.add_workspace_doc_members_with_options_async(request, headers, runtime)

    def add_workspace_members_with_options(
        self,
        tmp_req: aliding_20230426_models.AddWorkspaceMembersRequest,
        tmp_header: aliding_20230426_models.AddWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.AddWorkspaceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddWorkspaceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddWorkspaceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkspaceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/addWorkspaceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddWorkspaceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_workspace_members_with_options_async(
        self,
        tmp_req: aliding_20230426_models.AddWorkspaceMembersRequest,
        tmp_header: aliding_20230426_models.AddWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.AddWorkspaceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddWorkspaceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddWorkspaceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkspaceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/addWorkspaceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddWorkspaceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_workspace_members(
        self,
        request: aliding_20230426_models.AddWorkspaceMembersRequest,
    ) -> aliding_20230426_models.AddWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddWorkspaceMembersHeaders()
        return self.add_workspace_members_with_options(request, headers, runtime)

    async def add_workspace_members_async(
        self,
        request: aliding_20230426_models.AddWorkspaceMembersRequest,
    ) -> aliding_20230426_models.AddWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddWorkspaceMembersHeaders()
        return await self.add_workspace_members_with_options_async(request, headers, runtime)

    def create_sheet_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateSheetRequest,
        tmp_header: aliding_20230426_models.CreateSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateSheetResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/createSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateSheetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sheet_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateSheetRequest,
        tmp_header: aliding_20230426_models.CreateSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateSheetResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/createSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateSheetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sheet(
        self,
        request: aliding_20230426_models.CreateSheetRequest,
    ) -> aliding_20230426_models.CreateSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateSheetHeaders()
        return self.create_sheet_with_options(request, headers, runtime)

    async def create_sheet_async(
        self,
        request: aliding_20230426_models.CreateSheetRequest,
    ) -> aliding_20230426_models.CreateSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateSheetHeaders()
        return await self.create_sheet_with_options_async(request, headers, runtime)

    def create_todo_task_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateTodoTaskRequest,
        tmp_header: aliding_20230426_models.CreateTodoTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateTodoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateTodoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateTodoTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.content_field_list):
            request.content_field_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content_field_list, 'contentFieldList', 'json')
        if not UtilClient.is_unset(tmp_req.detail_url):
            request.detail_url_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail_url, 'detailUrl', 'json')
        if not UtilClient.is_unset(tmp_req.executor_ids):
            request.executor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_ids, 'executorIds', 'json')
        if not UtilClient.is_unset(tmp_req.notify_configs):
            request.notify_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_configs, 'notifyConfigs', 'json')
        if not UtilClient.is_unset(tmp_req.participant_ids):
            request.participant_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.participant_ids, 'participantIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.content_field_list_shrink):
            body['contentFieldList'] = request.content_field_list_shrink
        if not UtilClient.is_unset(request.creator_id):
            body['creatorId'] = request.creator_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.detail_url_shrink):
            body['detailUrl'] = request.detail_url_shrink
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.executor_ids_shrink):
            body['executorIds'] = request.executor_ids_shrink
        if not UtilClient.is_unset(request.is_only_show_executor):
            body['isOnlyShowExecutor'] = request.is_only_show_executor
        if not UtilClient.is_unset(request.notify_configs_shrink):
            body['notifyConfigs'] = request.notify_configs_shrink
        if not UtilClient.is_unset(request.participant_ids_shrink):
            body['participantIds'] = request.participant_ids_shrink
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.source_id):
            body['sourceId'] = request.source_id
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTodoTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/createTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_todo_task_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateTodoTaskRequest,
        tmp_header: aliding_20230426_models.CreateTodoTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateTodoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateTodoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateTodoTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.content_field_list):
            request.content_field_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content_field_list, 'contentFieldList', 'json')
        if not UtilClient.is_unset(tmp_req.detail_url):
            request.detail_url_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail_url, 'detailUrl', 'json')
        if not UtilClient.is_unset(tmp_req.executor_ids):
            request.executor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_ids, 'executorIds', 'json')
        if not UtilClient.is_unset(tmp_req.notify_configs):
            request.notify_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_configs, 'notifyConfigs', 'json')
        if not UtilClient.is_unset(tmp_req.participant_ids):
            request.participant_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.participant_ids, 'participantIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.content_field_list_shrink):
            body['contentFieldList'] = request.content_field_list_shrink
        if not UtilClient.is_unset(request.creator_id):
            body['creatorId'] = request.creator_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.detail_url_shrink):
            body['detailUrl'] = request.detail_url_shrink
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.executor_ids_shrink):
            body['executorIds'] = request.executor_ids_shrink
        if not UtilClient.is_unset(request.is_only_show_executor):
            body['isOnlyShowExecutor'] = request.is_only_show_executor
        if not UtilClient.is_unset(request.notify_configs_shrink):
            body['notifyConfigs'] = request.notify_configs_shrink
        if not UtilClient.is_unset(request.participant_ids_shrink):
            body['participantIds'] = request.participant_ids_shrink
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.source_id):
            body['sourceId'] = request.source_id
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTodoTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/createTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateTodoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_todo_task(
        self,
        request: aliding_20230426_models.CreateTodoTaskRequest,
    ) -> aliding_20230426_models.CreateTodoTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateTodoTaskHeaders()
        return self.create_todo_task_with_options(request, headers, runtime)

    async def create_todo_task_async(
        self,
        request: aliding_20230426_models.CreateTodoTaskRequest,
    ) -> aliding_20230426_models.CreateTodoTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateTodoTaskHeaders()
        return await self.create_todo_task_with_options_async(request, headers, runtime)

    def create_workspace_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateWorkspaceRequest,
        tmp_header: aliding_20230426_models.CreateWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/createWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateWorkspaceRequest,
        tmp_header: aliding_20230426_models.CreateWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/createWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: aliding_20230426_models.CreateWorkspaceRequest,
    ) -> aliding_20230426_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateWorkspaceHeaders()
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: aliding_20230426_models.CreateWorkspaceRequest,
    ) -> aliding_20230426_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateWorkspaceHeaders()
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def create_workspace_doc_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateWorkspaceDocRequest,
        tmp_header: aliding_20230426_models.CreateWorkspaceDocHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateWorkspaceDocResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateWorkspaceDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateWorkspaceDocShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_node_id):
            body['ParentNodeId'] = request.parent_node_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspaceDoc',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/createWorkspaceDoc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateWorkspaceDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_doc_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateWorkspaceDocRequest,
        tmp_header: aliding_20230426_models.CreateWorkspaceDocHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateWorkspaceDocResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateWorkspaceDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateWorkspaceDocShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_node_id):
            body['ParentNodeId'] = request.parent_node_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspaceDoc',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/createWorkspaceDoc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateWorkspaceDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace_doc(
        self,
        request: aliding_20230426_models.CreateWorkspaceDocRequest,
    ) -> aliding_20230426_models.CreateWorkspaceDocResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateWorkspaceDocHeaders()
        return self.create_workspace_doc_with_options(request, headers, runtime)

    async def create_workspace_doc_async(
        self,
        request: aliding_20230426_models.CreateWorkspaceDocRequest,
    ) -> aliding_20230426_models.CreateWorkspaceDocResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateWorkspaceDocHeaders()
        return await self.create_workspace_doc_with_options_async(request, headers, runtime)

    def delete_todo_task_with_options(
        self,
        tmp_req: aliding_20230426_models.DeleteTodoTaskRequest,
        tmp_header: aliding_20230426_models.DeleteTodoTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteTodoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteTodoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteTodoTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTodoTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/deleteTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_todo_task_with_options_async(
        self,
        tmp_req: aliding_20230426_models.DeleteTodoTaskRequest,
        tmp_header: aliding_20230426_models.DeleteTodoTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteTodoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteTodoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteTodoTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTodoTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/deleteTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteTodoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_todo_task(
        self,
        request: aliding_20230426_models.DeleteTodoTaskRequest,
    ) -> aliding_20230426_models.DeleteTodoTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteTodoTaskHeaders()
        return self.delete_todo_task_with_options(request, headers, runtime)

    async def delete_todo_task_async(
        self,
        request: aliding_20230426_models.DeleteTodoTaskRequest,
    ) -> aliding_20230426_models.DeleteTodoTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteTodoTaskHeaders()
        return await self.delete_todo_task_with_options_async(request, headers, runtime)

    def delete_workspace_doc_members_with_options(
        self,
        tmp_req: aliding_20230426_models.DeleteWorkspaceDocMembersRequest,
        tmp_header: aliding_20230426_models.DeleteWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteWorkspaceDocMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteWorkspaceDocMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteWorkspaceDocMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkspaceDocMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteWorkspaceDocMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteWorkspaceDocMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_doc_members_with_options_async(
        self,
        tmp_req: aliding_20230426_models.DeleteWorkspaceDocMembersRequest,
        tmp_header: aliding_20230426_models.DeleteWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteWorkspaceDocMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteWorkspaceDocMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteWorkspaceDocMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkspaceDocMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteWorkspaceDocMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteWorkspaceDocMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace_doc_members(
        self,
        request: aliding_20230426_models.DeleteWorkspaceDocMembersRequest,
    ) -> aliding_20230426_models.DeleteWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteWorkspaceDocMembersHeaders()
        return self.delete_workspace_doc_members_with_options(request, headers, runtime)

    async def delete_workspace_doc_members_async(
        self,
        request: aliding_20230426_models.DeleteWorkspaceDocMembersRequest,
    ) -> aliding_20230426_models.DeleteWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteWorkspaceDocMembersHeaders()
        return await self.delete_workspace_doc_members_with_options_async(request, headers, runtime)

    def delete_workspace_members_with_options(
        self,
        tmp_req: aliding_20230426_models.DeleteWorkspaceMembersRequest,
        tmp_header: aliding_20230426_models.DeleteWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteWorkspaceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteWorkspaceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteWorkspaceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkspaceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteWorkspaceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteWorkspaceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_members_with_options_async(
        self,
        tmp_req: aliding_20230426_models.DeleteWorkspaceMembersRequest,
        tmp_header: aliding_20230426_models.DeleteWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.DeleteWorkspaceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteWorkspaceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteWorkspaceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkspaceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/deleteWorkspaceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteWorkspaceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace_members(
        self,
        request: aliding_20230426_models.DeleteWorkspaceMembersRequest,
    ) -> aliding_20230426_models.DeleteWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteWorkspaceMembersHeaders()
        return self.delete_workspace_members_with_options(request, headers, runtime)

    async def delete_workspace_members_async(
        self,
        request: aliding_20230426_models.DeleteWorkspaceMembersRequest,
    ) -> aliding_20230426_models.DeleteWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteWorkspaceMembersHeaders()
        return await self.delete_workspace_members_with_options_async(request, headers, runtime)

    def get_user_with_options(
        self,
        tmp_req: aliding_20230426_models.GetUserRequest,
        tmp_header: aliding_20230426_models.GetUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetUserResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetUserShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/im/getUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        tmp_req: aliding_20230426_models.GetUserRequest,
        tmp_header: aliding_20230426_models.GetUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.GetUserResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetUserShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/im/getUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: aliding_20230426_models.GetUserRequest,
    ) -> aliding_20230426_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetUserHeaders()
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: aliding_20230426_models.GetUserRequest,
    ) -> aliding_20230426_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetUserHeaders()
        return await self.get_user_with_options_async(request, headers, runtime)

    def insert_rows_before_with_options(
        self,
        tmp_req: aliding_20230426_models.InsertRowsBeforeRequest,
        tmp_header: aliding_20230426_models.InsertRowsBeforeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.InsertRowsBeforeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InsertRowsBeforeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InsertRowsBeforeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.row):
            body['Row'] = request.row
        if not UtilClient.is_unset(request.row_count):
            body['RowCount'] = request.row_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertRowsBefore',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/insertRowsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InsertRowsBeforeResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_rows_before_with_options_async(
        self,
        tmp_req: aliding_20230426_models.InsertRowsBeforeRequest,
        tmp_header: aliding_20230426_models.InsertRowsBeforeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.InsertRowsBeforeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InsertRowsBeforeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InsertRowsBeforeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.row):
            body['Row'] = request.row
        if not UtilClient.is_unset(request.row_count):
            body['RowCount'] = request.row_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertRowsBefore',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/insertRowsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InsertRowsBeforeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_rows_before(
        self,
        request: aliding_20230426_models.InsertRowsBeforeRequest,
    ) -> aliding_20230426_models.InsertRowsBeforeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InsertRowsBeforeHeaders()
        return self.insert_rows_before_with_options(request, headers, runtime)

    async def insert_rows_before_async(
        self,
        request: aliding_20230426_models.InsertRowsBeforeRequest,
    ) -> aliding_20230426_models.InsertRowsBeforeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InsertRowsBeforeHeaders()
        return await self.insert_rows_before_with_options_async(request, headers, runtime)

    def query_org_todo_tasks_with_options(
        self,
        tmp_req: aliding_20230426_models.QueryOrgTodoTasksRequest,
        tmp_header: aliding_20230426_models.QueryOrgTodoTasksHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryOrgTodoTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryOrgTodoTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryOrgTodoTasksShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.is_done):
            body['isDone'] = request.is_done
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrgTodoTasks',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/queryOrgTodoTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryOrgTodoTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_org_todo_tasks_with_options_async(
        self,
        tmp_req: aliding_20230426_models.QueryOrgTodoTasksRequest,
        tmp_header: aliding_20230426_models.QueryOrgTodoTasksHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.QueryOrgTodoTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryOrgTodoTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryOrgTodoTasksShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.is_done):
            body['isDone'] = request.is_done
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrgTodoTasks',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/queryOrgTodoTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryOrgTodoTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_org_todo_tasks(
        self,
        request: aliding_20230426_models.QueryOrgTodoTasksRequest,
    ) -> aliding_20230426_models.QueryOrgTodoTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryOrgTodoTasksHeaders()
        return self.query_org_todo_tasks_with_options(request, headers, runtime)

    async def query_org_todo_tasks_async(
        self,
        request: aliding_20230426_models.QueryOrgTodoTasksRequest,
    ) -> aliding_20230426_models.QueryOrgTodoTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryOrgTodoTasksHeaders()
        return await self.query_org_todo_tasks_with_options_async(request, headers, runtime)

    def update_todo_task_with_options(
        self,
        tmp_req: aliding_20230426_models.UpdateTodoTaskRequest,
        tmp_header: aliding_20230426_models.UpdateTodoTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateTodoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateTodoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateTodoTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.executor_ids):
            request.executor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_ids, 'executorIds', 'json')
        if not UtilClient.is_unset(tmp_req.participant_ids):
            request.participant_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.participant_ids, 'participantIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.done):
            body['done'] = request.done
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.executor_ids_shrink):
            body['executorIds'] = request.executor_ids_shrink
        if not UtilClient.is_unset(request.participant_ids_shrink):
            body['participantIds'] = request.participant_ids_shrink
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTodoTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/updateTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_todo_task_with_options_async(
        self,
        tmp_req: aliding_20230426_models.UpdateTodoTaskRequest,
        tmp_header: aliding_20230426_models.UpdateTodoTaskHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateTodoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateTodoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateTodoTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.executor_ids):
            request.executor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_ids, 'executorIds', 'json')
        if not UtilClient.is_unset(tmp_req.participant_ids):
            request.participant_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.participant_ids, 'participantIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.done):
            body['done'] = request.done
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.executor_ids_shrink):
            body['executorIds'] = request.executor_ids_shrink
        if not UtilClient.is_unset(request.participant_ids_shrink):
            body['participantIds'] = request.participant_ids_shrink
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTodoTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/updateTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateTodoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_todo_task(
        self,
        request: aliding_20230426_models.UpdateTodoTaskRequest,
    ) -> aliding_20230426_models.UpdateTodoTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateTodoTaskHeaders()
        return self.update_todo_task_with_options(request, headers, runtime)

    async def update_todo_task_async(
        self,
        request: aliding_20230426_models.UpdateTodoTaskRequest,
    ) -> aliding_20230426_models.UpdateTodoTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateTodoTaskHeaders()
        return await self.update_todo_task_with_options_async(request, headers, runtime)

    def update_todo_task_executor_status_with_options(
        self,
        tmp_req: aliding_20230426_models.UpdateTodoTaskExecutorStatusRequest,
        tmp_header: aliding_20230426_models.UpdateTodoTaskExecutorStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateTodoTaskExecutorStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateTodoTaskExecutorStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateTodoTaskExecutorStatusShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.executor_status_list):
            request.executor_status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_status_list, 'executorStatusList', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.executor_status_list_shrink):
            body['executorStatusList'] = request.executor_status_list_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTodoTaskExecutorStatus',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/updateTodoTaskExecutorStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateTodoTaskExecutorStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_todo_task_executor_status_with_options_async(
        self,
        tmp_req: aliding_20230426_models.UpdateTodoTaskExecutorStatusRequest,
        tmp_header: aliding_20230426_models.UpdateTodoTaskExecutorStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateTodoTaskExecutorStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateTodoTaskExecutorStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateTodoTaskExecutorStatusShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.executor_status_list):
            request.executor_status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_status_list, 'executorStatusList', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.executor_status_list_shrink):
            body['executorStatusList'] = request.executor_status_list_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTodoTaskExecutorStatus',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/task/updateTodoTaskExecutorStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateTodoTaskExecutorStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_todo_task_executor_status(
        self,
        request: aliding_20230426_models.UpdateTodoTaskExecutorStatusRequest,
    ) -> aliding_20230426_models.UpdateTodoTaskExecutorStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateTodoTaskExecutorStatusHeaders()
        return self.update_todo_task_executor_status_with_options(request, headers, runtime)

    async def update_todo_task_executor_status_async(
        self,
        request: aliding_20230426_models.UpdateTodoTaskExecutorStatusRequest,
    ) -> aliding_20230426_models.UpdateTodoTaskExecutorStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateTodoTaskExecutorStatusHeaders()
        return await self.update_todo_task_executor_status_with_options_async(request, headers, runtime)

    def update_workspace_doc_members_with_options(
        self,
        tmp_req: aliding_20230426_models.UpdateWorkspaceDocMembersRequest,
        tmp_header: aliding_20230426_models.UpdateWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateWorkspaceDocMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateWorkspaceDocMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateWorkspaceDocMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceDocMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/updateWorkspaceDocMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateWorkspaceDocMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_doc_members_with_options_async(
        self,
        tmp_req: aliding_20230426_models.UpdateWorkspaceDocMembersRequest,
        tmp_header: aliding_20230426_models.UpdateWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateWorkspaceDocMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateWorkspaceDocMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateWorkspaceDocMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceDocMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/updateWorkspaceDocMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateWorkspaceDocMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace_doc_members(
        self,
        request: aliding_20230426_models.UpdateWorkspaceDocMembersRequest,
    ) -> aliding_20230426_models.UpdateWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateWorkspaceDocMembersHeaders()
        return self.update_workspace_doc_members_with_options(request, headers, runtime)

    async def update_workspace_doc_members_async(
        self,
        request: aliding_20230426_models.UpdateWorkspaceDocMembersRequest,
    ) -> aliding_20230426_models.UpdateWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateWorkspaceDocMembersHeaders()
        return await self.update_workspace_doc_members_with_options_async(request, headers, runtime)

    def update_workspace_members_with_options(
        self,
        tmp_req: aliding_20230426_models.UpdateWorkspaceMembersRequest,
        tmp_header: aliding_20230426_models.UpdateWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateWorkspaceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateWorkspaceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateWorkspaceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/updateWorkspaceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateWorkspaceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_members_with_options_async(
        self,
        tmp_req: aliding_20230426_models.UpdateWorkspaceMembersRequest,
        tmp_header: aliding_20230426_models.UpdateWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.UpdateWorkspaceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateWorkspaceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateWorkspaceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/updateWorkspaceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateWorkspaceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace_members(
        self,
        request: aliding_20230426_models.UpdateWorkspaceMembersRequest,
    ) -> aliding_20230426_models.UpdateWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateWorkspaceMembersHeaders()
        return self.update_workspace_members_with_options(request, headers, runtime)

    async def update_workspace_members_async(
        self,
        request: aliding_20230426_models.UpdateWorkspaceMembersRequest,
    ) -> aliding_20230426_models.UpdateWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateWorkspaceMembersHeaders()
        return await self.update_workspace_members_with_options_async(request, headers, runtime)
